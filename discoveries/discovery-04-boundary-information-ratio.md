# Discovery 04 — Boundary Information Ratio (BIR): A Holographic Building Metric

## Status: Formally defined, not found in architectural literature
## Evidence level: L1 (mathematically defined)

---

## The gap in current knowledge

The holographic principle in physics states that the information content of a volume can be fully encoded on its boundary. The formal expression (PhilArchive, 2024) is:

    BIR_physics = I_boundary(A) / I_volume(V)

For truly holographic systems, BIR approaches 1.0.

In spatial theory, the idea that physical environments encode information has been asserted since Rapoport (1980s) and partially formalised in arXiv 1910.06367 (Assessing Spatial Information in Physical Environments). That paper asks: "how the built environment could encode forms of information in its own physical structures in the first place, and how such amounts of information could be measured empirically." It does not answer this question for adaptive facades.

Existing entropy applications to facades measure visual regularity (Nexus Network Journal, 2025) or structural composition (Entropy and the City, arXiv 2403.15199). None measure the ratio of boundary information to interior information in a dynamic, operational building.

---

## The original contribution

This project defines a measurable **Boundary Information Ratio (BIR)** for buildings:

### Definitions

    I_boundary = H_space(t) computed from panel state distribution on envelope
                 [bits, from Discovery 01]

    I_interior = H_interior(t) computed from interior state distribution:
                 - zone temperature variance
                 - CO2 concentration variance across zones
                 - occupancy distribution across zones
                 [bits, normalised to same scale]

    BIR(t) = I_boundary(t) / I_interior(t)

### Interpretation

- BIR = 0: facade is static, encodes no information about interior state regardless of interior complexity
- BIR = 1: boundary perfectly encodes all interior complexity (holographic limit)
- BIR > 1: facade encodes more spatial differentiation than the interior it serves (over-responsive)
- BIR < 0.5: facade is under-responsive to interior conditions

### Design application

BIR can be used as a design optimisation target:
- Static facade: BIR = 0 by definition
- Adaptive facade: BIR > 0 if panels respond differently to different interior conditions
- Well-designed adaptive facade: BIR approaches 1.0 during occupied hours
- Poorly designed adaptive facade: BIR near 0 despite active components (controller not responding meaningfully)

---

## Connection to holographic physics (bounded analogy)

The holographic principle in AdS/CFT correspondence (Susskind, 't Hooft, 1994; formalised in tensor network models, arXiv 2102.02619) states that a gravitational bulk theory is informationally equivalent to a boundary quantum field theory. Information stored in the bulk is stored redundantly on the boundary, in the manner of a quantum error-correcting code.

The BIR for buildings is NOT a claim that buildings implement AdS/CFT.
It IS a claim that the ratio structure is meaningful and measurable in buildings:
- Interior state = analogue of bulk
- Facade state distribution = analogue of boundary
- BIR = measurable ratio of boundary to interior information content

The analogy is structural, bounded, and generates a testable prediction: a well-designed adaptive facade should have BIR(t) significantly greater than zero during occupied hours, and approaching 1.0 is a design aspiration, not a physics claim.

---

## Why this is hidden from the mainstream

Building performance metrics are almost entirely energy-centric (kWh, W/m2, lux). Information-theoretic metrics are used in urban morphology and visual perception research but not in facade performance engineering. The holographic principle is discussed in quantum gravity, consciousness theory, and information philosophy, but not in building physics or architectural computation.

The specific combination of:
1. Shannon entropy of facade panel states as I_boundary
2. Shannon entropy of interior sensor distributions as I_interior
3. Their ratio as a design and operational metric
4. Bounded connection to holographic information theory

has not appeared in any reviewed paper in architecture, building physics, or spatial theory.

---

## Path to validation

1. Implement H_space(t) in GhPython from simulation panel states (Step 6)
2. Implement H_interior(t) from simulated zone temperature and CO2 distributions
3. Compute BIR(t) for each hour of the simulation year
4. Plot BIR(t) over time for S0, S1, S2
5. If BIR(S2) significantly exceeds BIR(S0) = 0 and shows diurnal patterns consistent with occupancy, publish as technical note.

Target venue: Building and Environment (Elsevier) or Automation in Construction.
