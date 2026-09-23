# Hostile Referee Report
# Manuscript as implied by the holographic-envelope architecture/math corpus
# (AI-CONTEXT.md, MATH-SKELETON.md, discoveries/discovery-02-*, discovery-01, discovery-04,
#  research/paper-draft-v1.md, research/formal-model.md)
# Target journal: Building and Environment
# CRITIC first wake — 2026-09-23
# Register: reject / major revision only if the authors withdraw the physics claims
# and replace every number that was not computed.

---

## Summary recommendation

Reject.

The authors submit a framework, not a building-science result. Building and Environment publishes measurements: energy, IEQ, envelope performance, validated simulation. This corpus contains no EPW output table, no Wallacei archive, no prototype time series, and no sensor-derived entropy. research/paper-draft-v1.md Section 6 is an empty table. The same draft's introduction claims a Grasshopper workflow "validated against a Sydney climate EPW file." That sentence is false on the authors' own files (validation/simulation-baseline.md: "simulation pending").

What remains is a stack of analogies (Shannon product, Ising Hamiltonian, AdS/CFT, Parisi RSB) whose internal algebra does not close. I would not send this to a second round until the Hamiltonian, the coupling matrix, and the information metrics are consistent with each other and evaluated on data. A rewrite that keeps the present D02 "formal equivalence" language should be rejected again.

---

## Major concerns

### 1. There are no results

validation/evidence-report.md grades the novel claim ("Multi-objective facade optimisation exhibits a frustration-like landscape") as L0: "NOT yet computationally tested." discoveries/README.md: TFE "computation pending," D02 "Wallacei run pending," BIR "simulation validation pending." validation/prototype-log.md: every build stage dated "—".

A Building and Environment paper without a climate calculation, a chamber test, or a field dataset is a manifesto. The journal is not a venue for unpublished Hamiltonians.

paper-draft-v1.md contribution (2) asserts EPW validation. Section 6 contradicts it. That is not a missing figure. It is a false claim in the contribution list.

### 2. "Formally equivalent" to a spin glass is false as written

AI-CONTEXT.md D02: "Multi-objective facade optimisation is formally equivalent to finding low-energy configurations of a spin-glass Hamiltonian."

discovery-02-mathematics.md 2.3: the Pareto set F* "is the set of lowest-energy configurations of a spin glass."

It is not. A spin-glass Hamiltonian is a scalar. A Pareto set is a partial order. The authors know this: 2.3 says F* is a set "because the objectives are incommensurable," and 3.2 says weighted-sum scalarisation "produces the worst approximation" of disconnected fronts. MATH-SKELETON.md 3.2 then defines H_facade as exactly that scalarisation (quadratic couplings plus linear field plus penalty). The object used to "be" the spin glass is the object they say cannot represent the Pareto front.

SK / Parisi theory in discovery-02-mathematics.md Part I is not transferable to N = 6 continuous genes with a deterministic sparse J. Exponential complexity Sigma(e), threshold energy E_th, non-ergodicity, extensive barriers — these are large-N, quenched-disorder statements. Copying them into a 6-parameter Grasshopper genome is not a derivation.

### 3. The coupling matrix is uncalibrated and self-contradictory

I checked the arithmetic and the words.

discovery-02-coupling-matrix.md 3.4 builds J^arch by setting every |df_k / ds_j| = 1. MATH-SKELETON.md 3.3 writes the actual Gram matrix of objective gradients. Those are different matrices. No Jacobian was ever evaluated on a model.

The published entry J(d,a) = -1/2 is glossed "cooperative: both reduce radiation" (AI-CONTEXT.md; coupling-matrix 3.4). The same coupling file's Jacobian (3.3) says increasing aperture raises interior radiation. The gloss is wrong.

Sign convention: coupling-matrix 3.1 defines ferromagnetic as J < 0. Hamiltonian 4.1 / MATH-SKELETON 3.2 is H = -sum J_ij sigma_i sigma_j, under which J > 0 is ferromagnetic. The table's "frustrating" entries may be the cooperative ones.

External field: h_a = -0.20 is said to "push s_a up" (coupling-matrix 4.2). The term -h_a sigma_a with h_a < 0 is minimised at sigma_a < 0. The predicted ground state s_a ~ +0.3 (4.3) fights the field. sigma* is not a recorded minimiser of H_facade; it is a guessed vector inverse-mapped to millimetres.

I will not accept a 6x6 matrix of +/- 1/2 and +/- 1/4, a hand-set Sydney field, and a guessed sigma* as "the first formal Ising Hamiltonian encoding" of a facade (coupling-matrix Part VI).

### 4. The frustrated triangle is not frustrated under the authors' own test

MATH-SKELETON.md 2.4: Phi_ijk = -1 frustrated.

For (eps, ms, wr), J_ij are all positive. Product = +1. coupling-matrix 3.5 computes this, writes "consistent", then announces a "CLASSICAL FRUSTRATED TRIANGLE when all J_ij > 0." That is not how they defined Phi, and it is not how their H treats positive J.

AI-CONTEXT.md uses this triangle to "guarantee" multiple local minima and an inaccessible global optimum. A 6-D quadratic does not inherit Parisi RSB from a misclassified triangle. Eigenvalues of J^arch are not in the manuscript because they were not computed.

### 5. The RSB protocol cannot confirm RSB

MATH-SKELETON.md 2.3 vs 3.4: Parisi overlap P(q) is replaced by a histogram of pairwise Euclidean distances among Pareto archives, P_arch(d). Hartigan p < 0.05 and GMM K >= 2 are declared "RSB equivalent confirmed" (AI-CONTEXT.md; discovery-02-mathematics.md 3.3, Part V).

That test is not specific. Any extended Pareto archive has a distance distribution. Crowding and seed-to-seed drift in NSGA-II produce multiple modes without thermodynamic states. Five runs, population 50, 100 generations, is a student workshop setting, not a replica-symmetric-breaking experiment.

The implementation note in prompts/prompts-algorithmic.md A05 fits a GMM on 1-D distances and then calls predict on 6-D gene vectors. That code cannot label design families. The comment "if k >= 2: RSB equivalent detected" is how a metaphor becomes a false positive.

Part IV calls neural-network loss-landscape RSB "INDEPENDENT VALIDATION" of the facade claim. It is not. It is a different system.

### 6. f3 is constant; the four-objective frustration is not formulated

discovery-02-mathematics.md 2.1 and grasshopper/optimization-setup.md: genome = one global (d, a, r, eps, maxStep, wr). f3 = number of unique panel geometry types. Under that genome every panel shares one geometry. f3 = 1 for all individuals. The fabrication-versus-performance conflict (2.2) is not in the search space.

The authors cannot claim a four-objective frustrated landscape while encoding a single facade type.

### 7. TFE is not an information measure of interior state

MATH-SKELETON.md 1.4: TFE(i,t) = H_space(t) x H_time(i). Product of entropies. Units bits^2. Not joint entropy, not mutual information.

H_space is defined twice:
- MATH-SKELETON 1.2: occupation frequencies of discrete states (a distribution)
- discovery-01 / formal-model / paper-draft 3.4: "p_i = normalised open ratio of panel i" inside -sum p log p (not a distribution)

Those formulae will not return the same number. Neither has been computed. AI-CONTEXT.md still claims a literature "gap confirmed" and a strict ordering TFE_optimised > TFE_rule-based > TFE_static = 0.

discovery-01 then says higher TFE "encodes more information about interior conditions." TFE has no interior argument. A solar tracker produces TFE. So does a humidity bilayer that never sees occupancy (MATH-SKELETON 5.2). Encoding is I(boundary; interior), which is absent.

### 8. BIR is an ad hoc ratio with two numerators and a decorative cap

MATH-SKELETON 1.5: BIR = H_boundary / H_interior, H_boundary = H_space, range capped [0,1] "by holographic principle analogy."
MATH-SKELETON Section 6: "Eq 1.4 (TFE) is the numerator of Eq 1.5."
AI-CONTEXT D04: H_boundary = TFE.

Pick one numerator.

H_interior uses "normalised interior variable j" as if it were a probability (1.5). It is not. If H_interior -> 0 (empty building) BIR diverges; the cap manufactures the holographic limit. discovery-04 allows BIR > 1. The definition disagrees with itself.

Section 6: minimising H_facade "should achieve" BIR -> 1. H_facade does not contain BIR. No identity connects them. This is how a journal gets a physics-sounding objective that the optimiser is not optimising.

Axiom A5 (research/boundary-axioms.md) correctly forbids claiming black-hole physics. README.md then says the envelope "can behave like the event horizon of a black hole" and that "Four measurable discoveries support it." None were measured. The authors cannot police the analogy in one file and sell it in another.

### 9. The closed loop is a storyboard

AI-CONTEXT.md Section 3: D03 produces TFE; TFE plus sensors produce BIR; H_facade predicts the high-TFE family; BIR rewards a controller; material loop closes.

D03 has no cork-spore theta(n) in this repo (MATH-SKELETON 5.1: "to be calibrated"). Humidity actuation, if it worked, would couple to exterior RH, undermining BIR as interior encoding. D01 and D04 are uncomputed. D02 has no front. There is no loop.

---

## Minor concerns

1. Citation identifiers are sloppy. "arXiv 2606.16792 (2025)" (AI-CONTEXT.md; discovery-02-mathematics.md 3.2) mixes a June 2026 arXiv stem with a 2025 year. I cannot verify that this paper exists from the repo. Do not cite what you have not filed.

2. Evidence-class inflation. discovery-02-mathematics.md Part V upgrades to "L2 with simulation" for stable clusters. The project's own ladder (validation/validation-framework.md) reserves L2 for performance outcomes (radiation, daylight), not a dip test.

3. grasshopper/step-04-TFE.md quotes expected TFE bands (0.1-0.5 rule-based, 1.5-4.0 optimised, ~8 theoretical) as if they were results. They are wishes.

4. materials/selection-matrix.md: a metamaterial lattice "directly validates the spin-glass optimisation analogy because the geometry of the lattice IS the optimisation variable." Geometry-as-gene does not validate RSB. Remove.

5. paper-draft-v1.md still carries PCM 15-45% energy savings into an envelope paper whose mechanism is geometric / informational. That literature claim is off-target and unused by H_facade.

6. Controller defaults (eps = 0.05, maxStep = 0.10 in formal-model.md) are not the sigma* implied values (eps ~ 0.064, ms ~ 0.14). Two uncalibrated parameter sets.

7. ROADMAP.md progress tracker marks Steps 1, 2, 6, 8, 10 "not started" while the corresponding files claim "complete." Editorial control is weak.

8. Novelty sentences ("first," "never been stated," "no existing metric") are not a substitute for a search protocol. literature-map.md Pillar 5 already admits the spin-glass–architecture link was not found, which is not the same as not existing.

---

## Questions the authors must answer

Q1. Evaluate H_facade on a 20^6 grid or a dense multi-start. How many distinct local minima? What are the eigenvalues of J^arch? If the quadratic is convex, withdraw the RSB language.

Q2. Recompute Phi_ijk for every triplet with the written J and the written definition (MATH-SKELETON 2.4). Which triplets are frustrated? Why was (eps, ms, wr) retained after the product came out +1?

Q3. State, in one paragraph, whether J > 0 is ferromagnetic or antiferromagnetic under H = -sum J sigma_i sigma_j. Then rewrite every "cooperative / frustrating" caption so it matches that paragraph.

Q4. Produce the 4x6 Jacobian at the predicted sigma* from a documented radiation + daylight model. Show J^arch from MATH-SKELETON 3.3, not from |F|=1. If you cannot, delete the numerical matrix.

Q5. Minimise the written H_facade with the written h. Is the minimiser the published sigma*? If not, delete sigma*.

Q6. Explain how f3 varies under a single global 6-gene genome. If it does not, drop f3 or change the genome.

Q7. Which quantity is H_boundary: H_space or TFE? Delete one definition.

Q8. Why is -sum_i (open_ratio_i) log(open_ratio_i) Shannon entropy? If it is not, delete it from formal-model.md and paper-draft Section 3.4.

Q9. Report I(panel states; interior sensors) on any dataset you have. If you have none, stop claiming encoding.

Q10. Run the three-envelope TFE test in validation/falsification-protocol.md D01. Publish the three numbers. If the order fails, the metric fails.

Q11. Run Wallacei 5x as specified. Publish P_arch(d), Hartigan p, GMM K, and cluster centroids. Also publish the same statistics on a synthetic connected front. If the synthetic front trips K>=2, your RSB detector is worthless.

Q12. Show a monotonic relationship, or a scatter, of H_facade versus BIR. If none, delete MATH-SKELETON Section 6's claim that 3.2 targets 4.2.

Q13. Produce the Sydney EPW table that paper-draft contribution (2) says already exists, or retract the sentence.

Q14. Which file is binding when README's event-horizon sentence conflicts with Axiom A5?

---

## What evidence would change my mind

I will read a major-revision if and only if all of the following are in the manuscript, not in a future-work paragraph:

1. A consistent Hamiltonian: one sign convention, one J construction from a computed Jacobian, eigenvalues, and a real minimiser. No "formally equivalent to SK." Bounded language: "we tested a quadratic interaction model with 6 genes."

2. A genome in which every objective can move. If f3 matters, genes must be per-panel or discrete types. Show the front.

3. One entropy definition, implemented once, run on S0 / S1 / S2. TFE reported as what it is (a product of histogram entropies), not as interior information, unless mutual information is also reported.

4. BIR either dropped or redefined without a holographic cap and without two numerators. If kept, show the time series and its correlation with occupancy, CO2, and exterior RH separately.

5. The RSB claim reduced to: "multiple Wallacei seeds produced K clusters; here are the designs." No Parisi, no "confirmed equivalent," no neural-net "independent validation." Include a negative-control distance histogram.

6. Retraction of "validated against Sydney EPW" until the CSV exists. Empty Section 6 is acceptable in a draft; it is not acceptable next to a validation claim.

7. Title and abstract that a Building and Environment reader can cash: climate, envelope, metric, number. "Holographic" stays only as a clearly bounded analogy, consistent with Axiom A5, or it goes.

Until then the correct editorial decision is reject. The authors have a research programme and a self-contradictory skeleton. They do not have a paper.
