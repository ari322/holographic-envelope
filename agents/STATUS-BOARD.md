# STATUS BOARD
# Updated by agents as they complete tasks
# Human reviewer: check this file to monitor parallel progress

| Agent | Last completed | Next task | Blocked |
|-------|---------------|-----------|--------|
| MATHEMATICIAN  | — (not started) | coupling-matrix-derivation.md | NO |
| SIMULATOR      | Task 2: facade-sim.py + SYNTHETIC Pareto + rsb-detection.py (2026-09-23) | grasshopper-complete.md (Task 1) | NO |
| MATERIALS      | — (not started) | spore-data-survey.md | NO |
| THEORIST       | — (not started) | TFE-Kolmogorov.md | NO |
| WRITER         | — (not started) | abstract-v1.md | NO |
| OCTOPUS-BRIDGE | — (not started) | TFE-for-agents.md | NO |
| CRITIC         | — (not started) | unsupported-claims.md | NO |

---

## Conflict Log

| Conflict ID | Description | Raised by | Status |
|------------|-------------|-----------|--------|
| — | no conflicts yet | — | — |

---

## SIMULATOR Task 2 notes (2026-09-23)

Files added under `agents/simulator/`:

- `facade-sim.py` — standalone controller. Inputs: EPW-style weather + `sigma`. Outputs: `panel_angle_series`, `f1`–`f4`, `TFE_total`.
- `rsb-detection.py` — pairwise `d = ||ga-gb||_2 / sqrt(6)`, Hartigan dip, GMM+BIC on `P_arch(d)`.
- `generate_synthetic_pareto.py` — writes the fixture (5 runs x 50 solutions, seeds 42/137/256/891/1024).
- `synthetic-pareto.json` — **SYNTHETIC** test fixture only.
- `README.md`, `requirements.txt`

How to run:

```
python agents/simulator/facade-sim.py
python agents/simulator/rsb-detection.py
```

SYNTHETIC reminder: `synthetic-pareto.json` is constructed (two planted gene families). It is not Wallacei output and is not evidence for RSB / D02. Demo weather in `facade-sim.py` is labelled `SYNTHETIC_DEMO` when no EPW file is present. f1/f2 are geometric proxies, not Ladybug/Honeybee.

## Human Notes

_Add notes here when reviewing agent outputs._
