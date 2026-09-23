# Hostile-but-fair critic notes — open draft PRs #1–#6
# CRITIC wave 2 — 2026-09-23
# Scope: holographic-envelope draft PRs #1 through #6 only.
# Ignore later PRs (#7, #8, …). Do not touch Octopus.
# Wake pack (unsupported-claims / failure-modes / hostile-review) lives on
# PR #5 and is not rewritten here.

For each PR: what is solid, what overclaims, what must be fixed before
merge, whether it conflicts with CRITIC PR #5.

---

## Snapshot (heads read 2026-09-23)

| PR | Title | Role | Verdict |
|----|-------|------|---------|
| #1 | MATHEMATICIAN: Jacobian re-derivation of J^arch and conflict note | Math | Mergeable as verification. Do not treat as a repaired landscape. |
| #2 | THEORIST wake: TFE–Kolmogorov argument and BIR / AdS/CFT limits | Theory | Mergeable as labelled audit. Do not treat as a repaired BIR. |
| #3 | DESIGN DOCS: Octopus Bridge TFE / H_coord / BIR mappings | Bridge | Hold. Analytic mappings copy D02/D04 failure modes. |
| #4 | Writer: Building and Environment abstract and introduction (v1) | Writer | Do not merge as-is. Most dangerous of #1–#6. |
| #5 | CRITIC first wake: unsupported claims + three failure modes | Critic | Mergeable as the wake inventory. This PR does not replace it. |
| #6 | MATERIALS: spore-actuator literature survey and 7-panel protocol | Materials | Mergeable as protocol. Do not treat cork / Fibonacci n as data. |

Most dangerous to merge as-is: **PR #4**. It writes Phi = -1 into
publication prose and presents the broken D02/D04 objects as a paper.

---

## PR #1 — MATHEMATICIAN (Jacobian / J^arch conflict)

URL: https://github.com/ari322/holographic-envelope/pull/1
Head read: coupling-matrix-derivation.md, J-arch-jacobian-mismatch.md,
frustration-proof.md, frustration-convention-mismatch.md.

**Solid**

- Entry-wise (1/4) F^T F from the project's own unit-magnitude sign
  table. Arithmetic is checkable. J_pub != J_der is documented, not
  silently patched.
- Sign mismatches named: (a,wr), (r,wr), (eps,wr), (ms,wr). Magnitude
  mismatches named: (d,r), (d,wr), (eps,ms).
- frustration-proof.md locks H = -sum J sigma sigma and MATH-SKELETON
  2.4, then shows Phi(eps, ms, wr) = +1 on both J_pub and J_der.
  Isolated-triangle satisfying assignments are given.
- RSB is left PREDICTED. That is the correct refusal.

**Overclaims**

- None of the "formal equivalence" class. The remaining softness is
  leaving the all-positive = "classical AF" story as
  "convention-dependent" instead of dead under the locked H.
- STATUS-BOARD on that branch advancing MATHEMATICIAN past
  frustration-proof is a process row, not a landscape result.

**Must fix before merge**

- Keep both conflict tickets OPEN until a canon (H, J-sign, Phi)
  triple is chosen. Merging the notes is fine; merging them as if
  J^arch were now trustworthy is not.
- Next mathematician file (complexity-function.md) must not assume
  Phi-frustration of (eps, ms, wr). PR #1 already says this. Enforce it.
- Do not let anyone cite J_der as "the" matrix without repeating that
  |F_kj| = 1 is still a prior.

**Conflict with PR #5**

None. Strengthens C08, C09, C12, C13. The wake asked for a
re-derivation before sigma* is treated as a prediction. This is that
re-derivation. Compatible.

---

## PR #2 — THEORIST (TFE–Kolmogorov + BIR limits)

URL: https://github.com/ari322/holographic-envelope/pull/2
Head read: TFE-Kolmogorov.md, BIR-limits.md.

**Solid**

- TFE is not a lower bound on K(X). Units (bits^2 vs bits), product of
  marginals vs joint / program length, and Axiom A1
  (K(X) <= K(B) + K(X_in)) are independent kills. Correct.
- BIR-limits names the live breaks: no dictionary, climate as third
  region, Shannon vs area-law entropy, cap vs completeness, no RT/QEC.
  Numerator fork (H_space vs TFE) is left visible, not silently repaired.
- [CONFIRMED] vs [SPECULATIVE] tagging is enforced. Speculative
  repairs carry "this would be falsified if..." sentences.

**Overclaims**

- The "usable residue" paragraph can be misread as "BIR still works
  as a KPI." The residue is Axiom A1 plus a diversity statistic, not
  D04 as written.
- Speculative BIR_enc is the right successor object. It is not BIR.
  Citing PR #2 as if it repaired MATH-SKELETON 1.5 would be a lie.

**Must fix before merge**

- None blocking as a theorist note, provided the files stay labelled
  theory and do not edit MATH-SKELETON.
- Do not let BIR-greater-than-one.md (unwritten ROLE 04 task 4) treat
  overflow as a new physical regime. Overflow is the case the cap hides.

**Conflict with PR #5**

None on the math. Agrees with C23, C29, C30, C32, FM3. Tone is more
charitable about a leftover KPI; PR #5 and BIR-critique.md are not.
That is a disagreement about leftovers, not about the breaks.

---

## PR #3 — OCTOPUS BRIDGE (analytic mappings only)

URL: https://github.com/ari322/holographic-envelope/pull/3
Head read: TFE-for-agents.md, hamiltonian-for-agents.md,
BIR-for-agents.md, integration-proposal.md, README.md.

Critique of the *mappings*. No Octopus repository is discussed as a
place to write.

**Solid**

- First-line DESIGN DOCUMENT / FUTURE DESIGN / ANALOGY labels.
  Explicit "not a fifth discovery," "not implemented," "do not copy
  J^arch numbers."
- TFE alphabet A is observational and not a copy of
  {CLOSED, SHADED, VENTILATE, OPEN, SAFE}. Falsification section
  rejects "higher TFE = healthier."
- Hamiltonian file refuses to paste facade J or Sydney h into agents.
  F4 (architectural-number leak) is the right rejection rule.
- BIR-for-agents locks H_boundary := H_space (bits), refuses TFE as
  an unconverted numerator, and refuses to emit BIR = 1 when
  H_interior = 0. That is stricter than MATH-SKELETON 1.5 / A06.
- integration-proposal.md is the most honest file in #1–#6 besides
  the critic wake: do not connect now; wait for facade tests, critic
  inventory, and owner GO. No new broker.

**Overclaims**

- TRACE mode invents a second spatial ensemble (B-event bundles from
  one agent). D01's H_space is a many-panel snapshot. A sliding
  self-histogram is not that object. FLEET mode is the only structural
  map; TRACE is a new metric wearing D01's name.
- hamiltonian-for-agents.md copies the false D02 certificate:
  all-positive (persist, step, explore) is treated as a classical AF
  triangle while admitting Phi = +1 under 2.4. Same override PR #1
  just killed on the facade.
- P_coord(d) + Hartigan / GMM is P_arch(d) transplanted. Category
  error FM2, now in agent traces. The file says "do not claim RSB"
  and then keeps the detector that was built to say yes.
- Hypothetical J and h are written as numbers. They will be cited.
  "HYPOTHETICAL" in the same file is not a sufficient barrier.
- BIR-for-agents still scores encoding by equality of two Shannon
  numbers, then min(.,1). Different alphabets A vs B avoid the
  tautology of using A twice; they do not create a dictionary or
  I(interior; boundary | climate). Way 3 "boundary intelligence"
  is the D04 slogan on logs.
- README / STATUS-BOARD on that branch claim ROLE 06 tasks 1–5 are
  written. Fine as a folder index. Not fine as "the bridge is ready."

**Must fix before merge**

- State that TRACE is a distinct estimator, not TFE.
- Delete or fence the all-positive = frustrated paragraph. Point at
  PR #1 / MATH-SKELETON 2.4. Phi = +1 is consistent.
- Rename P_coord(d) protocol: "multimodal coordination attractors,"
  never "RSB template," and add a connected-front negative control.
- Move hypothetical J/h to an appendix titled DO NOT CITE, or drop
  the numbers.
- Replace BIR cap-as-score with raw_ratio plus a planned BIR_enc, or
  keep the ratio and drop "intelligence."
- integration-proposal stays. Do not weaken "do not implement now."

**Conflict with PR #5**

Yes, on the mappings. FM1 and FM2 are reproduced in H_coord / P_coord.
FM3's equality-not-encoding error is reproduced in BIR-for-agents
(partially mitigated by the empty-interior refusal). The integration
page agrees with PR #5 that connection is premature. Merge the
integration page's *verdict*; do not merge the mappings as if they
escaped the wake.

---

## PR #4 — WRITER (Building and Environment abstract + introduction)

URL: https://github.com/ari322/holographic-envelope/pull/4
Head read: abstract-v1.md, introduction-v1.md.

**Solid**

- Word counts in band. No new citations. RSB stated as unrun.
  Cork theta_max(n) "has not been measured." BIR "not derived from
  AdS/CFT." Octopus untouched.
- Introduction uses the bit-valued H_space / H_time definitions, not
  the open-ratio abuse in discovery-01 / formal-model.

**Overclaims (disqualifying)**

- Abstract: "Multi-objective facade design *is* an architectural
  Ising Hamiltonian." Identity, not analogy. Contradicts Axiom A5
  and wake C01.
- Abstract: J^arch "contains a frustrated triangle on (eps, Delta s,
  wr), predicting a multi-modal landscape and RSB structure in
  P_arch(d)." The triangle is Phi = +1. P_arch(d) is not P(q).
  "Predicting RSB structure" launders FM1+FM2 into a journal lead.
- Introduction, explicit false equation:
  "Phi_ijk = sign(J_ij) sign(J_jk) sign(J_ik) = -1"
  MATH-SKELETON 2.4 on the published couplings is +1. PR #1 proves
  +1 on J_pub and J_der. This is not a rounding error. It is a
  fabricated evaluation of the project's own definition.
- J^arch "is constructed from the objective Jacobian" — PR #1 shows
  it is not.
- Closed loop (D03 -> D01 -> D04, D02 selects highest BIR) restated
  as the paper's organising claim. Wake C33 / C36: no link is
  computed; H_facade does not target BIR.
- Cork as "the stated substrate" in a journal introduction, while
  PR #6's survey says no published cork+spore actuator data in the
  brief.
- S_BH used as "the physical reference" for a clipped Shannon ratio.
  Axiom A5 / scientific-position.md forbid this as load-bearing.

**Must fix before merge**

- Delete Phi = -1. Write Phi = +1, or delete the triangle sentence.
- Replace "is an architectural Ising Hamiltonian" with "can be
  written, as a model, in Edwards-Anderson form; the identification
  is untested and the published J is not the Jacobian Gram matrix."
- Delete "RSB structure in P_arch(d)" as a predicted property of
  this problem. Keep "a clustering protocol is specified and unrun."
- Do not close the D01–D04 loop in the lead. List open tests.
- Do not use S_BH as a bound for BIR.
- Do not merge until PR #5's relevant blockers (C01, C12, C13, C30,
  C33) are visible in the prose as open, not as solved by tone.

**Conflict with PR #5**

Direct. PR #4 is the document PR #5's hostile-review was written to
stop. Merging #4 as publication-ready text overwrites the wake with
Building-and-Environment English. Also conflicts with PR #1
(Phi = -1 vs proven +1) and with BIR-critique.md / spin-glass-critique.md
on this branch.

---

## PR #5 — CRITIC first wake

URL: https://github.com/ari322/holographic-envelope/pull/5
Files: unsupported-claims.md, failure-modes.md, hostile-review.md,
STATUS-BOARD CRITIC row. Not redone here.

**Solid**

- 43 unsupported claims with file/section quotes and missing-data
  lines. Empirical inventory is accurate: no EPW table, no Wallacei
  archive, no TFE/BIR number, no dated prototype log.
- Three failure modes name equations (Phi / J, P_arch(d), TFE x BIR).
- Hostile review is the correct venue voice for Building and
  Environment given the empty Section 6.

**Overclaims**

- None of the physics-confirmation class. Severity labels are
  critic judgments; a later owner can downgrade minors. Blockers
  C01, C12, C13, C22, C26, C30, C33 should not be downgraded without
  new algebra or data.

**Must fix before merge**

- None for content. Coordinate STATUS-BOARD with this wave-2 PR
  so the CRITIC row is one coherent line, not two fighting drafts.
- Do not treat the wake as complete ROLE 07. Tasks 3–4 were still
  open; they are this PR.

**Conflict with PR #5**

Not applicable (self). This wave-2 PR extends it. It does not reopen
the three wake files.

---

## PR #6 — MATERIALS (spore survey + 7-panel protocol)

URL: https://github.com/ari322/holographic-envelope/pull/6
Head read from PR body and file list: spore-data-survey.md,
fabrication-protocol.md, MATERIALS status / STATUS-BOARD row.

**Solid**

- Literature vs design-proposal split is enforced. Chen 2014/2015
  and Birch 2021 numbers are tagged. Cork is *not* sold as measured.
- Birch layers 1–4; angle plateaus near 4 (~43 deg, ~12% spore-strain
  limit) while Stoney force still rises. That is a live falsifier
  for MATH-SKELETON 5.1 "f monotone increasing" at Fibonacci n > 4.
- Cycle-life honesty: Birch 10 cycles on latex; Chen 1e6 on
  polyimide with elongation reduced, not "100% stable." Lift:
  Birch >= 150% actuator mass vs Chen HYDRA ~50x — different
  devices, not one number.
- Protocol steps tagged [LITERATURE-CONFIRMED] vs [DESIGN-PROPOSAL].
  No fabrication results claimed. Octopus untouched.

**Overclaims**

- Fibonacci n = 5, 8, 13, 21 is an exploration grid. If the PR text
  anywhere lets a reader think those n inherit Birch's monotone
  theta_max, that is an overclaim. The body as read flags the
  plateau risk. Keep that flag in the protocol title, not only in
  the PR description.
- AI-CONTEXT D03 still says cork is optimal, 40 C / 2 h dry,
  parylene seal, 100% stable, 1e6 cycles. PR #6 correctly treats
  those as unverified project claims. Merging #6 without a conflict
  ticket against AI-CONTEXT leaves the brief lying to the next
  writer (see PR #4 cork sentence).

**Must fix before merge**

- Add or keep an explicit conflict: AI-CONTEXT D03 / MATH-SKELETON
  5.1–5.3 vs surveyed literature (substrate, dry protocol, cycle
  life, n > 4 plateau). Do not silently edit AI-CONTEXT in this
  critic PR; require MATERIALS or owner to open the ticket.
- test-protocol.md / alternatives.md remain out of scope for #6.
  Do not read #6 as ROLE 03 complete.

**Conflict with PR #5**

None on math. Strengthens C35 / C42 (D03 -> TFE -> BIR loop is
humidity, not interior; cork/tau/n_layers uncalibrated). Conflicts
with PR #4's casual cork sentence. Compatible with the wake.

---

## Cross-PR merge order (if anyone merges)

1. PR #5 (wake inventory) and this wave-2 critic PR (BIR / D02
   critiques + this file).
2. PR #1 (J / Phi proof) and PR #2 (TFE/BIR theory audit).
3. PR #6 (materials protocol) after an AI-CONTEXT conflict ticket.
4. PR #3 only after the mapping fixes above, or merge
   integration-proposal.md alone.
5. PR #4 last, after the false Phi = -1 and identity claims are
   deleted.

Merging #4 before #1/#5 is how a false Phi becomes the paper.

---

## One-line calls

| PR | Merge as-is? | One-line reason |
|----|--------------|-----------------|
| #1 | Yes, as verification | Documents that J_pub != J_der and Phi = +1. |
| #2 | Yes, as audit | TFE is not K; BIR analogy breaks at the missing dictionary. |
| #3 | No | Copies FM1/FM2/FM3 into agent mappings. |
| #4 | No | Writes Phi = -1 and "is an Ising Hamiltonian" for Elsevier. |
| #5 | Yes, as wake | Inventory and three named equation failures. |
| #6 | Yes, as protocol | Literature/proposal split; cork not data. |
