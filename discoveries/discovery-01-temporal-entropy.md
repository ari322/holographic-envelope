# Discovery 01 — Temporal Facade Entropy as a Performance Metric

## Status: Original contribution — not found in reviewed literature
## Evidence level: L1 (mathematically defined, computation pending)

---

## The gap in current knowledge

Existing adaptive facade metrics are all energy-centric: U-value, g-value, UDI, kWh/m2.
These are instantaneous or integrated scalars. They measure HOW MUCH energy or light, not HOW DIFFERENTLY the facade behaved across space and time.

A systematic review of dynamic facade metrics (Eindhoven University, 2018, Pure repository) confirms that conventional characterisation methods based on static assumptions provide limited and potentially misleading information for adaptive systems. The review explicitly states that adaptive facades require time-varying state representations, not static enclosure parameters.

Yet no reviewed paper defines a spatial information metric for facade state distribution.

---

## The original contribution

This project defines **Temporal Facade Entropy (TFE)** as a dual metric:

### Spatial entropy at time t

    H_space(t) = - sum_i [ p_i(t) * log2( p_i(t) ) ]

Where p_i(t) = normalised open ratio of panel i at time t.

H_space = 0: all panels identical (no spatial information encoded on boundary)
H_space = log2(N): maximum differentiation across N panels

### Temporal entropy over a day

    H_time(i) = - sum_t [ q_t(i) * log2( q_t(i) ) ]

Where q_t(i) = fraction of time panel i spends in each discrete state.

H_time = 0: panel never changes state (static behaviour)
H_time = log2(K): panel cycles evenly through K states

### Combined TFE surface

    TFE(i,t) = H_space(t) * H_time(i)

This 2D surface can be plotted as a heatmap over panel index (space) and hour of day (time).
It shows WHEN and WHERE the facade is most informationally active.

---

## Why this matters

1. A static facade always has H_space = 0. Adaptive facades have H_space > 0 during occupied hours. TFE provides a single number to compare adaptive and static facades on information grounds, not just energy grounds.

2. TFE is independent of which technology drives adaptation (PCM, hygromorphic, mechanical, servo). It is a property of the state distribution, not the mechanism.

3. The holographic analogy becomes formally testable: a facade with higher TFE encodes more information about interior conditions on the exterior boundary. This is a measurable hypothesis.

4. TFE can be used as a real-time operational indicator. A building management system could monitor H_space(t) in real time. A drop toward zero signals that the facade is behaving statically despite dynamic environmental conditions — indicating sensor failure or controller drift.

---

## Connection to existing literature

- Mathematical Regularity Coefficient for Facade Patterns (Nexus Network Journal, 2025, DOI 10.1007/s00004-025-00827-x): Shannon entropy applied to facade visual regularity across 245 architectural compositions. This paper uses spatial entropy for visual analysis, not for dynamic performance.
- Entropy and the City (arXiv 2403.15199): Shannon entropy applied to urban spatial configurations. Not applied to time-varying adaptive facade states.
- Entropy as a Lens (TU Dortmund 2023): Shannon entropy for eye-tracking analysis of architect gaze in built environments.

**None of these papers apply temporal Shannon entropy to the panel state distribution of an adaptive facade as a performance metric.**

TFE is a new metric.

---

## Path to publication

Target journal: Journal of Building Performance Simulation (Elsevier) or Building and Environment.
Contribution type: technical note proposing and validating a new metric.
Required steps: implement TFE computation in GhPython or Python, run on Sydney EPW simulation output, compare TFE values for S0 (static), S1 (static open), and S2 (adaptive). If TFE(S2) > TFE(S0) = 0 and correlates with improved UDI, the metric is validated.
