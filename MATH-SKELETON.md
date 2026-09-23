# MATH-SKELETON.md
# All Equations in One Place

> Single source of truth for all mathematical expressions in this project.
> If an equation appears in a discovery file, it must appear here first.

---

## Section 1 — Information Theory

### 1.1 Shannon Entropy (base)
  H(X) = -∑_i p_i · log2(p_i)
  Units: bits
  Domain: probability distribution over discrete states

### 1.2 Spatial Panel Entropy at time t
  H_space(t) = -∑_{i=1}^{N} p_i(t) · log2(p_i(t))
  where p_i(t) = fraction of panels in state i at time t
  N = number of distinct panel states

### 1.3 Temporal Panel Entropy for panel i
  H_time(i) = -∑_{t=1}^{T} p_t(i) · log2(p_t(i))
  where p_t(i) = fraction of time panel i spends in state t
  T = number of distinct time-states observed

### 1.4 Temporal Facade Entropy (TFE) — Discovery 01
  TFE(i, t) = H_space(t) × H_time(i)
  Scalar summary: TFE_total = (1/N) ∑_i (1/T) ∑_t TFE(i,t)
  Range: [0, log2(N) × log2(T)]

### 1.5 Boundary Information Ratio (BIR) — Discovery 04
  BIR(t) = H_boundary(t) / H_interior(t)
  H_boundary(t) = H_space(t)   [facade surface entropy]
  H_interior(t) = -∑_j q_j(t) · log2(q_j(t))   [interior state entropy]
  where q_j(t) = normalised interior variable j at time t
  Range: [0, 1]   (capped)

---

## Section 2 — Spin-Glass Physics

### 2.1 Edwards-Anderson Hamiltonian
  H_EA(s) = -∑_{i<j} J_ij · s_i · s_j - ∑_i h_i · s_i
  s_i ∈ {-1, +1}   (Ising spins)
  J_ij ~ N(0, J²/N)   (SK model: Gaussian, quenched disorder)

### 2.2 p-spin generalisation
  H_p = -∑_{i1<...<ip} J_{i1...ip} · s_{i1} · ... · s_{ip}
  Complexity: N_minima(e) ~ exp(N · Σ(e))
  Threshold: E_th separates saddle-dominated from minima-dominated regions

### 2.3 Overlap distribution (RSB detector)
  P(q) = < δ(q - (1/N) ∑_i s_i^a · s_i^b) >
  Paramagnetic: single peak at q=0
  Spin glass with RSB: multiple interior peaks at q≠0

### 2.4 Frustration condition for triangle (i,j,k)
  Φ_ijk = sign(J_ij) · sign(J_jk) · sign(J_ik)
  Φ_ijk = -1: frustrated (impossible to satisfy all pairwise preferences)
  Φ_ijk = +1: consistent

---

## Section 3 — Architectural Ising Hamiltonian — Discovery 02

### 3.1 Gene normalisation
  σ_k = 2·(g_k - g_k_min)/(g_k_max - g_k_min) - 1
  σ ∈ [-1, +1]^6

### 3.2 Facade Hamiltonian
  H_facade(σ) = -∑_{i<j} J^arch_ij · σ_i · σ_j - ∑_i h_i · σ_i + λ·P(σ)

### 3.3 Coupling construction from objective Jacobian
  J^arch_ij = (1/M) ∑_{k=1}^{M} (∂f_k/∂σ_i) · (∂f_k/∂σ_j)
  M = number of objectives (M=4 here)

### 3.4 Architectural overlap distribution
  P_arch(d) = distribution of d(g_a, g_b) for all Pareto pairs
  d(g_a, g_b) = (1/√6) · ||g_a - g_b||_2
  RSB detected if: Hartigan dip test p < 0.05 and K ≥ 2 Gaussian components

---

## Section 4 — Holographic Analogy

### 4.1 Bekenstein-Hawking entropy (physical reference)
  S_BH = A / (4 · l_p²)
  A = event horizon area
  l_p = Planck length
  Principle: interior volume information encoded on boundary area

### 4.2 BIR as macroscale holographic measure
  BIR → 1 means: H_boundary / H_interior → 1
  Interpretation: facade encodes as much information as the interior generates
  NOTE: This is an analogy, not a derivation from quantum gravity

---

## Section 5 — Bacterial Spore Actuator — Discovery 03

### 5.1 Layer-to-angle encoding
  θ_max(i) = f(n_i)   where n_i = number of spore monolayers on panel i
  f is monotone increasing, empirically determined
  Approximate linear model (to be calibrated): θ_max ≈ α · n_i

### 5.2 Spatial entropy from layer gradient
  If n_i varies across panels, then p_i(t) varies with humidity h(t)
  → H_space(t) > 0 at all t where h(t) ≠ h_ref
  → TFE > 0 at zero operational energy cost

### 5.3 Response dynamics
  θ(i, t) = θ_max(i) · (1 - exp(-t/τ))
  τ ≈ 180 seconds   (from literature: response < 3 minutes)
  Relaxation: symmetric on drying cycle

---

## Section 6 — Connections Between Sections

  Eq 1.4 (TFE) is the numerator of Eq 1.5 (BIR)
  Eq 5.2 shows D03 generates D01
  Eq 3.4 (RSB detection) uses Eq 2.3 (overlap distribution) as template
  Eq 3.2 (H_facade) is the architectural instance of Eq 2.1 (H_EA)
  Eq 4.2 (BIR→1) is the design target that Eq 3.2 (H_facade optimisation) should achieve

  Full dependency chain:
  D03 (n_layers) → D01 (TFE) → D04 (BIR)
  D02 (H_facade) predicts which design achieves highest BIR
