# Complexity Function Sigma(e) for H_facade
# Agent: MATHEMATICIAN
# Date: 2026-09-23
# Status: VERIFICATION / FORMAL TEMPLATE (not a numerical discovery)
# Depends on: coupling-matrix-derivation.md, frustration-proof.md

## Purpose

Define and bound the complexity function counting local minima of
H_facade at energy density e. This is a formal scaffold for N=6
architectural genes. It is NOT a measured Sigma from Wallacei.

Falsification / completion condition:
  (F1) On the discrete hypercube sigma in {-1,+1}^6 (64 states), compute
       exact N_minima(E) by enumeration under a locked (J,h,lambda,P).
       If the empirical Sigma_disc(e) = (1/6) log N_minima(e) disagrees
       with any claimed closed form in this file by more than machine
       epsilon on any occupied energy bin, discard that closed form.
  (F2) On continuous [-1,+1]^6, if a gradient/Hessian census finds K
       strict local minima and K = 1 for the locked H, then any claim
       of exponentially many minima for this N is FALSE.

RSB is not confirmed by writing Sigma(e).

---

## 1. Hamiltonian reminder

  H(sigma) = - sum_{i<j} J_ij * sigma_i * sigma_j
             - sum_i h_i * sigma_i
             + lambda * P(sigma)

  sigma in [-1,+1]^6
  J from either J_pub or J_der (see coupling-matrix-derivation.md)
  h = [+0.30, -0.20, +0.15, -0.10, -0.10, +0.25]  (Sydney prior; approximate)

Energy density for N=6:
  e = H(sigma) / 6

---

## 2. What SK complexity means (and what it does not)

In the thermodynamic SK / p-spin setting (N -> infinity):
  N_minima(e) ~ exp( N * Sigma(e) )
  Sigma(e) > 0 on an interval (e_gs, e_th) in mean-field glasses.

For H_facade, N = 6 is microscopic. There is no justified N -> infinity
limit for six facade genes. Therefore:

CLAIM C1: No SK-style asymptotic Sigma_SK(e) may be quoted as a
property of H_facade without an explicit large-N embedding (e.g. many
panels as spins). Falsify by providing that embedding in MATH-SKELETON
and re-deriving.

What remains well-defined for N=6:
  N_minima(E) = number of local minima with H(sigma) in a bin of energy E
  Sigma_6(E) = log N_minima(E)    (not divided by N unless comparing to SK)
  or sigma_density(e) = (1/6) log N_minima(6e)

---

## 3. Discrete surrogate (exact in principle)

Restrict sigma to {-1,+1}^6. Then |config space| = 64.

Local minimum (discrete): H(sigma) <= H(sigma') for all single-spin flips
sigma' of sigma.

Algorithm (for SIMULATOR / future enumeration; MATHEMATICIAN does not run it):
  1. Lock J (J_pub or J_der), h, lambda, P.
  2. Evaluate H on all 64 vertices.
  3. Mark local minima by the one-flip test.
  4. Histogram N_minima(E).
  5. Report Sigma_6(E) = log N_minima(E).

CLAIM C2: Until that enumeration exists in-repo, any numerical table of
Sigma(e) for H_facade is UNAUTHORISED. This file ships the definition only.
  Falsify: land an enumeration artifact under agents/simulator/ and cite it.

Expected scale (not a measurement): N_minima total is between 1 and 64.
That alone already shows exponential-in-N language is inappropriate at N=6.

---

## 4. Continuous case

On the cube [-1,+1]^6, critical points satisfy
  grad H(sigma) = 0  in the interior, or first-order KKT conditions on faces.

Quadratic part from the pairwise term:
  H_quad = - (1/2) sigma^T J sigma   (with J symmetric, zero diagonal)
  Hess H_quad = -J

Interior local minimum requires Hess H = -J + Hess(lambda P) - 0 from
linear h  to be positive definite on the tangent space.

Because J is indefinite whenever both positive and negative couplings
exist (true for J_der; for J_pub the control block is all-positive but
the geometric block has mixed signs), -J is not PD on R^6. Interior
minima, if any, require the penalty P or the box constraints to
stabilise them.

CLAIM C3: Without a specified P, the number of interior local minima of
the unconstrained quadratic - (1/2) sigma^T J sigma - h·sigma is either
0 or undefined as a minimum (saddle-rich). Box constraints can create
boundary minima; their count is empirical.
  Falsify: specify P twice differentiable, exhibit an interior PD critical
  point count.

---

## 5. Link to frustration-proof.md

frustration-proof.md shows Phi(eps,ms,wr) = +1 for J_pub and J_der under
locked H. Therefore one must NOT invoke "AF triangle => exponential
complexity" for this triplet. Complexity, if present, must come from:
  - mixed signs elsewhere in J (e.g. geometric block),
  - multi-objective origin of J (Pareto structure),
  - or the constraint penalty P,
not from Phi=-1 on (eps,ms,wr).

---

## 6. Working definition to ship

  Sigma_facade(e) := (1/6) * log( max( 1, N_minima(e; J,h,lambda,P) ) )

with N_minima defined by discrete one-flip minima on {-1,+1}^6 as the
default computable surrogate, and continuous KKT minima as an optional
refinement labelled separately.

No closed-form Sigma_facade(e) is claimed.

---

## 7. Claims locked

CLAIM C1: no SK asymptotic without large-N embedding.
CLAIM C2: no numerical Sigma table until enumeration exists.
CLAIM C3: unconstrained quad part is not a PD interior landscape.
CLAIM C4: RSB remains PREDICTED; Sigma template does not confirm it.
  Falsify C4: only by the Wallacei Hartigan protocol in MATH-SKELETON 3.4.
