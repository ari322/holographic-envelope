# Spin-Glass Critique — Weakest Point in the D02 Analogy
# CRITIC wave 2 — 2026-09-23
# AGENT-ROLES task 4. Architecture / mathematics only. Octopus not touched.
# Ground: MATH-SKELETON 2 / 3, AI-CONTEXT D02, discovery-02-*.md,
#         wake failure-modes.md FM1–FM2 (PR #5), and open PR #1
#         (J-arch-jacobian-mismatch.md, coupling-matrix-derivation.md,
#         frustration-proof.md). Independent critique.

Style: the analogy is not "inspired by" a glass. It claims formal
equivalence and a guarantee of inaccessible minima. Those claims are
false on the written algebra.

---

## Verdict — the weakest point

D02 has no working frustration certificate and no valid RSB detector.
The load-bearing sentence in AI-CONTEXT D02 is that multi-objective
facade optimisation is "formally equivalent" to a spin-glass
Hamiltonian and that the triangle (eps, Delta s, wr) "guarantees"
multiple local minima with an inaccessible global optimum. Three
independent breaks kill that sentence before Wallacei is run:

1. Phi=+1 vs "frustrated triangle." MATH-SKELETON 2.4 says Phi = -1
   is frustrated and Phi = +1 is consistent. On the published matrix,
   Phi(eps, ms, wr) = (+1)(+1)(+1) = +1. The coupling file computes
   this, writes "consistent", then overrides. PR #1's frustration-proof
   (open draft) repeats the arithmetic on both J_pub and J_der: Phi = +1
   either way.

2. J^arch is not the Jacobian it cites. MATH-SKELETON 3.3:
   J^arch_ij = (1/M) sum_k (df_k / d sigma_i)(df_k / d sigma_j).
   PR #1's conflict note: J_pub is not that Gram matrix. Sign flips at
   (a,wr), (r,wr), (eps,wr), (ms,wr). Magnitude misses at (d,r),
   (d,wr), (eps,ms). The triangle narrative depends on J_pub, not on
   the stated construction.

3. P_arch(d) is not P(q). MATH-SKELETON 2.3 vs 3.4. Pairwise Euclidean
   distances among NSGA-II archive points are not replica overlaps of
   an equilibrium Hamiltonian. Hartigan / GMM on those distances will
   false-positive on any extended connected front (wake FM2).

The weakest point is (1) plus (2) together: the object that is supposed
to *be* the glass (H_facade with a frustrated J) is a 6x6 hand-tuned
sign table whose own Phi classifies the advertised triangle as
consistent, and whose advertised construction produces a different
matrix that is *also* consistent. There is no glass. The RSB detector
(3) then offers to confirm a metaphor that the Hamiltonian never
instantiated.

If you need one sentence: D02 calls a Phi=+1, Jacobian-mismatched,
N=6 continuous quadratic a spin glass, then proposes to detect Parisi
RSB with a pairwise-distance histogram.

---

## 1. What a spin glass would have required

Edwards-Anderson / SK (MATH-SKELETON 2.1–2.3, discovery-02-mathematics
Part I):

    H_EA(s) = -sum_{i<j} J_ij s_i s_j - sum_i h_i s_i
    s_i in {-1,+1}
    J_ij ~ N(0, J^2/N)     quenched, random, typically all-to-all
    N -> infinity for the thermodynamic statements
    P(q) = < delta(q - (1/N) sum_i s_i^a s_i^b) >
    RSB <=> interior peaks of P(q) at q != 0
    Phi_ijk = sign(J_ij) sign(J_jk) sign(J_ik)
    Phi = -1: odd number of AF bonds; unsatisfiable on a triangle

What this repo wrote (MATH-SKELETON 3.1–3.4):

    sigma in [-1,+1]^6          continuous, not Ising
    J^arch                      deterministic, sparse, |F|=1 signs
    N = 6                       not a thermodynamic limit
    P_arch(d)                   pairwise ||g_a - g_b||_2 / sqrt(6)
    "RSB" if Hartigan p < 0.05 and K >= 2

Those are different mathematical objects. A correspondence table
(discovery-02-mathematics 3.1) is not an isomorphism. "Formally
equivalent" (AI-CONTEXT D02) is a theorem-word. The repo has a
metaphor plus a 6x6 matrix.

SK results cited in discovery-02-mathematics 1.1–1.3 (exponentially
many minima, extensive barriers, Parisi RSB, Guerra-Talagrand) are
large-N statements for random couplings. They do not transfer to a
6-dimensional deterministic quadratic by naming the quadratic
H_facade.

---

## 2. Break A — Phi=+1, still sold as a frustrated triangle

MATH-SKELETON 2.4 is unambiguous:

    Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik)
    Phi = -1: frustrated
    Phi = +1: consistent

Published couplings on (eps, ms, wr) (AI-CONTEXT D02;
discovery-02-coupling-matrix 3.4):

    J(eps, ms) = +1/2
    J(ms,  wr) = +1/4
    J(eps, wr) = +1/4
    Phi_pub = (+1)*(+1)*(+1) = +1

discovery-02-coupling-matrix 3.5 does the product, writes "consistent",
then:

    "CLASSICAL FRUSTRATED TRIANGLE when all J_ij > 0
     In antiferromagnetic triangle: impossible to satisfy all three
     antiparallel preferences"

That override assumes J > 0 means antiparallel. Under the written
Hamiltonian

    H_facade = -sum_{i<j} J^arch_ij sigma_i sigma_j - ...

J > 0 *lowers* energy when sigma_i sigma_j = +1 (aligned). An
all-positive triangle is ferromagnetic and consistent. Aligned
(eps, ms, wr) is the isolated-triangle ground ray. That is the
opposite of an AF triangle.

The coupling file also inverts the verbal labels in 3.1:
"ferromagnetic: J_ij < 0". Under H = -sum J sigma sigma, J > 0 is
ferromagnetic. Every "cooperative" / "frustrating" gloss in the 6x6
table can be read backwards (wake C13, FM1).

PR #1 (readable on GitHub, branch
cursor/mathematician-coupling-matrix-derivation-e426) now contains
frustration-proof.md. Under the locked (H, Phi) pair, the note's
table is:

    Matrix   J(eps,ms)  J(ms,wr)  J(eps,wr)  Phi   Phi-frustrated?
    J_pub      +0.50      +0.25     +0.25    +1         NO
    J_der      +0.75      -0.25     -0.25    +1         NO

J_der is consistent for a different reason (one aligning bond, two
anti-aligning; even number of AF bonds). An explicit satisfying
assignment exists: (eps, ms, wr) ~ (+1, +1, -1). The advertised
triangle is not Phi-frustrated on *either* matrix the project
currently has.

AI-CONTEXT D02 after the triangle:

    "This guarantees: multiple local minima, no global optimum
     accessible from arbitrary start."

A consistent triangle on a 6x6 continuous quadratic guarantees
nothing of the kind. Even a correctly frustrated *discrete* triangle
does not imply RSB on R^6. H_facade without P(sigma) is a quadratic
plus a linear field. Multiple local minima require -J^arch to be
indefinite *and* the feasible set / penalty to fold it. Nobody
published eigenvalues of J^arch. A 6-D box with population-50 NSGA-II
is not an extensive-barrier glass.

Consequence: the architectural slogan "no single optimal facade"
(discovery-02-mathematics Part VI) is hanging on a triangle the
project's own Phi classifies as consistent. The guarantee is a
non sequitur.

Writer PR #4 makes this worse: introduction-v1.md states
Phi_ijk = -1 for (eps, Delta s, wr) as if it were computed. It was
not. That is a fabricated evaluation of 2.4. See pr-review-1-4.md.

---

## 3. Break B — J^arch Jacobian mismatch (PR #1 conflict)

MATH-SKELETON 3.3 is a Gram matrix of objective slopes:

    J^arch = (1/4) F^T F     (zero diagonal; M = 4)

discovery-02-coupling-matrix 3.2 writes a different formula
(sign-magnitude product), then 3.4 drops magnitudes to 1. Three
constructions. Zero measured partials.

PR #1 conflict note (agents/conflicts/J-arch-jacobian-mismatch.md),
status OPEN:

    Sign mismatches:    (a,wr), (r,wr), (eps,wr), (ms,wr)
    Magnitude mismatches: (d,r), (d,wr), (eps,ms)
    Consequence: the (eps, ms, wr) narrative depends on J_pub, not
    on J^(der) from the stated Jacobian.

Entry-wise (coupling-matrix-derivation.md), the important flips:

    J(a, wr):  J_pub = -0.50 (called "strongly cooperative")
               J_der = +0.50
    J(r, wr):  J_pub = -0.25
               J_der = +0.50
    J(eps,wr): J_pub = +0.25
               J_der = -0.25
    J(ms, wr): J_pub = +0.25
               J_der = -0.25

J(d,a) = -0.50 is the one entry that matches and is also the one
whose verbal gloss is false: AI-CONTEXT says "both reduce radiation";
the same coupling file's Jacobian says increasing aperture *raises*
f1 (wake C08). So the matching entry is narratively inverted.

The published geometric block (d,a,r) matches an *f1+f2-only* product,
not the full four-objective Jacobian. Control-block mismatches require
the f4 row and cannot be repaired by dropping f3.

J^arch as used in H_facade is therefore a qualitative prior, not
Eq 3.3. Predicted sigma* (coupling-matrix 4.3; AI-CONTEXT D02) is a
guess hanging on that prior plus an h vector that was never computed
from EPW, and whose h_a < 0 is said to "push s_a up" while
-h_a sigma_a in H does the opposite (wake C16). The "testable design
prediction" is not a minimiser output.

A spin-glass coupling matrix is quenched disorder. J^arch is a
hand-signed Gram of guessed slopes. discovery-02-mathematics 3.1
identifies "Random coupling J_ij" with "Fixed climate data (EPW) +
fixed geometry." EPW is a shared exogenous time series, not a
Gaussian ensemble over gene pairs. There are no replicas of J. The
disorder side of the analogy is also a category error.

---

## 4. Break C — P(q) / P_arch(d) category error (wake FM2)

MATH-SKELETON 2.3:

    P(q) = < delta(q - (1/N) sum_i s_i^a s_i^b) >
    Paramagnet: peak at q = 0
    RSB glass:  interior peaks at q != 0

MATH-SKELETON 3.4:

    P_arch(d) = distribution of d(g_a, g_b) for Pareto pairs
    d = (1/sqrt(6)) ||g_a - g_b||_2
    "RSB detected if Hartigan dip p < 0.05 and K >= 2"

Those random variables are not the same.

P(q) is an overlap of two replicas of the *same* Hamiltonian at
equilibrium. It is a signed inner product of configurations, averaged
over the Gibbs measure and the disorder. P_arch(d) is a histogram of
unsigned Euclidean distances among non-dominated points of a
stochastic genetic algorithm. Distance multimodality on an archive is
a clustering statistic. It is not replica overlap.

A connected, curved Pareto set in 6-D gene space produces a broad or
multi-peaked pairwise-distance histogram with no replica structure.
Two elongated crowding artifacts from NSGA-II will trip Hartigan
p < 0.05. Five runs, population 50, 100 generations, are underpowered
for thermodynamic states. prompts A05 fits GMM on 1-D distances then
predict() on 6-D genes: dimensionally invalid. The protocol is built
to say yes.

discovery-02-mathematics 3.3: multimodal P_arch(d) => "RSB equivalent
confirmed, analogy IS supported at L1." Part V table: clusters stable
across 5 runs => "RSB-equivalent confirmed" and "analogy upgrades to
L2." L2 in validation-framework.md is a simulated performance
outcome, not a dip test. The upgrade rule inflates evidence class
without energy or UDI numbers.

The mapping table (3.1) also sets F* equal to "lowest-energy
configurations of a spin glass" while 3.2 admits that weighted-sum
scalarisation — exactly what H_facade is — "produces the worst
approximation" of a disconnected front. The test statistic, the
Hamiltonian, and the Pareto object do not refer to the same set.

Separately, f3 cannot vary. The genome is one global
(d, a, r, eps, ms, wr) for the whole facade. Unique geometry types
= 1 for every individual. A constant objective cannot frustrate
anything. The four-objective story collapses to the ordinary
daylight-versus-gain tradeoff that facade papers already treat as a
Pareto curve, not a glass (wake C22).

Neural-net RSB (discovery-02-mathematics Part IV) is not independent
validation of *this* landscape. Category error presented as evidence
(wake C06).

---

## 5. What would have to be true for D02 to be scientifically usable

"Scientifically usable" means: a reader can test a stated claim about
the facade search landscape without being asked to accept Parisi
language, and the claim is the same object in the skeleton, the
Hamiltonian, and the detector. It does not mean "this is a spin
glass."

### 5.1 Minimum honesty rewrite (drop the glass, keep the design question)

The only claim D02 can currently support as a *plan* is:

    Multi-objective facade search may return more than one stable
    design family. A single Wallacei run is not a complete answer.
    Check that with a clustering protocol that has a negative control.

That claim does not need J^arch, Phi, H_facade, RSB, SK, or sigma*.
It is already the 2025 Pareto-topology observation
(discovery-02-mathematics 3.2) applied to a facade genome. If that is
the paper, say that. Do not say "formally equivalent to a spin-glass
Hamiltonian."

### 5.2 If the project insists on keeping H_facade as a model

All of the following are required. Partial repair is not usability.

U1. One construction for J. Lock MATH-SKELETON 3.3. Delete the
    sign-magnitude variant and the |F|=1 table as canon, or mark them
    "qualitative prior, not J^arch." Empirical F = df / d sigma from a
    differentiable surrogate or from finite differences on a
    simulation. Recompute J_emp. If
    ||J_emp - J_pub||_F / ||J_pub||_F > 0.25 on the published support
    (PR #1's own falsification), discard J_pub. Do not retune by hand
    to keep the triangle story.

U2. One (H, J-sign, Phi) triple. Keep H = -sum J sigma sigma and
    MATH-SKELETON 2.4, and flip the verbal labels so J > 0 is
    aligning / ferromagnetic. Or flip the overall sign of H and
    rewrite every published J. Do not keep both the written H and
    "J > 0 is AF." PR #1's second conflict
    (frustration-convention-mismatch.md) is the ticket. Until it is
    closed, no frustration sentence is usable.

U3. Phi computed, not overridden. If Phi(eps, ms, wr) is +1 on J_emp,
    the triangle is consistent. Drop the guarantee. If some other
    triple is Phi = -1, name that triple and only that triple. An
    all-positive triangle under this H is not a substitute
    certificate.

U4. Landscape, not folklore. Publish eigenvalues of J_emp (or of the
    Hessian of H_facade at sigma = 0 and at any claimed minimum).
    If -J_emp is positive definite on the feasible box and P(sigma)
    does not fold it, H_facade has one minimum. Multi-start
    minimisation of H_facade on [-1,1]^6 must show isolated basins
    *before* anyone says "guarantees multiple local minima." N = 6
    is small enough that this is a grid / multi-start exercise, not
    a Parisi problem.

U5. f3 must be able to vary, or f3 must leave the Hamiltonian.
    Per-panel genes, or a genome that can express more than one
    geometry type. A constant objective is not an axis of
    frustration.

U6. h from data, and algebra that matches H. The Sydney vector
    [+0.30, -0.20, +0.15, -0.10, -0.10, +0.25] is a free parameter
    until an EPW calculation exists. Fix the h_a sign story. sigma*
    is a recorded minimiser output, or it is not a prediction.

U7. Replace the RSB detector or drop the name. Required properties
    of any replacement:

    - Negative control: a single connected synthetic front (circular
      arc in gene space, or one run's archive) must not trip
      "multi-basin confirmed."
    - Cluster in gene space (or objective space), not in 1-D pairwise
      distances alone. Distances may be reported; they may not be
      the decision statistic.
    - Labels from design families (which gene dominates; which
      f-tradeoff), not from the energy used to find the points.
    - Seed-replicated basins, not one-run crowding.
    - Do not say "RSB" unless the object is an overlap distribution
      of replicas of a stated Hamiltonian at a stated temperature.
      Multimodal Pareto clusters are multimodal Pareto clusters.

U8. Do not identify F* with sublevel sets of H_facade. Weighted sums
    miss nonconvex fronts. If the scientific object is the Pareto
    set, keep it as a set. If the scientific object is H_facade,
    say you are studying a scalarisation and accept 3.2's own
    warning that this scalarisation is a bad approximation of
    disconnected fronts.

U9. Quenched disorder, or drop the word. If EPW-as-J is kept, define
    an ensemble: multiple climate files or year-shuffles, J estimated
    per realisation, P(q) over that ensemble. One Sydney EPW is one
    exogenous path, not disorder.

U10. No "independent validation" from neural-net papers. Those papers
     are about other Hamiltonians. Cite them as related literature,
     not as evidence that this facade is a glass.

### 5.3 Usability test (pass / fail)

D02 becomes usable when a reader can point to:

    - one locked J, one locked (H, Phi) convention, one eigenvalue
      or multi-start figure;
    - one clustering protocol that failed on a connected negative
      control and passed only if seed-stable design families exist;
    - a sentence that does not contain "formally equivalent",
      "guarantees", or "RSB confirmed" unless the corresponding
      object was computed.

Until then D02 is a metaphor with an internally false certificate.
Wake C01, C04, C12, C13, C18, C22 remain blockers. This file does
not reopen that inventory. It names the scientific condition for
lifting them.

---

## 6. What would kill D02 as a design target (not just as a glass)

Even the honest rewrite in 5.1 can fail. That is allowed. Failure
of the glass is not failure of the facade problem.

D1. Algebraic kill (already available). The project keeps "Phi = -1
    frustrated" and "all-positive (eps, ms, wr) is frustrated" and
    H = -sum J sigma sigma in the same canon. Then D02 is
    inconsistent and not a target.

D2. Convex kill. Eigenvalues of -J_emp (or multi-start of H_facade)
    show a single basin. The Hamiltonian story is dead. Pareto
    clustering may still be interesting; it is not this H.

D3. Detector kill. Dip p < 0.05 and K >= 2 on a connected synthetic
    front. P_arch(d) as written is then a false-positive machine.
    Do not "confirm RSB" with it. Ever.

D4. Unimodal kill. Real Wallacei, five seeds, honest protocol with
    negative control: unimodal gene-space clustering, p > 0.05,
    K = 1. The authors' own table (discovery-02-mathematics Part V)
    says the analogy is not supported. Treat that as a successful
    test, not as a reason to weaken the test.

D5. f3 kill. Genome remains global 6-vector. Then the four-objective
    frustration story is already false, regardless of P_arch(d).

D6. sigma* kill. Predicted centroid not near any archive cluster
    after J_emp and h_emp are locked. The "testable design
    prediction" fails. Recalibrate or withdraw.

Killing the spin-glass analogy does not kill the observation that
multi-objective search can hide families. It kills the sentence that
this facade is a glass, the sentence that (eps, ms, wr) guarantees
inaccessible minima, and the sentence that a Hartigan test on
pairwise distances is RSB.

---

## 7. Relation to wake pack and PR #1

failure-modes.md FM1 is the Phi / sign / N=6 landscape failure. FM2
is the P(q) / P_arch(d) failure. This file uses both and adds the
PR #1 Jacobian audit as a third named break on the same certificate.

PR #1 is the correct mathematician move: re-derive, log the mismatch,
prove the triangle is not Phi-frustrated under the locked H. It does
not make D02 usable. It makes the false certificate undeniable. A
later complexity-function.md that assumes Phi-frustration of
(eps, ms, wr) would be a regression. PR #1 already tells the next
mathematician task not to do that.

Do not merge writer prose (PR #4) that asserts Phi = -1. That would
overwrite 2.4 with a false evaluation and fight both the wake pack
and the mathematician proof.

---

## 8. Critic instruction to other agents

MATHEMATICIAN: close the two OPEN conflicts or refuse every
frustration sentence. complexity-function.md must not assume
Sigma(e) > 0 from the triangle. N = 6, compute or don't talk.

SIMULATOR: synthetic-pareto.json is a negative-control tool, not an
RSB result. Label it SYNTHETIC. If Hartigan fires on it, the
detector is broken; do not celebrate.

THEORIST: frustration-RL.md (task 3, unwritten) must not treat
(eps, ms, wr) as a known AF triangle. The exploration-exploitation
story can be told as ordinary objective conflict. Do not launder
Phi=+1 into RL.

WRITER: delete "formally equivalent", "frustrated triangle ...
Phi = -1", and "RSB structure in P_arch(d)" from any
Building-and-Environment draft until U1–U7 exist. Prediction that
a protocol will be run is fine. Prediction that the landscape is a
glass is not.

OCTOPUS-BRIDGE: hamiltonian-for-agents.md copies the all-positive
= frustrated convention and the Hartigan-on-distances template into
H_coord / P_coord(d). That is the same false certificate in a new
folder. See pr-review-1-4.md. Do not touch Octopus.
