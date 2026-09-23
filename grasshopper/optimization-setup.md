# Frustration Landscape — Optimisation Setup

## Status: Step 8 — Framework complete, Wallacei run pending

---

## The core scientific question of this step

In spin-glass physics, a frustrated system has an energy landscape with many local minima and no single global optimum. The system does not converge — it distributes across a landscape of near-equivalent states.

In multi-objective architectural optimisation, the same structure appears: no design simultaneously minimises solar gain, maximises daylight, minimises fabrication complexity, and minimises actuation energy. The Pareto front IS the frustration landscape.

**Falsification criterion for the analogy:** If the Wallacei Pareto front shows clear multi-modal clustering (multiple distinct solution families rather than a smooth curve), the spin-glass analogy gains computational support (upgrades from L0 to L1). If the front is smooth and unimodal, the analogy remains illustrative but loses explanatory power for this specific system.

---

## Objectives

    f1 = mean incident solar radiation across all panels (kWh/m2)  — MINIMISE
    f2 = daylight deficit: fraction of hours below 300 lux          — MINIMISE
    f3 = number of unique panel geometries (fabrication cost proxy)  — MINIMISE
    f4 = total actuation events per simulated day                    — MINIMISE

f1 and f2 are directly in conflict: opening panels improves daylight but increases solar gain.
f3 and f4 are in conflict with f1 and f2: more responsive panels improve performance but increase complexity and wear.

This four-objective conflict structure is the formal equivalent of frustration.

---

## Gene variables (Wallacei genome)

| Gene | Range | Description |
|---|---|---|
| panel_depth | 50–300 mm | Depth of panel reveal |
| aperture_ratio | 0.1–0.9 | Max open fraction |
| rotation_angle | 0–90 deg | Maximum rotation |
| epsilon | 0.01–0.15 | Hysteresis dead band |
| maxStep | 0.05–0.30 | Max change per time step |
| wr | 0.2–0.8 | Weight of radiation in mapping |

---

## Solver setup

- **Single objective:** Galapagos (evolutionary solver, built into Grasshopper)
- **Multi-objective Pareto:** Wallacei X plugin for Grasshopper
  - Population: 50 individuals
  - Generations: 100 minimum
  - Crossover rate: 0.9
  - Mutation rate: 0.1
  - Objectives: f1, f2, f3, f4 (all minimised)

---

## Expected output

1. Pareto front visualisation: 4D scatter (f1 vs f2 vs f3 vs f4)
2. Solution family identification: do clusters exist?
3. Dominant gene values per cluster: which panel geometry drives each family?
4. Recommendation: which solution from the Pareto front is most buildable?

---

## Connection to spin-glass physics

The formal connection is not that facade panels ARE spins.
The connection is structural:
- Spin glass: many interacting degrees of freedom, conflicting constraints, no global minimum.
- Facade optimisation: many panel parameters, conflicting performance objectives, no globally optimal design.
- Both systems explore their state space and settle into locally stable configurations.
- Both exhibit sensitivity to initial conditions and parameter perturbations.

This is a bounded, falsifiable, computationally testable analogy — not a claim of physical equivalence.
