# Simulation Baseline Plan

## Status: Step 6 — Framework complete, simulation pending EPW run

---

## Three scenarios to compare

| Scenario | Description |
|---|---|
| S0 — Static closed | All panels fully closed at all times |
| S1 — Static open | All panels fully open at all times |
| S2 — Adaptive | GhPython state controller active |

---

## Target metrics

| Metric | Unit | Target for S2 vs S0 |
|---|---|---|
| Mean incident radiation | kWh/m2/year | Reduce by at least 10% |
| UDI 100–2000 lux | % of occupied hours | Increase by at least 10% |
| Open-area ratio | % of panel area open | Measurable variation (not constant) |
| Actuation events | events/day | < 8 per panel on average |
| Facade entropy H(t) | bits | H > 0 for at least 50% of occupied hours |

---

## EPW file

- Location: Sydney, NSW, Australia
- Recommended file: Sydney Observatory Hill (lat -33.86, lon 151.21) or Bankstown
- Source: EnergyPlus Weather Data (energyplus.net/weather)
- Analysis period: full year, occupied hours 8:00–18:00

---

## Grasshopper setup for simulation

1. Load EPW with LB Import EPW.
2. Generate annual sky matrix with LB SkyMatrix.
3. Apply to facade mesh with LB Incident Radiation.
4. Compare raw radiation output for S0, S1, S2.
5. Run Honeybee UDI analysis for S2 only (S0 and S1 use theoretical limits).
6. Export all results as CSV from GhPython.

---

## Falsification criterion

If S2 does not outperform S0 by at least 10% on the primary radiation metric:
- The weight parameters (wr, wu) must be recalibrated.
- The panel grid density must be reviewed.
- If after recalibration the improvement is less than 5%, the adaptive logic must be redesigned before claiming performance benefit.

---

## Status note

This plan is ready to execute. Actual numerical results require a Rhino/Grasshopper session with a Sydney EPW file loaded. Results will be added to this file as a table once the simulation is run.
