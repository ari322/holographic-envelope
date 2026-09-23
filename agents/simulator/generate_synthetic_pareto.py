#!/usr/bin/env python3
"""Generate SYNTHETIC Wallacei-shaped Pareto data for RSB-script tests.

THIS FILE WRITES SYNTHETIC DATA ONLY.

It does not run Wallacei, Ladybug, Honeybee, or facade-sim.py. The 5 x 50
gene vectors are sampled from two planted Gaussian families so the RSB
detector can be exercised on a known multimodal P_arch(d).

Do not present the output JSON as simulation results, as a Pareto front from
Sydney EPW, or as evidence for Discovery 02 / Replica Symmetry Breaking.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Dict, List

import numpy as np

# Wallacei protocol seeds (prompt A04 / AI-CONTEXT RSB protocol)
SEEDS = [42, 137, 256, 891, 1024]
N_PER_RUN = 50
N_RUNS = 5

GENE_BOUNDS = {
    "d": (50.0, 300.0),
    "a": (0.1, 0.9),
    "r": (0.0, 90.0),
    "eps": (0.01, 0.15),
    "ms": (0.05, 0.30),
    "wr": (0.2, 0.8),
}
GENE_ORDER = ("d", "a", "r", "eps", "ms", "wr")

# Two planted families in *physical* gene space (test fixture, not a finding).
# Family 0 sits near the documented sigma* prediction (deep / radiation-weighted).
# Family 1 is a contrasting high-aperture / low-rotation family.
FAMILY_MEANS = np.array(
    [
        [175.0, 0.62, 45.0, 0.064, 0.14, 0.65],
        [90.0, 0.80, 20.0, 0.11, 0.24, 0.35],
    ],
    dtype=float,
)
FAMILY_STDS = np.array(
    [
        [12.0, 0.04, 5.0, 0.008, 0.015, 0.04],
        [10.0, 0.035, 4.5, 0.010, 0.018, 0.035],
    ],
    dtype=float,
)


def _clip_genes(g: np.ndarray) -> np.ndarray:
    out = np.empty_like(g)
    for i, name in enumerate(GENE_ORDER):
        lo, hi = GENE_BOUNDS[name]
        out[i] = float(np.clip(g[i], lo, hi))
    return out


def genes_to_sigma(genes: Dict[str, float]) -> List[float]:
    sig = []
    for name in GENE_ORDER:
        lo, hi = GENE_BOUNDS[name]
        sig.append(float(2.0 * (genes[name] - lo) / (hi - lo) - 1.0))
    return sig


def synthetic_objectives(g: np.ndarray) -> Dict[str, float]:
    """Algebraic placeholders matching documented Jacobian *signs* only.

    Not facade-sim output. Not Ladybug/Honeybee. SYNTHETIC.
    """
    d, a, r, eps, ms, wr = (float(x) for x in g)
    f1 = 220.0 + 55.0 * a - 0.18 * d + 0.15 * r - 30.0 * wr
    f2 = 0.40 - 0.30 * a + 0.00045 * d - 0.0012 * r + 0.05 * (1.0 - wr)
    f3 = 1.0 + float(int(r // 30.0))
    f4 = 14.0 * ((0.15 - eps) / 0.14) * (ms / 0.30)
    return {
        "f1": float(f1),
        "f2": float(np.clip(f2, 0.0, 1.0)),
        "f3": float(f3),
        "f4": float(max(f4, 0.0)),
    }


def generate(n_runs: int = N_RUNS, n_per_run: int = N_PER_RUN) -> dict:
    runs = []
    for run_id, seed in enumerate(SEEDS[:n_runs], start=1):
        rng = np.random.default_rng(seed)
        # Slight run-to-run mix so seeds are not identical copies.
        mix = 0.45 + 0.10 * ((run_id - 1) % 3) / 2.0
        solutions = []
        for _ in range(n_per_run):
            fam = 0 if rng.random() < mix else 1
            raw = rng.normal(FAMILY_MEANS[fam], FAMILY_STDS[fam])
            g = _clip_genes(raw)
            genes = {name: float(g[i]) for i, name in enumerate(GENE_ORDER)}
            solutions.append(
                {
                    "label": "SYNTHETIC",
                    "planted_family": int(fam),
                    "genes": genes,
                    "sigma": genes_to_sigma(genes),
                    "objectives": synthetic_objectives(g),
                    "objectives_note": (
                        "SYNTHETIC algebraic placeholders — not facade-sim, "
                        "not Ladybug, not Wallacei."
                    ),
                }
            )
        runs.append(
            {
                "run_id": run_id,
                "seed": seed,
                "label": "SYNTHETIC",
                "n_solutions": n_per_run,
                "solutions": solutions,
            }
        )

    return {
        "label": "SYNTHETIC",
        "data_class": "SYNTHETIC",
        "notice": (
            "SYNTHETIC Pareto-front-style data. NOT real Wallacei output, "
            "NOT a Sydney EPW simulation, NOT evidence for Replica Symmetry "
            "Breaking or Discovery 02. Constructed with two planted gene-space "
            "families so agents/simulator/rsb-detection.py can be tested."
        ),
        "do_not_cite_as": [
            "Wallacei results",
            "Ladybug / Honeybee results",
            "confirmed RSB",
            "empirical Pareto front",
        ],
        "protocol_shape": {
            "runs": n_runs,
            "solutions_per_run": n_per_run,
            "seeds": SEEDS[:n_runs],
            "source_docs": [
                "prompts/prompts-algorithmic.md A04",
                "MATH-SKELETON.md 3.4",
                "AI-CONTEXT.md RSB detection protocol",
            ],
        },
        "gene_names": list(GENE_ORDER),
        "gene_bounds": {k: list(v) for k, v in GENE_BOUNDS.items()},
        "planted_family_means": {
            "family_0_deep_reveal_like": {
                name: float(FAMILY_MEANS[0, i]) for i, name in enumerate(GENE_ORDER)
            },
            "family_1_high_aperture_like": {
                name: float(FAMILY_MEANS[1, i]) for i, name in enumerate(GENE_ORDER)
            },
        },
        "generated_on": date.today().isoformat(),
        "generator": "agents/simulator/generate_synthetic_pareto.py",
        "runs": runs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Write SYNTHETIC Pareto JSON")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent / "synthetic-pareto.json",
    )
    args = parser.parse_args()
    payload = generate()
    args.out.write_text(json.dumps(payload, indent=2))
    n = sum(len(r["solutions"]) for r in payload["runs"])
    print(f"Wrote SYNTHETIC Pareto fixture: {args.out}  ({n} solutions, 2 planted families)")
    print("Do not present this file as real simulation results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
