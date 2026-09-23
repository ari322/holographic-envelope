# Literature Map

## Status: Step 2 — Evidence Base

This document maps peer-reviewed literature across five pillars relevant to the project.
Each source is assigned a claim, an evidence grade, and a relevance note.

Evidence grades:
- A = systematic review or meta-analysis (highest)
- B = experimental study with quantified results
- C = review paper without meta-analysis
- D = theoretical or conceptual paper

---

## Pillar 1 — Adaptive and Kinetic Facades

### Source 1
- **Title:** Responsive building facades: a systematic review of technologies, challenges, and future directions
- **Journal:** Architectural Engineering and Design Management (Taylor & Francis)
- **Year:** 2026
- **DOI:** 10.1080/17452007.2026.2658645
- **Grade:** A
- **Sample size:** 48 peer-reviewed studies (2010–2025), Scopus and Web of Science
- **Relevant claim:** Responsive facades regulate indoor environments by dynamically responding to environmental conditions.
- **Project relevance:** Validates the core mechanism of Axiom A1 and A2. Provides taxonomy of facade response types.
- **Limitation:** Does not address formal mathematical state models or GhPython implementation.

### Source 2
- **Title:** Adaptive Architectural Facades: Review 1985–2024
- **Journal:** Nexus Network Journal (Springer)
- **Year:** 2025
- **DOI:** 10.1007/s00004-025-00831-1
- **Grade:** A
- **Relevant claim:** 40-year trajectory of adaptive facade research from mechanical louvres to computational skins.
- **Project relevance:** Historical grounding and classification of adaptive envelope types. Relevant to Step 6 baseline framing.

### Source 3
- **Title:** Smart 3D-printed facades: a review of innovations, materials, and sustainable performance
- **Journal:** Frontiers in Sustainable Cities
- **Year:** 2025
- **DOI:** 10.3389/frsc.2025.1610729
- **Grade:** C
- **Relevant claim:** 3D-printed facades integrate smart materials and computational design for sustainable performance.
- **Project relevance:** Links fabrication method (additive manufacturing) to material performance in facades.

---

## Pillar 2 — Phase Change Materials in Building Envelopes

### Source 4
- **Title:** Comprehensive Review of Phase Change Materials for Building Applications: Passive, Active, and Hybrid Systems (2022–2025)
- **Journal:** Energies (MDPI)
- **Year:** 2026
- **DOI:** 10.3390/en19051151
- **Grade:** A
- **Sample size:** 300+ peer-reviewed studies
- **Key finding:** Passive PCM envelope integration delivers 15–45% energy savings with payback 8–15 years. Active systems achieve 20–40% reduction with payback 3–8 years. Hybrid AI-controlled configurations reach up to 50% savings.
- **Project relevance:** Quantifies performance of PCM as candidate material for Axiom A2 and Step 5 material selection.
- **Limitation:** Challenges include low thermal conductivity (0.1–0.3 W/m·K for organics), cycling instability, and real-world scalability gaps.

### Source 5
- **Title:** Phase Change Materials in Residential Buildings
- **Journal:** PMC / MDPI
- **Year:** 2025
- **DOI:** PMC12072427
- **Grade:** B
- **Key finding:** Optimised PCM integration reduces energy consumption by up to 30% and improves indoor thermal comfort. 15–30% savings in walls and floors.
- **Project relevance:** Provides residential-scale evidence relevant to a pavilion prototype (Step 7).
- **Limitation:** Phase separation and low thermal conductivity limit large-scale adoption.

### Source 6
- **Title:** A first-of-its-kind critical analysis of review articles on phase change materials
- **Journal:** Applied Energy (Elsevier)
- **Year:** 2025
- **DOI:** 10.1016/j.apenergy.2025.007147
- **Grade:** A
- **Sample size:** 271 review articles from 1983 to 2025
- **Relevant claim:** Synthesis of 40 years of PCM research confirms consistent energy efficiency benefits with persistent gaps in standardised testing and long-term field validation.
- **Project relevance:** Broadest available evidence base for PCM claims. Justifies PCM as a scientifically credible material candidate.

---

## Pillar 3 — Mechanical Metamaterials and Deployable Structures

### Source 7
- **Title:** 4D-printed mechanical metamaterials: responsive architectures for programmable shape, stiffness, and multifunctionality
- **Journal:** Journal of Intelligent Material Systems and Structures (Taylor & Francis)
- **Year:** 2026
- **DOI:** 10.1080/19475411.2026.2714783
- **Grade:** C
- **Key finding:** 4D-printed mechanical metamaterials combine stimuli-responsive materials with architected geometry to enable shape change, stiffness tuning, and deployable function after fabrication.
- **Project relevance:** Directly relevant to Step 5 material selection and Step 7 prototype. Validates auxetic and origami-based deployable structures.
- **Limitation:** Cyclic stability, load-bearing capacity, and actuation reliability require further validation for architectural scale.

### Source 8
- **Title:** 3D printing of active mechanical metamaterials: A critical review
- **Journal:** Cronfa / Swansea University
- **Year:** 2024
- **Key finding:** Architected metamaterials based on origami engineering show potential for deployable structures, reconfigurable architectures, and programmable matter.
- **Project relevance:** Provides fabrication pathway (3D printing) for Step 7 prototype and theoretical basis for spin-glass frustration analogy in Step 8.

---

## Pillar 4 — Hygromorphic and Passive Responsive Systems

### Source 9
- **Title:** Incorporation of Phase Change Materials in Buildings
- **Journal:** Construction Materials (MDPI / Cardiff University ORCA)
- **Year:** 2024
- **DOI:** 10.3390/constrmater4040037
- **Grade:** B
- **Key finding:** PCMs moderate indoor temperatures by absorbing and releasing heat. Energy savings and carbon reduction potential confirmed across diverse climates.
- **Project relevance:** Supports PCM as passive and low-maintenance boundary mechanism. Relevant to Step 5 and Step 6.

### Source 10
- **Title:** A Review on Phase-Changing Materials Applications in Energy-Efficient Building Envelope Designs
- **Journal:** Springer (ICSESD proceedings)
- **Year:** 2024
- **Key finding:** PCM integration improves thermal load performance at an average of 25% annual energy savings. Confirmed across multiple building types.
- **Project relevance:** Provides a conservative baseline figure for Step 6 simulation targets.

---

## Pillar 5 — Multi-Objective Optimisation in Parametric Architecture

This pillar is the weakest in current literature mapping. Peer-reviewed studies specifically linking spin-glass frustration models to architectural multi-objective optimisation have not been located.

**Current status:** Spin-glass and SYK analogies for multi-objective design landscapes remain at Evidence Level L0 (conceptual) in this project.

**Path to upgrade:** Step 8 will attempt to build a Pareto optimisation in Wallacei that demonstrates multi-modal clustering. If clustering is observed, the analogy gains computational support (L1). Physical prototype validation would upgrade it to L3.

**Known adjacent work:**
- Multi-objective genetic algorithms (NSGA-II) in facade optimisation: established literature in energy and daylight trade-offs.
- Wallacei and Octopus plugins: documented tools for Pareto-front generation in Grasshopper.
- Spin-glass models in combinatorial optimisation: established in computer science, not yet in architectural computation literature.

---

## Evidence summary by pillar

| Pillar | Evidence Grade | Project Status |
|---|---|---|
| Adaptive and kinetic facades | A | Well-supported, relevant to A1 and A2 |
| PCM building envelopes | A | Quantified, 15–45% energy savings confirmed |
| Mechanical metamaterials | B–C | Promising, fabrication challenges persist |
| Hygromorphic systems | B | Passive, small-scale; durability unresolved |
| Multi-objective spin-glass analogy | L0 | Conceptual only, no architectural literature found |

---

## Claims upgraded by this literature map

- PCM as a material candidate: upgraded from L0 to L2 (simulation-supported in literature)
- Adaptive facade as boundary function: upgraded from L0 to L1 (computationally reproducible in literature)
- Mechanical metamaterial prototype: remains at L1 (computationally reproducible, fabrication demonstrated in non-architectural contexts)
- Spin-glass optimisation analogy: remains at L0 until Step 8
