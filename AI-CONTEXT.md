# AI-CONTEXT.md
# Full Project Briefing — Optimised for Language Model Context

> **Read this file first if you are an AI model joining this project.**
> It contains everything you need to understand, continue, and extend this research.
> Human collaborator: architect-researcher, Sydney AU, September 2026.

---

## 1. What Problem Are We Solving?

Current building envelopes are static or pseudo-adaptive.
They respond to energy commands but do not encode interior information.
They are optimised by running a single parametric search that finds ONE Pareto front
and presents it as the complete answer — which it is not.

We are building a theoretical and computational framework that treats the building skin as:
1. An information channel (Shannon entropy framework)
2. A frustrated spin-glass system (Ising Hamiltonian)
3. A holographic surface (AdS/CFT analogy at macroscale)
4. A programmable biological material (bacterial spore actuators)

---

## 2. The Four Discoveries — Machine-Readable Summary

### D01: Temporal Facade Entropy (TFE)

Definition:
  TFE(i, t) = H_space(t) × H_time(i)
  H_space(t) = -∑ p_i(t) log2 p_i(t)   [Shannon entropy of panel states at time t]
  H_time(i)  = -∑ p_t(i) log2 p_t(i)   [Shannon entropy of panel i states over time]

Range: [0, log2(N) × log2(T)]
TFE = 0: static envelope (all panels identical, all time)
TFE = max: maximally diverse panel states across space and time

Novelty: No existing metric measures adaptive envelope behaviour as information.
Gap confirmed in: Renewable and Sustainable Energy Reviews 232 (2026), Frontiers Built Env (2026).

Falsification: Compute TFE for 3 envelopes (static, rule-based, optimised).
Prediction: TFE_optimised > TFE_rule-based > TFE_static = 0.

---

### D02: Pareto Frustration — Spin-Glass Mapping

Core claim: Multi-objective facade optimisation is formally equivalent to finding
low-energy configurations of a spin-glass Hamiltonian.

Gene vector (normalised to [-1,+1]):
  σ = [s_d, s_a, s_r, s_ε, s_Δs, s_wr]
  where d=depth, a=aperture, r=rotation, ε=hysteresis, Δs=maxStep, wr=radiation weight

Architectural Ising Hamiltonian:
  H_facade(σ) = -∑_{i<j} J^arch_ij · σ_i · σ_j - ∑_i h_i · σ_i + λ·P(σ)

Coupling matrix J^arch (6×6, symmetric, zero diagonal):
  J(d,a)   = -0.50  [cooperative: both reduce radiation]
  J(a,r)   = +0.50  [frustrating: aperture vs rotation conflict]
  J(d,r)   = -0.50  [cooperative]
  J(ε,Δs)  = +0.50  [frustrating: responsiveness vs smoothness]
  J(wr,a)  = -0.50  [cooperative]
  J(ε,wr)  = +0.25  [weak frustration]
  J(Δs,wr) = +0.25  [weak frustration]
  J(d,wr)  = -0.25  [weak cooperation]
  J(r,wr)  = -0.25  [weak cooperation]
  all other entries = 0

Frustrated triangle: (ε, Δs, wr) — all three pairwise couplings > 0.
In antiferromagnetic triangle: impossible to satisfy all three antiparallel preferences.
This guarantees: multiple local minima, no global optimum accessible from arbitrary start.

External field h (Sydney EPW climate prior):
  h = [+0.30, -0.20, +0.15, -0.10, -0.10, +0.25]

Predicted ground state σ*:
  σ* ≈ [+0.4, +0.3, 0.0, -0.2, -0.1, +0.5]
  → d≈175mm, a≈0.62, r≈45°, wr≈0.65

RSB detection protocol:
  1. Run Wallacei 5× with different random seeds
  2. Compute pairwise distances d(g_a, g_b) in gene space
  3. Plot histogram P_arch(d)
  4. Apply Hartigan dip test
  5. If p < 0.05 and K ≥ 2 modes: RSB equivalent confirmed

Novelty: First Ising Hamiltonian encoding of a multi-objective architectural design problem.
Gap confirmed in: arXiv 2606.16792 (2025), PhysRevE 110.045308 (2024).

---

### D03: Programmable Bacterial Spore Panels

Mechanism: Bacillus subtilis spores expand/contract with humidity change.
Response time: < 3 minutes.
Reversibility: 100% stable over 1,000,000 cycles.
Lift capacity: 150% of own weight.
Programming: number of spore monolayers = bending angle.

Panel encoding:
  n_layers(panel_i) ∈ {1, 2, 3, ..., N_max}
  θ_max(panel_i) = f(n_layers)   [monotone increasing function]
  Spatial gradient: panels with different n_layers create differential response.

Key innovation: A facade with panels having different layer counts creates
a spatial response gradient WITHOUT electronics, sensors, or power.
This directly generates TFE > 0 at zero operational energy cost.

Substrate (2025): cork (Quercus suber) identified as optimal — lightweight, bio-compatible.

Fabrication protocol:
  1. Laser-cut cork substrate to panel geometry
  2. Spin-coat spore suspension at concentration C
  3. Dry at 40°C for 2h per layer
  4. Repeat n_layers times
  5. Seal edges with parylene coating

Novelty: Spatial gradient programming of spore actuator panels.
Gap: All existing spore literature uses uniform layers across full sample.

---

### D04: Boundary Information Ratio (BIR)

Definition:
  BIR(t) = H_boundary(t) / H_interior(t)

Where:
  H_boundary(t) = TFE at time t (information encoded on facade surface)
  H_interior(t) = Shannon entropy of interior state variables
                  (occupancy density, zone temperatures, activity levels)

Range: [0, 1] (capped at 1 by holographic principle analogy)
BIR = 0: envelope is blind to interior — static facade
BIR = 1: holographic limit — envelope fully encodes interior state

Physical analogy:
  Black hole event horizon: S_BH = A/(4·l_p²)   [Bekenstein-Hawking]
  Building facade: BIR → 1 means facade area encodes interior entropy

Measurement:
  H_interior: computed from sensor data (CO2, temperature, PIR occupancy)
  H_boundary: computed from panel state log (TFE)

Novelty: First information-theoretic metric bridging building physics and holographic principle.
No existing building performance standard measures this quantity.

---

## 3. Mathematical Relationships Between Discoveries

  D03 (spore layers) → produces → D01 (TFE > 0)
  D01 (TFE) + interior sensors → computes → D04 (BIR)
  D02 (H_facade landscape) → predicts → which design family achieves highest TFE
  D04 (BIR) → can serve as → reward function for RL building controller

The four discoveries form a closed loop:
  Material → Behaviour → Information → Optimisation → back to Material

---

## 4. What AI Models Should NOT Do

- Do not add citations that are not in the discoveries/ files
- Do not conflate AdS/CFT (quantum gravity) with BIR (macroscale analogy)
  BIR is an ANALOGY, not a derivation from string theory
- Do not assume the coupling matrix J^arch is exact
  It is a physically motivated approximation to be calibrated by simulation
- Do not claim RSB is confirmed — it is PREDICTED and must be tested
- Do not add new discoveries without adding a falsification protocol

---

## 5. Open Questions (as of September 2026)

1. Does the Wallacei RSB detection protocol produce K ≥ 2 for Sydney EPW?
2. What is the empirical n_layers → θ_max function for cork substrate?
3. Can BIR be measured on an existing building with available sensor data?
4. Is H_facade the correct scalarisation of the multi-objective problem,
   or does a better scalarisation exist that preserves more landscape structure?
5. Can the frustrated triangle (ε, Δs, wr) be eliminated by reparameterisation?

---

## 6. Tone and Voice for This Project

This project speaks in three registers simultaneously:
- Physics: precise, falsifiable, equation-grounded
- Architecture: spatial, experiential, material
- Biology: process-oriented, adaptive, self-organising

When writing for this project:
- Lead with the physical mechanism, follow with the architectural consequence
- Every claim must have a falsification condition
- Mathematical notation: use plain ASCII in .md files, LaTeX in formal papers
- Metaphors are welcome but must not replace equations
