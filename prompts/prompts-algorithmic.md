# Prompts — Algorithmic, Grasshopper, and Python

> For computational designers using Grasshopper + Wallacei + Python.
> Each prompt is executable as a task briefing.

---

## A01 — Grasshopper Geometry Setup

```
You are a Grasshopper expert helping build an adaptive facade simulation.

Write the complete node sequence (as pseudocode describing each Grasshopper node
and its connections) for the following geometry:

- A 10m × 8m rectangular facade surface
- Divided into a 10×8 grid = 80 panels
- Each panel is a rectangular solid: width=1m, height=1m, depth=variable (gene d)
- Each panel has a pivot axis at its top edge
- Each panel can rotate around its top edge by angle θ ∈ [0°, 90°]
- Panel rotation is driven by a slider (for manual testing) AND by a gene value (for Wallacei)

Provide: list of Grasshopper components, parameter names, and data flow connections.
```

---

## A02 — Ladybug Radiation Analysis

```
You are a Grasshopper + Ladybug expert.

Write the pseudocode for computing cumulative annual solar radiation on 80 facade panels:
- Input: Grasshopper geometry from A01, Sydney EPW weather file
- Component: LB Incident Radiation
- Output: per-panel radiation value in kWh/m² per year
- Aggregate: mean radiation across all panels = objective f1

Also write the Honeybee daylight simulation for UDI (Useful Daylight Illuminance):
- Occupied hours: 8am-6pm weekdays
- Target: fraction of occupied hours below 300 lux = objective f2
- Output: per-zone UDI value, aggregate to facade mean
```

---

## A03 — TFE Computation in Python (Grasshopper GHPython node)

```python
# PASTE THIS INTO A GHPYTHON NODE IN GRASSHOPPER
# Inputs: panel_states (list of lists: [panel_index][time_step] = state_value)
# Outputs: TFE_total (float), H_space_series (list), H_time_series (list)

import math

def shannon_entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

def compute_TFE(panel_states):
    N = len(panel_states)       # number of panels
    T = len(panel_states[0])    # number of time steps
    
    # Discretise states into bins
    n_bins = 5
    
    # H_space(t): entropy of panel state distribution at each time t
    H_space = []
    for t in range(T):
        states_at_t = [panel_states[i][t] for i in range(N)]
        hist = [0] * n_bins
        for s in states_at_t:
            bin_idx = min(int(s * n_bins), n_bins - 1)
            hist[bin_idx] += 1
        probs = [h / N for h in hist]
        H_space.append(shannon_entropy(probs))
    
    # H_time(i): entropy of time series for each panel i
    H_time = []
    for i in range(N):
        time_series = panel_states[i]
        hist = [0] * n_bins
        for s in time_series:
            bin_idx = min(int(s * n_bins), n_bins - 1)
            hist[bin_idx] += 1
        probs = [h / T for h in hist]
        H_time.append(shannon_entropy(probs))
    
    # TFE(i, t) = H_space(t) * H_time(i)
    TFE_matrix = [[H_space[t] * H_time[i] for t in range(T)] for i in range(N)]
    TFE_total = sum(TFE_matrix[i][t] for i in range(N) for t in range(T)) / (N * T)
    
    return TFE_total, H_space, H_time

TFE_total, H_space_series, H_time_series = compute_TFE(panel_states)
```

---

## A04 — Wallacei Setup Briefing

```
You are a Wallacei expert helping configure a multi-objective optimisation in Grasshopper.

Configure Wallacei X for the following problem:

Genes (6 total, all continuous):
  Gene 1: panel_depth         range [50, 300] mm
  Gene 2: aperture_ratio      range [0.1, 0.9]
  Gene 3: rotation_angle      range [0, 90] degrees
  Gene 4: hysteresis_epsilon  range [0.01, 0.15]
  Gene 5: maxStep             range [0.05, 0.30]
  Gene 6: radiation_weight    range [0.2, 0.8]

Objectives (4 total, all minimise):
  f1: mean incident solar radiation [kWh/m²]
  f2: daylight deficit (fraction occupied hours < 300 lux)
  f3: number of unique panel geometry types (fabrication cost proxy)
  f4: mean daily actuation events per panel (operational complexity)

Settings:
  Population size: 50
  Generations: 100
  Run 5 times with different random seeds: [42, 137, 256, 891, 1024]

Output required:
  - Full Pareto front from each run (gene values + objective values)
  - Convergence plots
  - Pairwise gene distance matrix for RSB detection
```

---

## A05 — RSB Detection in Python

```python
# RSB Detection Protocol for Wallacei output
# Input: pareto_solutions — list of gene vectors from all 5 Wallacei runs
# Output: dip_statistic, p_value, n_clusters, cluster_labels

import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

def compute_pairwise_distances(pareto_solutions):
    n = len(pareto_solutions)
    sols = np.array(pareto_solutions)  # shape (n, 6)
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(sols[i] - sols[j]) / np.sqrt(6)
            distances.append(d)
    return np.array(distances)

def fit_gmm_and_select_k(distances, k_max=5):
    d_reshaped = distances.reshape(-1, 1)
    bic_scores = []
    for k in range(1, k_max+1):
        gmm = GaussianMixture(n_components=k, random_state=42)
        gmm.fit(d_reshaped)
        bic_scores.append(gmm.bic(d_reshaped))
    best_k = np.argmin(bic_scores) + 1
    best_gmm = GaussianMixture(n_components=best_k, random_state=42)
    best_gmm.fit(d_reshaped)
    labels = best_gmm.predict(np.array(pareto_solutions))
    return best_k, labels, bic_scores

# Usage:
# distances = compute_pairwise_distances(pareto_solutions)
# k, labels, bic = fit_gmm_and_select_k(distances)
# if k >= 2: print('RSB equivalent detected')
```

---

## A06 — BIR Measurement from Building Sensor Data

```python
# BIR Computation from real sensor data
# Inputs: facade_log (panel states over time), interior_sensors (dict of sensor time series)
# Output: BIR time series

import math
import numpy as np

def shannon_entropy_continuous(values, n_bins=10):
    hist, _ = np.histogram(values, bins=n_bins, density=False)
    total = sum(hist)
    probs = [h/total for h in hist if h > 0]
    return -sum(p * math.log2(p) for p in probs)

def compute_BIR_timeseries(facade_log, interior_sensors, window=24):
    """
    facade_log: dict {panel_id: [state_t0, state_t1, ...]}
    interior_sensors: dict {sensor_name: [value_t0, value_t1, ...]}
    window: rolling window in timesteps
    """
    T = len(next(iter(facade_log.values())))
    BIR_series = []
    
    for t in range(window, T):
        # H_boundary: spatial entropy of panel states in window
        states_window = [facade_log[p][t-window:t] for p in facade_log]
        flat_states = [s for panel in states_window for s in panel]
        H_boundary = shannon_entropy_continuous(flat_states)
        
        # H_interior: joint entropy of interior sensors in window
        sensor_values = [interior_sensors[s][t-window:t] for s in interior_sensors]
        H_interior = sum(shannon_entropy_continuous(sv) for sv in sensor_values)
        H_interior = H_interior / len(sensor_values)  # normalise
        
        BIR = min(H_boundary / H_interior, 1.0) if H_interior > 0 else 0.0
        BIR_series.append(BIR)
    
    return BIR_series
```
