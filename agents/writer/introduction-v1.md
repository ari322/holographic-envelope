# Introduction

**Word count:** 841

Adaptive building envelopes are intended to vary geometry or transmittance as climate and occupancy change. In practice most skins remain static, or they are only pseudo-adaptive: they execute threshold rules or energy set-points without recording how much interior information is present on the exterior surface. Performance is still scored with instantaneous or integrated scalars. Those scalars do not distinguish a facade that is uniformly closed from one whose panels occupy a structured distribution of states. A second limitation is computational. Multi-objective parametric search is routinely run once, a single Pareto front is extracted, and that front is treated as complete. Competing objectives need not admit a unique low-cost family of designs. If the search landscape is frustrated, different random starts can return qualitatively different fronts, and a single run conceals that structure.

The missing quantity is informational. Let p_i(t) be the fraction of panels in discrete state i at time t, and let p_t(i) be the fraction of time that panel i occupies a given time-state. Shannon entropy then supplies two bit-valued measures,

H_space(t) = −∑_{i=1}^{N} p_i(t) · log2(p_i(t)),

H_time(i) = −∑_{t=1}^{T} p_t(i) · log2(p_t(i)).

Their product is Temporal Facade Entropy,

TFE(i, t) = H_space(t) × H_time(i),

with scalar summary TFE_total = (1/N) ∑_i (1/T) ∑_t TFE(i,t) and range [0, log2(N) × log2(T)]. TFE = 0 if and only if the envelope is uniform in space and frozen in time. The architectural consequence is that TFE is a technology-independent discriminator of adaptive behaviour: a static skin is identically zero; a rule-based or optimised skin is predicted to occupy the strict ordering TFE_optimised > TFE_rule-based > TFE_static = 0. That ordering is a falsification condition, not a reported measurement.

The same conflict that produces a non-unique Pareto front can be written as a spin-glass Hamiltonian. Facade genes g_k — depth, aperture, rotation, hysteresis ε, maximum step Δs, and radiation weight wr — are normalised to σ ∈ [−1, +1]^6 by

σ_k = 2 · (g_k − g_k,min) / (g_k,max − g_k,min) − 1.

The architectural energy is the Edwards–Anderson form with a penalty term,

H_facade(σ) = −∑_{i<j} J^arch_ij · σ_i · σ_j − ∑_i h_i · σ_i + λ·P(σ),

where J^arch is constructed from the objective Jacobian,

J^arch_ij = (1/M) ∑_{k=1}^{M} (∂f_k/∂σ_i) · (∂f_k/∂σ_j),

with M = 4. Pairwise signs on the gene triplet (ε, Δs, wr) form a frustrated triangle: Φ_ijk = sign(J_ij) · sign(J_jk) · sign(J_ik) = −1, so the three antiparallel preferences cannot be satisfied together. Frustration of this kind is the physical mechanism that produces multiple local minima. The architectural consequence is a predicted replica-symmetry-breaking (RSB) signature in the pairwise gene-distance distribution P_arch(d), with

d(g_a, g_b) = (1/√6) · ||g_a − g_b||_2.

The detection protocol is specified and unexecuted: five Wallacei runs with distinct seeds, a Hartigan dip test on P_arch(d), and RSB-equivalent structure only if p < 0.05 and K ≥ 2 Gaussian components. No such test has been run; RSB is not confirmed.

A material instantiation that can generate TFE > 0 without operational power follows from hygroscopic actuation of Bacillus subtilis spores. Spores expand and contract with ambient humidity. The bending angle of a coated panel relaxes as

θ(i, t) = θ_max(i) · (1 − exp(−t/τ)),

with τ ≈ 180 s and a symmetric drying cycle. Maximum angle is programmed by monolayer count, θ_max(i) = f(n_i), where f is monotone increasing and is approximated, pending calibration, by the linear model θ_max ≈ α · n_i. If n_i varies across the facade, the panel-state occupancy p_i(t) varies with humidity h(t) whenever h(t) ≠ h_ref, which forces H_space(t) > 0 and therefore TFE > 0 at zero operational energy. Cork (Quercus suber) is the stated substrate. The empirical map θ_max(n) on cork has not been measured; fabrication results are not claimed.

Boundary encoding is scored by the Boundary Information Ratio. Interior entropy is

H_interior(t) = −∑_j q_j(t) · log2(q_j(t)),

with q_j(t) a normalised interior variable (occupancy, zone temperature, activity). Facade-surface entropy is H_boundary(t) = H_space(t). Their ratio

BIR(t) = H_boundary(t) / H_interior(t)

is capped on [0, 1]. BIR = 0 is a blind, static envelope; BIR → 1 is the stated design target in which the facade encodes as much information as the interior generates. The Bekenstein–Hawking formula S_BH = A / (4 · l_p²) is used only as the physical reference that interior volume information can be represented on a boundary area. BIR is a macroscale analogy. It is not derived from AdS/CFT, and no claim is made that a building realises a holographic dual.

The four quantities close a loop that organises the paper. Spore-layer gradients (D03) are a proposed generator of TFE (D01). TFE, together with interior sensor entropy, defines BIR (D04). The H_facade landscape (D02) is the predicted selector of which design family maximises BIR; that prediction remains untested. Later sections state the information metrics, the architectural Hamiltonian and RSB protocol, the spore-panel encoding, and the open empirical programme: Wallacei RSB detection, cork θ_max(n), and BIR on existing sensor logs. Claims here are definitional and predictive. They stand or fall by those tests.
