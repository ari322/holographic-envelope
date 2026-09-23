# BIR Critique — Weakest Point in the AdS/CFT Analogy
# CRITIC wave 2 — 2026-09-23
# AGENT-ROLES task 3. Architecture / mathematics only. Octopus not touched.
# Ground: MATH-SKELETON 1.5 / 4 / 6, AI-CONTEXT D04, discovery-04, Axiom A5,
#         falsification-protocol D04, prompts A06, and (open PR #2) theorist
#         BIR-limits.md. This is an independent critique, not a paraphrase.

Style: name the break, name the equation, say what would rescue or kill the
design target. No holographic courtesy language.

---

## Verdict — the weakest point

BIR cannot carry the AdS/CFT analogy, and it cannot carry the design target
"facade encodes the interior," because the written object is not an encoding
test. It is a ratio of two independently chosen Shannon scalars, then clipped
to 1.

AdS/CFT is an isomorphism of theories plus a dictionary: bulk data are
reconstructible from boundary data. BIR(t) = H_boundary(t) / H_interior(t)
is equality of two histogram numbers after a holographic cap. Equality of
marginal entropies is not reconstructibility. That is the break. The
numerator fork, the units clash, the fiat cap, the climate third region,
and the non-simplex interior "probabilities" are how the break is
implemented in this repo. Fixing any one of them without replacing the
ratio by a channel quantity leaves the analogy dead.

If you need one sentence: BIR = 1 is a bookkeeping coincidence, not a
holographic limit.

---

## 1. What the repo actually wrote (three incompatible BIR objects)

MATH-SKELETON 1.5:

    BIR(t) = H_boundary(t) / H_interior(t)
    H_boundary(t) = H_space(t)                 [bits]
    H_interior(t) = -sum_j q_j(t) log2(q_j(t))
    q_j(t) = "normalised interior variable j"
    Range: [0, 1]   (capped)

MATH-SKELETON Section 6 and AI-CONTEXT D04:

    H_boundary(t) = TFE at time t              [bits^2]
    "Eq 1.4 (TFE) is the numerator of Eq 1.5 (BIR)"

Discovery 04:

    I_boundary = H_space(t)
    I_interior = entropy of zone T, CO2, occupancy
    BIR = I_boundary / I_interior
    BIR = 1: "boundary perfectly encodes all interior complexity"
    BIR > 1: allowed ("over-responsive")
    BIR < 0.5: "under-responsive"

prompts/prompts-algorithmic.md A06:

    H_interior = mean of independent per-sensor Shannon numbers
    BIR = min(H_boundary / H_interior, 1.0)

Those are not one metric. A design target that is not the same object in
the skeleton, the discovery file, the context brief, and the measurement
script is not a design target. It is a slogan with four implementations.

Theorist PR #2 (BIR-limits.md) already flags the numerator tension and
refuses to silently repair it. Correct. This critique does not repair it
either. The critic job is to say the target is undefined until one object
is locked.

---

## 2. Definitional inconsistencies (exact)

### 2.1 Numerator fork: H_space vs TFE

H_space is bits (MATH-SKELETON 1.2). TFE = H_space * H_time is bits^2
(MATH-SKELETON 1.4). You cannot put both in the same slot of

    BIR = H_boundary / H_interior

and keep a meaning. If H_boundary = H_space and H_interior is bits, BIR
is dimensionless. If H_boundary = TFE, BIR has units of bits. The
holographic slogan ("ratio approaches 1") is only typed in the first
writing. Section 6 and AI-CONTEXT D04 are not typed. A06 inherits the
uncapped-then-clipped dimensionless form and ignores TFE as numerator.

This is not a notation quibble. The closed loop in AI-CONTEXT Section 3
is "D01 (TFE) + interior sensors -> D04 (BIR)". That sentence is false
under 1.5 and true only under the untyped writing. Either the loop is
wrong or the skeleton is wrong. Both cannot be canon.

### 2.2 Interior "probabilities" are not a distribution

MATH-SKELETON 1.5: q_j(t) = normalised interior variable j. Discovery 04
lists zone temperature variance, CO2 variance, occupancy. Those are
different physical units. Scaling each to [0,1] does not make them a
probability simplex. -sum q log q on a list of scaled sensors is not
Shannon entropy of an interior state.

A06 then averages independent 1-D histogram entropies. That is a third
object: not joint entropy, not the 1.5 formula, not Discovery 04's
"interior state distribution." Joint interior entropy of (T, CO2,
occupancy) over zones is the only quantity that could even sit in a
coding argument. It is not written and not computed.

Same class of error as discovery-01 / formal-model using raw open ratios
as p_i inside H_space (wake C26). The denominator of BIR is undefined as
information.

### 2.3 Cap by fiat

AI-CONTEXT D04: "Range: [0, 1] (capped at 1 by holographic principle
analogy)." MATH-SKELETON 1.5 copies the cap. Discovery 04 explicitly
allows BIR > 1. A06 implements min(., 1.0).

Nothing in Shannon arithmetic forces H_boundary <= H_interior. The
alphabets are chosen independently. A five-state panel histogram can
exceed a one-zone occupancy binary. An empty or uniform interior
(H_interior -> 0) sends the raw ratio to infinity. The cap hides that
pole and relabels it "holographic limit."

The holographic bound S <= A / (4 l_p^2) is a statement about
thermodynamic / Planck-scale bit density. It does not license clipping
an operational ratio of two coarse histograms. Importing the cap from
the slogan is how the analogy writes itself into the metric. That is
circular: BIR is capped because holography says so; BIR approaching the
cap is then cited as holographic.

### 2.4 Climate is a third region

Axiom A1: B(t) : X(t) -> S(t) with X containing radiation, temperature,
CO2, occupancy, wind. The formal model feeds radiation and exterior
temperature into o_i(t). MATH-SKELETON 5.2: a spore-layer gradient
produces H_space(t) > 0 whenever humidity differs from a reference — no
interior variable in the clause. D03 is an exterior-RH actuator.

AdS/CFT has two sides: bulk theory, boundary theory. A building envelope
has three regions: interior volume, facade, exterior climate. H_boundary
is a mixture of climate-driven actuation, interior-driven actuation,
hysteresis, and SAFE overrides. The slogan "interior readable on the
boundary" fails whenever the dominant driver is outside the interior
alphabet. That is structural, not a calibration leftover.

A spore facade on an empty building on a humid day can raise H_space,
drop H_interior, and sit on the cap. That building is not holographic.
It is weather-painted.

### 2.5 Equality is not encoding

Discovery 04 / AI-CONTEXT D04 / MATH-SKELETON 4.2:

    BIR -> 1 means "facade encodes as much information as the interior
    generates"

H(A) = H(B) does not imply that A encodes B. Two unrelated random
variables can share a Shannon number. Encoding is mutual information,
or a reconstruction map. Neither is in MATH-SKELETON.

Axiom A1 gives the forward map B: inputs -> panel states. The holographic
claim needs an inverse: panel states -> interior labels, at a declared
coarse-graining, after climate is conditioned out. No map R is defined.
No I(interior; facade) is defined. No I(interior; facade | climate) is
defined.

This is the AdS/CFT break in one line. The duality is a dictionary. BIR
has no dictionary.

### 2.6 Wrong entropy type; no area law; no extra dimension

MATH-SKELETON 4.1 quotes S_BH = A / (4 l_p^2). Section 4.2 then says BIR
is an analogy. Axiom A5 and scientific-position.md already forbid reading
the facade as a horizon.

Operational H_space on ~80 panels with a 5-state alphabet is either
<= log2(5) ~ 2.32 bits (histogram convention, Step 04) or O(N_panels *
log2(5)) if extensive. Interior thermodynamic entropy of air, occupants,
and contents is larger by many orders of magnitude. If BIR used physical
entropies it would sit at ~0 for every feasible skin. The project must
use a coarse alphabet or the ratio is idle. That choice severs the last
quantitative link to Bekenstein-Hawking.

There is no radial extra dimension, no Ryu-Takayanagi surface, no designed
quantum error-correcting redundancy. Losing one panel loses that panel's
angle. Adjacent-panel subsets are construction joints, not entanglement
wedges. Using those words as metaphors violates Axiom A5.

### 2.7 H_facade does not target BIR

MATH-SKELETON Section 6: "Eq 4.2 (BIR->1) is the design target that
Eq 3.2 (H_facade optimisation) should achieve." AI-CONTEXT Section 3:
"D02 (H_facade) predicts which design achieves highest BIR."

H_facade scalarises f1..f4 (radiation, daylight deficit, unique geometry
count, actuation events). None of those is BIR. There is no identity
argmin H_facade = argmax BIR, no monotonicity proof, no evaluated pair
(H_facade, BIR). If f3 is constant under a global 6-gene genome (wake
C22 / FM2), the Hamiltonian is not even the intended four-objective
object. A design target that the optimiser does not see is not a design
target. It is a caption.

---

## 3. Where the analogy actually dies (not a list of "also"s)

Theorist PR #2 lists five breaks: no dual pair / dictionary; third
region; Shannon vs area-law entropy; cap vs completeness; no RT / QEC /
extra dimension. All five are real. The weakest point is not "the
analogy is imperfect." Analogies are imperfect.

The weakest point is that the load-bearing design sentence uses the
analogy as if it supplied a completeness criterion, while the formula
cannot express completeness.

    Load-bearing sentence (4.2 / D04):
      BIR -> 1  <=>  facade encodes interior information

    What the formula can say:
      two Shannon numbers are equal after optional clipping

Those are different predicates. AdS/CFT would license the first only
after a dictionary and a reconstruction theorem. This repo has a ratio.
The analogy is therefore not "bounded and generative" (Axiom A5's
allowed transfer). It is load-bearing for a claim the operational
object cannot test. That is the failure mode of the analogy as a
research instrument, not as a metaphor.

Everything in Section 2 is a way to manufacture BIR ~ 1 without
encoding:

- pick TFE as numerator and a small H_interior (units + pole);
- pick a rich panel alphabet and a poor interior alphabet (capacity
  mismatch);
- let climate drive H_space (third region);
- clip the overflow (fiat cap);
- call the clip "holographic."

A metric that can be greened by bookkeeping is not a design target.

---

## 4. What would rescue BIR as a design target

Rescue means: the number, under a locked definition, measures whether
the skin carries interior information, and can be used as an optimisation
or operational KPI without holographic rhetoric. It does not mean "the
building is a CFT."

Minimum package (all required):

1. Lock one numerator. H_boundary := H_space (bits). Delete Section 6's
   "TFE is the numerator" and AI-CONTEXT's "H_boundary = TFE," or define
   an explicit conversion and never mix them. Two numerators = no target.

2. Lock one interior alphabet. Finite, declared, used in every paper and
   script. q is an occupancy over that alphabet, not a list of scaled
   sensors. Joint entropy, not a mean of 1-D entropies, unless a
   conditional-independence argument is written and tested.

3. Replace the ratio by a channel quantity:

       BIR_enc(t) = I(interior(t); facade(t) | climate(t))
                    / H(interior(t) | climate(t))

   Range is then in [0,1] because mutual information cannot exceed the
   residual interior entropy. The cap becomes a theorem, not a slogan.

4. Publish a reconstruction map R: facade state -> interior labels, with
   a stated error on occupied hours. BIR_enc near 1 without a working R
   is still a coincidence; R is the dictionary analogue Axiom A5 can
   allow.

5. Residualise climate. Completeness is evaluated after a climate-only
   predictor is removed, or climate is inside the encoded source and
   named as such. Spore RH response may not count as interior encoding.

6. Drop S_BH and "holographic limit" from the metric definition. Area,
   if used, means "more independently addressable panels raise channel
   capacity." Not A / (4 l_p^2).

7. Show that the optimiser that claims to target BIR actually sees it:
   either put BIR_enc in the Wallacei objective list, or prove a
   monotone link to f1..f4. Section 6 as written is false.

Rescue evidence (empirical):

- On a logged building or a complete B(t) simulation, BIR_enc separates
  static, climate-lockstep, and interior-coupled controllers.
- corr(raw BIR, climate) is high and corr(BIR_enc, climate) is low.
- R beats chance; a climate-only baseline does not.
- Empty-building hours are flagged, not capped to 1.
- Two independent implementations (histogram definition locked) agree.

Until that package exists, BIR is an L1 operational ratio with a
disputed formula. It is not a holographic design target.

---

## 5. What would kill BIR as a design target

Any one of these is sufficient. They are not all required.

K1. Definitional kill (already available, no experiment). The project
    refuses to lock a numerator and an interior simplex. Then BIR is
    not a quantity. Design targets must be quantities.

K2. Channel kill. On a complete simulation of B(t) or a year of paired
    panel/sensor logs, I(interior; facade | climate) / H(interior |
    climate) stays near 0 while capped H_space / H_interior is forced
    to 1 by alphabet choice or min(.,1). The present BIR is then
    holographic by bookkeeping and empty as encoding.

K3. Climate kill. After residualising panel state against EPW / RH /
    radiation, H_boundary is indistinguishable from noise while raw
    H_space stays large. The boundary entropy is weather. D03 as a
    BIR generator (MATH-SKELETON 5.2, AI-CONTEXT Section 3) is then
    false for D04's slogan.

K4. Optimiser kill. Designs that minimise H_facade do not raise BIR
    (or BIR_enc) relative to a static or rule-based baseline. Section 6
    is false as an optimisation statement. BIR cannot be the target of
    D02.

K5. Static-mixed kill. A static facade with mixed fixed angles has
    H_space > 0. If that BIR is comparable to the adaptive case, the
    metric is scoring spatial variety, not adaptation or encoding
    (wake C28). Discovery 04's "static facade: BIR = 0 by definition"
    is then a definitional cheat, not a finding.

K6. Pole kill. BIR(t) spikes when the building is empty (H_interior
    small) and sits on the cap under A06. The time series is a
    normalisation artefact. Unusable as an operational KPI.

K7. Falsification-protocol kill as written. validation/falsification-protocol.md
    D04: if BIR_static >= BIR_adaptive on a real dataset, "the metric
    is dominated by H_interior" and "normalisation must be revised."
    That protocol already admits the ratio can fail by denominator
    games. If the first real dataset trips it, do not retune the cap.
    Retire the holographic target.

A killed holographic target does not kill Axiom A1. An envelope can
still be a measurable map from inputs to panel states. Shannon entropy
of those states can still be a diversity statistic (D01, if the p_i
definition is locked). What dies is the sentence that this ratio is
how holographic a building is, and the sentence that BIR -> 1 is the
thing H_facade should achieve.

---

## 6. What does not rescue it

These will be offered. They do not work.

- "We said it was only an analogy." Axiom A5 allows a bounded analogy
  that generates a testable design claim. The testable claim in
  Discovery 04 that does not need AdS/CFT is: adaptive BIR >> 0 in
  occupied hours. That claim needs corr(interior, facade), i.e. Axiom
  A1. It does not need a cap, S_BH, or BIR = 1 as completeness. Using
  "analogy" to keep the cap and the slogan is the disallowed transfer.

- "PhilArchive 2024 writes BIR_physics = I_boundary / I_volume."
  Discovery 04's physics citation is not in the repo as a sourced
  excerpt. Even if that ratio exists in a philosophy note, it is not
  a dictionary and not a reconstruction theorem. Copying a ratio
  symbol is not AdS/CFT.

- "Tensor networks / arXiv 2102.02619." Named in Discovery 04. Not
  used. No code, no isometry, no bulk reconstruction. Citation as
  atmosphere.

- Theorist PR #2's speculative BIR_enc successor. That successor is
  the right object. It is not BIR as written. Citing BIR-limits.md as
  if it repaired D04 is a category error: the theorist labelled it
  speculative and said it would be falsified if the mutual-information
  index failed to separate controllers while raw BIR was forced to 1.
  Until that index is adopted in MATH-SKELETON, D04 is the broken
  ratio.

---

## 7. Relation to wake pack (PR #5) — do not redo, do extend

unsupported-claims.md already rates C29 (cap), C30 (numerator fork),
C31 (q_j not a distribution), C32 (encodes), C33 (H_facade targets
BIR) as major/blocker. failure-modes.md FM3 says TFE x BIR is not a
well-posed information functional. This file does not relitigate those
inventory items.

What this file adds: the AdS/CFT analogy's weakest joint is the
substitution of entropy-equality for encoding, and the design-target
use of BIR inherits that substitution. The analogy is not an extra
metaphor around a sound KPI. It is the reason the KPI was capped,
named "holographic limit," and hung on H_facade. Remove the analogy
and the remaining honest question is ordinary and still unanswered:

    How much of the declared interior uncertainty is visible in the
    skin after climate is conditioned out?

That question does not need AdS/CFT. BIR as written does not answer
it.

---

## 8. Critic instruction to other agents

MATHEMATICIAN: do not "derive" BIR = 1 from holography. There is
nothing to derive. If you touch 1.5, lock the numerator and replace
the ratio or mark it non-canon.

THEORIST: BIR-limits.md is the right audit. Do not let
BIR-greater-than-one.md (task 4, unwritten) treat overflow as a new
physical regime. Overflow is the case the cap was invented to hide.

WRITER: do not submit Building and Environment text that calls BIR
a holographic limit or that uses S_BH as a reference bound for a
clipped Shannon ratio. That is PR #4's live defect (see
pr-review-1-4.md).

SIMULATOR: if you implement A06, report raw_ratio and H_interior
separately. Do not ship min(.,1) as the only series.

OCTOPUS-BRIDGE: BIR-for-agents.md (PR #3) copies the cap and the
equality-not-encoding error into agent traces. Do not treat a fleet
H_space / H_interior = 1 as "boundary intelligence." Critique of that
mapping is in pr-review-1-4.md. Do not touch any Octopus repo.
