# Evidence Report

## Status: Step 9 — Living document, updated as steps complete

This document classifies every major claim in the project against the four-level evidence ladder.

Levels:
- L0  conceptual analogy only
- L1  computationally reproducible model
- L2  simulated performance outcome
- L3  physical prototype demonstration
- L4  comparative evidence against baseline

---

## Claim 1
**Statement:** An adaptive facade can be modelled as a boundary function mapping environmental inputs to panel states.

| Field | Value |
|---|---|
| Evidence level | L1 |
| Source | GhPython state controller (this repo) + systematic review Tandf 2026 DOI 10.1080/17452007.2026.2658645 |
| Status | Confirmed at L1, simulation (L2) pending |
| Path to upgrade | Run Ladybug simulation with Sydney EPW → Step 6 |

---

## Claim 2
**Statement:** PCM integration in building envelopes reduces energy consumption by 15–45%.

| Field | Value |
|---|---|
| Evidence level | L2 |
| Source | Energies MDPI 2026 DOI 10.3390/en19051151 (300+ studies) |
| Status | Confirmed at L2 in literature. Not yet prototyped in this project. |
| Path to upgrade | Add PCM layer to Step 7 prototype for thermal measurement |

---

## Claim 3
**Statement:** Mechanical metamaterials with auxetic or deployable geometry can produce repeatable shape change without external energy input.

| Field | Value |
|---|---|
| Evidence level | L1–L2 |
| Source | Taylor & Francis 2026 DOI 10.1080/19475411.2026.2714783 + Swansea review 2024 |
| Status | Confirmed in non-architectural contexts. Architectural prototype (L3) pending Step 7. |
| Path to upgrade | Build 5-panel metamaterial prototype → Step 7 |

---

## Claim 4
**Statement:** Hygromorphic cellulosic bilayers can actuate passively at architectural scale.

| Field | Value |
|---|---|
| Evidence level | L3 |
| Source | Nature Communications 2024 DOI 10.1038/s41467-024-54808-8 |
| Status | Confirmed at L3 in literature for architectural-scale demonstration. |
| Path to upgrade | Reproduce at 1:5 scale in this project → Step 7 |

---

## Claim 5
**Statement:** The holographic principle from black-hole physics directly applies to building envelopes.

| Field | Value |
|---|---|
| Evidence level | L0 |
| Source | Conceptual analogy only |
| Status | NOT a physical claim. Used only as information analogy (boundary encodes interior state). See Axiom A5. |
| Path to upgrade | No upgrade path for the physics claim. The information version upgrades via facade entropy H(t) measurement in Step 6. |

---

## Claim 6
**Statement:** Facade state distribution can be measured as Shannon entropy H(t), providing a formal information-theoretic metric for boundary complexity.

| Field | Value |
|---|---|
| Evidence level | L1 |
| Source | Formal model (this repo, research/formal-model.md) + Shannon 1948 |
| Status | Mathematically defined. Not yet computed from simulation output. |
| Path to upgrade | Compute H(t) from Step 6 simulation output per hour |

---

## Claim 7
**Statement:** Multi-objective facade optimisation exhibits a frustration-like landscape analogous to spin-glass systems.

| Field | Value |
|---|---|
| Evidence level | L0 |
| Source | Structural analogy to spin-glass frustration literature (combinatorial optimisation) |
| Status | NOT yet computationally tested in architectural context. This is the project's most novel and most uncertain claim. |
| Path to upgrade | Run Wallacei optimisation (Step 8). If Pareto front shows multi-modal clustering, upgrade to L1. |

---

## Claim 8
**Statement:** The SYK model or quantum chaos directly governs facade behaviour.

| Field | Value |
|---|---|
| Evidence level | L0 — REJECTED as literal claim |
| Source | No architectural or building physics literature supports this |
| Status | Removed from main research narrative per Axiom A5. |
| Path to upgrade | None. This claim is permanently bounded as illustrative analogy only. |

---

## Summary table

| Claim | Level | Status |
|---|---|---|
| Facade as boundary function | L1 | Confirmed, simulation pending |
| PCM energy savings 15–45% | L2 | Confirmed in literature |
| Metamaterial shape change | L1–L2 | Confirmed, prototype pending |
| Hygromorphic actuation at scale | L3 | Confirmed in literature |
| Holographic physics equivalence | L0 | Rejected as literal claim |
| Facade Shannon entropy H(t) | L1 | Defined, computation pending |
| Frustration landscape analogy | L0 | Most novel claim, Step 8 will test it |
| SYK direct application | L0 | Permanently rejected as literal claim |
