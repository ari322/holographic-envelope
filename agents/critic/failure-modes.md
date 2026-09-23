# Failure Modes — Architecture / Mathematics
# CRITIC first wake — 2026-09-23
# Exactly three. Named from MATH-SKELETON.md and discovery-02-*.
# Each: how it fails, what you would observe.

The program does not fail because "the math might be wrong."
It fails at three specific written objects.

---

## FM1 — The frustrated-triangle certificate does not create a spin-glass landscape

**Named objects**
- MATH-SKELETON.md 2.4: Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik); Phi = -1 frustrated, +1 consistent
- MATH-SKELETON.md 3.2: H_facade(sigma) = -sum_{i<j} J^arch_ij sigma_i sigma_j - sum_i h_i sigma_i + lambda P(sigma)
- MATH-SKELETON.md 3.3: J^arch_ij = (1/M) sum_k (df_k / d sigma_i)(df_k / d sigma_j)
- discovery-02-coupling-matrix.md 3.4–3.5: J(eps, ms) = +1/2, J(ms, wr) = +1/4, J(eps, wr) = +1/4; claimed "CLASSICAL FRUSTRATED TRIANGLE"
- AI-CONTEXT.md D02: "This guarantees: multiple local minima, no global optimum accessible from arbitrary start."

**How it fails**

Three independent breaks, any one of which kills the guarantee.

1. Phi on (eps, ms, wr) is +1, not -1. discovery-02-coupling-matrix.md 3.5 computes the product, writes "consistent", then overrides the project's own definition. An all-positive triangle is ferromagnetic under H = -sum J sigma_i sigma_j (MATH-SKELETON 3.2). Aligned (eps, ms, wr) lowers energy. That is the opposite of an antiferromagnetic triangle.

2. Verbal J-signs are inverted relative to H. coupling-matrix 3.1: "ferromagnetic: J_ij < 0." Under 3.2, J > 0 is ferromagnetic. Every "cooperative" / "frustrating" label in the 6x6 table can be read backwards. J(d,a) = -1/2 is called cooperative because "both reduce radiation," but the same file's Jacobian says increasing a raises f1. The matrix is a sign-agreement table with |F_kj| set to 1. It is not Eq 3.3.

3. Even a correctly frustrated discrete triangle does not imply RSB on R^6. sigma is continuous in [-1,+1]^6 (MATH-SKELETON 3.1), not Ising. H_facade without P(sigma) is a 6x6 quadratic plus a linear field. Multiple local minima require the quadratic form -J^arch to be indefinite *and* the feasible set / penalty to fold it. Nobody computed eigenvalues of J^arch. SK results cited in discovery-02-mathematics.md 1.1–1.3 (exponentially many minima, extensive barriers, Parisi RSB) are thermodynamic-limit statements for random couplings with N -> infinity. N = 6, J deterministic and sparse, is a different object.

Consequence: the "guarantee" of inaccessible global optima is a non sequitur. The architectural slogan "no single optimal facade" (discovery-02-mathematics.md Part VI) is hanging on a triangle that the project's own Phi classifies as consistent.

**Observable signature**

- Eigenvalues of J^arch (or of the Hessian of H_facade at sigma=0): if all eigenvalues of -J^arch are positive (or the constrained quadratic is convex), H_facade has one minimum. Prediction of many basins is dead before Wallacei.
- Direct grid or multi-start minimisation of H_facade on [-1,1]^6: one attractor, or a connected valley, not K isolated minima.
- Recalculated Phi_ijk over the written matrix: only the special-plead (eps, ms, wr) is called frustrated, and it fails Eq 2.4.
- If Wallacei is later run and P_arch(d) is unimodal (discovery-02-mathematics.md 3.3, "analogy is NOT supported"), that is the empirical form of this failure. It is not required; the algebra already fails.

---

## FM2 — P_arch(d) is not P(q); the RSB detector will confirm a metaphor that is not there

**Named objects**
- MATH-SKELETON.md 2.3: P(q) = < delta(q - (1/N) sum_i s_i^a s_i^b) >; RSB <=> multiple interior peaks at q != 0
- MATH-SKELETON.md 3.4: P_arch(d) = distribution of d(g_a, g_b) for Pareto pairs; d = (1/sqrt(6)) ||g_a - g_b||_2; "RSB detected if Hartigan dip p < 0.05 and K >= 2"
- discovery-02-mathematics.md 3.1: "Replica Symmetry Breaking | Different Wallacei runs converge to different Pareto segments"
- discovery-02-mathematics.md 3.3 and Part V: 5 seeds, population 50, 100 generations; K>=2 => "RSB equivalent confirmed"
- discovery-02-mathematics.md 2.1 / optimization-setup.md: one global 6-gene vector; f3 = unique geometry count
- prompts/prompts-algorithmic.md A05: GMM fitted on 1-D distances, then predict() on 6-D genes; "if k >= 2: RSB equivalent detected"

**How it fails**

P(q) is an overlap of two replicas of the same Hamiltonian at equilibrium. P_arch(d) is a histogram of pairwise Euclidean distances among non-dominated points of a stochastic genetic algorithm. Those are not the same statistic.

A connected, curved Pareto set in 6-D gene space produces a broad or even multi-peaked pairwise-distance histogram without any replica structure. Two elongated clusters that are artifacts of NSGA-II archive crowding will trip Hartigan p < 0.05. Five short runs (N_pop=50, 100 gen) are underpowered for claiming thermodynamic states. GMM-on-distances in A05 is a second, weaker detector; its label step is dimensionally invalid (1-D model, 6-D predict). The protocol is built to say yes.

The mapping table (discovery-02-mathematics.md 3.1) also mis-identifies the disorder: "Random coupling J_ij = Fixed climate data (EPW) + fixed geometry." EPW is a shared exogenous time series, not a quenched Gaussian J_ij ensemble. There are no replicas of J.

Separately, f3 cannot vary. The genome is one (d,a,r,eps,ms,wr) for 80 panels. Unique geometry types = 1 for every individual. The four-objective "frustration" of discovery-02-mathematics.md 2.2 loses the fabrication axis. The remaining conflict is the ordinary daylight-versus-gain tradeoff, which every facade paper already treats as a Pareto curve, not a spin glass.

discovery-02-mathematics.md 2.3 then sets F* equal to "lowest-energy configurations of a spin glass" while 3.2 admits weighted-sum scalarisation (exactly what H_facade is) "produces the worst approximation" of a disconnected front. The test statistic, the Hamiltonian, and the Pareto object do not refer to the same set.

**Observable signature**

- Dip p < 0.05 and K >= 2 on a *single* connected synthetic front (e.g. a circular arc in gene space, or one Wallacei run's archive). If that happens, the detector false-positives. The repo currently has no synthetic-pareto.json; this check is still unrun.
- Cluster labels that do not match distinct design families (the "deep-reveal / high-rotation / low-actuation" story in Part V). Multimodality of distances without stable, seed-replicated basins is crowding, not RSB.
- f3 identically 1 across all individuals. Then the 4-objective Hamiltonian story is already dead, regardless of P_arch(d).
- Predicted sigma* (coupling-matrix 4.3) not near any archive centroid. That kills the "testable design prediction" without needing Parisi language.
- Honest negative: unimodal P_arch(d), p > 0.05, K = 1. The authors' own table says the analogy is not supported. Treat that as success of the protocol, not as a reason to weaken the test.

---

## FM3 — TFE x BIR is not a well-posed information functional, so H_facade cannot target it

**Named objects**
- MATH-SKELETON.md 1.2 vs discovery-01-temporal-entropy.md / formal-model.md: two different p_i(t) (state occupation frequencies vs raw open ratios)
- MATH-SKELETON.md 1.4: TFE(i,t) = H_space(t) x H_time(i); TFE_total = average of the product
- MATH-SKELETON.md 1.5: BIR(t) = H_boundary(t) / H_interior(t), H_boundary := H_space(t), range capped [0,1]
- MATH-SKELETON.md Section 6: "Eq 1.4 (TFE) is the numerator of Eq 1.5 (BIR)" and "Eq 4.2 (BIR→1) is the design target that Eq 3.2 (H_facade optimisation) should achieve"
- AI-CONTEXT.md D04: H_boundary(t) = TFE at time t  (contradicts 1.5)
- MATH-SKELETON.md 5.2 / AI-CONTEXT.md Section 3: n_layers gradient => H_space > 0 => TFE > 0 at zero operational energy, then BIR

**How it fails**

The numerator is not defined once. Skeleton 1.5 uses H_space. Skeleton Section 6 and AI-CONTEXT D04 use TFE. TFE is a product of entropies (bits^2), H_space is bits. You cannot swap them inside a ratio and keep a meaning.

H_space itself is not defined once. Skeleton 1.2 is a histogram over discrete panel states (valid Shannon entropy if the bins partition the facade). discovery-01 and formal-model feed normalised open ratios of each panel into -sum p log p. Those ratios are not a probability distribution. The formal-model formula is not entropy.

H_interior in 1.5 uses q_j(t) = "normalised interior variable j." Temperature, CO2, occupancy scaled to [0,1] do not sum to 1. The ratio BIR is then capped at 1 "by holographic principle analogy." discovery-04 allows BIR > 1. Capping hides the empty-building pole H_interior -> 0.

TFE does not mention the interior. A high-TFE facade can be tracking solar geometry only. MATH-SKELETON 5.2 makes this worse: humidity-programmed spores produce H_space > 0 from exterior RH. That raises TFE and can raise a naively computed BIR without any interior encoding. The holographic slogan (README; AI-CONTEXT D04) requires a coding relation, i.e. mutual information, not a ratio of two marginal-looking scalars.

H_facade (3.2) scalarises f1..f4 (radiation, daylight deficit, uniqueness, actuation). None of those is BIR. Section 6 asserts that minimising 3.2 should drive BIR -> 1. There is no Lagrange identity, no monotonicity proof, and no evaluated pair (H_facade, BIR). If f3 is constant (FM2), the Hamiltonian is not even the intended 4-objective object.

**Observable signature**

- Two TFE implementations (histogram vs open-ratio) on the same panel_states array disagree by O(1) bits / bits^2. The metric is not reproducible across the project's own files.
- TFE_rule-based >= TFE_optimised (falsification-protocol D01) or TFE_static > 0 for a mixed static design. Ordering claims collapse.
- BIR(t) spikes when the building is empty (H_interior small) and sits at the cap 1.0 under A06's min(.,1). The series is an artefact of normalisation, not a holographic limit.
- corr(TFE, interior occupancy or CO2) ~ 0 while corr(TFE, exterior RH or radiation) > 0, especially on a spore-gradient model. Boundary entropy is not interior information.
- Designs that minimise H_facade do not maximise BIR (or TFE). The Section 6 dependency chain is false as an optimisation statement.

---

## Why these three, not others

Spore fabrication risk is real (D03 L0 in architecture) but it is not a MATH-SKELETON / discovery-02 failure. Citation hygiene and EPW-not-run are process failures; they do not name an equation.

These three name the equations the architecture stands on:
FM1 — J^arch and Phi do not give the landscape they advertise.
FM2 — P_arch(d) will not be RSB even if it looks multimodal.
FM3 — TFE/BIR is not a quantity H_facade can target, and it is not interior information.

If FM1 and FM2 both trigger, D02 is rhetoric. If FM3 triggers, D01+D04 do not measure what the title claims. The closed loop in AI-CONTEXT.md Section 3 then has no working node.
