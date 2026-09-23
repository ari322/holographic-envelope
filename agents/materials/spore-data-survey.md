# Bacillus subtilis spore actuator survey
# ROLE 03 — MATERIALS SCIENTIST
# Date: 2026-09-23
# Status: literature survey only. No panels have been built.
# Citation source: HE MATERIALS verified literature brief (2026-09-23).
# No DOI or paper is cited here unless it appears in that brief.

Claim tags used throughout:
- [LITERATURE-CONFIRMED] = published fact from the verified brief, with paper + DOI (or journal cite if the brief gives no DOI).
- [PROJECT-CLAIM / UNVERIFIED] = statement from AI-CONTEXT.md (D03) or related project files that is not supported by the surveyed papers.

Plain ASCII math.

---

## 0. Scope and papers used

This survey compiles published Bacillus subtilis spore-actuator metrics that are relevant to D03 (programmable bacterial spore panels). It is not a new experiment and it does not add discoveries.

Core papers (verified brief):

| ID | Paper | Venue | DOI |
|----|-------|-------|-----|
| P1 | Chen, X., Mahadevan, L., Driks, A. and Sahin, O. Bacillus spores as building blocks for stimuli-responsive materials and nanogenerators. | Nature Nanotechnology 9, 137-141 (2014) | 10.1038/nnano.2013.290 |
| P2 | Chen, X. et al. Scaling up nanoscale water-driven energy conversion into evaporation-driven engines and generators. | Nature Communications 6, 7346 (2015) | 10.1038/ncomms8346 |
| P3 | Birch, E., Bridgens, B., Zhang, M. and Dade-Robertson, M. Bacterial Spore-Based Hygromorphs: A Novel Active Material with Potential for Architectural Applications. | Sustainability 13, 4030 (2021) | 10.3390/su13074030 |

Related / secondary (verified brief; cite carefully):

| ID | Paper | Notes |
|----|-------|-------|
| P4a | Sahin, O., Yong, E.H., Driks, A. and Mahadevan, L. Physical basis for the adaptive flexibility of Bacillus spore coats. J. R. Soc. Interface 9, 3156-3160 (2012). | Coat-mechanics context. Brief gives no DOI; none invented here. |
| P4b | Bioinspir. Biomim. (2024) DOI 10.1088/1748-3190/ad3a4d | Programming via etch direction and spore concentration; latex ~0.4 mm; architectural aperture prototypes. |
| P4c | Wang et al. Sci. Adv. 2017 | Biohybrid wearables; vegetative / related constructs. Not treated as pure spore-monolayer data. |
| P4d | Ramirez-Figueroa et al. ACADIA 2017 | Design proposals; limited experimental scope per Birch. |

---

## 1. Mechanism

[LITERATURE-CONFIRMED] Bacillus subtilis spores change size with ambient water activity / relative humidity and can be assembled into water-responsive (hygromorphic) actuators (Chen 2014, DOI 10.1038/nnano.2013.290; Birch 2021, DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2014 reports that B. subtilis spores function as building blocks for stimuli-responsive materials, with energy density >10 MJ m^-3, stated as two orders of magnitude above typical synthetic water-responsive materials (DOI 10.1038/nnano.2013.290).

[LITERATURE-CONFIRMED] Chen 2014 reports that mutations can approximately double that energy density (DOI 10.1038/nnano.2013.290).

[LITERATURE-CONFIRMED] Chen 2014: spores self-assemble into dense, submicrometre-thick monolayers on silicon microcantilevers and elastomer sheets, forming bio-hybrid hygromorph actuators (DOI 10.1038/nnano.2013.290).

[LITERATURE-CONFIRMED] Related coat-mechanics literature (Sahin 2012; cited via the brief as the source of the ~12% figure used in later architectural papers) reports spore diameter change with humidity of about 12%. Birch 2021 uses this ~12% contraction limit when interpreting angle plateau (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: a densely packed monolayer is approximately 3 um thick (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2015 HYDRA constructs: spore coats on ~8 um polyimide with a spore layer ~3 um (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Chen 2015: HYDRAs can quadruple in length between RH <30% and RH >80%, with moisture exchange <5% by weight (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Birch 2021: on 0.5 mm natural latex, hydration/dehydration produces reversible bending with no direction hysteresis (the same angle at the same RH on the hydrate and dehydrate paths) (DOI 10.3390/su13074030).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03 states the mechanism as "Bacillus subtilis spores expand/contract with humidity change" and then treats n_layers as a monotone encoder of theta_max. The humidity mechanism is literature-supported; the monotone encoder is not (see Section 5).

---

## 2. Response time

Published response times are substrate- and geometry-dependent. They must not be collapsed into a single project number.

[LITERATURE-CONFIRMED] Chen 2015: HYDRA strips on ~8 um polyimide respond to an RH change in about 3 seconds (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Birch 2021: 0.5 mm latex coupons reach maximum deflection in <3 min when switched between ~42% RH and >95% RH (DOI 10.3390/su13074030).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03 lists "Response time: < 3 minutes" with no substrate. That number matches Birch 2021 latex architectural coupons, not Chen 2015 HYDRA strips. Using <3 min as a universal spore-actuator time is substrate-mismatched.

Implication for architecture: a facade-scale bilayer on millimetre-class latex (or any thicker passive sheet) should be budgeted on the Birch minute-scale, not the Chen second-scale, until measured.

---

## 3. Reversibility / cycle life

This is the most overstated cluster in AI-CONTEXT.md.

[LITERATURE-CONFIRMED] Birch 2021: local cycle test of 10 hydration/dehydration cycles showed no performance loss on the latex hygromorphs (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 cites Chen et al. for 1e6-cycle durability on other constructs; Birch does not itself demonstrate 1e6 cycles on latex architectural bilayers (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2015: after 1,000,000 humidity cycles and 80 days, HYDRA elongation was reduced only slightly (DOI 10.1038/ncomms8346). Substrate = polyimide tape. Some HYDRA samples used cotE gerE mutant spores.

[LITERATURE-CONFIRMED] Birch 2021 prefers wild-type B. subtilis for cycle resilience: cotE gerE mutant spores expand more but lack repeated-cycle resilience; B. thuringiensis spores are larger but pack less densely and are less repeatable (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: actuation is reversible, with no direction hysteresis on the RH-angle curve (DOI 10.3390/su13074030).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03: "Reversibility: 100% stable over 1,000,000 cycles."
This is overstated and substrate-mismatched:
1. Chen 2015 does not say 100% stable; it says elongation was reduced only slightly.
2. The 1e6-cycle result is on polyimide HYDRAs (and includes cotE gerE samples), not on latex architectural bilayers.
3. Birch 2021 measured 10 cycles on latex and then pointed to Chen for long-cycle context.
4. Therefore "100% stable / 1e6 cycles" must not be used as a latex-panel or cork-panel specification.

Falsification for the project claim: a latex (or cork) bilayer that loses more than a slight fraction of stroke after >>10 cycles, or that never reaches 1e6 cycles without cracking/delamination, falsifies the AI-CONTEXT wording. It does not falsify Chen 2015, which is a different construct.

---

## 4. Lift / force / work density

[LITERATURE-CONFIRMED] Chen 2014: spore energy density >10 MJ m^-3 (DOI 10.1038/nnano.2013.290).

[LITERATURE-CONFIRMED] Chen 2015: HYDRA strips can lift load weights about 50x strip mass; strip work density about 17 J kg^-1 (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Birch 2021: 4-monolayer latex actuators lifted paper loads equivalent to >=150% of actuator mass; deflection fell linearly with load (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 Stoney force: up to 26.7 N/m at the greatest monolayer count tested (4). Force vs layers was linear from 2 to 4. Birch cites a Chen latex reference of about 16 N/m at similar RH (DOI 10.3390/su13074030).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03: "Lift capacity: 150% of own weight." This is Birch's 4-monolayer latex result, not a general spore-panel constant, and not demonstrated on cork.

Do not mix Chen 2015 50x lift (thin polyimide HYDRA) with Birch 1.5x lift (0.5 mm latex). They are different devices.

---

## 5. Layer-count vs bending

This section is the architectural programming claim.

[LITERATURE-CONFIRMED] Birch 2021 tested 1, 2, 3, and 4 monolayers on 0.5 mm natural latex (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: 1 monolayer did not supply enough force to deflect that latex substrate against gravity (vertical deflection test) (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: deflection angle increased with layer count; the trend was approximately linear from 1 to 3 monolayers; diminishing returns / plateau appeared at 4 monolayers for angle, which Birch attributes to the spore contraction limit of about 12% (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: maximum deflection about 43 degrees at 4 monolayers (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: force (Stoney) continued to rise linearly from 2 to 4 monolayers even as angle approached plateau (DOI 10.3390/su13074030). This is the key split: angle saturates while force can still increase.

[LITERATURE-CONFIRMED] Bioinspir. Biomim. 2024 (DOI 10.1088/1748-3190/ad3a4d): programming demonstrated via etch direction and spore concentration (4.2-33.2 uL cm^-2), with poly-L-lysine on latex ~0.4 mm, rocking shaker deposition, and 99% RH / 24 h equilibration; architectural aperture prototypes are reported. This is concentration / pattern programming, not a 21-layer Fibonacci series.

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03:
```
n_layers(panel_i) in {1, 2, 3, ..., N_max}
theta_max(panel_i) = f(n_layers)   [monotone increasing function]
```
Birch's data do not support an unbounded monotone f. Angle is not guaranteed to keep rising past ~4 monolayers. A spatial gradient built only from n_layers therefore has a short useful range on latex of the Birch type, unless a different substrate or patterning method restores dynamic range.

[PROJECT-CLAIM / UNVERIFIED] The Fibonacci panel set n = 1, 2, 3, 5, 8, 13, 21 is a project experiment, not a published series. Birch stopped at 4. Layers 5-21 are exploratory for force, cracking, and delamination, not guaranteed larger theta_max.

Expected diminishing returns (architecture note, not a new discovery):
- If theta_max(n) is flat for n >= 5 while force rises then plateaus, that confirms the spore-strain limit (~12%) as the angle cap.
- If both angle and force collapse, or films crack/delaminate, that is a fabrication limit, not a programming gain.
- The Fibonacci set also skips n = 4, which is exactly Birch's plateau point. An n = 4 control coupon is recommended in the fabrication protocol as a DESIGN-PROPOSAL add-on so the published plateau is not missed.

---

## 6. Substrates used

Published actuator substrates in this survey:

| Substrate | Thickness / form | Paper | DOI | Role |
|-----------|------------------|-------|-----|------|
| Silicon microcantilevers | microcantilever | Chen 2014 | 10.1038/nnano.2013.290 | monolayer assembly / nanomechanics |
| Elastomer sheets | sheet (thickness not restated in brief) | Chen 2014 | 10.1038/nnano.2013.290 | bio-hybrid hygromorph |
| Polyimide tape | ~8 um film; spore layer ~3 um | Chen 2015 | 10.1038/ncomms8346 | HYDRA engines / generators |
| Natural latex | 0.5 mm; E ~ 3.0 MPa | Birch 2021 | 10.3390/su13074030 | architectural-relevance hygromorph |
| Natural latex | ~0.4 mm | Bioinspir. Biomim. 2024 | 10.1088/1748-3190/ad3a4d | programmed apertures |

[LITERATURE-CONFIRMED] Chen 2015 substrate is polyimide tape. It is not cork (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Birch 2021 substrate is 0.5 mm natural latex, roughened with 000 wire wool, washed, and dried (DOI 10.3390/su13074030).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03: "Substrate (2025): cork (Quercus suber) identified as optimal — lightweight, bio-compatible."
No published cork + spore actuator dataset is in the verified brief. Literature substrates are latex, polyimide, silicon, and elastomer. Cork remains a DESIGN-PROPOSAL trial, not a literature baseline.

[PROJECT-CLAIM / UNVERIFIED] Discovery-03 (project file, not used as a citation) further specifies cork sheet 3-5 mm and a 2025 Tocco.Earth substrate screen. Those claims are outside the verified brief and are not treated as literature.

---

## 7. Culture / biosafety notes

[LITERATURE-CONFIRMED] Birch 2021: preferred working organism is wild-type Bacillus subtilis (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 spore stock: OD600 35-40, approximately 5-6 x 10^9 CFU/mL; 16.6 uL of that stock per monolayer per 1 cm x 2 cm strip (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 notes B. subtilis in a GRAS / BSL-1 context (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2015 used cotE gerE mutant spores for some HYDRA samples (DOI 10.1038/ncomms8346). Birch 2021 explicitly prefers wild-type when cycle resilience matters (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: B. thuringiensis spores are larger but give less dense packing and less repeatable actuation (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 states remaining gaps: longer-term real-environment studies, germination control for architectural durability, and broader substrates beyond latex (DOI 10.3390/su13074030).

Culture-media recipes (exact broth, sporulation salts, wash cycles) are not restated in the verified brief. Any media recipe written in the fabrication protocol is [DESIGN-PROPOSAL] unless taken from Birch/Chen methods sections by a later literature pass.

---

## 8. Fabrication methods in the literature (vs AI-CONTEXT)

[LITERATURE-CONFIRMED] Birch 2021 deposition: micropipette + gentle hand rocking. Not spin-coating. Air-dry at about 42% RH between layers. Room-temperature air-dry, not a 40 C oven bake (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 adhesion: 16.6 uL poly-L-lysine per 1 cm x 2 cm strip, air-dried at about 40% RH (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021 post-fab equilibration: 24 h at >95% RH before testing (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2015 fabrication: poly-L-lysine adhesion; spore-glue mixture; dry at about 40% RH for small samples, or about 90% RH for long wavy HYDRAs to prevent premature curvature; alternating-side patterning for linear actuation (DOI 10.1038/ncomms8346).

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03 fabrication:
1. Laser-cut cork substrate
2. Spin-coat spore suspension at concentration C
3. Dry at 40 C for 2 h per layer
4. Repeat n_layers times
5. Seal edges with parylene

Mismatches:
- Cork: no published cork+spore actuator data in this survey.
- Spin-coat: not the Birch 2021 or Chen 2015 method.
- "Dry at 40 C for 2 h": the literature number is ~40% RH (Chen 2015; Birch ~40-42% RH), not 40 C. This looks like a unit/quantity substitution (percent RH read as degrees C).
- Parylene edge seal: not confirmed in the surveyed papers.

---

## 9. Metrics table (paper + DOI)

Values are as stated in the verified brief. Blank cells mean the brief does not give that number for that paper.

| Metric | Value | Construct / notes | Paper | DOI | Tag |
|--------|-------|-------------------|-------|-----|-----|
| Energy density | >10 MJ m^-3 | B. subtilis spores; two orders above typical synthetic water-responsive materials | Chen 2014 | 10.1038/nnano.2013.290 | [LITERATURE-CONFIRMED] |
| Energy density, mutants | ~2x wild-type | mutations can approximately double energy density | Chen 2014 | 10.1038/nnano.2013.290 | [LITERATURE-CONFIRMED] |
| Monolayer form | dense, submicrometre-thick | on Si cantilevers and elastomer sheets | Chen 2014 | 10.1038/nnano.2013.290 | [LITERATURE-CONFIRMED] |
| Spore diameter change | ~12% | coat-mechanics figure used by Birch as contraction limit | Sahin 2012 / Birch 2021 | 10.3390/su13074030 (Birch use) | [LITERATURE-CONFIRMED] |
| Polyimide thickness | ~8 um | HYDRA substrate | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| Spore-layer thickness (HYDRA) | ~3 um | on polyimide | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| HYDRA length change | up to 4x | RH <30% to >80% | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| Moisture exchange | <5% by weight | HYDRA | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| HYDRA response time | ~3 s | RH step, polyimide strips | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| HYDRA cycle life | 1e6 cycles + 80 days; elongation reduced only slightly | polyimide; some cotE gerE | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| HYDRA lift | ~50x strip mass | polyimide HYDRA | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| HYDRA work density | ~17 J kg^-1 | strip | Chen 2015 | 10.1038/ncomms8346 | [LITERATURE-CONFIRMED] |
| Latex thickness | 0.5 mm | natural latex, E ~ 3.0 MPa | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Coupon size (Birch) | 1 cm x 2 cm | metrology strip | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| PLL volume | 16.6 uL / strip | poly-L-lysine, air-dry ~40% RH | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Spore stock | OD600 35-40 (~5-6e9 CFU/mL) | 16.6 uL per monolayer per strip | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Monolayer thickness (latex) | ~3 um densely packed | | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Deposition | pipette + hand rock; air-dry ~42% RH | not spin-coat; not 40 C | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Equilibration | 24 h at >95% RH | before testing | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Latex response time | max deflection <3 min | ~42% RH <-> >95% RH | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Layers tested | 1, 2, 3, 4 | not 5-21 | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| 1-layer result | insufficient force to deflect 0.5 mm latex (vertical, gravity) | | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Angle vs layers | linear-ish 1-3; plateau at 4 | spore-strain limit ~12% | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| theta_max | ~43 deg | 4 monolayers | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Force (Stoney) | up to 26.7 N/m | greatest monolayer count (4); linear force 2-4 | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Chen latex force (as cited by Birch) | ~16 N/m | similar RH | Birch 2021 citing Chen | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Latex lift | >=150% of actuator mass | 4 monolayers; paper loads | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Latex local cycles | 10 cycles, no performance loss | | Birch 2021 | 10.3390/su13074030 | [LITERATURE-CONFIRMED] |
| Spore concentration range (2024) | 4.2-33.2 uL cm^-2 | latex ~0.4 mm | Bioinspir. Biomim. 2024 | 10.1088/1748-3190/ad3a4d | [LITERATURE-CONFIRMED] |
| 2024 equilibration | 99% RH, 24 h | rocking shaker | Bioinspir. Biomim. 2024 | 10.1088/1748-3190/ad3a4d | [LITERATURE-CONFIRMED] |
| Cork + spore actuator | no published metric in this survey | | — | — | [PROJECT-CLAIM / UNVERIFIED] |
| "100% stable" at 1e6 cycles | not what Chen 2015 reports | polyimide HYDRA, slight elongation loss | AI-CONTEXT D03 vs Chen 2015 | 10.1038/ncomms8346 | [PROJECT-CLAIM / UNVERIFIED] |
| Spin-coat + 40 C / 2 h | not Birch, not Chen | likely 40% RH misread as 40 C | AI-CONTEXT D03 | — | [PROJECT-CLAIM / UNVERIFIED] |
| Parylene edge seal | not in surveyed papers | | AI-CONTEXT D03 | — | [PROJECT-CLAIM / UNVERIFIED] |
| Fibonacci n = 1,2,3,5,8,13,21 | not a published series | Birch = 1-4 only | AI-CONTEXT / AGENT-ROLES | — | [PROJECT-CLAIM / UNVERIFIED] |

---

## 10. Explicit call-outs: AI-CONTEXT.md overstated or substrate-mismatched numbers

These five items are listed in the verified brief as not literature-confirmed. Restated here with the literature correction.

### 10.1 Cork (Quercus suber) as optimal substrate (2025)

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03 names cork as the 2025 optimal substrate.

Correction: surveyed actuator substrates are silicon, elastomer, polyimide, and latex. No cork+spore actuator curve, force, or cycle number is in the brief. A cork trial is allowed only as a labelled DESIGN-PROPOSAL branch (see fabrication-protocol.md).

### 10.2 "100% stable" over 1,000,000 cycles

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03.

Correction: Chen 2015 (DOI 10.1038/ncomms8346) reports slight elongation reduction after 1e6 cycles on polyimide HYDRAs. Birch 2021 (DOI 10.3390/su13074030) measured 10 cycles on latex and cited Chen for long-cycle context. Neither paper supports "100% stable" on latex architectural bilayers.

### 10.3 Spin-coat spore suspension; dry at 40 C for 2 h per layer

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03.

Correction: Birch 2021 uses pipette + rock and air-dries at room temperature / ~42% RH (DOI 10.3390/su13074030). Chen 2015 dries at ~40% RH or ~90% RH depending on geometry (DOI 10.1038/ncomms8346). The project "40 C / 2 h" step is not a literature protocol and should be treated as a likely confusion of 40% RH with 40 C.

### 10.4 Parylene edge seal

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03.

Correction: not described in Chen 2014, Chen 2015, or Birch 2021 as surveyed. Optional only, and only in a separated DESIGN-PROPOSAL branch.

### 10.5 Monolayer count as an unbounded bending encoder / Fibonacci 21-layer stack

[PROJECT-CLAIM / UNVERIFIED] AI-CONTEXT.md D03 plus AGENT-ROLES Fibonacci set.

Correction: Birch 2021 saw angle plateau by ~4 monolayers while force still rose (DOI 10.3390/su13074030). Extending to n = 5, 8, 13, 21 is an experiment about force, cracking, and delamination, not a promise of larger theta_max.

---

## 11. Gaps for architecture

These are gaps, not discoveries.

1. Substrate gap. Architectural literature in this survey is latex (0.4-0.5 mm). Cork is untested as a spore actuator substrate. Silicon and polyimide are laboratory / HYDRA constructs, not facade sheets.
2. Layer-count gap. Published angle data stop at 4 monolayers. The useful programming range of n_layers on Birch-type latex is short. Force may still be programmable after angle saturates; that has not been mapped past 4 layers.
3. Cycle-life gap. 1e6-cycle data are polyimide HYDRA data with slight loss. Latex architectural coupons: 10 cycles. Real-environment, multi-month, germination-controlled durability is an explicit Birch gap.
4. Scale gap. Birch metrology coupons are 1 cm x 2 cm. Facade-scale panels, spatial gradients across many panels, and edge/seal durability are not demonstrated in the surveyed papers. Bioinspir. Biomim. 2024 reports architectural aperture prototypes; it does not replace a Fibonacci panel series.
5. Method gap. Project spin-coat / 40 C / parylene steps are not the published baseline. Using them silently would make results incomparable to Birch.
6. Organism gap. Wild-type vs cotE gerE is a real trade-off (stroke vs cycle resilience). Architectural work should default to wild-type unless a mutant series is declared.
7. Programming-mode gap. Literature already has two programming axes besides raw layer count: spore concentration (4.2-33.2 uL cm^-2) and etch / pattern direction (Bioinspir. Biomim. 2024). A spatial TFE gradient could in principle use those axes. That is a literature option, not a new discovery. It is not the Fibonacci n_layers experiment requested by ROLE 03.
8. Claim-hygiene gap. AI-CONTEXT D03 currently reads as if cork, 1e6-cycle 100% stability, spin-coat/40 C, parylene, and monotone theta_max(n) were established. They are not. Downstream agents (writer, critic, simulator) should take numbers from this survey, not from the D03 summary lines.

---

## 12. What this survey does not claim

- No panels have been fabricated or tested in this repository.
- No cork result is reported.
- No new energy-density, cycle-life, or angle number is introduced.
- theta_max(n) for n > 4 is unknown.
- Discovery-03 project numbers that are not in the verified brief (cork 3-5 mm, Tocco.Earth 2025 screen, 1-layer = 15-20 deg, 2-layer = 25-32 deg, active layer 0.5-2 mm, "viable for hundreds to thousands of years") are not adopted as literature.

---

## 13. Pointers

- Fabrication (7-panel Fibonacci protocol, literature vs proposal split): `agents/materials/fabrication-protocol.md`
- Next ROLE 03 task (not written in this pass): `agents/materials/test-protocol.md`
- Project D03 summary (contains unverified lines flagged above): `AI-CONTEXT.md` section D03
