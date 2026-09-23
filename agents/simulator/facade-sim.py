#!/usr/bin/env python3
"""Standalone facade controller simulator — Holographic Envelope (HE).

Implements the documented kinetic-facade controller and TFE metric in plain
Python (numpy). No Grasshopper, Rhino, Ladybug, or Honeybee.

Inputs
------
  weather : EPW-style hourly arrays (radiation, temperature, occupancy, wind)
  sigma   : normalised gene vector in [-1, +1]^6
            [s_d, s_a, s_r, s_eps, s_ms, s_wr]

Outputs
-------
  panel_angle_series : (n_panels, n_times) degrees
  f1, f2, f3, f4     : documented Wallacei objectives (all minimise)
  TFE_total          : Temporal Facade Entropy (MATH-SKELETON 1.4 / prompt A03)

Formula sources (do not invent replacements):
  gene bounds / sigma map : MATH-SKELETON 3.1, discovery-02-coupling-matrix.md
  controller + hysteresis : research/formal-model.md,
                            grasshopper/ghpython_state_controller.py
  TFE                     : MATH-SKELETON 1.2-1.4, prompts/prompts-algorithmic.md A03
  objectives              : prompts A04, grasshopper/optimization-setup.md

f1 and f2 are geometric *proxies* for Ladybug incident radiation and Honeybee
UDI. They follow the documented signs and definitions, not a full radiosity
solve. Do not present proxy values as Ladybug/Honeybee results.

This module is a callable facade: import via importlib (hyphenated filename)
or run as a script. See agents/simulator/README.md.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np

# ---------------------------------------------------------------------------
# Documented constants
# ---------------------------------------------------------------------------

N_COLS = 10
N_ROWS = 8
N_PANELS = N_COLS * N_ROWS  # 80 — prompts A01, grasshopper/step-01-geometry.md

# TFE discretisation: 5 bins on [0, 1]  (step-04-TFE.md, prompt A03)
N_BINS_TFE = 5

GENE_NAMES: Tuple[str, ...] = ("d", "a", "r", "eps", "ms", "wr")
GENE_BOUNDS: Dict[str, Tuple[float, float]] = {
    "d": (50.0, 300.0),   # mm
    "a": (0.1, 0.9),      # aperture ratio
    "r": (0.0, 90.0),     # max rotation, degrees
    "eps": (0.01, 0.15),  # hysteresis dead band
    "ms": (0.05, 0.30),   # maxStep
    "wr": (0.2, 0.8),     # radiation weight
}

# Documented predicted ground-state sigma (AI-CONTEXT / coupling-matrix).
# Used only as the demo default, not as a confirmed optimum.
SIGMA_STAR = np.array([0.4, 0.3, 0.0, -0.2, -0.1, 0.5], dtype=float)

# Occupied hours 8:00-18:00 weekdays (prompt A02, validation/simulation-baseline.md)
OCCUPIED_HOUR_START = 8
OCCUPIED_HOUR_END = 18  # exclusive of 18
LUX_THRESHOLD = 300.0
# Typical luminous efficacy of daylight (lm/W). Proxy only — not Honeybee.
LUMINOUS_EFFICACY_LM_PER_W = 110.0
# Physical scale for radiation normalisation (W/m2).
RADIATION_SCALE_W_M2 = 1000.0
# Formal-model SAFE override: wind above this (m/s) forces default position.
WIND_SAFE_LIMIT_M_S = 15.0
SAFE_DEFAULT_STATE = 0.0  # closed — mechanical fail-safe


# ---------------------------------------------------------------------------
# Gene encoding  (MATH-SKELETON 3.1)
# ---------------------------------------------------------------------------

def sigma_to_genes(sigma: Sequence[float]) -> Dict[str, float]:
    """Map sigma in [-1, +1]^6 to physical genes.

    sigma_k = 2*(g_k - g_min)/(g_max - g_min) - 1
    => g_k = g_min + (sigma_k + 1)/2 * (g_max - g_min)
    """
    s = np.asarray(sigma, dtype=float).reshape(-1)
    if s.size != 6:
        raise ValueError("sigma must have length 6: [s_d, s_a, s_r, s_eps, s_ms, s_wr]")
    s = np.clip(s, -1.0, 1.0)
    genes = {}
    for k, name in enumerate(GENE_NAMES):
        lo, hi = GENE_BOUNDS[name]
        genes[name] = float(lo + (s[k] + 1.0) * 0.5 * (hi - lo))
    return genes


def genes_to_sigma(genes: Dict[str, float]) -> np.ndarray:
    """Inverse of sigma_to_genes (MATH-SKELETON 3.1)."""
    out = np.zeros(6, dtype=float)
    for k, name in enumerate(GENE_NAMES):
        lo, hi = GENE_BOUNDS[name]
        g = float(genes[name])
        out[k] = 2.0 * (g - lo) / (hi - lo) - 1.0
    return np.clip(out, -1.0, 1.0)


def clamp(x: Union[float, np.ndarray], lo: float = 0.0, hi: float = 1.0):
    return np.clip(x, lo, hi)


# ---------------------------------------------------------------------------
# Weather (EPW-style)
# ---------------------------------------------------------------------------

@dataclass
class WeatherArray:
    """Hourly EPW-style fields used by the controller.

    radiation, temperature, occupancy, wind_speed may be shape (T,) or (T, N).
    When 1-D they are broadcast to all panels, then given a documented spatial
    modulation (row/column variation on a 10x8 grid).
    """

    radiation: np.ndarray
    temperature: np.ndarray
    occupancy: np.ndarray
    wind_speed: np.ndarray
    hour: np.ndarray
    weekday: np.ndarray
    source: str = "SYNTHETIC_DEMO"
    n_times: int = 0

    def __post_init__(self) -> None:
        self.radiation = np.asarray(self.radiation, dtype=float)
        self.temperature = np.asarray(self.temperature, dtype=float)
        self.occupancy = np.asarray(self.occupancy, dtype=float)
        self.wind_speed = np.asarray(self.wind_speed, dtype=float)
        self.hour = np.asarray(self.hour, dtype=int)
        self.weekday = np.asarray(self.weekday, dtype=int)
        self.n_times = int(self.radiation.shape[0])


def _panel_spatial_weights(n_panels: int = N_PANELS) -> np.ndarray:
    """Mild row/column weights so panels are not identical.

    Higher rows see slightly more radiation (less neighbour shade).
    Centre columns have slightly higher occupancy (interior-adjacent).
    This is geometry bookkeeping for the 10x8 grid, not a new physical model.
    """
    rows = np.arange(n_panels) // N_COLS
    cols = np.arange(n_panels) % N_COLS
    rad_w = 0.92 + 0.16 * (rows / max(N_ROWS - 1, 1))
    occ_w = 0.85 + 0.30 * (1.0 - np.abs(cols - (N_COLS - 1) / 2.0) / (N_COLS / 2.0))
    return rad_w.astype(float), occ_w.astype(float)


def expand_weather(weather: WeatherArray, n_panels: int = N_PANELS) -> WeatherArray:
    """Broadcast 1-D series to (T, N) with spatial weights."""
    T = weather.n_times
    rad_w, occ_w = _panel_spatial_weights(n_panels)

    def _to_TN(arr: np.ndarray, weights: Optional[np.ndarray] = None) -> np.ndarray:
        a = np.asarray(arr, dtype=float)
        if a.ndim == 2:
            if a.shape != (T, n_panels):
                raise ValueError("2-D weather field must have shape (n_times, n_panels)")
            return a
        if a.ndim != 1 or a.shape[0] != T:
            raise ValueError("1-D weather field must have length n_times")
        out = np.repeat(a.reshape(T, 1), n_panels, axis=1)
        if weights is not None:
            out = out * weights.reshape(1, -1)
        return out

    return WeatherArray(
        radiation=_to_TN(weather.radiation, rad_w),
        temperature=_to_TN(weather.temperature, None),
        occupancy=clamp(_to_TN(weather.occupancy, occ_w), 0.0, 1.0),
        wind_speed=_to_TN(weather.wind_speed, None),
        hour=weather.hour,
        weekday=weather.weekday,
        source=weather.source,
        n_times=T,
    )


def make_demo_weather(
    n_hours: int = 168,
    seed: int = 0,
    start_doy: int = 15,
    labelled_synthetic: bool = True,
) -> WeatherArray:
    """Build a small Sydney-like hourly series when no EPW file is present.

    Labelled SYNTHETIC / DEMO. Not an EnergyPlus weather file and not a
    climate-normal product. Used only so the controller can run.
    """
    rng = np.random.default_rng(seed)
    t = np.arange(n_hours)
    hour = t % 24
    doy = (start_doy + t // 24) % 365
    weekday = ((t // 24) + 0) % 7  # start Monday

    # Simple clear-sky-ish daily + seasonal envelope (demo only).
    elev = np.clip(np.sin(np.pi * (hour - 6.0) / 12.0), 0.0, None)
    seasonal = 1.0 + 0.18 * np.sin(2.0 * np.pi * (doy - 15) / 365.0)
    cloud = 0.85 + 0.15 * rng.random(n_hours)
    radiation = 850.0 * elev * seasonal * cloud
    radiation = np.where((hour >= 6) & (hour <= 18), radiation, 0.0)

    temperature = (
        20.0
        + 6.0 * np.sin(2.0 * np.pi * (hour - 8) / 24.0)
        + 4.0 * np.sin(2.0 * np.pi * (doy - 15) / 365.0)
        + rng.normal(0.0, 0.4, n_hours)
    )

    occupied = ((hour >= OCCUPIED_HOUR_START) & (hour < OCCUPIED_HOUR_END) & (weekday < 5))
    occupancy = np.where(occupied, 0.55 + 0.35 * rng.random(n_hours), 0.05 + 0.10 * rng.random(n_hours))
    occupancy = np.clip(occupancy, 0.0, 1.0)

    wind_speed = np.clip(rng.normal(3.5, 1.2, n_hours), 0.0, None)
    # A few gust hours so the SAFE branch is exercised.
    gust_idx = rng.choice(n_hours, size=max(1, n_hours // 80), replace=False)
    wind_speed[gust_idx] = 16.5

    source = "SYNTHETIC_DEMO" if labelled_synthetic else "demo"
    return WeatherArray(
        radiation=radiation,
        temperature=temperature,
        occupancy=occupancy,
        wind_speed=wind_speed,
        hour=hour,
        weekday=weekday,
        source=source,
    )


def load_epw(path: Union[str, Path], n_hours: Optional[int] = None) -> WeatherArray:
    """Parse a standard EnergyPlus EPW file (8 header lines).

    Columns used (0-based, after the 8-line header):
      1 month, 2 day, 3 hour, 6 dry-bulb C,
      13 GHI Wh/m2, 21 wind speed m/s.
    Occupancy is not an EPW field; it is derived from hour / weekday
    (occupied 8-18 weekdays) as in prompt A02.
    """
    path = Path(path)
    rows: List[List[str]] = []
    with path.open(newline="") as fh:
        reader = csv.reader(fh)
        for i, row in enumerate(reader):
            if i < 8:
                continue
            if row:
                rows.append(row)
    if not rows:
        raise ValueError(f"No EPW data rows in {path}")
    if n_hours is not None:
        rows = rows[: int(n_hours)]

    month = np.array([int(float(r[1])) for r in rows])
    day = np.array([int(float(r[2])) for r in rows])
    hour = np.array([int(float(r[3])) % 24 for r in rows])
    temperature = np.array([float(r[6]) for r in rows])
    radiation = np.array([float(r[13]) for r in rows])
    wind_speed = np.array([float(r[21]) for r in rows])

    # Approximate weekday from month/day assuming a non-leap year starting Thursday
    # (EPW convention is often 2017 = Sunday-start; we only need weekday vs weekend).
    doy = _month_day_to_doy(month, day)
    weekday = (doy + 6) % 7  # rough; occupancy uses weekday < 5
    occupied = (hour >= OCCUPIED_HOUR_START) & (hour < OCCUPIED_HOUR_END) & (weekday < 5)
    occupancy = np.where(occupied, 0.7, 0.08).astype(float)

    return WeatherArray(
        radiation=radiation,
        temperature=temperature,
        occupancy=occupancy,
        wind_speed=wind_speed,
        hour=hour,
        weekday=weekday,
        source=f"EPW:{path.name}",
    )


def _month_day_to_doy(month: np.ndarray, day: np.ndarray) -> np.ndarray:
    mdays = np.array([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    cums = np.cumsum(mdays)
    return cums[month - 1] + day - 1


# ---------------------------------------------------------------------------
# TFE  (MATH-SKELETON 1.2-1.4, prompt A03)
# ---------------------------------------------------------------------------

def shannon_entropy(probs: Iterable[float]) -> float:
    """H = -sum p log2 p, ignoring p = 0 (MATH-SKELETON 1.1)."""
    h = 0.0
    for p in probs:
        if p > 0.0:
            h -= p * math.log2(p)
    return h


def _bin_index(state: float, n_bins: int = N_BINS_TFE) -> int:
    # prompt A03: bin_idx = min(int(s * n_bins), n_bins - 1), s in [0, 1]
    s = min(max(float(state), 0.0), 1.0)
    return min(int(s * n_bins), n_bins - 1)


def compute_TFE(
    panel_states: np.ndarray,
    n_bins: int = N_BINS_TFE,
) -> Tuple[float, np.ndarray, np.ndarray]:
    """Temporal Facade Entropy.

    panel_states : array [n_panels][n_times] with values in [0, 1]
                   (angle / 90, as in grasshopper/step-04-TFE.md)

    H_space(t) = Shannon entropy of the 5-bin histogram across panels at t
    H_time(i)  = Shannon entropy of the 5-bin histogram of panel i over time
    TFE(i, t)  = H_space(t) * H_time(i)
    TFE_total  = (1/N) sum_i (1/T) sum_t TFE(i, t)   = mean of the product

    Returns TFE_total, H_space (length T), H_time (length N).
    """
    states = np.asarray(panel_states, dtype=float)
    if states.ndim != 2:
        raise ValueError("panel_states must be 2-D [n_panels, n_times]")
    n_panels, n_times = states.shape
    if n_panels == 0 or n_times == 0:
        return 0.0, np.zeros(0), np.zeros(0)

    H_space = np.zeros(n_times, dtype=float)
    for t in range(n_times):
        hist = np.zeros(n_bins, dtype=float)
        for s in states[:, t]:
            hist[_bin_index(s, n_bins)] += 1.0
        H_space[t] = shannon_entropy(hist / n_panels)

    H_time = np.zeros(n_panels, dtype=float)
    for i in range(n_panels):
        hist = np.zeros(n_bins, dtype=float)
        for s in states[i, :]:
            hist[_bin_index(s, n_bins)] += 1.0
        H_time[i] = shannon_entropy(hist / n_times)

    # TFE_total = mean_{i,t} H_space[t] * H_time[i]
    tfe_total = float(np.mean(H_space[None, :] * H_time[:, None]))
    return tfe_total, H_space, H_time


# ---------------------------------------------------------------------------
# Controller
# ---------------------------------------------------------------------------

@dataclass
class FacadeController:
    """Hysteresis facade controller (formal-model + GhPython).

    Mapping (research/formal-model.md), with solar sign from the existing
    GhPython controller (high radiation -> close):

        solar_response = 1 - R
        target = clamp(wr * solar_response + wt * T + wu * U)

    Remaining weight after wr is split between occupancy and temperature
    (wu : wt = 0.85 : 0.15) so wr + wt + wu = 1. CO2 is omitted unless a
    caller supplies it via ``co2`` (then wc takes 0.10 of the remainder).

    Hysteresis gate (formal-model.md):
        if |target - prev| < epsilon: hold
        else: step by at most maxStep toward target

    SAFE override (formal-model.md): wind > W_limit -> safe default.
    """

    wr: float
    epsilon: float
    max_step: float
    wu: float = 0.0
    wt: float = 0.0
    wc: float = 0.0
    wind_limit: float = WIND_SAFE_LIMIT_M_S
    safe_state: float = SAFE_DEFAULT_STATE

    def __post_init__(self) -> None:
        rem = max(0.0, 1.0 - float(self.wr))
        if self.wu == 0.0 and self.wt == 0.0 and self.wc == 0.0:
            self.wu = 0.85 * rem
            self.wt = 0.15 * rem
            self.wc = 0.0

    def step(
        self,
        previous: np.ndarray,
        radiation: np.ndarray,
        occupancy: np.ndarray,
        temperature: np.ndarray,
        wind_speed: np.ndarray,
        co2: Optional[np.ndarray] = None,
    ) -> np.ndarray:
        """Advance one hour. All arrays length n_panels."""
        r = clamp(np.asarray(radiation, dtype=float) / RADIATION_SCALE_W_M2)
        u = clamp(np.asarray(occupancy, dtype=float))
        # Temperature in [10 C, 35 C] -> [0, 1]
        tnorm = clamp((np.asarray(temperature, dtype=float) - 10.0) / 25.0)
        if co2 is None:
            cnorm = np.zeros_like(r)
        else:
            cnorm = clamp(np.asarray(co2, dtype=float))

        solar_response = 1.0 - r
        target = clamp(
            self.wr * solar_response + self.wt * tnorm + self.wu * u + self.wc * cnorm
        )

        prev = np.asarray(previous, dtype=float)
        delta = target - prev
        hold = np.abs(delta) < self.epsilon
        stepped = prev + np.clip(delta, -self.max_step, self.max_step)
        nxt = np.where(hold, prev, stepped)

        wind = np.asarray(wind_speed, dtype=float)
        unsafe = wind > self.wind_limit
        nxt = np.where(unsafe, self.safe_state, nxt)
        return clamp(nxt)


# ---------------------------------------------------------------------------
# Objectives  (prompt A04 / optimization-setup.md)
# ---------------------------------------------------------------------------

def _effective_opening(state: np.ndarray, aperture: float, rotation_deg: float) -> np.ndarray:
    """Open fraction from controller state, aperture gene, and max rotation.

    state=0 -> closed (0). state=1 -> (rotation/90)*aperture.
    """
    rot_frac = float(rotation_deg) / 90.0
    return clamp(state) * float(aperture) * rot_frac


def _depth_shade_factor(depth_mm: float) -> float:
    """Self-shading from panel depth / reveal.

    Documented qualitative sign: deeper panel reduces transmitted radiation
    (discovery-02-coupling-matrix.md Jacobian for f1 vs d). Linear remap of
    d in [50, 300] mm onto a shade fraction in [0.05, 0.45].
    """
    lo, hi = GENE_BOUNDS["d"]
    u = (float(depth_mm) - lo) / (hi - lo)
    return float(0.05 + 0.40 * np.clip(u, 0.0, 1.0))


def compute_f1_radiation_kwh_m2(
    weather: WeatherArray,
    opening: np.ndarray,
    depth_mm: float,
) -> float:
    """f1: mean incident/transmitted solar radiation [kWh/m2] — MINIMISE.

    Proxy for Ladybug LB Incident Radiation mean (prompt A02). Hourly W/m2
    * opening * (1 - depth_shade), then Wh -> kWh. Not a Ladybug result.
    ``opening`` must be shape (n_times, n_panels), matching weather.radiation.
    """
    shade = _depth_shade_factor(depth_mm)
    transmitted = weather.radiation * opening * (1.0 - shade)
    # Each step is one hour: kWh/m2 = mean over panels of sum_t W/m2 / 1000
    per_panel_kwh = transmitted.sum(axis=0) / 1000.0
    return float(np.mean(per_panel_kwh))


def compute_f2_daylight_deficit(
    weather: WeatherArray,
    opening: np.ndarray,
) -> float:
    """f2: fraction of occupied hours below 300 lux — MINIMISE.

    Occupied hours: 8-18 weekdays (prompt A02). Lux proxy:
        lux = radiation_W_m2 * opening * luminous_efficacy
    ``opening`` must be shape (n_times, n_panels). Not a Honeybee UDI result.
    """
    hour = weather.hour.reshape(-1)
    weekday = weather.weekday.reshape(-1)
    occupied = (hour >= OCCUPIED_HOUR_START) & (hour < OCCUPIED_HOUR_END) & (weekday < 5)
    if not np.any(occupied):
        return 0.0
    lux = weather.radiation * opening * LUMINOUS_EFFICACY_LM_PER_W
    mean_lux = lux.mean(axis=1)
    deficit = mean_lux[occupied] < LUX_THRESHOLD
    return float(np.mean(deficit))


def compute_f3_unique_geometries(
    genes: Dict[str, float],
    layer_counts: Optional[Sequence[int]] = None,
) -> int:
    """f3: number of unique panel geometry types — MINIMISE.

    A single gene vector programs one (depth, aperture, rotation) SKU, so
    f3 = 1. If D03 layer_counts are supplied, f3 is the number of unique
    n_layers values (programmable spore-panel types).
    """
    if layer_counts is None:
        return 1
    return int(len(set(int(x) for x in layer_counts)))


def compute_f4_actuation_events_per_day(
    states: np.ndarray,
    n_hours: int,
) -> float:
    """f4: mean daily actuation events per panel — MINIMISE.

    An event is a time step where the hysteresis gate allowed movement
    (state changed). Prompt A04 / formal-model.md.
    """
    if states.shape[1] < 2:
        return 0.0
    moved = np.abs(np.diff(states, axis=1)) > 1e-12
    events_per_panel = moved.sum(axis=1).astype(float)
    n_days = max(n_hours / 24.0, 1.0 / 24.0)
    return float(np.mean(events_per_panel / n_days))


# ---------------------------------------------------------------------------
# Simulation result + runner
# ---------------------------------------------------------------------------

@dataclass
class SimulationResult:
    panel_angle_series: np.ndarray
    panel_state_series: np.ndarray
    f1: float
    f2: float
    f3: float
    f4: float
    TFE_total: float
    H_space: np.ndarray
    H_time: np.ndarray
    genes: Dict[str, float]
    sigma: np.ndarray
    weather_source: str
    notes: List[str] = field(default_factory=list)

    def summary(self) -> Dict[str, object]:
        return {
            "sigma": [float(x) for x in self.sigma],
            "genes": {k: round(v, 6) for k, v in self.genes.items()},
            "f1_kwh_m2": self.f1,
            "f2_daylight_deficit": self.f2,
            "f3_unique_geometries": self.f3,
            "f4_mean_daily_actuations": self.f4,
            "TFE_total": self.TFE_total,
            "panel_angle_series_shape": list(self.panel_angle_series.shape),
            "weather_source": self.weather_source,
            "notes": list(self.notes),
        }


def simulate(
    weather: WeatherArray,
    sigma: Sequence[float],
    n_panels: int = N_PANELS,
    layer_counts: Optional[Sequence[int]] = None,
    initial_state: float = 0.5,
) -> SimulationResult:
    """Run the facade controller over a weather array.

    Parameters
    ----------
    weather : WeatherArray
        EPW-style hourly fields (see load_epw / make_demo_weather).
    sigma : length-6 sequence
        Normalised genes in [-1, +1].
    n_panels : int
        Default 80 (10x8).
    layer_counts : optional per-panel D03 layer counts (affects f3 only).
    initial_state : starting openness in [0, 1].
    """
    genes = sigma_to_genes(sigma)
    sigma_arr = genes_to_sigma(genes)
    wx = expand_weather(weather, n_panels=n_panels)
    T = wx.n_times

    controller = FacadeController(
        wr=genes["wr"],
        epsilon=genes["eps"],
        max_step=genes["ms"],
    )
    states = np.zeros((n_panels, T), dtype=float)
    prev = np.full(n_panels, float(initial_state), dtype=float)
    for t in range(T):
        prev = controller.step(
            previous=prev,
            radiation=wx.radiation[t],
            occupancy=wx.occupancy[t],
            temperature=wx.temperature[t],
            wind_speed=wx.wind_speed[t],
        )
        states[:, t] = prev

    angles = states * genes["r"]  # theta = openness * max rotation (deg)
    # TFE uses angle / 90  (grasshopper/step-04-TFE.md)
    tfe_states = angles / 90.0
    tfe_total, h_space, h_time = compute_TFE(tfe_states)

    # weather fields are (T, N); controller series are (N, T)
    opening_TN = _effective_opening(states.T, genes["a"], genes["r"])
    f1 = compute_f1_radiation_kwh_m2(wx, opening_TN, genes["d"])
    f2 = compute_f2_daylight_deficit(wx, opening_TN)
    f3 = compute_f3_unique_geometries(genes, layer_counts=layer_counts)
    f4 = compute_f4_actuation_events_per_day(states, T)

    notes = [
        "f1/f2 are geometric proxies, not Ladybug/Honeybee outputs.",
        f"weather_source={wx.source}",
        "TFE uses 5-bin Shannon entropy (MATH-SKELETON 1.4 / prompt A03).",
    ]
    if str(wx.source).startswith("SYNTHETIC"):
        notes.append("Weather is SYNTHETIC/DEMO — not an EPW observation series.")

    return SimulationResult(
        panel_angle_series=angles,
        panel_state_series=states,
        f1=f1,
        f2=f2,
        f3=f3,
        f4=f4,
        TFE_total=tfe_total,
        H_space=h_space,
        H_time=h_time,
        genes=genes,
        sigma=sigma_arr,
        weather_source=wx.source,
        notes=notes,
    )


def simulate_static(
    weather: WeatherArray,
    angle_deg: float = 0.0,
    n_panels: int = N_PANELS,
    genes: Optional[Dict[str, float]] = None,
) -> SimulationResult:
    """Static envelope (all panels fixed). Implementation check: TFE ~ 0."""
    if genes is None:
        genes = sigma_to_genes(SIGMA_STAR)
    wx = expand_weather(weather, n_panels=n_panels)
    T = wx.n_times
    angles = np.full((n_panels, T), float(angle_deg), dtype=float)
    states = np.full((n_panels, T), float(angle_deg) / max(genes["r"], 1e-9), dtype=float)
    states = clamp(states)
    tfe_states = angles / 90.0
    tfe_total, h_space, h_time = compute_TFE(tfe_states)
    opening_TN = _effective_opening(states.T, genes["a"], genes["r"])
    return SimulationResult(
        panel_angle_series=angles,
        panel_state_series=states,
        f1=compute_f1_radiation_kwh_m2(wx, opening_TN, genes["d"]),
        f2=compute_f2_daylight_deficit(wx, opening_TN),
        f3=1,
        f4=0.0,
        TFE_total=tfe_total,
        H_space=h_space,
        H_time=h_time,
        genes=genes,
        sigma=genes_to_sigma(genes),
        weather_source=wx.source,
        notes=["static controller — implementation check, not a Wallacei result"],
    )


# ---------------------------------------------------------------------------
# CLI demo
# ---------------------------------------------------------------------------

def _find_default_epw(search_roots: Sequence[Path]) -> Optional[Path]:
    for root in search_roots:
        if not root.exists():
            continue
        for p in root.rglob("*.epw"):
            return p
    return None


def run_demo(epw: Optional[Path] = None, n_hours: int = 168, seed: int = 0) -> SimulationResult:
    if epw is None:
        epw = _find_default_epw(
            [
                Path.cwd(),
                Path(__file__).resolve().parent,
                Path(__file__).resolve().parents[2],
            ]
        )
    if epw is not None and epw.is_file():
        weather = load_epw(epw, n_hours=n_hours)
        print(f"Loaded EPW: {epw}  ({weather.n_times} hours)")
    else:
        weather = make_demo_weather(n_hours=n_hours, seed=seed)
        print(
            "No EPW file found. Using SYNTHETIC/DEMO weather "
            f"({weather.n_times} hours). Not observational climate data."
        )

    result = simulate(weather, SIGMA_STAR)
    static = simulate_static(weather, angle_deg=0.0, genes=result.genes)

    s = result.summary()
    print("=== HE facade-sim demo ===")
    print(f"sigma (documented sigma* default): {s['sigma']}")
    print(f"genes: {s['genes']}")
    print(f"panel_angle_series shape: {s['panel_angle_series_shape']}")
    print(f"f1 mean radiation proxy [kWh/m2]: {result.f1:.6f}")
    print(f"f2 daylight deficit (<300 lux occ. hours): {result.f2:.6f}")
    print(f"f3 unique geometries: {result.f3}")
    print(f"f4 mean daily actuations / panel: {result.f4:.6f}")
    print(f"TFE_total: {result.TFE_total:.6f}")
    print(
        f"implementation check (not a discovery claim): "
        f"TFE_static={static.TFE_total:.6f}  TFE_adaptive={result.TFE_total:.6f}"
    )
    for n in result.notes:
        print(f"note: {n}")
    return result


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="HE facade controller simulator")
    parser.add_argument("--epw", type=Path, default=None, help="Optional EnergyPlus EPW path")
    parser.add_argument("--hours", type=int, default=168, help="Hours to simulate (default 168)")
    parser.add_argument("--seed", type=int, default=0, help="Demo-weather RNG seed")
    args = parser.parse_args(argv)
    run_demo(epw=args.epw, n_hours=args.hours, seed=args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
