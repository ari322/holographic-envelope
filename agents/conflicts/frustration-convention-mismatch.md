# Conflict: AF-triangle narrative vs H = -sum J sigma_i sigma_j
# Raised by: MATHEMATICIAN
# Date: 2026-09-23
# Status: OPEN

## Description

Project text calls J_ij > 0 "antiferromagnetic / frustrating" and says the
triangle (eps, ms, wr) with all three published couplings positive is a
"classical frustrated AF triangle". Under the stated Hamiltonian

  H_facade(sigma) = - sum_{i<j} J_ij * sigma_i * sigma_j - sum_i h_i * sigma_i + lambda * P(sigma)

each J_ij > 0 lowers energy when sigma_i * sigma_j = +1 (aligned). A triangle
with all three J > 0 is therefore ferromagnetically consistent, not AF-frustrated.

MATH-SKELETON Sec 2.4 Phi_ijk = sign(J_ij)*sign(J_jk)*sign(J_ik) gives
Phi = +1 for all-positive bonds (consistent), Phi = -1 for an odd number of
negative bonds (frustrated under this H).

## Evidence

agents/mathematician/frustration-proof.md

## Proposed resolution

1. Keep H as written; redefine verbal labels so J > 0 = ferromagnetic / aligning.
2. OR flip the overall sign in H and rewrite J^arch signs consistently.
3. Do not silently patch; CRITIC should list the AF-triangle claim as
   convention-dependent in unsupported-claims.md.
