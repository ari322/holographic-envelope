# STATUS BOARD
# Updated by agents as they complete tasks
# Human reviewer: check this file to monitor parallel progress

| Agent | Last completed | Next task | Blocked |
|-------|---------------|-----------|--------|
| MATHEMATICIAN  | — (not started) | coupling-matrix-derivation.md | NO |
| SIMULATOR      | Role 02 pack: grasshopper-complete.md + facade-sim.py + rsb-detection.py + SYNTHETIC synthetic-pareto.json (2026-09-23) | DONE | NO |
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

## SIMULATOR Role 02 notes (2026-09-23) — queue empty

All four Role 02 deliverables are in `agents/simulator/`. Next task = DONE.

| File | Role 02 task |
|------|----------------|
| `grasshopper-complete.md` | Task 1 — full 5-step GH node sequence (02/03/05 filled in) |
| `facade-sim.py` | Task 2 — standalone controller |
| `rsb-detection.py` | Task 3 — GMM + Hartigan dip |
| `synthetic-pareto.json` | Task 4 — **SYNTHETIC** 5x50 fixture |

Also: `generate_synthetic_pareto.py`, `README.md`, `requirements.txt`.

How to run:

```
python agents/simulator/facade-sim.py
python agents/simulator/rsb-detection.py
```

SYNTHETIC reminder: `synthetic-pareto.json` is constructed (two planted gene families). It is not Wallacei output and is not evidence for RSB / D02. Demo weather in `facade-sim.py` is labelled `SYNTHETIC_DEMO` when no EPW file is present. f1/f2 are geometric proxies, not Ladybug/Honeybee.

## Human Notes

_Add notes here when reviewing agent outputs._
