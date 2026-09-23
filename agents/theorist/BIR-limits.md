# BIR Limits: Where the AdS/CFT Analogy Breaks

THEORIST wake note. Grounded in `AI-CONTEXT.md` D04 and Section 4, `MATH-SKELETON.md` Sections 1.5 and 4, Axiom A5 (`research/boundary-axioms.md`), `research/scientific-position.md`, and `discoveries/discovery-04-boundary-information-ratio.md`. This is an analogy audit, not a new empirical discovery. Critic has not written `unsupported-claims.md` or `BIR-critique.md`; those reviews remain next.

The project already forbids a category error: AdS/CFT is not to be conflated with BIR, and BIR is an analogy, not a derivation from string theory. The task here is to say *where* that analogy stops being structurally faithful, and what would have to be true for `BIR = 1` to mean something like holographic completeness rather than a capped ratio of two Shannon numbers.

---

## 1. What BIR is in this repository [CONFIRMED]

MATH-SKELETON 1.5:

```
BIR(t) = H_boundary(t) / H_interior(t)
H_boundary(t) = H_space(t)
H_interior(t) = - sum_j q_j(t) * log2(q_j(t))
Range: [0, 1]   (capped)
```

`H_space(t)` is the Shannon entropy of the facade panel-state histogram at time `t` (D01). `H_interior(t)` is the Shannon entropy of a chosen interior alphabet: occupancy, zone temperatures, activity or CO2 (`AI-CONTEXT` D04). The holographic slogan attached to the cap is: `BIR -> 1` means the facade encodes as much information as the interior generates.

Discovery 04 writes the same ratio as `I_boundary / I_interior` and interprets `BIR = 0` as a blind static skin, `BIR = 1` as a "holographic limit," and `BIR > 1` as over-response. MATH-SKELETON instead *caps* the range at 1. That is already a project-level fork: a cap imported from the holographic slogan versus an uncapped operational ratio. Both documents agree that no building measurement of BIR has been made.

MATH-SKELETON Section 4.1 quotes Bekenstein-Hawking as reference physics:

```
S_BH = A / (4 * l_p^2)
```

Section 4.2 then restates that `BIR -> 1` is an analogy, not a quantum-gravity derivation. Axiom A5 permits the transfer only if it is named as analogy, generates a testable design claim, and does not imply physical equivalence. Scientific position repeats the ban: a facade is not a black-hole horizon.

A definitional tension inside the repo must be kept visible rather than repaired here. `AI-CONTEXT` D04 and MATH-SKELETON Section 6 set the BIR numerator to TFE (a `bits^2` product). MATH-SKELETON 1.5 and Discovery 04 set it to `H_space(t)` (bits). The ratio is dimensionless only in the second writing. The first writing is `bits^2 / bits`. Arguments below use the bit/bit form of 1.5 unless the tension is the point.

---

## 2. What AdS/CFT actually supplies [CONFIRMED]

As used in the project's own Discovery 04 paragraph, the holographic principle (Susskind, 't Hooft) and AdS/CFT say that a gravitational theory in an asymptotically Anti-de Sitter bulk is informationally equivalent to a conformal field theory on the conformal boundary. In the textbook dictionary this is an equivalence of theories, not a ratio of two independently chosen entropies:

- the partition functions match under identified boundary conditions;
- operators and correlation functions are paired by a dictionary;
- bulk information is reconstructable from boundary data;
- in modern reconstructions, that encoding is redundant, in the manner of a quantum error-correcting code;
- black-hole entropy scales as horizon *area* in Planck units, not as a coarse operational histogram.

Ryu-Takayanagi-type statements further relate a *boundary* entanglement entropy to the area of a *bulk* extremal surface. Nothing in that package is a claim about Shannon entropy of HVAC sensors.

The only structural skeleton that BIR borrows is: "interior (bulk) information, boundary (facade) encoding, a number that approaches 1 when the encoding is complete." Everything else has to be checked.

---

## 3. Break 1 — There is no dual pair and no dictionary [CONFIRMED]

AdS/CFT is not "a surface that looks interesting." It is a claimed isomorphism between two complete theories. BIR compares two Shannon functionals computed from different instruments:

- facade: panel-state log, five angle bins in Step 04, or spore-layer-induced angles in D03;
- interior: a still-unspecified joint histogram over zones, temperatures, CO2, occupancy.

There is no stated map from interior observables to facade observables that would play the role of the AdS/CFT dictionary. `BIR(t) = 1` can occur because both entropies happen to be equal after normalisation, including cases where the facade is responding to *solar radiation* while the interior entropy is *occupancy*. Equality of two scalars is not reconstructibility.

The design claim that remains legitimate under Axiom A5 is weaker and already in Discovery 04: a well-designed adaptive facade should have `BIR(t)` significantly above zero in occupied hours. That claim does not need AdS/CFT. It needs a correlation between interior state and panel state (Axiom A1).

---

## 4. Break 2 — The building has a third region the duality does not [CONFIRMED]

In AdS/CFT the conformal boundary is the complete home of one theory; the bulk is dual, not "driven by a further exterior." A building envelope sits between *two* volumes:

1. interior occupied space (the intended "bulk" analogue);
2. exterior climate (radiation, wind, humidity, dry-bulb temperature).

Axiom A1 and the formal model feed *both* into `B(t)`. D03's spore mechanism is driven by humidity, which is typically an exterior or cavity field, not an occupancy code. MATH-SKELETON 5.2 even states that a layer gradient produces `H_space(t) > 0` whenever humidity differs from a reference — with no interior variable in the clause.

So `H_boundary` is not, in general, "interior information written on a screen." It is a mixture of climate-driven actuation, interior-driven actuation, hysteresis, and SAFE overrides. The holographic slogan (interior readable on the boundary) fails whenever the dominant driver is outside the interior alphabet. This is a structural break, not a calibration detail.

[SPECULATIVE] One could try to restore a two-region picture by folding exterior climate into an enlarged "bulk," or by residualising panel states against a climate-only predictor and calling only the residual `H_boundary`. This would be falsified if, after that residualisation, `H_boundary` were indistinguishable from noise while raw `H_space` stayed large — i.e. if almost all facade entropy were climate-explained.

---

## 5. Break 3 — Operational Shannon entropy is not area-law holographic entropy [CONFIRMED]

`S_BH = A / (4 * l_p^2)` is extensive in area and uses a Planck-scale bit density. A facade of order `10^2` panels with a 5-state alphabet has, depending on the entropy convention:

- histogram entropy `H_space <= log2(5) ~ 2.32` bits (MATH-SKELETON 1.2, Step 04), or
- an extensive upper bound of order `N_panels * log2(5)` bits if one sums independent panel uncertainties.

Either figure is an operational, coarse-grained Shannon number. It is not thermodynamic entropy of the interior air, not von Neumann entropy of a quantum field, and not an area-law count in Planck units. If BIR were computed from physical thermodynamic entropies, the denominator (interior air, occupants, contents) would dominate by many orders of magnitude and BIR would sit near zero for every feasible skin. The project therefore *must* use a coarse operational alphabet or the ratio is scientifically idle.

That choice is allowed as a design metric. It severs the last quantitative link to Bekenstein-Hawking. The cap `BIR <= 1` cannot be justified by "the holographic bound forbids more bits on the surface than in the volume," because the two sides are not those bits.

Discovery 01 also notes that `H_space` can be read as visual/state diversity rather than as a channel about the interior. High spatial entropy is then compatible with a facade that is informationally rich *and* holographically empty: it does not represent the room.

---

## 6. Break 4 — `BIR = 1` is a cap, not completeness [CONFIRMED]

In AdS/CFT, completeness means: given the boundary theory, the bulk theory is determined. In the repo, `BIR = 1` means `H_boundary = H_interior` after whatever normalisation and cap are applied. Those are different statements.

Nothing in the definitions forces `H_boundary <= H_interior`. The alphabets are chosen independently. Discovery 04 already contemplates `BIR > 1` (over-responsive skin). The MATH-SKELETON cap is therefore a modelling convention, not a theorem. Importing the cap from the holographic slogan hides the case the operational metric most needs: a facade that is *more* differentiated than the interior it claims to encode.

Even `H_boundary = H_interior` does not imply invertibility. Two distributions can share a Shannon number and still be unrelated as random variables. The holographic claim would require a reconstruction functional `R` such that `R(S(t))` recovers the interior state vector (at the chosen coarse-graining) up to a declared error. No such `R` is defined. Axiom A1 gives the forward map `B`, not its inverse.

[SPECULATIVE] If a reconstruction `R` existed with small error on occupied hours, BIR near 1 would become evidence of an encoding rather than of a numerical coincidence. This would be falsified if the best regression or codebook from panel-state vectors to interior vectors performed at chance while `BIR(t)` hovered near 1.

---

## 7. Break 5 — No extra dimension, no RT surface, no designed redundancy [CONFIRMED]

Several pieces of the modern holographic package have no building counterpart in the current math skeleton:

- There is no radial / extra dimension whose slices are RG scales. Floor plates and section are ordinary 3-space.
- There is no Ryu-Takayanagi rule relating a subset of facade panels to a surface in the interior. Adjacent-panel subsets are local construction joints, not entanglement wedges.
- There is no designed holographic error correction. Losing one panel typically loses that panel's local angle. Redundancy would have to be engineered (repeated encodings, global codes) and is not implied by D03 layer gradients.
- Time in BIR is a clock index `t` for a snapshot ratio. It is not the dynamical spacetime of a bulk evolution dual to a boundary QFT.

Using those terms as metaphors violates Axiom A5 (analogy must not replace a missing equation). MATH-SKELETON does not contain them; they should stay out of the metric's definition.

---

## 8. What would have to be true for `BIR = 1` to be "exact" [SPECULATIVE]

"Exact" here means: the ratio-1 condition coincides with informational completeness of the facade about the declared interior, in something like the bounded sense Axiom A5 allows — not "the building is a CFT."

A minimal package:

1. **Shared coarse-graining.** Interior and boundary alphabets are declared, finite, and used on both sides of every paper and script. The numerator is `H_space` (bits), not TFE, unless a conversion is defined.
2. **Channel, not just entropy.** Treat the envelope as a channel `interior -> facade` (possibly with climate as side information). Completeness is then mutual information, e.g. `I(interior; facade) / H_interior -> 1`, not `H_space / H_interior -> 1`. Mutual information is the quantity that actually measures encoding.
3. **Capacity vs demand.** Number of distinguishable facade configurations is at least the size of the interior alphabet one claims to encode. Histogram entropy of five global bins cannot encode a many-zone interior; an extensive panel-wise code might.
4. **Reconstruction test.** A public map `R` recovers interior labels from facade states alone at a stated accuracy.
5. **Climate residual.** Completeness is evaluated after removing the component of facade state predicted by exterior EPW-type drivers, or climate is explicitly inside the encoded source.
6. **Drop the Planck-area rhetoric.** Area scaling, if used at all, means "more independently addressable panels raise channel capacity," not `A / (4 l_p^2)`.

This package would be falsified if, on a logged building or a complete simulation of `B(t)`, `I(interior; facade) / H_interior` stayed near 0 while the Shannon ratio `H_space / H_interior` was forced to 1 by capping or by alphabet games. That single discrepancy would show that the present BIR can be made "holographic" by bookkeeping without any encoding.

A stronger, still speculative, requirement — exact AdS/CFT-style duality — would additionally need a bulk theory, a boundary theory, and a dictionary matching their generating functionals. This would be falsified (and should be rejected in advance under Axiom A5) as soon as those theories are asked for and only Shannon ratios are produced. The project does not have them and does not need them.

---

## 9. What survives the breaks [CONFIRMED]

After the breaks are named, a usable residue remains, and it is already the project's scientific position:

- An envelope is a measurable map from inputs to panel states (Axiom A1).
- Shannon entropy of those states is a legitimate diversity / uncertainty statistic (D01).
- The *ratio* of facade entropy to interior entropy is a possible operational KPI, provided both sides use declared alphabets and the ratio is not capped by physics rhetoric.
- The holographic story is a generator of the design aspiration "the skin should not be blind to the interior," not a derivation of the cap, the units, or `BIR = 1` as completeness.

[SPECULATIVE] The most honest successor to BIR is a climate-conditional mutual information,

```
BIR_enc(t) = I( interior(t) ; facade(t) | climate(t) ) / H(interior(t) | climate(t))
```

with range naturally in `[0, 1]` because mutual information cannot exceed the residual interior entropy. This would be falsified if that index failed to separate static, lockstep, and interior-coupled controllers on the same input chronicle — the separation Discovery 04 already predicts for raw BIR.

Until Critic files `BIR-critique.md` and a simulation exists, BIR should be cited as an L1 operational ratio with a bounded analogy, not as a macroscale AdS/CFT result. The analogy breaks at the missing dictionary, the third (exterior) region, the wrong entropy type, the conventional cap, and the absence of reconstruction, extra dimension, and redundancy. What does not break is the ordinary information-theoretic question the building can still answer: how much of the interior's declared uncertainty is visible in the skin.
