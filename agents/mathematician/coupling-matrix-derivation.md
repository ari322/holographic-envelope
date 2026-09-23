# Coupling Matrix J^arch — Jacobian Re-derivation
# Agent: MATHEMATICIAN
# Date: 2026-09-23
# Status: VERIFICATION (not a new discovery)

## Purpose

Re-derive each entry of the 6x6 architectural coupling matrix J^arch
from the objective Jacobian, using the construction in MATH-SKELETON.md
Sec 3.3 and discoveries/discovery-02-coupling-matrix.md Part III.

Falsification condition for this verification note:
  After Wallacei (or any differentiable surrogate) supplies empirical
  partial derivatives F_kj = df_k / d sigma_j at a reference design,
  recompute J_emp = (1/4) F^T F (off-diagonal). If
  ||J_emp - J_pub||_F / ||J_pub||_F > 0.25 on the published support,
  then J^arch in AI-CONTEXT.md must be recalibrated and the
  frustrated-triangle claim re-checked.

Do NOT treat this note as confirmation of RSB.

---

## 1. Gene order and objectives

Normalised genes sigma in [-1,+1]^6:
  index: 0=d, 1=a, 2=r, 3=eps, 4=ms (Delta s / maxStep), 5=wr

Objectives (all minimise), from discovery-02-mathematics.md:
  f1 = mean incident solar radiation
  f2 = fraction of occupied hours below 300 lux UDI
  f3 = count of unique panel geometry types
  f4 = mean actuation events per panel per day

M = 4.

---

## 2. Construction formula

MATH-SKELETON.md Sec 3.3:
  J^arch_ij = (1/M) sum_{k=1}^{M} (df_k / d sigma_i) * (df_k / d sigma_j)

With M=4 this is:
  J_ij = (1/4) sum_k F_ki * F_kj

equivalently J = (1/4) F^T F for the Gram matrix of columns of F,
then set diagonal to 0 (Ising pairwise sum is over i < j).

Sign convention in discovery-02-coupling-matrix.md:
  J_ij < 0  cooperative (called ferromagnetic in project docs)
  J_ij > 0  conflicting (called antiferromagnetic / frustrating)
  J_ii = 0

---

## 3. Stated approximate Jacobian sign matrix

From discoveries/discovery-02-coupling-matrix.md Sec 3.3
(unit magnitudes |F_kj|=1 when nonzero; 0 = negligible):

         d     a     r    eps    ms    wr
  f1:   -1    +1    +1    +1    +1    +1
  f2:   +1    -1    -1    +1    +1    -1
  f3:   -1     0    +1     0     0     0
  f4:    0     0     0    -1    -1    +1

Columns of F (as vectors F_d ... F_wr):
  F_d   = [-1, +1, -1,  0]
  F_a   = [+1, -1,  0,  0]
  F_r   = [+1, -1, +1,  0]
  F_eps = [+1, +1,  0, -1]
  F_ms  = [+1, +1,  0, -1]
  F_wr  = [+1, -1,  0, +1]

---

## 4. Entry-by-entry re-derivation (unit-magnitude Jacobian product)

Notation: J_ij^(der) = (1/4) * sum_k F_ki * F_kj, then J_ii^(der)=0.

### 4.1 Geometric block (d, a, r)

J_da:
  terms: (-1)(+1) + (+1)(-1) + (-1)(0) + (0)(0) = -1 -1 = -2
  J_da^(der) = -2/4 = -0.50
  J_pub = -0.50
  MATCH

J_dr:
  terms: (-1)(+1) + (+1)(-1) + (-1)(+1) + (0)(0) = -1 -1 -1 = -3
  J_dr^(der) = -3/4 = -0.75
  J_pub = -0.50
  MISMATCH (magnitude). Dropping the f3 term recovers -0.50,
  so the published geometric block is consistent with an f1+f2-only
  product, not the full 4-objective Jacobian.

J_ar:
  terms: (+1)(+1) + (-1)(-1) + (0)(+1) + (0)(0) = 1 + 1 = 2
  J_ar^(der) = +0.50
  J_pub = +0.50
  MATCH

### 4.2 Cross geometric-control (d/a/r with eps/ms/wr)

J_d_eps:
  terms: (-1)(+1) + (+1)(+1) + (-1)(0) + (0)(-1) = -1 + 1 = 0
  J_d_eps^(der) = 0
  J_pub = 0
  MATCH

J_d_ms: same as J_d_eps by F_eps = F_ms on nonzero pattern
  J_d_ms^(der) = 0 = J_pub
  MATCH

J_d_wr:
  terms: (-1)(+1) + (+1)(-1) + (-1)(0) + (0)(+1) = -1 -1 = -2
  J_d_wr^(der) = -0.50
  J_pub = -0.25
  MISMATCH (magnitude)

J_a_eps:
  terms: (+1)(+1) + (-1)(+1) + 0 + 0 = 1 - 1 = 0
  J_a_eps^(der) = 0 = J_pub
  MATCH

J_a_ms: 0 = J_pub
  MATCH

J_a_wr:
  terms: (+1)(+1) + (-1)(-1) + 0 + 0 = 1 + 1 = 2
  J_a_wr^(der) = +0.50
  J_pub = -0.50
  MISMATCH (SIGN). Published text calls this strongly cooperative;
  the Jacobian product from the stated sign table is conflicting (+).

J_r_eps: 0 = J_pub
  MATCH

J_r_ms: 0 = J_pub
  MATCH

J_r_wr:
  terms: (+1)(+1) + (-1)(-1) + (+1)(0) + 0 = 1 + 1 = 2
  J_r_wr^(der) = +0.50
  J_pub = -0.25
  MISMATCH (SIGN and magnitude)

### 4.3 Control block (eps, ms, wr)

J_eps_ms:
  terms: (+1)(+1) + (+1)(+1) + 0 + (-1)(-1) = 1 + 1 + 1 = 3
  J_eps_ms^(der) = +0.75
  J_pub = +0.50
  MISMATCH (magnitude). Same sign (frustrating / AF).

J_eps_wr:
  terms: (+1)(+1) + (+1)(-1) + 0 + (-1)(+1) = 1 - 1 - 1 = -1
  J_eps_wr^(der) = -0.25
  J_pub = +0.25
  MISMATCH (SIGN)

J_ms_wr:
  same algebra as J_eps_wr (F_eps = F_ms)
  J_ms_wr^(der) = -0.25
  J_pub = +0.25
  MISMATCH (SIGN)

---

## 5. Matrices side by side

Published J^arch (AI-CONTEXT / discovery-02-coupling-matrix), zero diagonal:

         d      a      r     eps     ms     wr
  d    [ 0   -0.50  -0.50   0       0    -0.25 ]
  a    [-0.50  0    +0.50   0       0    -0.50 ]
  r    [-0.50 +0.50   0     0       0    -0.25 ]
  eps  [ 0     0     0      0     +0.50  +0.25 ]
  ms   [ 0     0     0    +0.50     0    +0.25 ]
  wr   [-0.25 -0.50 -0.25  +0.25  +0.25    0   ]

Derived J^(der) from unit-magnitude sign table + (1/4)F^T F, zero diagonal:

         d      a      r     eps     ms     wr
  d    [ 0   -0.50  -0.75   0       0    -0.50 ]
  a    [-0.50  0    +0.50   0       0    +0.50 ]
  r    [-0.75 +0.50   0     0       0    +0.50 ]
  eps  [ 0     0     0      0     +0.75  -0.25 ]
  ms   [ 0     0     0    +0.75     0    -0.25 ]
  wr   [-0.50 +0.50 +0.50  -0.25  -0.25    0   ]

---

## 6. Consequence for the (eps, ms, wr) triangle

Frustration indicator (MATH-SKELETON Sec 2.4):
  Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik)
  Phi = -1 frustrated; Phi = +1 consistent.

Published J_pub on (eps, ms, wr):
  all three pairwise J > 0
  Phi_pub = (+)(+)(+) = +1
  Project docs still call this a classical AF triangle because all three
  bonds prefer anti-alignment under H = -sum J_ij sigma_i sigma_j with
  their sign convention for J>0. That narrative is convention-dependent.

Derived J^(der) on (eps, ms, wr):
  J_eps_ms = +0.75, J_ms_wr = -0.25, J_eps_wr = -0.25
  Phi_der = (+)(-)(-) = +1 (formally consistent under the Phi product)

Conclusion of this audit:
  Under the literal Jacobian product from the project's own approximate
  sign table, the (eps, ms, wr) triangle is NOT a Phi=-1 frustrated
  triangle, and several published couplings flip sign relative to J^(der).
  The published J^arch is therefore a qualitative / hand-tuned matrix,
  not the exact Gram matrix of the stated Jacobian. AI-CONTEXT.md already
  warns that J^arch is a physically motivated approximation to be
  calibrated by simulation; this derivation quantifies where it diverges.

Conflict ticket: agents/conflicts/J-arch-jacobian-mismatch.md

Next mathematician task: frustration-proof.md must state which matrix
(J_pub vs J_der) the Phi claim uses, and give a falsification protocol
that does not assume RSB confirmation.

---

## 7. Optional reduced geometric block (f1+f2 only)

If f3 and f4 rows are zeroed (geometry-only objectives):
  J_da = -0.50, J_dr = -0.50, J_ar = +0.50
which matches the published geometric triangle exactly.
Control-block mismatches remain; they require the f4 row and cannot
be repaired by dropping f3 alone.

---

## 8. Claims locked by this file

CLAIM A: J^(der) above is the unique symmetric zero-diagonal matrix
obtained from the stated unit-magnitude sign table via
J = (1/4) F^T F.
  Falsify: exhibit arithmetic error in Sec 4, or a different F table
  authorised in MATH-SKELETON / discovery-02.

CLAIM B: J_pub is not identical to J^(der); sign mismatches exist at
(a,wr), (r,wr), (eps,wr), (ms,wr).
  Falsify: show a magnitude assignment |F_kj| that reproduces J_pub
  from the same sign pattern under the Sec 2 formula.

CLAIM C: RSB remains untested. Nothing in this file upgrades RSB
beyond the existing PREDICTED status.
