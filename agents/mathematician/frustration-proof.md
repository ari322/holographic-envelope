# Frustrated Triangle Proof — (eps, ms, wr)
# Agent: MATHEMATICIAN
# Date: 2026-09-23
# Status: VERIFICATION (not a new discovery)
# Depends on: agents/mathematician/coupling-matrix-derivation.md
# Conflicts: agents/conflicts/J-arch-jacobian-mismatch.md
#            agents/conflicts/frustration-convention-mismatch.md

## Purpose

Verify the project's claim that the gene triplet (eps, ms, wr)
= (epsilon, maxStep / Delta s, radiation weight) is a frustrated triangle
in J^arch.

Falsification condition for this note:
  (F1) If the project adopts Hamiltonian H = -sum J_ij sigma_i sigma_j
       (as in MATH-SKELETON / AI-CONTEXT) AND keeps the Phi definition
       Phi = sign(J_ij)*sign(J_jk)*sign(J_ik) with Phi=-1 => frustrated,
       THEN the claim "(eps,ms,wr) is Phi-frustrated" is FALSE for both
       J_pub and J_der as computed in coupling-matrix-derivation.md.
  (F2) After empirical F = df/d sigma is measured, recompute J_emp and Phi.
       If Phi_emp(eps,ms,wr) = -1 under the locked convention, restore the
       Phi-frustration claim for that empirical matrix only.

RSB is not addressed here and remains PREDICTED only.

---

## 1. Definitions (locked)

Genes (control block):
  eps = hysteresis band (normalised sigma_eps)
  ms  = maxStep / Delta s (normalised sigma_ms)
  wr  = radiation weight (normalised sigma_wr)

Hamiltonian (MATH-SKELETON Sec 3.2, AI-CONTEXT D02):
  H_facade(sigma) = - sum_{i<j} J_ij * sigma_i * sigma_j
                    - sum_i h_i * sigma_i
                    + lambda * P(sigma)

Pair energy for one bond (ignore h, P):
  E_ij = - J_ij * sigma_i * sigma_j

Consequence of the minus sign:
  If J_ij > 0, E_ij is minimised when sigma_i * sigma_j = +1 (aligned).
  If J_ij < 0, E_ij is minimised when sigma_i * sigma_j = -1 (anti-aligned).

So under THIS H:
  J_ij > 0  <=>  aligning / ferromagnetic bond preference
  J_ij < 0  <=>  anti-aligning / antiferromagnetic bond preference

MATH-SKELETON Sec 2.4 frustration indicator for a triangle (i,j,k):
  Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik)
  Phi_ijk = -1 : frustrated (odd number of anti-aligning bonds)
  Phi_ijk = +1 : consistent

Lemma (standard Ising, odd cycle):
  On a triangle, the three pairwise alignment preferences can be satisfied
  simultaneously iff Phi = +1. Proof sketch: assign sigma_i = +1 without loss
  of generality; each positive-J bond forces the neighbour equal, each
  negative-J bond forces the neighbour opposite; closing the loop is
  consistent iff the number of negative-J bonds is even, i.e. Phi = +1.

---

## 2. Published matrix J_pub on (eps, ms, wr)

From AI-CONTEXT / discovery-02-coupling-matrix:
  J_pub(eps, ms) = +0.50
  J_pub(ms,  wr) = +0.25
  J_pub(eps, wr) = +0.25

All three signs positive.

Phi_pub(eps, ms, wr) = (+1)*(+1)*(+1) = +1

By Sec 1 Lemma: the triangle is CONSISTENT under H = -sum J sigma sigma.
Every bond wants alignment. Ground states of the isolated triangle:
  (eps, ms, wr) = (+s, +s, +s) or (-s, -s, -s) for s in (0,1]
(with continuous spins in [-1,+1], the same ray arguments apply).

CLAIM P1: Under the locked H and Phi, J_pub does NOT make (eps,ms,wr)
Phi-frustrated.
  Falsify: change H or Phi by explicit project amendment, or exhibit a
  sign error in the published triple.

---

## 3. Derived matrix J_der on (eps, ms, wr)

From coupling-matrix-derivation.md (unit-magnitude (1/4) F^T F):
  J_der(eps, ms) = +0.75
  J_der(ms,  wr) = -0.25
  J_der(eps, wr) = -0.25

Phi_der(eps, ms, wr) = (+1)*(-1)*(-1) = +1

Again CONSISTENT: one aligning bond (eps-ms) and two anti-aligning bonds
(eps-wr, ms-wr). Even number of AF bonds => satisfiable.

Explicit satisfying assignment (discrete illustration s=+/-1):
  Take sigma_eps = +1, sigma_ms = +1 (satisfies J_eps_ms > 0).
  Take sigma_wr = -1 (satisfies both J_eps_wr < 0 and J_ms_wr < 0).
  All three pairwise preferences held.

CLAIM P2: Under the locked H and Phi, J_der does NOT make (eps,ms,wr)
Phi-frustrated.
  Falsify: arithmetic error in J_der (see coupling-matrix-derivation.md
  CLAIM A) or a different authorised F table.

---

## 4. Where the project narrative disagrees

discovery-02-coupling-matrix.md Sec 3.5 states that (eps, ms, wr) with
all positive couplings is a "CLASSICAL FRUSTRATED TRIANGLE" because
"all three are antiferromagnetic" and "impossible to satisfy all three
antiparallel preferences".

That paragraph assumes:
  (A) J > 0 means antiferromagnetic / antiparallel preference, AND
  (B) three AF bonds on a triangle are frustrated.

(B) is true for AF bonds. (A) contradicts Sec 1 under H = -sum J sigma sigma,
where J > 0 prefers PARALLEL, not antiparallel.

If one rewrites the Hamiltonian as
  H_alt = + sum_{i<j} J_ij * sigma_i * sigma_j - ...
with the SAME numerical J_pub > 0, then J > 0 would prefer antiparallel,
and the all-positive triangle WOULD be AF-frustrated. That is a different
H than the one written in MATH-SKELETON / AI-CONTEXT.

CLAIM P3: The published "classical AF triangle" sentence is inconsistent
with the written H = -sum J sigma sigma unless verbal labels for the sign
of J are flipped.
  Falsify: produce a single self-consistent (H, J-sign-label, Phi) triple
in the canon files that makes the sentence true without changing arithmetic.

Conflict ticket: agents/conflicts/frustration-convention-mismatch.md

---

## 5. What CAN still be said without claiming Phi-frustration

Even when Phi = +1, the control block can be "difficult" for multi-objective
search in a weaker sense:

  (W1) Objectives f1,f2 favour responsive control (smaller eps, adjusted ms)
       while f4 favours fewer actuations (larger eps, smaller ms). That is
       objective-space conflict, not necessarily Phi=-1 in gene-gene J.

  (W2) Under J_der, wr is anti-aligned with both eps and ms, so the radiation
       weight prefers the opposite polarity of the (eps,ms) pair. That is a
       structured trade-off, still Phi-consistent.

  (W3) Landscape multiplicity (multiple Wallacei attractors) is an empirical
       question for the RSB protocol. It does NOT follow from Phi_pub or
       Phi_der alone for this triangle.

None of (W1)-(W3) upgrades RSB beyond PREDICTED.

---

## 6. Summary table

  Matrix   J(eps,ms)  J(ms,wr)  J(eps,wr)  Phi   Phi-frustrated?
  J_pub      +0.50      +0.25     +0.25    +1         NO
  J_der      +0.75      -0.25     -0.25    +1         NO

Verdict: Task "verify frustrated triangle for (eps, Delta s, wr)" under the
locked canon (H, Phi) returns NOT Phi-frustrated for both available matrices.
The stronger AF-triangle narrative is a convention mismatch, logged as conflict.

Next task: complexity-function.md (Sigma(e) for H_facade), which must not
assume Phi-frustration of (eps,ms,wr) without resolving the conflict.
