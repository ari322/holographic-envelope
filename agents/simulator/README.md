# SIMULATOR workspace (Task 2)

Standalone Python tools for the Holographic Envelope controller and for
testing the documented RSB detection protocol.

No Grasshopper. No Rhino. Dependencies: `numpy`, `scipy`, `scikit-learn`.

## Files

| File | What it is |
|------|------------|
| `grasshopper-complete.md` | Full 5-step Grasshopper node sequence (02/03/05 filled in) |
| `facade-sim.py` | Facade controller + TFE + f1–f4 |
| `rsb-detection.py` | Hartigan dip + GMM on pairwise gene distances |
| `generate_synthetic_pareto.py` | Writes the SYNTHETIC Pareto fixture |
| `synthetic-pareto.json` | **SYNTHETIC** 5×50 gene vectors (not Wallacei) |
| `requirements.txt` | numpy / scipy / scikit-learn |

## How to run

From the repository root (or this folder):

```bash
pip install -r agents/simulator/requirements.txt

# Controller demo (uses SYNTHETIC/DEMO weather if no .epw is found)
python agents/simulator/facade-sim.py
python agents/simulator/facade-sim.py --hours 168
python agents/simulator/facade-sim.py --epw /path/to/sydney.epw --hours 8760

# Regenerate SYNTHETIC Pareto fixture (overwrites JSON)
python agents/simulator/generate_synthetic_pareto.py

# RSB detector on the bundled SYNTHETIC file
python agents/simulator/rsb-detection.py
python agents/simulator/rsb-detection.py --input agents/simulator/synthetic-pareto.json
```

`facade-sim.py` has a hyphen, so other agents should load it with
`importlib` rather than `import facade-sim`:

```python
import importlib.util
from pathlib import Path
p = Path("agents/simulator/facade-sim.py")
spec = importlib.util.spec_from_file_location("facade_sim", p)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.simulate(mod.make_demo_weather(), mod.SIGMA_STAR)
print(result.TFE_total, result.f1, result.f2, result.f3, result.f4)
print(result.panel_angle_series.shape)  # (80, T)
```

## SYNTHETIC data — read this

`synthetic-pareto.json` is a **constructed test fixture**.

- Labelled `SYNTHETIC` in the filename context, JSON `label` / `data_class`,
  every run, and every solution.
- Two planted gene-space families exist so `rsb-detection.py` can be checked.
- It is **not** Wallacei output, **not** a Sydney EPW run, **not** facade-sim
  output, and **not** evidence for Discovery 02 or Replica Symmetry Breaking.
- A rule hit (`p < 0.05` and `K >= 2`) on this file only means the detector
  responded to the planted structure. Do not upgrade any evidence class.

Demo weather inside `facade-sim.py` is likewise labelled `SYNTHETIC_DEMO`
when no EPW file is present.

## What the controller implements (and what it does not)

Implemented from the HE docs:

- Gene vector `sigma` in `[-1, +1]^6` and bounds from MATH-SKELETON 3.1
- Hysteresis controller from `research/formal-model.md` and
  `grasshopper/ghpython_state_controller.py` (high radiation closes panels)
- TFE from MATH-SKELETON 1.4 / prompt A03 (5-bin Shannon product)
- Objectives f1–f4 names and units from prompt A04

Not implemented here (pending Grasshopper / materials / critic):

- Ladybug incident radiation or Honeybee UDI (f1/f2 are geometric proxies)
- A real Wallacei optimisation
- Any claim that RSB is confirmed
- Octopus integration
