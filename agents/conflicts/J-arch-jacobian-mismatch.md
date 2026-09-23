# Conflict: Published J^arch vs Jacobian product
# Raised by: MATHEMATICIAN
# Date: 2026-09-23
# Status: OPEN

## Description

The 6x6 matrix J^arch in AI-CONTEXT.md and
discoveries/discovery-02-coupling-matrix.md does not equal the Gram
matrix (1/4) F^T F built from the approximate Jacobian sign table in
the same discovery file (unit magnitudes).

Sign mismatches: (a,wr), (r,wr), (eps,wr), (ms,wr).
Magnitude mismatches: (d,r), (d,wr), (eps,ms).

Consequence: the narrative that (eps, ms, wr) is a frustrated triangle
depends on J_pub signs, not on J^(der) from the stated Jacobian.

## Evidence

Full entry-wise audit:
  agents/mathematician/coupling-matrix-derivation.md

## Proposed resolution (do not silently edit math)

1. Keep J_pub labelled as qualitative prior.
2. Replace or supplement with J^(der) once empirical |df/d sigma| exist.
3. CRITIC should list the frustrated-triangle claim as Jacobian-dependent
   in unsupported-claims.md.

## Blocked agents

MATHEMATICIAN next task frustration-proof.md should cite this conflict.
