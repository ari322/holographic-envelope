# Adaptive Architectural Envelopes as Information-Processing Boundaries
## Research Paper Draft v1

**Status:** Step 10 — Draft complete, simulation results pending for Section 6

---

## 1. Introduction

Architectural envelopes are the primary interface between interior space and exterior environment. Conventional static facades are designed for average conditions; they cannot respond to the dynamic range of real environmental and occupancy data. Adaptive and kinetic facades have received increasing research attention over the past four decades, with systematic reviews identifying growing evidence for performance benefits in energy and daylight regulation.

This paper proposes a formal framework for adaptive envelopes as boundary functions: deterministic, measurable, and falsifiable mappings from environmental input vectors to panel state vectors. The framework draws on bounded conceptual transfers from information theory, phase transition physics, and multi-objective optimisation to generate testable design hypotheses, while explicitly rejecting any claim of direct physical equivalence between building facades and quantum gravity phenomena.

The contribution of this paper is threefold:
1. A formal mathematical model for adaptive panel state control with hysteresis and discrete state machines.
2. A computational workflow implemented in Grasshopper and GhPython, validated against a Sydney climate EPW file.
3. A falsifiable optimisation framework that tests whether multi-objective facade design exhibits a frustration-like Pareto landscape.

---

## 2. Conceptual Framework

### 2.1 Boundary encoding as information analogy

The holographic principle in theoretical physics states that the information content of a volume can be encoded on its lower-dimensional boundary. This paper borrows only the information-theoretic structure of this idea, not its physical content. The claim is bounded: a facade with spatially differentiated panel states encodes information about interior conditions on the exterior boundary. This is quantifiable using Shannon entropy H(t) across the panel state distribution.

### 2.2 Phase transition as state logic

Phase transitions describe systems that shift between qualitatively different states as a control parameter crosses a threshold. In building envelopes, this maps to discrete state switching: CLOSED, SHADED, VENTILATE, OPEN, SAFE. The analogy is used to motivate the state machine design in Section 3, not to claim that building materials undergo quantum phase transitions.

### 2.3 Spin-glass frustration as optimisation analogy

Spin-glass systems in condensed matter physics exhibit frustration: competing interactions prevent convergence to a single global energy minimum, producing a landscape of many local minima. Multi-objective facade optimisation has the same formal structure: competing objectives (solar gain, daylight, fabrication complexity, actuation energy) prevent a single globally optimal design. The Pareto front is the architectural equivalent of the spin-glass energy landscape.

This analogy is falsifiable: if a Wallacei optimisation of the facade system produces a multi-modal Pareto front with distinct solution clusters, the analogy gains computational support. If the front is smooth and unimodal, the analogy loses explanatory relevance for this system.

---

## 3. Formal Model

### 3.1 Mapping function

For panel i at time t:

    o_i(t) = clamp( w_r*R_i + w_t*T_i + w_c*C_i + w_u*U_i , 0, 1 )

Inputs are normalised to [0,1]. Weights sum to 1.0. Output 0 = fully closed, 1 = fully open.

### 3.2 Hysteresis gate

    if |o_i(t) - o_i(t-1)| < epsilon: hold
    else: step by min(|delta|, maxStep)

Epsilon = 0.05, maxStep = 0.10 as default starting values.

### 3.3 Discrete state machine

Priority order: SAFE > VENTILATE > SHADED > OPEN > CLOSED

SAFE is a hard override activated by sensor failure, wind above limit, or power loss.

### 3.4 Information entropy

    H(t) = - sum_i [ p_i * log2(p_i) ]

p_i = normalised open ratio of panel i. H > 0 indicates spatially differentiated facade state, the formal definition of boundary information encoding in this project.

---

## 4. Computational Workflow

The workflow is implemented in Rhino/Grasshopper with Ladybug Tools for climate analysis. The full component chain is documented in grasshopper/workflow.md in this repository.

Key steps:
- Surface panelisation using Divide Domain2 and Isotrim
- Incident radiation per panel using LB Incident Radiation with a Sydney EPW sky matrix
- Occupancy as normalised proximity of agent point cloud to panel centroids
- State control via GhPython state controller (grasshopper/ghpython_state_controller.py)
- Geometric response: rotation or aperture scaling per panel
- Output: panel states as list, facade entropy H(t), CSV export for analysis

---

## 5. Material Strategy

Five material families were evaluated: phase change materials (PCM), shape memory alloys (SMA), shape memory polymers (SMP), hygromorphic systems, and mechanical metamaterials.

For this prototype, mechanical metamaterials (auxetic or deployable lattice, FDM-printed) are recommended as the primary candidate based on highest combined score across eight criteria including fabrication feasibility, fail-safe behaviour, reversible cycles, and direct testability.

Hygromorphic wood bilayer is the passive fallback, validated at architectural scale by Nature Communications (2024, DOI 10.1038/s41467-024-54808-8).

PCM is noted as a supplementary thermal layer, not the primary geometric mechanism, with 15–45% energy savings confirmed across 300+ studies (Energies MDPI, 2026).

---

## 6. Simulation Results

**[PENDING — to be completed after Grasshopper/Ladybug simulation with Sydney EPW]**

Placeholder table:

| Scenario | Mean radiation kWh/m2 | UDI % | Open ratio % | H(t) mean |
|---|---|---|---|---|
| S0 Static closed | — | — | 0% | 0 |
| S1 Static open | — | — | 100% | 0 |
| S2 Adaptive | — | — | — | — |

Target: S2 reduces radiation by at least 10% vs S0 and increases UDI by at least 10%.

---

## 7. Discussion

### What the analogies explain

- The information analogy (holography) provides a formal metric (H(t)) for evaluating how much spatially differentiated information the facade encodes. This is measurable and useful regardless of its physical origin.
- The phase transition analogy motivates a state machine design that is more stable than a purely continuous controller, because it builds in hysteresis and priority ordering.
- The frustration analogy, if confirmed by Wallacei results, would mean that the multi-objective facade problem has an irreducibly multi-modal solution space — which has direct implications for how designers should interpret optimisation outputs (no single correct answer exists).

### What the analogies do not explain

- None of these analogies imply that the facade implements quantum physics.
- The SYK model does not govern facade behaviour.
- The holographic principle of black-hole thermodynamics is not physically realised in a building envelope.
- These boundaries are stated explicitly so the research is not misread as quantum architecture.

---

## 8. Conclusion

This paper presents a formal, falsifiable framework for adaptive architectural envelopes as information-processing boundaries. The framework is grounded in peer-reviewed evidence for the physical mechanisms (PCM, metamaterials, hygromorphic systems), implemented as a reproducible computational workflow, and evaluated against measurable performance metrics.

The most novel contribution is the frustration landscape hypothesis for multi-objective facade optimisation. This hypothesis is testable with existing computational tools and will be evaluated in the next phase of research.

Open questions:
1. Does the Pareto front of facade optimisation exhibit multi-modal clustering consistent with a frustration landscape?
2. What is the optimal epsilon and maxStep combination for a Sydney climate?
3. Can facade Shannon entropy H(t) be used as a real-time performance indicator during building operation?
4. How does the hygromorphic or metamaterial prototype perform over 100+ actuation cycles under real humidity and temperature variation in Sydney?

**Target venue:** ACADIA, eCAADe, or the Journal of Building Performance Simulation.

---

## References

1. Responsive building facades: systematic review. Architectural Engineering and Design Management, 2026. DOI: 10.1080/17452007.2026.2658645
2. Adaptive Architectural Facades: Review 1985–2024. Nexus Network Journal, 2025. DOI: 10.1007/s00004-025-00831-1
3. Comprehensive Review of PCM for Building Applications. Energies MDPI, 2026. DOI: 10.3390/en19051151
4. 4D-printed mechanical metamaterials. Journal of Intelligent Material Systems, 2026. DOI: 10.1080/19475411.2026.2714783
5. Weather-responsive hygromorphic 4D-printing. Nature Communications, 2024. DOI: 10.1038/s41467-024-54808-8
6. Phase Change Materials in Residential Buildings. PMC/MDPI, 2025. PMC12072427
7. A first-of-its-kind critical analysis of PCM reviews. Applied Energy, 2025. DOI: 10.1016/j.apenergy.2025.007147
8. Shannon, C.E. A Mathematical Theory of Communication. Bell System Technical Journal, 1948.
