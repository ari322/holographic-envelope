# What a BIR > 1 Building Would Mean

THEORIST wake note (ROLE 04, task 4). Grounded in `AI-CONTEXT.md` D04, `MATH-SKELETON.md` 1.5 and 4.2, `discoveries/discovery-04-boundary-information-ratio.md`, Axiom A5, `research/scientific-position.md`, and the companion note `agents/theorist/BIR-limits.md`. ROLE 04 requires this file to be speculative and clearly labelled. It is not a discovery. No building has been measured. Critic has not written `unsupported-claims.md` or `BIR-critique.md`.

**Short answer.** [CONFIRMED] Discovery 04 already names `BIR > 1` as over-response; MATH-SKELETON and `AI-CONTEXT` instead cap the range at 1. Those cannot both be operational. [SPECULATIVE] An uncapped `BIR(t) > 1` would not mean a building that "beats" the holographic principle. It would mean the Shannon ratio has left the encoding story: the skin is more mixed than the declared interior, usually because climate, alphabet games, an empty interior, or a `bits^2` numerator have entered the fraction.

---

## 1. What the repo already says [CONFIRMED]

MATH-SKELETON 1.5 (bit/bit form, used below unless noted):

```
BIR(t) = H_boundary(t) / H_interior(t)
H_boundary(t) = H_space(t)
Range: [0, 1]   (capped)
```

`AI-CONTEXT` D04 repeats the cap "by holographic principle analogy" and never defines `BIR > 1`. Discovery 04 does:

```
BIR > 1: facade encodes more spatial differentiation than the interior it serves (over-responsive)
```

`BIR-limits.md` Section 6 already records the fork: the cap is imported from the slogan, not derived from the two Shannon sums. Independently chosen alphabets do not obey `H_space <= H_interior`. Axiom A5 and the scientific position forbid reading any of this as a black-hole bound.

A second confirmed tension: `AI-CONTEXT` and MATH-SKELETON Section 6 put TFE (`H_space * H_time`, units `bits^2`) in the numerator. Then `BIR` is not dimensionless and can exceed 1 by unit mismatch alone. This file uses `H_space / H_interior` unless the TFE numerator is the point.

Division by zero is also unhandled. If the interior alphabet is a single occupied state (empty night, uniform temperature, one CO2 bin), `H_interior = 0` and the ratio is undefined. The cap hides that singularity; it does not fix it.

Nothing below is a measurement. The rest is labelled speculation about what the number would *mean* if it were computed uncapped and came out above 1.

---

## 2. What BIR > 1 cannot mean [CONFIRMED]

It cannot mean the facade violates Bekenstein-Hawking or AdS/CFT. Those statements are about Planck-scale area laws and dual quantum theories (`MATH-SKELETON` 4.1; Axiom A5). Operational Shannon entropies of five angle bins and a handful of zone sensors are not those quantities (`BIR-limits.md` Breaks 1 and 3). Calling `BIR > 1` a "super-holographic building" is a disallowed claim.

It also cannot, by itself, mean the facade *encodes more interior states than the interior has*. Encoding is mutual information, not a ratio of two marginal entropies (`BIR-limits.md` Section 8). `H_space > H_interior` is a comparison of two histogram widths. It is compatible with `I(interior; facade) = 0`.

---

## 3. Reading A — over-response, already named [SPECULATIVE]

Discovery 04's own gloss: the skin is more spatially mixed than the room it serves. Architecturally that is a facade that keeps changing (or stays spatially diverse) after the interior has become simple — lockstep solar tracking on a uniformly occupied floor, a D03 humidity gradient on an empty Sunday, SAFE/VENTILATE chatter that does not track occupancy.

This would be falsified if, on a logged or fully simulated year, every hour with `H_space(t) > H_interior(t)` also had high interior-to-facade reconstructibility (a map `R` from panel-state vectors to interior labels beating a climate-only baseline). Over-response would then be the wrong name: the extra boundary entropy would still be about the room.

A narrower version: `BIR > 1` in occupied hours is a design fault (controller over-actuation, f4 waste); `BIR > 1` in vacant hours is expected weather noise. This would be falsified if occupied-hour `BIR > 1` clustered with *better* f1/f2 and no f4 penalty — i.e. if "too much skin entropy" were the high-performance regime, not over-response.

---

## 4. Reading B — climate leak, not a smarter hologram [SPECULATIVE]

`BIR-limits.md` Break 2: the envelope has a third region. Axiom A1 and the formal model feed radiation, temperature, wind, and humidity into `B(t)` beside occupancy. MATH-SKELETON 5.2 says a spore-layer gradient produces `H_space(t) > 0` whenever humidity differs from a reference, with no interior variable in the clause. Then `BIR > 1` is the generic vacant-daytime state: weather writes a rich pattern on a low-entropy interior.

This would be falsified if residualising panel states against an EPW-type climate predictor drove almost all `BIR > 1` hours down through 1, while interior-coupled hours stayed put. The excess would then be identified as climate, not as "more than holographic" encoding. It would also be falsified if a climate-only controller (D03-like, `wr`-heavy, no occupancy term) *never* produced `BIR > 1` on a low-`H_interior` chronicle — that would mean weather cannot overfill the numerator, contrary to 5.2.

---

## 5. Reading C — empty-interior singularity [SPECULATIVE]

When `H_interior -> 0+`, any positive `H_space` sends `BIR` to `+inf`. A static-looking occupied afternoon can have modest BIR; the same skin at 3 a.m. with one occupied-state bin explodes the ratio. That is a property of the quotient, not of a smarter envelope.

A regulariser is a modelling choice, not in MATH-SKELETON:

```
BIR_reg(t) = H_space(t) / (H_interior(t) + eta)
```

or a gated index that is undefined / reported separately when `H_interior < eta`. This would be falsified if, after any such gate, the remaining `BIR > 1` hours still coincided exactly with the vacated-and-weather-driven set — i.e. if the only excess were the singularity. It would also be falsified if occupied hours with `H_interior` well above `eta` still produced a large mass of `BIR > 1` that a climate residual (Reading B) could not remove. That remainder would need another reading (A, D, or E).

---

## 6. Reading D — alphabet and unit artefacts [SPECULATIVE]

`H_space` and `H_interior` use independently chosen bins. Step 04 discretises angles into five bins (`H_space <= log2(5) ~ 2.32` bits as a *histogram* entropy). Interior entropy depends on how many zones and how CO2, temperature, and occupancy are jointly binned. Coarse interior bins shrink the denominator; fine facade bins (or an extensive sum over panels instead of a global histogram) grow the numerator. `BIR > 1` can be manufactured without touching the building.

If the numerator is TFE, the fraction has units `bits^2 / bits`. Then `BIR > 1` is not a dimensionless overshoot; it is a typed expression that can exceed 1 while both factors are small. This would be falsified if, under a *fixed* published alphabet pair (same bins on every script), `BIR > 1` disappeared while a TFE-numerator script on the same log still reported `BIR > 1`. That would diagnose the unit fork, not a physical regime. It would also be falsified if two honest alphabets of comparable cardinality still produced stable `BIR > 1` after climate residualisation — the artefact reading would then be insufficient.

---

## 7. Reading E — the skin as an independent source [SPECULATIVE]

The interesting architectural remainder, after A-D are subtracted: `H_space` stays above `H_interior` *and* above climate-predicted facade entropy, *and* `I(interior; facade)` is not larger than `H_interior`. The extra bits are then neither hologram nor weather. They are an autonomous pattern — ornamental program, civic display, art-driven state machine, or a controller exploring its own frustrated `(eps, Delta_s, wr)` triangle (`frustration-RL.md`) rather than tracking the room.

That is the opposite of D04's design aspiration (skin readable as interior). It can still be a valid building. It is just not a holographic envelope in the project's own sense. Scientific-position bans ("consciousness, agency") still apply: independent source means statistically unexplained residual, not a living facade.

This would be falsified if, whenever climate-residual `H_space` exceeded `H_interior`, mutual information `I(interior; facade | climate)` also rose — i.e. if leftover skin entropy was always interior-informative. It would also be falsified if those leftover bits vanished after freezing the explore/exploit genes at a high-hold point (`high eps`, `low Delta_s`), which would mean the "independent source" was just the triangle's tracking mode, already named in ROLE 04 task 3.

---

## 8. Mutual-information BIR cannot exceed 1 [CONFIRMED / SPECULATIVE]

[CONFIRMED] For any pair of discrete variables, `I(X; Y) <= H(X)` and `I(X; Y) <= H(Y)`. The successor index proposed in `BIR-limits.md` Section 9,

```
BIR_enc(t) = I( interior(t) ; facade(t) | climate(t) ) / H(interior(t) | climate(t))
```

therefore lies in `[0, 1]` when the denominator is positive. There is no `BIR_enc > 1` regime.

[SPECULATIVE] The operational use of `BIR > 1` is then diagnostic: it flags that the *Shannon ratio* has left the set that an encoding index can occupy. A dashboard that plots both,

```
BIR_raw(t)   = H_space(t) / H_interior(t)          (uncapped)
BIR_enc(t)   in [0, 1]
```

would treat `BIR_raw > 1` with `BIR_enc ~ 0` as climate/ornament/artefact, and `BIR_raw ~ 1` with `BIR_enc ~ 1` as the only "holographic-limit" candidate D04 actually wants. This would be falsified if `BIR_raw > 1` hours were exactly the hours of maximum `BIR_enc` — the raw overshoot would then be a monotonic proxy for encoding, and the diagnostic split would be unnecessary.

---

## 9. Design and optimisation consequences [SPECULATIVE]

If Wallacei maximises TFE or raw BIR without a cap, the search can harvest `BIR > 1` by (i) emptying the interior alphabet in the scoring hours, (ii) amplifying climate-driven diversity, or (iii) inflating facade bins. That would look like a "more holographic" score and be the opposite. A capped BIR (`min(ratio, 1)`) hides the failure instead of penalising it.

A cleaner outer objective, still speculative, is:

```
max  BIR_enc
s.t. f1, f2, f4   (existing performance)
     BIR_raw reported, not rewarded when > 1
```

or a penalty `max(BIR_raw - 1, 0)` if the team wants to treat overshoot as over-actuation (Reading A). This would be falsified if, on the same chronicle, maximising uncapped `BIR_raw` produced higher `BIR_enc` and better f1/f2 than maximising `BIR_enc` itself. The raw overshoot would then be a useful objective, not a pathology.

Occupancy-conditioned reporting is the minimum process claim: never quote a single annual-mean BIR that mixes 3 a.m. singularities with occupied peaks. This would be falsified if occupied-only and all-hours means of `BIR_raw` agreed to within a declared tolerance on S0/S1/S2 — the singularity would then be numerically idle.

---

## 10. What a BIR > 1 building is *not* allowed to be [CONFIRMED]

Per Axiom A5 and scientific position:

- not a counterexample to the holographic principle;
- not a CFT with more boundary degrees of freedom than bulk;
- not evidence of agency or biological life in the skin;
- not a new discovery. Discovery 04 already reserved the phrase "over-responsive." This note only unpacks that phrase and the competing bookkeeping readings.

Evidence level of every speculative reading above is L0 until a simulation logs `H_space`, `H_interior`, climate, and (if claimed) `I(interior; facade)`. Path to L1: the same GhPython / Python pipeline Discovery 04 already lists, with the cap removed and the hours split by occupancy.

---

## 11. Position

[CONFIRMED] `BIR > 1` is already in Discovery 04 and is forbidden by the MATH-SKELETON cap. The cap is a convention. The holographic analogy does not extend above 1; it simply stops.

[SPECULATIVE] The productive meaning of an uncapped `BIR > 1` building is almost always one of: over-response, climate leak, empty-interior blow-up, alphabet/TFE-unit artefact, or an autonomous skin residual. None of those is "more holographic than 1." The quantity that *cannot* exceed 1 is `BIR_enc`. This would be falsified if a future log showed `BIR_raw > 1` hours coinciding with high climate-conditional mutual information and high reconstructibility, under a fixed alphabet, in occupied time — the one case in which overshoot would deserve to be called extra encoding rather than extra noise.

Until that log exists, THEORIST's claim is: do not cap BIR to protect an analogy; report the overshoot, split it by occupancy and climate, and refuse any sentence that says the building exceeded AdS/CFT.
