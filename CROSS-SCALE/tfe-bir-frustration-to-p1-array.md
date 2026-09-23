# CROSS-SCALE: TFE / BIR / frustration → P1 4×4 array

Role: HE_THEORIST (Theory Mapper).  
Status: transfer map only. No 4×4 log exists. No TFE, BIR, RSB, or intelligence measurement on a building or Grasshopper array is in-repo.  
Octopus: computational-scale comparison placeholder (P5 timing). Not a manager. This note does not touch any Octopus repository.

`claim_type` vocabulary is exactly: `inspiration` | `formal_model` | `tested_analogy` | `validated_result`.  
No row below is `validated_result` (no measured TFE/BIR/RSB on a building or 4×4). No row is `tested_analogy` (no P1 CSV yet).  
[CONFIRMED] = definitional or textbook fact already in SoT / theorist notes.  
[SPECULATIVE] = transfer hypothesis; each such claim includes a falsifier.

Critic deliverables (`agents/critic/unsupported-claims.md` and siblings) already exist from ROLE 07 / PR #5 class. They are **pending owner/merge reading**, not re-run or rewritten here.

---

## 0. Scope and SoT pointers

Program SoT: `CHARTER.md` (this branch / PR #12 lineage). Season goal: a discovery machine, not a mega-law and not a sold panel.

P1 (from `ROADMAP.md`), treated as the only experimental body this note maps onto:

- 4×4 cellular array in Grasshopper (N_cells = 16)
- Inputs: radiation, RH, temperature, occupancy proxy, previous state
- Controls: homogeneous array + random array
- Log: angle, aperture, response time, recovery time, hysteresis
- Artifacts: CSV + time-lapse / animation

Source theorist notes (already on this line; ROLE 04 complete):

- `agents/theorist/TFE-Kolmogorov.md` — TFE is a `bits^2` Shannon product, not a lower bound on Kolmogorov `K`
- `agents/theorist/BIR-limits.md` — AdS/CFT analogy breaks; prefer climate-conditional mutual information
- `agents/theorist/BIR-greater-than-one.md` — uncapped `BIR > 1` is not super-holographic
- `agents/theorist/frustration-RL.md` — `(eps, Delta_s, wr)` is three-way explore/exploit, not `eps_greedy`

Equations: `MATH-SKELETON.md` §§1, 2.4, 3, 4. Briefing: `AI-CONTEXT.md` D01/D02/D04. Axioms: `research/boundary-axioms.md` A1–A5. Controller: `research/formal-model.md`. Array geometry currently specified for 80 panels (`grasshopper/step-04-TFE.md`); P1 shrinks the ensemble to 16 cells without changing the histogram formulas.

Idea atom for this map: `schemas/IS-0009.yaml` (`id: IS-0009`, `claim_type: inspiration`, `status: proposed`). IS-0001–0008 are reserved for measured-array candidates and are not created here.

This note is **not** ROADMAP P5. P5 is cross-scale transfer *after* P1–P4 results. This is a P0/P1 theory map: what may be computed on the first 16-cell log, and what language must stay boxed.

OPEN and left OPEN (do not resolve, do not patch math):

1. `J-arch-jacobian-mismatch` — `agents/conflicts/J-arch-jacobian-mismatch.md`
2. `frustration-convention-mismatch` — `agents/conflicts/frustration-convention-mismatch.md`

---

## 1. Claim table

| id | claim | claim_type | transfers_to_P1? | falsifier | metaphor risk |
|---|---|---|---|---|---|
| CS-TFE-01 | TFE is `H_space(t) * H_time(i)` in `bits^2`; it is not `K(X)` | formal_model | Yes — compute both factors on 16 cells; never report TFE as complexity | Typed inequality `TFE <= K` on any finite log (already ill-typed; see §2) | Kolmogorov / "incompressible facade" |
| CS-TFE-02 | On N=16, `H_space(t) <= log2(S)` bits for an S-bin histogram (S=5 → ~2.32 bits); product range is `[0, log2(S)*log2(S_time)]` | formal_model | Yes — same formulas as MATH-SKELETON 1.2–1.4 | A published P1 script that uses a different entropy than 1.2–1.4 while calling it TFE | None if units stay explicit |
| CS-TFE-03 | Homogeneous control → `H_space ~ 0`; random control → high `H_space` without interior meaning; a driven 4×4 should sit between them on TFE only if spatial mixing *and* temporal mixing both rise | inspiration | Yes — primary P1 ranking | Same chronicle: TFE(homogeneous) ≥ TFE(driven) **or** TFE(random) fails to exceed TFE(homogeneous) after the same discretisation | "Optimised = intelligent" |
| CS-TFE-04 | TFE may *correlate* with compressed CSV length across the three P1 families; that is a proxy test, not a K bound | inspiration | Optional sidecar on the CSV | Fixed compressor ranking disagrees with TFE ranking on the three families | Kolmogorov lower bound |
| CS-BIR-01 | Operational BIR as `H_space / H_interior` is a ratio of two chosen histograms, not reconstructibility | formal_model | Yes — report uncapped ratio; do not treat =1 as completeness | n/a (definitional) | AdS/CFT, holographic limit |
| CS-BIR-02 | Encoding index `BIR_enc = I(interior; facade \| climate) / H(interior \| climate)` lies in `[0,1]` when the denominator is > 0 | formal_model | Yes — preferred P1 path | n/a (Shannon inequality) | Holographic cap imported from physics |
| CS-BIR-03 | Climate (radiation, RH, temperature) is a third region; occupancy proxy is the interior alphabet | formal_model | Yes — P1 already logs those inputs | n/a (A1 + ROADMAP P1 inputs) | "Skin writes the room" |
| CS-BIR-04 | Random-array high `H_space` with near-chance `BIR_enc` is climate/ornament, not a hologram; homogeneous low `H_space` is a blind skin | inspiration | Yes — the two P1 controls | After climate residual, random `BIR_enc` ≥ driven `BIR_enc` on occupied hours | AdS/CFT completeness |
| CS-BIR-05 | Uncapped `H_space > H_interior` is over-response / climate leak / empty-interior / alphabet artefact — not super-holographic | inspiration | Yes — occupancy-split report | Occupied hours with `BIR_raw > 1` *and* high `BIR_enc` *and* a working reconstruction `R` under a fixed alphabet | "Beats holographic principle" |
| CS-FR-01 | `(eps, Delta_s, wr)` is a three-way hold / slew / radiation-prior conflict; `eps_hyst` is not `eps_greedy` | inspiration | Yes — hysteresis, response time, recovery time logs | Independent sweeps find a direction that jointly improves tracking, smoothness, and radiation-priority (see §4) | Spin-glass / RSB |
| CS-FR-02 | Vanilla one-knob `eps_greedy` is not the P1 controller object | inspiration | Yes — do not collapse the gene triple in the 4×4 | One-scalar EE controller matches the three-gene (tracking, actuation, radiation-follow) front on the same chronicle | RL-agent facade |
| CS-FR-03 | RSB / `P(q)` / Hartigan-on-Wallacei is **not** a P1 4×4 claim | formal_model | No | n/a — P1 is one array, not a 5-seed Pareto archive | Replica symmetry breaking |
| CS-OPEN-J | Published `J^arch` ≠ Jacobian Gram matrix | formal_model | No — do not use `J_pub` as a fitted 16-cell coupling | n/a; conflict stays OPEN | "Calibrated Ising facade" |
| CS-OPEN-PHI | All-positive triangle has `Phi = +1` (consistent) under MATH-SKELETON 2.4, while D02 calls it AFM-frustrated | formal_model | No — verbal conflict may still be swept; Phi is not repaired here | n/a; conflict stays OPEN | "Classical AF triangle proved" |
| CS-IG-01 | P1 logs can *speak to* sensing / memory / feedback / self-organization / adaptation; they cannot prove intelligence | inspiration | Yes — columns only | See §7; a single kinetic demo is not ≥3/5 | "Intelligent panel" |
| CS-OCT-01 | Octopus TFE/BIR/H_coord maps are FUTURE DESIGN placeholders for P5 | inspiration | No (not now) | n/a until P1–P4 exist | Octopus-as-owner / validated cross-scale law |
| CS-NO-01 | AdS/CFT, RT surfaces, QEC, Bekenstein-Hawking, SK/RSB, and `K(X)` do not transfer as tested statements | formal_model | No | n/a | Entire leakage list in §5 |

Upgrade rule: a row moves `inspiration → tested_analogy` only after a P1 CSV + declared controls + the listed falsifier is run and survived. It does **not** jump to `validated_result` from one 4×4 script.

---

## 2. TFE → P1 (H_space / H_time on 16 cells; bits² product, not K)

### 2.1 What is already definitional

**CS-TFE-01** — `claim_type: formal_model` — [CONFIRMED]

MATH-SKELETON 1.2–1.4 and `TFE-Kolmogorov.md`:

```
H_space(t) = - sum_s p_s(t) * log2(p_s(t))     # bits; s = angle or aperture bin
H_time(i)  = - sum_s q_s(i) * log2(q_s(i))     # bits; i = cell 0..15
TFE(i,t)   = H_space(t) * H_time(i)            # bits^2
TFE_total  = <H_space>_t * <H_time>_i
```

`p_s(t)` is the fraction of the 16 cells in bin `s` at tick `t`. `q_s(i)` is the fraction of ticks cell `i` spends in bin `s`. Step 04's five angle bins `[0-18], [18-36], [36-54], [54-72], [72-90]` remain a legal alphabet; aperture can use the same five-bin rule on `[0,1]`. N_cells = 16 changes sample size, not the functional form.

TFE is a computable diversity index. Kolmogorov complexity `K` of the flattened log is an uncomputable bit length of one string. Product units are `bits^2`. No conversion to bits is defined. Therefore `TFE <= K` is not a typed inequality (`TFE-Kolmogorov.md` §3.1).

**CS-TFE-02** — `claim_type: formal_model` — [CONFIRMED]

Histogram entropy of an S-state snapshot cannot exceed `log2(S)` bits, regardless of whether the array has 16 or 80 cells. Extensive surrogates `16 * H_space(t)` or `T * H_time(i)` are *not* TFE and are *not* `K`. If a later script reports "TFE in bits," it has changed the object.

P1 implication: the CSV must carry raw `angle` and `aperture` so bins can be audited. Do not pre-collapse to a single "entropy" column that hides the product.

### 2.2 What transfers as a P1 computation (not a discovery)

On each tick, from the 16-cell state vector:

1. Bin angle (and, separately, aperture — do not silently mix).
2. Compute `H_space(t)` from the 16-bin histogram.
3. After the run, compute `H_time(i)` per cell.
4. Form `TFE_total` and keep units `bits^2` in the header.

Previous state is already a P1 input: it is the `S(t-1)` argument of Axiom A1 / the hysteresis gate. It is used to compute response and recovery; it is not a third entropy factor.

**CS-TFE-03** — `claim_type: inspiration` — [SPECULATIVE]

Transfer of D01's ranking, resized to P1 controls (static/rule/optimised in `validation/falsification-protocol.md` is *not* the P1 pair):

```
TFE(homogeneous)  <  TFE(driven 4x4)  <  TFE(random)
```

or, more carefully, two comparisons:

- Homogeneous vs driven: driven should raise `H_space` and/or `H_time` if cells are not lockstep-identical.
- Random vs driven: random should usually win raw TFE (white spatial histogram) while losing any interior-coupling score (see BIR). TFE alone cannot tell "adaptive" from "noise."

This would be falsified if, on one shared input chronicle (same radiation, RH, temperature, occupancy-proxy series), TFE(homogeneous) ≥ TFE(driven) under a frozen alphabet, **or** if TFE(random) ≤ TFE(homogeneous). The second clause failing means the controls are not controls. The first clause failing means TFE does not separate a driven skin from a flat one on this 4×4.

Small-N caveat (still [SPECULATIVE], same falsifier): with 16 cells, `H_space` estimates are coarse. A 5-bin histogram on 16 draws is legal but high-variance. This would be falsified as a *useful* P1 metric if bootstrap resampling of the 16 cells reversed the homogeneous/driven ranking in a large fraction of resamples (declare the fraction before looking). That is a usefulness kill, not a math kill.

### 2.3 What must not be smuggled in

**CS-TFE-04** — `claim_type: inspiration` — [SPECULATIVE]

`TFE-Kolmogorov.md` §5 allows a compressor-sidecar: gzip / a `B`-replay of the controller on the recorded inputs, compared with TFE ranking. This would be falsified if the TFE ranking and the compressed-length ranking of {homogeneous, driven, random} CSVs disagreed for a fixed compressor and discretisation.

Until that sidecar exists, the honest sentence is: P1 can compute TFE; P1 cannot measure `K`; P1 must not say "the 4×4 is algorithmically complex because TFE is high."

A travelling wave, a global lockstep cycle, and spatially white i.i.d. noise can share similar histograms and therefore similar TFE (`TFE-Kolmogorov.md` §3.2). Time-lapse is the qualitative check; spatial autocorrelation (P3) is the later quantitative check. P1 should *store* the per-cell series so those tests remain possible.

---

## 3. BIR → P1 (mutual-information path; climate as third region)

### 3.1 What is already definitional

**CS-BIR-01** — `claim_type: formal_model` — [CONFIRMED]

MATH-SKELETON 1.5:

```
BIR(t) = H_boundary(t) / H_interior(t)
H_boundary(t) = H_space(t)
```

`AI-CONTEXT` D04 and MATH-SKELETON §6 also put TFE in the numerator (`bits^2 / bits`). Discovery 04 uses `H_space` (bits). This note does **not** repair the fork. P1 should compute the bit/bit form and, if anyone insists on a TFE numerator, label it a different symbol. Equality of two Shannon numbers is not a dictionary and not reconstructibility (`BIR-limits.md` Breaks 1 and 6).

The `[0,1]` cap is a modelling convention imported from the holographic slogan, not a theorem. Discovery 04 already names `BIR > 1` as over-response. Do not cap the P1 series to protect an analogy (`BIR-greater-than-one.md`).

**CS-BIR-02** — `claim_type: formal_model` — [CONFIRMED]

For discrete variables, `I(X;Y) <= H(X)` and `I(X;Y|Z) <= H(X|Z)`. Therefore

```
BIR_enc(t) = I( interior(t) ; facade(t) | climate(t) ) / H(interior(t) | climate(t))
```

lies in `[0, 1]` when `H(interior|climate) > 0`. There is no `BIR_enc > 1` regime. This is the successor index already proposed in `BIR-limits.md` §9. It is still unmeasured.

**CS-BIR-03** — `claim_type: formal_model` — [CONFIRMED]

Axiom A1 and the formal model feed radiation, temperature, humidity/RH, and occupancy into `B(t)`. A building envelope has two volumes plus a climate drive. AdS/CFT does not (`BIR-limits.md` Break 2). P1's input list *is* that third region: radiation, RH, temperature = climate; occupancy proxy = interior alphabet (plus any later zone-temperature column if added). Previous state is controller memory, not interior entropy.

### 3.2 What transfers onto the 4×4 log

Declare, in the CSV header, three alphabets before the run:

| Region | P1 columns | Suggested coarse alphabet (design choice, not a result) |
|---|---|---|
| Facade | `angle`, `aperture` per cell | 5 angle bins and/or 5 aperture bins; also the 16-vector as a joint symbol if cardinality is kept tiny |
| Interior | `occupancy_proxy` (and later zone T if present) | 2–4 occupancy bins; joint with a coarse T bin only if that column exists |
| Climate | `radiation`, `RH`, `temperature` | Independent bins; used as the conditioning variable, not as "interior" |

Compute and archive, per occupied / vacant split:

```
BIR_raw(t)  = H_space(t) / H_interior(t)          # uncapped; undefined if H_interior = 0
BIR_enc     = I(interior; facade | climate) / H(interior | climate)
```

Gating: when `H_interior < eta`, report `BIR_raw` as undefined, not as infinity and not as 1 (`BIR-greater-than-one.md` Reading C). `eta` is a pre-registered threshold, not a fitted "holographic" fudge.

**CS-BIR-04** — `claim_type: inspiration` — [SPECULATIVE]

P1 controls as BIR instruments:

- **Homogeneous array:** all 16 cells share one law and one state. Expect `H_space ~ 0`, `BIR_raw ~ 0` when defined, `BIR_enc ~ 0`. Blind skin.
- **Random array:** independent draws (or independent noise on targets). Expect high `H_space`, possibly `BIR_raw > 1`, `BIR_enc` near chance. Climate/ornament, not encoding.
- **Driven 4×4:** the actual controller under test (formal-model gate or local rule). The only interesting win is `BIR_enc(driven) > BIR_enc(homogeneous)` **and** `BIR_enc(driven) > BIR_enc(random)` on occupied hours, after climate conditioning.

This would be falsified if, after residualising facade state against a climate-only predictor (radiation+RH+temperature, no occupancy), `BIR_enc` of the random array is ≥ `BIR_enc` of the driven array on occupied hours. That would mean the "adaptive" skin is not carrying interior information beyond weather and noise.

A second falsifier (reconstruction, `BIR-limits.md` §6): this would be falsified if `BIR_raw` is forced near 1 (or capped at 1) while the best map `R` from the 16-vector to occupancy-proxy bins performs at chance versus a climate-only baseline.

**CS-BIR-05** — `claim_type: inspiration` — [SPECULATIVE]

Uncapped `BIR_raw > 1` on the 4×4 means one of the readings in `BIR-greater-than-one.md` (over-response, climate leak, empty-interior singularity, alphabet/TFE-unit artefact, autonomous residual). It does **not** mean the array beat AdS/CFT.

This would be falsified if occupied hours with `BIR_raw > 1` were exactly the hours of maximum `BIR_enc` *and* a working `R`, under one frozen alphabet. That is the single case in which overshoot would be extra encoding rather than extra noise. Until then, report the overshoot; do not reward it.

RH is a first-class P1 climate channel. MATH-SKELETON 5.2 already says a spore-layer gradient produces `H_space > 0` whenever humidity differs from a reference, with no interior variable in the clause. A humidity-driven 4×4 can look "alive" on TFE and blind on `BIR_enc`. That is a feature of the third region, not a bug to hide.

---

## 4. Frustration / RL → P1 (three-way explore-exploit; OPEN conflicts)

### 4.1 What is already definitional — and what stays OPEN

Formal-model gate (Axiom A4), unchanged for 16 cells:

```
o_i(t) = clamp( wr*R_i + wt*T_i + wc*C_i + wu*U_i , 0, 1 )
delta  = o_i(t) - o_i(t-1)
if |delta| < eps:   hold
else:               step by min(|delta|, Delta_s) * sign(delta)
```

P1 logs map onto the gate without new physics:

| Log column | Gate object |
|---|---|
| `angle`, `aperture` | state `S_i(t)` / open-ratio proxy |
| `previous state` | `S_i(t-1)` |
| `hysteresis` | whether `|delta| < eps` fired (hold vs move) |
| `response time` | ticks from input step to leaving the dead-band and reaching a stated fraction of the new target |
| `recovery time` | ticks to resettle after the input returns or after a perturbation |

**CS-OPEN-J** — `claim_type: formal_model` — [CONFIRMED] — **OPEN, not repaired**

`J^arch` published in `AI-CONTEXT` D02 does not equal the Gram matrix from the Jacobian sign table (`agents/conflicts/J-arch-jacobian-mismatch.md`). Sign mismatches include `(a,wr), (r,wr), (eps,wr), (ms,wr)`. The frustrated-triangle *narrative* depends on `J_pub`, not on `J^(der)`. P1 must not treat `J_pub` as a fitted coupling among 16 cells, nor as a calibrated Ising model of the array.

**CS-OPEN-PHI** — `claim_type: formal_model` — [CONFIRMED] — **OPEN, not repaired**

MATH-SKELETON 2.4: `Phi_ijk = sign(J_ij)*sign(J_jk)*sign(J_ik)`. All-positive published bonds give `Phi = +1` (consistent) under `H = -sum J sigma_i sigma_j`, while D02 calls the same triangle a classical AFM frustrated triangle (`agents/conflicts/frustration-convention-mismatch.md`). `frustration-RL.md` already uses the *verbal* pairwise-conflict table and refuses to resolve `Phi`. This note does the same.

Critic has already listed Jacobian- and convention-dependent triangle claims (`unsupported-claims.md`; STATUS-BOARD CRITIC-C12/C13). Pending. Not re-derived here.

### 4.2 What transfers as a sweep, not as RSB

**CS-FR-01** — `claim_type: inspiration` — [SPECULATIVE]

`frustration-RL.md` map, applied to P1 knobs (not to a claimed spin glass):

```
eps      <->  stickiness / hold   (high eps = exploit current cell state)
Delta_s  <->  slew / action magnitude
wr       <->  radiation-channel prior vs occupancy / RH / T
```

Inverted-epsilon: larger `eps` means *less* motion. That is the opposite of `eps_greedy`. Name collision only.

P1 can test the *verbal* three-way conflict without touching `J^arch` or `Phi`:

- Raise `eps`, hold `Delta_s`, `wr`: expect fewer moves, longer effective response time, more hysteresis holds, lower actuation count.
- Raise `Delta_s`, hold `eps`, `wr`: expect shorter response time, possible overshoot, faster recovery *or* chatter.
- Raise `wr`, hold the gate: expect tighter follow of radiation, weaker follow of occupancy proxy / RH; larger `|delta|` when radiation ramps, so more fights with the dead-band and the slew cap.

This would be falsified if an independent sweep of `(eps, Delta_s, wr)` on a fixed P1 chronicle found a direction that simultaneously improved (or held) (i) occupancy-or-radiation tracking error, (ii) actuation / chatter (response+recovery+hold count), and (iii) the priority channel named by `wr`. That is the operational meaning of "the triangle is not a dilemma."

A second falsifier on the inverted-epsilon name (`frustration-RL.md` §3): this would be falsified if high `eps` *increased* state-space coverage or actuation count rather than decreasing them.

**CS-FR-02** — `claim_type: inspiration` — [SPECULATIVE]

Do not collapse the 4×4 controller to a single `eps_greedy`. A one-knob "explore rate" cannot represent `wr` (which channel is trusted) and inverts `eps`. This would be falsified if a one-scalar EE controller recovered the same non-dominated set of (tracking, actuation, radiation-follow) outcomes as the three-gene controller on the same chronicle.

**CS-FR-03** — `claim_type: formal_model` — [CONFIRMED]

RSB detection in MATH-SKELETON 3.4 is a protocol on a *Wallacei Pareto archive*: pairwise gene distances, Hartigan dip, GMM `K >= 2`. A 4×4 time series is not that archive. `P_arch(d)` is not `P(q)`. Simulator `synthetic-pareto.json` is labelled SYNTHETIC and is not evidence. P1 must not emit "RSB confirmed," "spin-glass ground state," or "replica families" from 16 cells, a time-lapse, or a three-knob sweep.

If someone later runs many *design* seeds (P3/Wallacei), that is a different experiment. It is not P1.

### 4.3 Three-way explore-exploit on the array (still speculative)

The 4×4 can instantiate three *families* of behaviour without claiming multiple thermodynamic basins:

- high-hold / quiet (high `eps`, low `Delta_s`)
- radiation-tracking / high-slew (high `wr`, high `Delta_s`)
- mixed-channel / moderate gate (split `wr` with occupancy / RH / T)

Time-lapse should show those families as different movies, not as one "optimal" clip. This would be falsified if the three corners of the box produced indistinguishable angle/aperture series (same response, recovery, and hold counts within a pre-registered tolerance). Visual similarity is not RSB; it is a control that the knobs do something.

---

## 5. Metaphor leakage — do not use as if tested on the 4×4

Axiom A5: analogy must be named, must generate a test, and must not imply physical equivalence. The following words are **banned as results** of P1. They may appear only inside a leakage warning or a "not claimed" sentence.

| Language | Why it does not attach to a 16-cell Grasshopper log | Allowed P1 substitute |
|---|---|---|
| AdS/CFT, "the CFT on the facade," bulk/boundary duality | No dual pair, no dictionary, no matching partition functions (`BIR-limits.md` Break 1) | `BIR_enc`, reconstruction `R` |
| Holographic completeness, `BIR = 1` as exact encoding | Cap is conventional; equal Shannon numbers ≠ invertibility | Occupied-hour `BIR_enc` vs chance and vs climate-only |
| Bekenstein-Hawking, `A/(4 l_p^2)`, Planck-area bits | Operational 5-bin Shannon is not area-law entropy (Break 3) | Channel capacity = distinguishable 16-cell configurations |
| Ryu-Takayanagi, entanglement wedge, extra radial dimension | No RT rule; floor plates are ordinary 3-space (Break 5) | Spatial autocorrelation of the 4×4 (P3) |
| Holographic QEC / redundant bulk reconstruction | Losing one cell loses that cell's angle unless redundancy is *engineered* | Explicit repeated encodings, if ever designed |
| Spin glass, Edwards-Anderson, SK, quenched Gaussian `J` | `J^arch` is a 6×6 design-gene table, OPEN vs Jacobian; 16 cells are not SK N→∞ | Named knob conflict + sweep table |
| RSB, replica, `P(q)` multi-peak as "confirmed" | Protocol not run; P1 is not a Pareto archive; SYNTHETIC fixture is planted | Do not use |
| "Formally equivalent to a spin-glass Hamiltonian" | Critic C01: correspondence table ≠ isomorphism; pending | "Quadratic scalarisation of four objectives" if used at all |
| Kolmogorov `K`, incompressible / algorithmically random facade | TFE is `bits^2` histograms; `K` uncomputable | Compressor sidecar, labelled upper bound |
| `eps_greedy` as the hysteresis gene | Sign of "more eps" is inverted | `eps_hyst` / hold threshold |
| Super-holographic / BIR>1 beats physics | Category error (`BIR-greater-than-one.md` §2) | Uncapped `BIR_raw` diagnostic |
| Intelligent / living / agentive skin | Intelligence gate not passable by motion; CHARTER forbids solo verdict | Kinetic / interactive until ≥3/5 measured |
| Octopus as manager, owner, or current validation | CHARTER; ROADMAP P5 only after P1–P4 | Placeholder paragraph in §8 |

Time-lapse especially invites leakage ("it looks holographic"). A movie is an artifact, not a dual theory.

---

## 6. What does NOT transfer

Even as `inspiration`, the following stay off the P1 scoreboard:

1. **80-panel expected TFE ranges** from `grasshopper/step-04-TFE.md` (0.1–0.5 rule-based, 1.5–4.0 optimised, ~8 max). Those numbers assume 80 panels and an 8760-hour year. They are not 4×4 forecasts.
2. **Wallacei / σ\* / Sydney `h` field** as a predicted 4×4 ground state. No EPW-solved Wallacei archive is in-repo; σ\* is an untested narrative point.
3. **RSB, Hartigan, GMM `K`** (see CS-FR-03).
4. **Fitted `J^arch` or a repaired `Phi`.** Both conflicts remain OPEN. No silent edit of `MATH-SKELETON.md` or `AI-CONTEXT.md`.
5. **TFE as `K` or as BIR numerator without a unit note.**
6. **Capped BIR as physics.**
7. **Spore `theta_max(n)` / 1e6-cycle / cork-optimal claims** as 4×4 results. Materials protocols are protocols; no coupons. P1 is a Grasshopper array.
8. **Central SAFE/OPEN/SHADED/VENTILATE as self-organization.** CHARTER keeps that stack as a *central-controller baseline* versus self-organization. If P1 uses it, label it baseline, not collective intelligence.
9. **P2 two-history memory, P3 local-rule vs sum-of-16, P4 lag-MI as completed.** P1 only *logs* the columns those phases will need.
10. **Commercial / market / NCC** — non-core (`DOWNSTREAM/`). Not used here.
11. **Critic rewrite.** Unsupported-claims list remains the Critic artifact. This map may cite it as pending.

---

## 7. Intelligence gate — how P1 logs could speak (not prove)

CHARTER: motion is not intelligence. A later "intelligent structure" claim needs **at least three of five** measurable properties. No agent may alone declare intelligence proved. P1 can only instrument the questions.

| Property | What a P1 CSV + time-lapse could show later | What would *not* count | Suggested control |
|---|---|---|---|
| Sensing | Repeatable correlation between an input (radiation, RH, T, occupancy proxy) and `angle`/`aperture` | Any motion; random array twitching | Homogeneous lock + climate-only vs occupancy-on |
| Memory | `previous_state` changes present output at matched current input (hysteresis holds; path dependence) | Drift, fatigue, or a clock that was not reset — those are P2 confounders | Same final input, two prior histories (full test is P2; P1 only stores the series) |
| Feedback | Prior structure state (`S(t-1)`, hold/move flag) statistically affects `S(t)` beyond the raw target `o(t)` | A memoryless map `S(t)=f(X(t))` with no gate | Freeze `eps=0` and `Delta_s=1` as a no-feedback control |
| Self-organization | A local rule yields a 4×4 pattern that the sum of 16 independent cells does not (spatial correlation, not just high TFE) | Homogeneous lockstep; random salt; a global SAFE broadcast | Homogeneous + random + (later) independent-cell clone — this is P3's job; P1 can only avoid deleting per-cell series |
| Adaptation | After an input step or perturbation, recovery time is finite and performance (tracking error, chatter) returns toward baseline | One pretty transient in a time-lapse | Step RH or radiation; compare recovery across the three families in §4.3 |

**CS-IG-01** — `claim_type: inspiration` — [SPECULATIVE]

If P1 is logged as specified, it can *supply evidence toward* sensing (input–state correlation), feedback (hysteresis gate), and a weak adaptation readout (recovery time). Memory and self-organization are under-determined until P2/P3. That is at most a path to three columns, not a passed gate.

This would be falsified as an intelligence claim — and must stay labelled kinetic — if the driven array's input–state correlations are indistinguishable from the random control, **or** if `eps=0`, `Delta_s=1` reproduces the same series as the hysteretic gate, **or** if recovery times are not shorter (or more stable) than the random array's after the same step. Any public sentence that the 4×4 is intelligent is out of scope for this note and out of scope for P1 alone.

---

## 8. Octopus exemplar (placeholder only; P5 timing)

**CS-OCT-01** — `claim_type: inspiration` — [SPECULATIVE] as a *future comparison*, not as a present result.

`agents/octopus-bridge/*` are DESIGN DOCUMENTS. They map TFE / a coordination Hamiltonian / BIR onto observable agent traces if an owner later says GO. CHARTER: Octopus is one computational-scale exemplar, not the manager or owner of this repository. ROADMAP P5: extract one limited operational principle only after P1–P4 results, then compare the *same relation* in a biological system or the Octopus computational exemplar, stating substrate differences. Nothing in those design files is implemented; nothing here writes to an Octopus repo.

Until a 4×4 CSV exists, the only honest cross-scale sentence is: if P1 later supports `TFE = bits^2` diversity plus `BIR_enc` as climate-conditional mutual information, those *same two functionals* could be computed on agent traces as a comparison, not as proof that facades and fleets share a law. This would be falsified if the two functionals failed to separate the P1 controls in §2–§3 — in that case there is no principle to export. Do not schedule that comparison now.

---

## 9. Upgrade paths (inspiration → tested_analogy)

Each path needs the P1 artifacts (CSV + time-lapse), the named controls, and a pre-registered falsifier. Survival upgrades `claim_type` one step. Failure refutes the transfer, not the whole program.

| From | Measurement on the 4×4 | Controls | Falsifier (pre-register) | If survived |
|---|---|---|---|---|
| CS-TFE-03 | `TFE_total` in `bits^2` from 5-bin angle (and separately aperture) | homogeneous, random, driven | ranking collapse or bootstrap reversal of homogeneous vs driven | `tested_analogy` for "TFE separates flat from mixed 16-cell logs" |
| CS-TFE-04 | compressed size of the three CSVs vs TFE | same three families; one compressor | ranking disagreement | `tested_analogy` for "TFE tracks a compressor on this alphabet" — still not `K` |
| CS-BIR-04 | `BIR_enc` occupied-hours; climate-only residual | homogeneous, random, driven; climate-only predictor | random ≥ driven after residual | `tested_analogy` for "driven skin carries occupancy beyond weather" |
| CS-BIR-05 | occupancy-split `BIR_raw` vs `BIR_enc` | vacant vs occupied; fixed alphabet | `BIR_raw>1` hours = max `BIR_enc` + working `R` | either drop "over-response" name or keep it — data decides |
| CS-FR-01 | sweep `eps`, `Delta_s`, `wr`; log holds, response, recovery | three-knob grid on one chronicle | joint improvement direction for tracking, chatter, priority | `tested_analogy` for "three-way gate conflict" — still not RSB, still not a resolved `Phi` |
| CS-FR-02 | one-knob EE vs three-gene front | wr frozen vs free | one knob matches the front | if matched, collapse is allowed *operationally*; OPEN math conflicts still OPEN |
| CS-IG-01 | correlations, hold-flag Granger/lag, recovery | random + no-gate | see §7 | at most "gate columns are live"; never `validated_result` for intelligence from P1 |

Uncertainty to log with every number: bin edges, tick duration, `eta`, occupancy split, whether angle or aperture entered `H_space`, missing ticks, and that N=16 makes `H_space` high-variance.

---

## 10. Position

[CONFIRMED] (`claim_type: formal_model`) TFE is a `bits^2` histogram product on whatever ensemble is logged — 16 cells included. BIR as a Shannon ratio is not completeness. Mutual information is the encoding functional and is naturally capped. Climate is a third region already present in the P1 input list. `J^arch` vs Jacobian and AFM-vs-`Phi=+1` remain OPEN. RSB is predicted, not measured. Critic's unsupported-claims list is already on disk and is not this note.

[SPECULATIVE] (`claim_type: inspiration`) The 4×4 can host three honest tests: TFE ranking against homogeneous and random controls; `BIR_enc` versus those controls after climate conditioning; a three-knob gate sweep that does not collapse to `eps_greedy`. This would be falsified if those tests failed as specified in §§2–4. None of them licenses AdS/CFT, spin-glass RSB, Kolmogorov bounds, or an intelligence verdict.

P5 and Octopus wait. Commercialization is not activated.
