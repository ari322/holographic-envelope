#!/usr/bin/env python3
"""RSB detection on Pareto gene vectors — Holographic Envelope (HE).

Follows MATH-SKELETON 3.4 and prompts/prompts-algorithmic.md A05:

  1. Pairwise distances  d(g_a, g_b) = ||g_a - g_b||_2 / sqrt(6)
  2. Histogram of P_arch(d)
  3. Hartigan dip test on the distance sample
  4. GMM on distances, K selected by BIC
  5. If p < 0.05 and K >= 2: the *script reports* an RSB-equivalent pattern
     on THIS dataset. That is not a scientific confirmation of D02.

A05 fits GMM on 1-D distances then calls predict() on 6-D genes (shape
mismatch). This script keeps GMM-on-distances for K (as specified) and fits a
second GMM in standardised gene space only to label solutions (protocol
step 4: characterise each cluster).

Hartigan & Hartigan (1985) dip statistic is implemented in numpy. The p-value
is a uniform-bootstrap approximation (null: unimodal). sklearn GMM + BIC
selects K.

SYNTHETIC DATA
--------------
If the input JSON has label/data_class SYNTHETIC (the bundled
synthetic-pareto.json does), this script prints a hard warning and will NOT
claim Replica Symmetry Breaking is confirmed. Synthetic data exists only to
exercise the detector.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
from scipy.spatial.distance import pdist
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

GENE_ORDER = ("d", "a", "r", "eps", "ms", "wr")


# ---------------------------------------------------------------------------
# Distances  (MATH-SKELETON 3.4)
# ---------------------------------------------------------------------------

def compute_pairwise_distances(pareto_solutions: np.ndarray) -> np.ndarray:
    """d = ||g_a - g_b||_2 / sqrt(6) for all pairs a < b."""
    sols = np.asarray(pareto_solutions, dtype=float)
    if sols.ndim != 2 or sols.shape[1] != 6:
        raise ValueError("pareto_solutions must have shape (n, 6)")
    if sols.shape[0] < 2:
        return np.zeros(0, dtype=float)
    return pdist(sols, metric="euclidean") / math.sqrt(6.0)


# ---------------------------------------------------------------------------
# Hartigan dip test (numpy; no diptest package)
# ---------------------------------------------------------------------------

def _greatest_convex_minorant(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Lower convex hull interpolated back onto x (Andrew monotone chain)."""
    n = x.size
    stack: List[int] = []
    for i in range(n):
        while len(stack) >= 2:
            i1, i2 = stack[-2], stack[-1]
            # pop if i2 is on or above the line i1 -> i (not a lower-hull vertex)
            if (x[i2] - x[i1]) * (y[i] - y[i1]) <= (x[i] - x[i1]) * (y[i2] - y[i1]):
                stack.pop()
            else:
                break
        stack.append(i)
    idx = np.array(stack, dtype=int)
    return np.interp(x, x[idx], y[idx])


def _least_concave_majorant(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return -_greatest_convex_minorant(x, -y)


def hartigan_dip_statistic(sample: np.ndarray) -> float:
    """Hartigan & Hartigan (1985) dip: inf over unimodal G of ||F_n - G||_inf.

    For each candidate mode index m the closest unimodal CDF is the greatest
    convex minorant of the ECDF on the left of m and the least concave
    majorant on the right. The dip is the minimum of those sup-deviations.

    Returns a value in [0, 0.25]. 0 is perfectly unimodal (e.g. a single point
    or a sample matching a unimodal envelope).
    """
    x = np.sort(np.asarray(sample, dtype=float).reshape(-1))
    n = x.size
    if n < 3 or x[0] == x[-1]:
        return 0.0

    # Mid-ecdf at each sample point: (i + 0.5) / n reduces left/right bias.
    F = (np.arange(n, dtype=float) + 0.5) / n
    best = 0.5
    # Evaluate a stride of candidate modes (every point if n is modest).
    step = 1 if n <= 2500 else max(1, n // 2500)
    for m in range(0, n, step):
        d_left = 0.0
        d_right = 0.0
        if m >= 2:
            xl, Fl = x[: m + 1], F[: m + 1]
            g = _greatest_convex_minorant(xl, Fl)
            d_left = float(np.max(np.abs(Fl - g)))
        if m <= n - 3:
            xr, Fr = x[m:], F[m:]
            c = _least_concave_majorant(xr, Fr)
            d_right = float(np.max(np.abs(Fr - c)))
        best = min(best, max(d_left, d_right))
    return float(best)


def hartigan_dip_test(
    sample: np.ndarray,
    n_boot: int = 200,
    seed: int = 42,
    max_n: int = 4000,
) -> Tuple[float, float, int]:
    """Dip statistic + bootstrap p-value under a uniform (unimodal) null.

    Large distance samples are subsampled to ``max_n`` (deterministic after
    sort + stride) so the O(n^2) dip stays usable. GMM still uses all pairs.
    """
    rng = np.random.default_rng(seed)
    x = np.sort(np.asarray(sample, dtype=float).reshape(-1))
    if x.size > max_n:
        idx = np.linspace(0, x.size - 1, max_n).astype(int)
        x = x[idx]
    dip = hartigan_dip_statistic(x)
    n = x.size
    if n < 3:
        return dip, 1.0, n
    null_dips = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        u = np.sort(rng.uniform(0.0, 1.0, size=n))
        null_dips[b] = hartigan_dip_statistic(u)
    p = float((1.0 + np.sum(null_dips >= dip)) / (n_boot + 1.0))
    return dip, p, n


# ---------------------------------------------------------------------------
# GMM on distances (prompt A05) + gene-space labels (protocol step 4)
# ---------------------------------------------------------------------------

def fit_gmm_select_k(
    distances: np.ndarray,
    k_max: int = 5,
    seed: int = 42,
) -> Tuple[int, List[float], GaussianMixture]:
    """Fit 1-D GMMs on P_arch(d); choose K by lowest BIC (prompt A05)."""
    d = np.asarray(distances, dtype=float).reshape(-1, 1)
    bic_scores: List[float] = []
    models: List[GaussianMixture] = []
    for k in range(1, k_max + 1):
        gmm = GaussianMixture(n_components=k, random_state=seed, covariance_type="full")
        gmm.fit(d)
        bic_scores.append(float(gmm.bic(d)))
        models.append(gmm)
    best_i = int(np.argmin(bic_scores))
    return best_i + 1, bic_scores, models[best_i]


def fit_gene_space_gmm(
    solutions: np.ndarray,
    k: int,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """Cluster solutions in standardised gene space for characterisation."""
    scaler = StandardScaler()
    z = scaler.fit_transform(np.asarray(solutions, dtype=float))
    k = max(1, int(k))
    gmm = GaussianMixture(n_components=k, random_state=seed)
    labels = gmm.fit_predict(z)
    means = scaler.inverse_transform(gmm.means_)
    return labels, means


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def _genes_from_solution(sol: Dict[str, Any]) -> List[float]:
    if "genes" in sol and isinstance(sol["genes"], dict):
        return [float(sol["genes"][name]) for name in GENE_ORDER]
    if "gene_vector" in sol:
        v = sol["gene_vector"]
        if len(v) != 6:
            raise ValueError("gene_vector must have length 6")
        return [float(x) for x in v]
    raise KeyError("solution missing 'genes' or 'gene_vector'")


def load_pareto_json(path: Path) -> Tuple[np.ndarray, Dict[str, Any], bool]:
    """Load gene vectors from the project JSON schema (or a flat list)."""
    payload = json.loads(path.read_text())
    synthetic = False
    solutions: List[List[float]] = []

    if isinstance(payload, dict):
        label = str(payload.get("label", payload.get("data_class", "")))
        synthetic = "SYNTHETIC" in label.upper() or bool(payload.get("synthetic", False))
        if "runs" in payload:
            for run in payload["runs"]:
                if "SYNTHETIC" in str(run.get("label", "")).upper():
                    synthetic = True
                for sol in run.get("solutions", []):
                    solutions.append(_genes_from_solution(sol))
                    if "SYNTHETIC" in str(sol.get("label", "")).upper():
                        synthetic = True
        elif "solutions" in payload:
            for sol in payload["solutions"]:
                solutions.append(_genes_from_solution(sol))
        elif "pareto_solutions" in payload:
            for v in payload["pareto_solutions"]:
                solutions.append([float(x) for x in v])
        else:
            raise KeyError("JSON must contain runs, solutions, or pareto_solutions")
    elif isinstance(payload, list):
        for v in payload:
            solutions.append([float(x) for x in v])
    else:
        raise TypeError("JSON root must be object or list")

    arr = np.asarray(solutions, dtype=float)
    if arr.ndim != 2 or arr.shape[1] != 6:
        raise ValueError(f"expected (n, 6) gene matrix, got {arr.shape}")
    return arr, payload if isinstance(payload, dict) else {"raw": True}, synthetic


@dataclass
class RSBResult:
    n_solutions: int
    n_pairs: int
    dip_statistic: float
    p_value: float
    dip_sample_size: int
    k_distances: int
    bic_scores: List[float]
    gene_cluster_labels: np.ndarray
    gene_cluster_means: np.ndarray
    distances: np.ndarray
    synthetic: bool
    notes: List[str] = field(default_factory=list)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "n_solutions": self.n_solutions,
            "n_pairs": self.n_pairs,
            "dip_statistic": self.dip_statistic,
            "p_value": self.p_value,
            "dip_sample_size": self.dip_sample_size,
            "k_from_distance_gmm": self.k_distances,
            "bic_scores": self.bic_scores,
            "gene_cluster_counts": {
                int(k): int(np.sum(self.gene_cluster_labels == k))
                for k in sorted(set(self.gene_cluster_labels.tolist()))
            },
            "gene_cluster_means": {
                name: [float(m[i]) for m in self.gene_cluster_means]
                for i, name in enumerate(GENE_ORDER)
            },
            "synthetic": self.synthetic,
            "notes": list(self.notes),
        }


def detect_rsb(
    solutions: np.ndarray,
    synthetic: bool = False,
    k_max: int = 5,
    n_boot: int = 200,
    seed: int = 42,
) -> RSBResult:
    distances = compute_pairwise_distances(solutions)
    dip, p_value, dip_n = hartigan_dip_test(distances, n_boot=n_boot, seed=seed)
    k, bic, _gmm = fit_gmm_select_k(distances, k_max=k_max, seed=seed)
    labels, means = fit_gene_space_gmm(solutions, k=k, seed=seed)

    notes = [
        "Protocol: MATH-SKELETON 3.4 / prompt A05 (GMM+BIC on P_arch(d), Hartigan dip).",
        "Decision rule in the docs: p < 0.05 and K >= 2 is the RSB-equivalent pattern.",
        "This function reports that rule on the supplied sample only.",
    ]
    if synthetic:
        notes.append(
            "SYNTHETIC data — do not treat a positive rule hit as confirmation of D02 / RSB."
        )
        notes.append("CRITIC has not authorised a discovery claim from this output.")

    return RSBResult(
        n_solutions=int(solutions.shape[0]),
        n_pairs=int(distances.size),
        dip_statistic=dip,
        p_value=p_value,
        dip_sample_size=dip_n,
        k_distances=k,
        bic_scores=bic,
        gene_cluster_labels=labels,
        gene_cluster_means=means,
        distances=distances,
        synthetic=synthetic,
        notes=notes,
    )


def _print_report(result: RSBResult) -> None:
    print("=== HE RSB detection ===")
    if result.synthetic:
        print("*** SYNTHETIC DATA — NOT a Wallacei run, NOT a scientific RSB result ***")
    print(f"solutions: {result.n_solutions}   pairwise distances: {result.n_pairs}")
    print(f"Hartigan dip: {result.dip_statistic:.6f}   bootstrap p: {result.p_value:.4f}   (n={result.dip_sample_size})")
    print(f"GMM-on-distances K (BIC): {result.k_distances}")
    print("BIC by K:", ", ".join(f"K={i+1}:{b:.1f}" for i, b in enumerate(result.bic_scores)))
    print("gene-space cluster sizes:", result.as_dict()["gene_cluster_counts"])
    rule_hit = (result.p_value < 0.05) and (result.k_distances >= 2)
    print(f"documented rule (p<0.05 and K>=2) on this sample: {rule_hit}")
    if result.synthetic:
        print(
            "Classification: SYNTHETIC detector exercise only. "
            "Do not upgrade D02 evidence class from this file."
        )
    else:
        print(
            "Classification: report K, p, and BIC. Do not claim RSB is confirmed "
            "unless the sample is real multi-seed Wallacei output and CRITIC agrees."
        )
    for n in result.notes:
        print(f"note: {n}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="HE RSB detection (GMM + Hartigan dip)")
    parser.add_argument(
        "--input",
        type=Path,
        default=here / "synthetic-pareto.json",
        help="Pareto JSON (default: bundled SYNTHETIC file)",
    )
    parser.add_argument("--k-max", type=int, default=5)
    parser.add_argument("--n-boot", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=None, help="Optional JSON report path")
    args = parser.parse_args(argv)

    solutions, payload, synthetic = load_pareto_json(args.input)
    if isinstance(payload, dict) and "SYNTHETIC" in str(payload.get("label", "")).upper():
        synthetic = True
    print(f"Loaded {solutions.shape[0]} gene vectors from {args.input}")
    result = detect_rsb(
        solutions,
        synthetic=synthetic,
        k_max=args.k_max,
        n_boot=args.n_boot,
        seed=args.seed,
    )
    _print_report(result)
    if args.out is not None:
        args.out.write_text(json.dumps(result.as_dict(), indent=2))
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
