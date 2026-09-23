# Unsupported Claims — Architecture / Mathematics
# CRITIC first wake — 2026-09-23
# Scope: AI-CONTEXT, MATH-SKELETON, discovery-02-*, related math/discovery docs
# Rule: a claim is unsupported if this repo contains no empirical measurement that backs it.
# Empirical inventory of this repo: zero Wallacei fronts, zero EPW result tables,
# zero TFE numbers, zero BIR numbers, zero prototype logs with dates,
# zero sensor traces, zero Jacobian evaluations, zero eigenvalue spectra of J^arch.
# validation/simulation-baseline.md is a plan. validation/prototype-log.md is empty.
# validation/evidence-report.md already grades the core D02 claim as L0.

Style: quote short and exact. Cite file and section. Name the missing data. Rate severity.

Severity:
- blocker: the research program cannot be submitted, or the math is internally false
- major: a central prediction or metric has no data and may be uninterpretable
- minor: a side claim, novelty boast, or parameter guess without data

---

## Empirical baseline (what is actually in the repo)

| Required measurement | File that should hold it | Contents |
|---|---|---|
| Sydney EPW radiation / UDI table | validation/simulation-baseline.md | placeholders; "simulation pending" |
| S0/S1/S2 result table | research/paper-draft-v1.md Section 6 | empty cells |
| Wallacei Pareto genes | grasshopper/optimization-setup.md | "Wallacei run pending" |
| Pairwise P_arch(d), dip p, K | discovery-02-mathematics.md Part V | protocol only |
| H_facade evaluated on any sigma | MATH-SKELETON.md 3.2 | formula only |
| Jacobian F = df/ds | discovery-02-coupling-matrix.md 3.3 | signs, then |F_kj|=1 |
| Eigenvalues of J^arch or -J^arch | nowhere | absent |
| Prototype actuation angles | validation/prototype-log.md | all stages dated "—" |
| Cork-spore theta(n) curve | MATH-SKELETON.md 5.1 | "to be calibrated" |
| Building sensor BIR series | discovery-04-boundary-information-ratio.md | path to validation, not data |

Do not treat literature citations, planned falsification protocols, or synthetic-data notes as empirical support. The SIMULATOR role has not written synthetic-pareto.json. No numeric experiment exists.

---

## D02 — Equivalence, landscape, novelty

### C01
**Quote:** "Multi-objective facade optimisation is formally equivalent to finding low-energy configurations of a spin-glass Hamiltonian."
**Source:** AI-CONTEXT.md Section 2 D02
**Missing data:** A demonstrated isomorphism: same variables, same quenched disorder, same thermodynamic-limit RSB, and a computed spectrum of H_facade(sigma) on real Wallacei points. Equivalence is a theorem, not a metaphor. The repo has a 6x6 deterministic sign table and a correspondence table (discovery-02-mathematics.md 3.1). That is not equivalence.
**Severity:** blocker

### C02
**Quote:** "This is the first formal Ising Hamiltonian encoding of a multi-objective adaptive facade optimisation problem in the architectural computation literature."
**Source:** discovery-02-coupling-matrix.md Part VI; AI-CONTEXT.md D02 "Novelty"
**Missing data:** A documented search (query log, inclusion criteria, full-text review) showing no prior Ising / quadratic-interaction encoding of facade genes. research/literature-map.md Pillar 5 only says such papers "have not been located." Absence of a search is not a first.
**Severity:** major

### C03
**Quote:** "F* = the set of lowest-energy configurations of a spin glass (no other configuration is strictly better on all objectives)"
**Source:** discovery-02-mathematics.md 2.3
**Missing data:** Any scalar energy whose sublevel sets recover the Pareto set of (f1,f2,f3,f4). Weighted sums do not; the same file (3.2) states that weighted-sum scalarisation "produces the worst approximation." H_facade is a weighted quadratic. No computed F* exists to compare.
**Severity:** blocker

### C04
**Quote:** "This guarantees: multiple local minima, no global optimum accessible from arbitrary start."
**Source:** AI-CONTEXT.md D02, after the (eps, Delta s, wr) triangle
**Missing data:** (1) A correct frustration certificate (see C12). (2) Eigenvalues of the quadratic form -J^arch on R^6. (3) Multiple numerically distinct local minima of H_facade. A 6-dimensional continuous quadratic plus linear field can be convex. N=6 is not the SK thermodynamic limit. "Inaccessible global optimum" is not a theorem at this size.
**Severity:** blocker

### C05
**Quote:** "There is no single optimal facade design for a Sydney climate."
**Source:** discovery-02-mathematics.md Part VI, conditioned on K>=2, then stated as architectural fact
**Missing data:** Any Sydney optimisation result. Condition was never evaluated. The unconditional reading is unsupported.
**Severity:** major

### C06
**Quote:** "The neural network result provides INDEPENDENT VALIDATION of the RSB mechanism in a high-dimensional optimisation context."
**Source:** discovery-02-mathematics.md Part IV
**Missing data:** Facade data. RSB in another domain does not validate this domain. Category error presented as evidence.
**Severity:** major

### C07
**Quote:** "Gap confirmed in: arXiv 2606.16792 (2025), PhysRevE 110.045308 (2024)."
**Source:** AI-CONTEXT.md D02
**Missing data:** The cited files are not in the repo. arXiv 2606.* is a June 2026 identifier labelled "2025" — internally inconsistent. No excerpt demonstrates a gap about architectural facades; PhysRevE 110.045308 is an Ising-machine landscape paper, not a facade-optimisation gap.
**Severity:** minor

---

## D02 — Coupling matrix J^arch

### C08
**Quote:** "J(d,a) = -0.50 [cooperative: both reduce radiation]"
**Source:** AI-CONTEXT.md D02; discovery-02-coupling-matrix.md 3.4
**Missing data:** Evaluated partial derivatives of f1,f2,f3,f4 at any feasible sigma. The same coupling file (3.3) states larger aperture raises f1 (more radiation). The verbal gloss "BOTH reduce radiation" contradicts the authors' own Jacobian signs. The number -1/2 is (1/4)*sum of {-1,-1,0,0} with |F_kj| forced to 1 (3.4). Not a measurement.
**Severity:** blocker

### C09
**Quote:** "J^arch_ij = (1/M) sum_k (df_k/d sigma_i)(df_k/d sigma_j)"
**Source:** MATH-SKELETON.md 3.3
**Missing data:** The 4x6 Jacobian on a real or simulated design. discovery-02-coupling-matrix.md 3.2 writes a different formula (sign-magnitude product), then drops magnitudes. Three constructions, zero numbers.
**Severity:** blocker

### C10
**Quote:** "Using J_ij = (1/4) * sum_k F_ki * F_kj (simplified with magnitudes = 1)"
**Source:** discovery-02-coupling-matrix.md 3.4
**Missing data:** Any non-unit |df_k/ds_j|. Unit magnitudes make J a sign-agreement table, not a coupling matrix. No sensitivity study of how J changes if |df1/da| != |df2/da|.
**Severity:** major

### C11
**Quote:** "all other entries = 0"
**Source:** AI-CONTEXT.md D02
**Missing data:** Jacobian confirmation that (d,eps), (d,ms), (a,eps), (a,ms), (r,eps), (r,ms) are negligible. The sign matrix in coupling-matrix 3.3 already gives nonzero products for several of these (e.g. f1 and f2 both depend on d and eps). Zeroing them is an untested modelling choice.
**Severity:** major

### C12
**Quote:** "Frustrated triangle: (eps, Delta s, wr) — all three pairwise couplings > 0. ... This guarantees: multiple local minima"
**Source:** AI-CONTEXT.md D02; discovery-02-coupling-matrix.md 3.5; MATH-SKELETON.md 2.4
**Missing data:** A consistent frustration test. MATH-SKELETON 2.4: Phi_ijk = sign(J_ij)sign(J_jk)sign(J_ik); Phi = -1 frustrated. For (eps, ms, wr) the product is (+1)(+1)(+1) = +1. The coupling file computes this, writes "consistent", then overrides: "CLASSICAL FRUSTRATED TRIANGLE when all J_ij > 0." That override is not a derivation. No landscape sample shows multiple minima of H_facade.
**Severity:** blocker

### C13
**Quote:** "ferromagnetic: J_ij < 0" / "antiferromagnetic: J_ij > 0"
**Source:** discovery-02-coupling-matrix.md 3.1
**Missing data:** Reconciliation with H = -sum J_ij sigma_i sigma_j (MATH-SKELETON 3.2 / coupling-matrix 4.1). Under that Hamiltonian, J>0 lowers energy when spins align (ferromagnetic). Labels are inverted relative to the written H. Until H, J-signs, and words agree, every "cooperative" / "frustrating" entry is unsupported even as theory.
**Severity:** blocker

### C14
**Quote:** "In spin-glass physics, J_ij encodes whether spins i and j prefer to be aligned (ferromagnetic: J_ij < 0)"
**Source:** discovery-02-coupling-matrix.md 3.1
**Missing data:** Same as C13. Also: SK couplings are random, quenched, typically all-to-all (coupling-matrix Part I). J^arch is sparse, deterministic, hand-signed. No evidence it is a spin-glass coupling matrix rather than a 6x6 Gram matrix of guessed objective slopes.
**Severity:** major

---

## D02 — External field, ground state, RSB protocol

### C15
**Quote:** "h = [+0.30, -0.20, +0.15, -0.10, -0.10, +0.25]"
**Source:** AI-CONTEXT.md D02; discovery-02-coupling-matrix.md 4.2
**Missing data:** Any calculation from a Sydney EPW file. The text says "Estimated from Sydney solar data" and "Calibration against EPW simulation data (Step 6) will refine them." Step 6 has not been run. These are free parameters.
**Severity:** major

### C16
**Quote:** "h_a = -0.20 (some aperture needed for daylight; negative field pushes s_a up)"
**Source:** discovery-02-coupling-matrix.md 4.2 and 4.1
**Missing data:** Algebra that matches the Hamiltonian. H contains -h_i sigma_i. Minimising H with h_a < 0 favours sigma_a < 0 (smaller aperture). The parenthetical is false as written. Predicted s_a ~ +0.3 (4.3) fights the linear field.
**Severity:** blocker

### C17
**Quote:** "sigma* ≈ [+0.4, +0.3, 0.0, -0.2, -0.1, +0.5] → d≈175mm, a≈0.62, r≈45°, wr≈0.65"
**Source:** AI-CONTEXT.md D02; discovery-02-coupling-matrix.md 4.3
**Missing data:** A recorded minimisation of H_facade (gradient, grid, or closed form). The values are "approximate ... before simulation." Inverse-normalisation of +0.4 on d is arithmetic, not optimisation. No Wallacei centroid to compare.
**Severity:** major

### C18
**Quote:** "If K >= 2 modes: RSB equivalent confirmed"
**Source:** AI-CONTEXT.md D02 RSB protocol; MATH-SKELETON.md 3.4; discovery-02-mathematics.md 3.3
**Missing data:** Any P_arch(d) histogram, Hartigan p-value, or GMM K on real or even synthetic Pareto genes. Protocol is unrun. The identification of multimodal pairwise Euclidean distances with Parisi P(q) (MATH-SKELETON 2.3) is also unproven; those are different random variables.
**Severity:** blocker (as a confirmation claim); the protocol-as-plan is fine

### C19
**Quote:** "Clusters stable across 5 runs | RSB-equivalent confirmed | Analogy upgrades to L2 with simulation"
**Source:** discovery-02-mathematics.md Part V table
**Missing data:** Five Wallacei archives. L2 in validation/validation-framework.md is "simulated performance outcome," not a dip-test on gene distances. The upgrade rule inflates evidence class without performance numbers.
**Severity:** major

### C20
**Quote:** "Random coupling J_ij | Quenched disorder | Fixed climate data (EPW) + fixed geometry"
**Source:** discovery-02-mathematics.md 3.1 table
**Missing data:** A map from EPW time series to a random J ensemble. Climate is a shared exogenous input, not a Gaussian coupling between genes. No <J_ij>, <J_ij^2> estimated from weather realisations.
**Severity:** major

### C21
**Quote:** "Ground state E_gs | Unreachable global minimum | True global optimum (unreachable by NSGA-II from generic start)"
**Source:** discovery-02-mathematics.md 3.1
**Missing data:** Any NSGA-II / Wallacei failure-to-reach result. Unreachability is a property of extensive barriers in large-N glasses, not a 6-gene box with population 50. No barrier heights.
**Severity:** major

### C22
**Quote:** "f3(g) = count of unique panel geometry types"
**Source:** discovery-02-mathematics.md 2.1; grasshopper/optimization-setup.md
**Missing data:** A genome in which f3 can vary. The written genome is one global 6-vector (d,a,r,eps,ms,wr) for the whole facade. Then every panel shares one geometry and f3 = 1 for every individual. A constant objective cannot frustrate anything. No per-panel genes are specified.
**Severity:** blocker

---

## D01 — Temporal Facade Entropy

### C23
**Quote:** "TFE(i, t) = H_space(t) × H_time(i)"
**Source:** MATH-SKELETON.md 1.4; AI-CONTEXT.md D01; discovery-01-temporal-entropy.md
**Missing data:** Any computed TFE on panel time series. Also missing a justification that a product of two entropies is an information measure. Units are bits^2. It is not joint entropy, not mutual information, not transfer entropy. No correlation of TFE with UDI, radiation, or occupancy is in the repo.
**Severity:** major

### C24
**Quote:** "Novelty: No existing metric measures adaptive envelope behaviour as information. Gap confirmed in: Renewable and Sustainable Energy Reviews 232 (2026), Frontiers Built Env (2026)."
**Source:** AI-CONTEXT.md D01; discovery-01-temporal-entropy.md "TFE is a new metric."
**Missing data:** The cited papers are not stored here. discovery-01 itself cites Nexus Network Journal 2025 Shannon entropy on facade visual regularity. "No existing metric" is not demonstrated. No TFE value has been computed, so novelty-as-performance-metric is untested.
**Severity:** major

### C25
**Quote:** "Prediction: TFE_optimised > TFE_rule-based > TFE_static = 0."
**Source:** AI-CONTEXT.md D01; validation/falsification-protocol.md D01
**Missing data:** The three-envelope computation. Not run. grasshopper/step-04-TFE.md even publishes expected numeric bands (0.1-0.5, 1.5-4.0, ~8.0) with no series behind them.
**Severity:** major

### C26
**Quote:** "p_i(t) = normalised open ratio of panel i at time t" used inside H_space = -sum p_i log2 p_i
**Source:** discovery-01-temporal-entropy.md; research/formal-model.md; research/paper-draft-v1.md 3.4
**Missing data:** A probability simplex. Open ratios in [0,1] that do not sum to 1 are not a distribution. Shannon entropy on raw aperture fractions is undefined as information. MATH-SKELETON 1.2 uses a different definition (fraction of panels in state i). Two equations, neither evaluated on data.
**Severity:** blocker

### C27
**Quote:** "a facade with higher TFE encodes more information about interior conditions on the exterior boundary"
**Source:** discovery-01-temporal-entropy.md "Why this matters" item 3
**Missing data:** Mutual information I(panel states; interior sensors), or even a correlation. TFE is a function of facade states only. It can rise because exterior radiation varies, with zero interior encoding. No paired interior/boundary dataset.
**Severity:** blocker

### C28
**Quote:** "A static facade always has H_space = 0."
**Source:** discovery-01-temporal-entropy.md
**Missing data:** A computation. If H_space is entropy of a state histogram, a static facade with mixed fixed angles has H_space > 0. The claim is true only under the extra assumption that all static panels share one state. That assumption is not measured; S1 "static open" in simulation-baseline would be H=0, but a static mixed design would not.
**Severity:** minor

---

## D04 — BIR / holographic analogy

### C29
**Quote:** "Range: [0, 1] (capped at 1 by holographic principle analogy)"
**Source:** AI-CONTEXT.md D04; MATH-SKELETON.md 1.5
**Missing data:** A reason the ratio cannot exceed 1 except by fiat. discovery-04-boundary-information-ratio.md explicitly allows BIR > 1 ("over-responsive"). The cap is an analogy, not a measurement, and it hides the H_interior -> 0 singularity. No BIR(t) series exists.
**Severity:** major

### C30
**Quote:** "Eq 1.4 (TFE) is the numerator of Eq 1.5 (BIR)"
**Source:** MATH-SKELETON.md Section 6
**Missing data:** Consistency. Eq 1.5 sets H_boundary(t) = H_space(t), not TFE. AI-CONTEXT D04 sets H_boundary(t) = TFE. Two numerators. Neither computed.
**Severity:** major

### C31
**Quote:** "q_j(t) = normalised interior variable j at time t" inside H_interior = -sum q_j log2 q_j
**Source:** MATH-SKELETON.md 1.5
**Missing data:** A joint distribution over interior states. Normalised temperature, CO2, occupancy do not form a probability distribution. No sensor archive. prompts/prompts-algorithmic.md A06 averages independent histogram entropies and then caps BIR; that script has never been run on data.
**Severity:** blocker

### C32
**Quote:** "BIR → 1 means facade area encodes interior entropy"
**Source:** AI-CONTEXT.md D04; MATH-SKELETON.md 4.2
**Missing data:** Any pair (H_boundary, H_interior) approaching 1 for a reason other than the min(.,1) clip. Encoding requires a coding theorem or measured mutual information, not a ratio of two loosely defined entropies.
**Severity:** major

### C33
**Quote:** "D02 (H_facade) predicts which design achieves highest BIR" / "Eq 4.2 (BIR→1) is the design target that Eq 3.2 (H_facade optimisation) should achieve"
**Source:** AI-CONTEXT.md Section 3; MATH-SKELETON.md Section 6
**Missing data:** A derivation that argmin H_facade = argmax BIR, plus any evaluated pair (H_facade, BIR). H_facade scalarises radiation, daylight deficit, uniqueness, actuation. BIR is an entropy ratio. They are different functionals. No coincident optimum is shown.
**Severity:** blocker

### C34
**Quote:** "First information-theoretic metric bridging building physics and holographic principle."
**Source:** AI-CONTEXT.md D04
**Missing data:** Literature search plus a measured BIR. research/scientific-position.md and research/boundary-axioms.md Axiom A5 already forbid reading this as physics. As a metric, it has never been computed.
**Severity:** minor (novelty boast); the physics reading would be blocker and is already disallowed by A5

---

## Closed loop, controller, paper overclaim

### C35
**Quote:** "D03 (spore layers) → produces → D01 (TFE > 0)" and "TFE > 0 at zero operational energy cost"
**Source:** AI-CONTEXT.md Section 3; MATH-SKELETON.md 5.2
**Missing data:** A humidity-driven panel-state log and a TFE number. Even as theory: spores track exterior / local RH, not interior occupancy or zone temperature. H_space > 0 from outdoor humidity is not interior encoding and does not support D04. No chamber data in this repo.
**Severity:** major

### C36
**Quote:** "The four discoveries form a closed loop: Material → Behaviour → Information → Optimisation → back to Material"
**Source:** AI-CONTEXT.md Section 3; discoveries/README.md
**Missing data:** Any completed link. D03 not built. D01 not computed. D04 not computed. D02 not optimised. The loop is a diagram.
**Severity:** major

### C37
**Quote:** "a complete, internally consistent, and novel research system"
**Source:** discoveries/README.md
**Missing data:** Internal consistency (C08, C12, C13, C16, C22, C26, C30) and any empirical node. The system is not internally consistent on the written equations.
**Severity:** blocker

### C38
**Quote:** "A computational workflow implemented in Grasshopper and GhPython, validated against a Sydney climate EPW file."
**Source:** research/paper-draft-v1.md Section 1 contribution (2)
**Missing data:** EPW outputs. paper-draft Section 6 is empty. grasshopper/workflow.md is a node list. One controller stub exists (grasshopper/ghpython_state_controller.py). "Validated" is false.
**Severity:** blocker

### C39
**Quote:** "H > 0 encodes spatially differentiated information about the interior state on the boundary surface. This is measurable, not metaphorical."
**Source:** research/formal-model.md
**Missing data:** A measurement. Spatial variety of panel states is measurable. Interior encoding is not shown. Calling the latter "not metaphorical" without a dataset is the metaphor.
**Severity:** major

### C40
**Quote:** "This is the project's core falsifiable claim. If no measurable correlation between X(t) and S(t) can be established, the project's empirical basis fails."
**Source:** research/boundary-axioms.md Axiom A1
**Missing data:** corr(X,S) on simulation or prototype. The axiom correctly names the failure. The correlation has not been established. Empirical basis is currently failed-by-absence, not passed.
**Severity:** major

### C41
**Quote:** "Mechanical metamaterial ... Directly validates the spin-glass optimisation analogy in Step 8 because the geometry of the lattice IS the optimisation variable."
**Source:** materials/selection-matrix.md Recommendation
**Missing data:** Any lattice-gene Wallacei run. Geometry-as-variable does not validate RSB. Category error.
**Severity:** minor

### C42
**Quote:** "theta_max ≈ alpha · n_i" and "tau ≈ 180 seconds"
**Source:** MATH-SKELETON.md 5.1, 5.3
**Missing data:** Cork-substrate calibration in this repo. D03 architecture use (spatial gradient as TFE encoder) has evidence level L0 per discoveries/README.md. Literature numbers are not this project's measurements.
**Severity:** minor for materials; major when used to close the D03→D01→D04 loop (see C35)

### C43
**Quote:** "Four measurable discoveries support it" [the Holographic Envelope Principle]
**Source:** README.md Core Hypothesis
**Missing data:** Four measurements. README status: Wallacei not running, spore prototype not fabricated, BIR not measured. The same README's event-horizon sentence also violates Axiom A5.
**Severity:** blocker

---

## Count

| Severity | Count |
|---|---|
| blocker | 16 |
| major | 21 |
| minor | 6 |
| total | 43 |

Nothing in this list is supported by empirical data in holographic-envelope. Several blockers are worse than "no data": the written equations contradict each other (C08, C12, C13, C16, C22, C26, C30). Those fail before an experiment is run.
