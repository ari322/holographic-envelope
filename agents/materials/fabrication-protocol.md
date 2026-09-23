# Fabrication protocol — seven Fibonacci spore-panel coupons
# ROLE 03 — MATERIALS SCIENTIST
# Date: 2026-09-23
# Status: PROTOCOL ONLY. No panels have been built. No results are claimed.

Every step is tagged:
- [LITERATURE-CONFIRMED] = taken from published methods in the verified brief (Birch 2021 baseline; Chen 2014/2015 for monolayer physics and cycle-durability context).
- [DESIGN-PROPOSAL] = project choice not demonstrated in those papers.

Do not read untagged text as a completed experiment.

Citation keys (full references in spore-data-survey.md):
- Chen 2014, DOI 10.1038/nnano.2013.290
- Chen 2015, DOI 10.1038/ncomms8346
- Birch 2021, DOI 10.3390/su13074030
- Bioinspir. Biomim. 2024, DOI 10.1088/1748-3190/ad3a4d (secondary; concentration / shaker / 99% RH)

---

## 0. Purpose and scientific limits

ROLE 03 requires seven test panels with
```
n_layers in {1, 2, 3, 5, 8, 13, 21}
```
(Fibonacci series). This is a [DESIGN-PROPOSAL] experimental design. Birch 2021 measured only n = 1, 2, 3, 4 monolayers (DOI 10.3390/su13074030).

### Critical scientific note (must not be dropped)

[LITERATURE-CONFIRMED] Birch 2021: deflection angle increased with layer count from 1 to 3, then showed diminishing returns / plateau at 4 monolayers, attributed to the spore contraction limit of about 12%. Maximum angle was about 43 deg at 4 monolayers. Force (Stoney) still rose linearly from 2 to 4 monolayers, up to 26.7 N/m (DOI 10.3390/su13074030).

Therefore:
- n = 1, 2, 3 are attempts to reproduce Birch's published range (n = 1 is expected to be force-poor on 0.5 mm latex).
- n = 5, 8, 13, 21 are exploratory for force, cracking, and delamination. They are not guaranteed to produce larger theta_max.
- Expected diminishing returns: theta_max(n) is more likely to flatten than to keep climbing.
- Falsification: if theta_max(n) is flat for n >= 5 while force rises then plateaus, that confirms the spore-strain limit as the angle cap. If films crack, powder, or delaminate, that is a stack-integrity limit, not a programming gain.
- The Fibonacci set skips n = 4, which is Birch's plateau point. An optional n = 4 control coupon is listed in Section 12 so the published plateau is not missed. That control is [DESIGN-PROPOSAL].

[PROJECT context, not a result] AI-CONTEXT.md D03 writes theta_max = f(n_layers) as monotone increasing and names cork / spin-coat / 40 C / parylene. Those lines are not this protocol's baseline. See spore-data-survey.md.

---

## 1. Two tracks (do not mix)

```
TRACK A — LITERATURE BASELINE (build this first)
  Substrate: 0.5 mm natural latex
  Size:      1 cm x 2 cm coupons  [LITERATURE-CONFIRMED] Birch 2021
  Adhesion:  poly-L-lysine
  Deposit:   micropipette + gentle rocking
  Dry:       air-dry, room temperature, ~40-42% RH
  Equilibrate: 24 h at >95% RH
  Edge seal: none
  Organism:  wild-type B. subtilis

TRACK B — DESIGN-PROPOSAL BRANCHES (optional; physically separate; do not pool with Track A)
  B1. Larger architectural coupon (50 mm x 100 mm) on the same latex method
  B2. Optional cork (Quercus suber) substrate trial
  B3. Optional parylene edge seal
  B4. Optional n = 4 Birch-plateau control
```

Track A is the only track that can be compared to Birch 2021 without a substrate or method caveat. Track B results, if ever obtained, must be labelled DESIGN-PROPOSAL constructs.

Chen 2015 (polyimide HYDRA, ~3 s response, ~1e6 cycles with slight elongation loss, DOI 10.1038/ncomms8346) is context for monolayer thickness (~3 um) and cycle-durability language. It is not the architectural coupon recipe.

---

## 2. Panel set

### 2.1 Required Fibonacci series (both tracks use the same n list)

| Panel ID (Track A metrology) | n_layers | Role | Tag |
|------------------------------|----------|------|-----|
| HE-SP-LAT-M-n01 | 1 | Birch overlap; expect insufficient force on 0.5 mm latex | n=1 [LITERATURE-CONFIRMED] as a tested count; inclusion in this series [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n02 | 2 | Birch overlap | same |
| HE-SP-LAT-M-n03 | 3 | Birch overlap; last point before published plateau | same |
| HE-SP-LAT-M-n05 | 5 | first point past Birch's 4-layer plateau | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n08 | 8 | force / crack / delamination probe | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n13 | 13 | force / crack / delamination probe | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n21 | 21 | force / crack / delamination probe; highest stack risk | [DESIGN-PROPOSAL] |

[DESIGN-PROPOSAL] Build at least n_rep = 3 replicates per n_layers on Track A (21 metrology coupons). Single coupons cannot separate layer-count effects from coating defects.

### 2.2 Coupon sizes

| Class | Dimensions | Track | Tag |
|-------|------------|-------|-----|
| Metrology coupon | 10 mm x 20 mm (1 cm x 2 cm) | A | [LITERATURE-CONFIRMED] Birch 2021 |
| Architectural coupon | 50 mm x 100 mm (5 cm x 10 cm) | B1 | [DESIGN-PROPOSAL] 5x linear scale of Birch; first architectural size |
| Later facade mock-up | 150 mm x 300 mm | not in this protocol | [DESIGN-PROPOSAL] size appears in materials/selection-matrix.md and Discovery-03; too large for the first spore series |

Do not start at 150 mm x 300 mm. Scale only after Track A metrology coupons reproduce Birch's qualitative pattern (n=1 weak; angle rising to n=3; plateau near n=4 if the optional control is built).

### 2.3 Nominal stack thickness (order-of-magnitude only)

[LITERATURE-CONFIRMED] Densely packed monolayer ~3 um (Birch 2021; Chen 2015 spore layer ~3 um).

[DESIGN-PROPOSAL] If packing stays monolayer-like,
```
t_spore(n) ~ 3 um * n
```
so n=1 ~ 3 um, n=4 ~ 12 um, n=21 ~ 63 um. This is a packing estimate, not a measured stack. Multilayers may be less dense, cracked, or incompletely covering.

---

## 3. Materials and equipment

Temperatures and durations below are literature values where tagged; otherwise DESIGN-PROPOSAL placeholders.

### 3.1 Consumables

| Item | Specification | Temp / duration | Tag |
|------|---------------|-----------------|-----|
| Natural latex sheet | 0.5 mm; Young's modulus ~3.0 MPa (Birch) | store ambient, away from ozone/UV | [LITERATURE-CONFIRMED] Birch 2021 |
| Steel wire wool | grade 000 | used at room temperature | [LITERATURE-CONFIRMED] Birch 2021 |
| Wash water | deionized or distilled | room temperature | [DESIGN-PROPOSAL] Birch says washed; water grade not in brief |
| Poly-L-lysine | sterile solution as used by Birch / Chen | air-dry ~40% RH after pipetting | [LITERATURE-CONFIRMED] as adhesive class; exact catalogue concentration not in brief |
| Wild-type B. subtilis spore stock | OD600 35-40 (~5-6 x 10^9 CFU/mL) | handle at room temperature | [LITERATURE-CONFIRMED] Birch 2021 |
| Humidification water | sterile deionized | for >95% RH chamber | [DESIGN-PROPOSAL] |
| Disposable pipette tips | low-retention, sterile | — | [DESIGN-PROPOSAL] |
| Petri dishes / sealed boxes | for individual coupon drying | — | [DESIGN-PROPOSAL] |
| Labels + pencil or solvent-resistant marker | see Section 10 | — | [DESIGN-PROPOSAL] |
| Optional cork sheet (Track B2 only) | Quercus suber; start 1-2 mm experimental sheet, not 3-5 mm structural board | — | [DESIGN-PROPOSAL] no published cork+spore actuator spec |
| Optional parylene (Track B3 only) | type N or C, edge-only if used | vendor deposition cycle | [DESIGN-PROPOSAL] not in surveyed papers |

Do not use cotE gerE as the default architectural stock. [LITERATURE-CONFIRMED] Birch 2021 prefers wild-type for cycle resilience; cotE gerE expands more but lacks repeated-cycle resilience (DOI 10.3390/su13074030). [LITERATURE-CONFIRMED] Chen 2015 used cotE gerE for some HYDRA samples (DOI 10.1038/ncomms8346) — different construct.

### 3.2 Equipment

| Item | Setting | Tag |
|------|---------|-----|
| Micropipette | 16.6 uL per 1 cm x 2 cm face for PLL and for each spore monolayer | [LITERATURE-CONFIRMED] Birch 2021 volume |
| Humidity-controlled enclosure | two set-points: ~40-42% RH (coat/dry) and >95% RH (24 h equilibration) | [LITERATURE-CONFIRMED] Birch 2021 |
| Room / bench | air-dry at room temperature; do not oven-bake at 40 C | [LITERATURE-CONFIRMED] Birch air-dry; 40 C bake is a project mismatch |
| RH/T logger | place in both enclosures | [DESIGN-PROPOSAL] |
| Analytical balance | 0.1 mg or better, for mass and later lift tests | [DESIGN-PROPOSAL] |
| Optical microscope or USB scope | 10-50x, coverage / crack QC | [DESIGN-PROPOSAL] |
| Camera + scale / protractor | reserved for test-protocol.md | [DESIGN-PROPOSAL] |
| BSL-1 bench, autoclave or bleach waste path | see Section 13 | [LITERATURE-CONFIRMED] BSL-1 / GRAS context (Birch 2021); exact waste SOP [DESIGN-PROPOSAL] |
| Optional rocking shaker | low angle, gentle | [LITERATURE-CONFIRMED] as an alternative to hand rocking in Bioinspir. Biomim. 2024; Birch used hand rocking |
| Optional spin-coater | not used on Track A | [DESIGN-PROPOSAL] and not recommended; AI-CONTEXT spin-coat is unverified |
| Optional parylene coater | Track B3 only | [DESIGN-PROPOSAL] |

### 3.3 Target volumes

[LITERATURE-CONFIRMED] Birch 2021 on a 1 cm x 2 cm strip:
- 16.6 uL poly-L-lysine per strip
- 16.6 uL spore stock per monolayer per strip
- Areal dose = 16.6 uL / 2 cm^2 = 8.3 uL cm^-2

[LITERATURE-CONFIRMED] Bioinspir. Biomim. 2024 explored 4.2-33.2 uL cm^-2 on latex. Birch's 8.3 uL cm^-2 sits inside that window (DOI 10.1088/1748-3190/ad3a4d).

[DESIGN-PROPOSAL] Scale by area. Keep 8.3 uL cm^-2 unless a concentration series is declared.

```
A_metrology = 2 cm^2
V_A        = 16.6 uL per coating step

A_arch     = 50 mm x 100 mm = 50 cm^2
V_B1       = 8.3 uL cm^-2 * 50 cm^2 = 415 uL per coating step
```

[DESIGN-PROPOSAL] For n=21 Track A: 21 * 16.6 uL = 348.6 uL spore stock per coupon, plus 16.6 uL PLL. Budget stock from the n=21 replicates first; do not run out mid-series.

---

## 4. Spore culture outline

Exact broth, sporulation-salt, and wash recipes are not restated in the verified brief. Do not invent a Birch "official" medium.

### 4.1 Organism and stock target

1. [LITERATURE-CONFIRMED] Use wild-type Bacillus subtilis as the architectural default (Birch 2021, DOI 10.3390/su13074030).
2. [LITERATURE-CONFIRMED] Adjust the working spore stock to OD600 35-40, about 5-6 x 10^9 CFU/mL (Birch 2021).
3. [DESIGN-PROPOSAL] Obtain either a characterised wild-type spore stock from a collaborating lab that already reproduces Birch/Chen methods, or prepare spores in-house using that lab's written SOP. Record strain ID, lot, and OD600.
4. [DESIGN-PROPOSAL] If preparing in-house: grow vegetative cells, induce sporulation, wash until the pellet is free of obvious vegetative debris, and confirm spores by phase-contrast before concentrating to the OD600 target. Do not treat this outline as a complete microbiology SOP.
5. [DESIGN-PROPOSAL] Optional QC: a short heat treatment to reduce vegetative survivors. Time/temperature not in the brief; record whatever SOP is used and do not back-attribute it to Birch.
6. [LITERATURE-CONFIRMED] Do not substitute B. thuringiensis as a silent default (larger spores, less dense packing, less repeatable; Birch 2021).
7. [LITERATURE-CONFIRMED] Do not substitute cotE gerE as a silent default if the goal is cycle resilience (Birch 2021). A mutant series, if run, must be labelled and kept separate.

### 4.2 Storage

8. [DESIGN-PROPOSAL] Store concentrated stock refrigerated; mix gently immediately before each deposition so OD600 stays representative. Do not freeze-thaw unless the source SOP says so.
9. [DESIGN-PROPOSAL] Re-measure OD600 on each fabrication day. If OD600 drifts outside 35-40, dilute or concentrate before coating.

---

## 5. Track A — substrate preparation (latex, Birch)

Work at room temperature unless a step says otherwise.

10. [LITERATURE-CONFIRMED] Cut 0.5 mm natural latex into 1 cm x 2 cm strips (Birch 2021).
11. [DESIGN-PROPOSAL] Cut with a steel rule and fresh blade or a clean punch so edges are square. Laser-cutting latex is not in Birch; if tried, it is a method change and must be labelled.
12. [LITERATURE-CONFIRMED] Roughen the coating face with 000 wire wool (Birch 2021).
13. [DESIGN-PROPOSAL] Roughen with light, unidirectional strokes until the gloss breaks; do not tear through the sheet. Keep the back face unmarked so curvature later has a clear active side.
14. [LITERATURE-CONFIRMED] Wash and dry the roughened strips (Birch 2021).
15. [DESIGN-PROPOSAL] Wash in deionized water until wool grit is gone; blot; air-dry at room temperature at ~40-42% RH until mass is stable (suggest 1 h, not a literature duration).
16. [DESIGN-PROPOSAL] Weigh each bare strip (m0). Photograph both faces against a scale bar.
17. [DESIGN-PROPOSAL] Reject strips with pinholes, tears, or tapered thickness.

---

## 6. Track A — adhesion (poly-L-lysine)

18. [LITERATURE-CONFIRMED] Apply 16.6 uL poly-L-lysine per 1 cm x 2 cm strip (Birch 2021).
19. [LITERATURE-CONFIRMED] Spread by gentle rocking so the face is wetted, then air-dry at about 40% RH (Birch 2021).
20. [DESIGN-PROPOSAL] Typical dry-down: leave until the film is not mobile (suggest 30-60 min at RT / ~40% RH). Do not use a 40 C oven. Chen 2015's ~40% RH is humidity, not temperature (DOI 10.1038/ncomms8346).
21. [DESIGN-PROPOSAL] Inspect for dry spots or puddles. Re-coat only if the face is clearly incomplete; record the extra volume.
22. [DESIGN-PROPOSAL] Weigh after PLL dry-down (m_PLL) as an optional QC.

Chen 2015 also uses poly-L-lysine, then a spore-glue mixture, and dries small samples at ~40% RH or long wavy HYDRAs at ~90% RH to prevent premature curvature (DOI 10.1038/ncomms8346). [LITERATURE-CONFIRMED] as Chen's method. [DESIGN-PROPOSAL] if a glue mixture is substituted for Birch's aqueous spore stock — do not substitute on Track A.

---

## 7. Track A — spore deposition, layer by layer

This is the Birch monolayer physics path, not the AI-CONTEXT spin-coat path.

23. [LITERATURE-CONFIRMED] Deposit 16.6 uL of OD600 35-40 spore stock per monolayer per 1 cm x 2 cm strip (Birch 2021).
24. [LITERATURE-CONFIRMED] Use a micropipette and gentle hand rocking to spread a continuous film (Birch 2021). Not spin-coating.
25. [DESIGN-PROPOSAL] Rock immediately after pipetting; avoid droplets that dry as coffee rings. One slow long-axis rock cycle is enough; do not foam the suspension.
26. [LITERATURE-CONFIRMED] Air-dry at about 42% RH between layers, at ambient (room-temperature) conditions (Birch 2021).
27. [DESIGN-PROPOSAL] Do not bake at 40 C for 2 h. That AI-CONTEXT step is not Birch and not Chen. If a timed dry is needed for lab scheduling, use room temperature / ~42% RH until the film is matte and immobile (suggest 30-90 min; record actual time).
28. [DESIGN-PROPOSAL] After each dried layer: visual QC (coverage, cracks, flakes) and a photograph. Optional microscope field at mid-span and both ends.
29. [DESIGN-PROPOSAL] Optional mass QC after each layer (m_n). A layer that adds no mass is a missed coat.
30. [DESIGN-PROPOSAL] If a layer cracks or delaminates, stop stacking that coupon. Keep it as a failure specimen. Do not "repair" by flooding extra stock — that changes areal dose.
31. Repeat steps 23-30 until the coupon's assigned n_layers is reached.
32. [DESIGN-PROPOSAL] For n = 8, 13, 21, inspect more often (every layer, not every other). Stack failure is the result of interest, not a nuisance.

[LITERATURE-CONFIRMED] Chen 2014: spores can self-assemble into dense submicrometre-thick monolayers on silicon and elastomer (DOI 10.1038/nnano.2013.290). [LITERATURE-CONFIRMED] Birch/Chen 2015: densely packed working coats on latex/polyimide are ~3 um per layer. High-n stacks are not assumed to remain perfect monolayers.

---

## 8. Track A — equilibration (mandatory before any test)

33. [LITERATURE-CONFIRMED] After the last layer is dry, equilibrate 24 h at >95% RH before testing (Birch 2021, DOI 10.3390/su13074030).
34. [LITERATURE-CONFIRMED] Bioinspir. Biomim. 2024 used 99% RH for 24 h (DOI 10.1088/1748-3190/ad3a4d). Either >95% (Birch) or 99% (2024) is a literature-class wet equilibration; record the actual RH.
35. [DESIGN-PROPOSAL] Rest coupons flat, coated face up, in a closed box over water or a saturated-salt / fog system that holds >95% RH. Do not drip liquid water onto the spore face.
36. [DESIGN-PROPOSAL] Log RH and temperature for the full 24 h. If RH drops below 95% for more than a brief door-open, restart the 24 h clock.
37. [LITERATURE-CONFIRMED] Birch then tested reversible switching between ~42% RH and >95% RH, with max deflection in <3 min and no direction hysteresis (DOI 10.3390/su13074030). Those measurements belong in test-protocol.md, not here.

---

## 9. Edge sealing

### 9.1 Track A (literature baseline)

38. [LITERATURE-CONFIRMED] Birch 2021 does not describe an edge seal. Track A coupons are left unsealed.

### 9.2 Track B3 — optional parylene (DESIGN-PROPOSAL only)

This subsection is not part of the Birch protocol. Do not describe Track A coupons as parylene-sealed.

39. [DESIGN-PROPOSAL] If an edge-seal trial is run, use a separate coupon set (IDs HE-SP-LAT-M-nXX-PAR). Never parylene the only replicate of a given n.
40. [DESIGN-PROPOSAL] Mask the active face. Deposit parylene on edges (and optionally the back face) only. A full-face parylene coat would block water exchange and kill the actuator.
41. [DESIGN-PROPOSAL] Record polymer type, thickness target, and whether the mask held. Compare sealed vs unsealed siblings in test-protocol.md.
42. [DESIGN-PROPOSAL] Parylene is a project idea from AI-CONTEXT.md D03. It is not literature-confirmed for spore hygromorphs in this survey.

---

## 10. Panel labeling

43. [DESIGN-PROPOSAL] Write the ID on the uncoated back face before PLL, or on a tag that does not stiffen the strip.

ID pattern:
```
HE-SP-<SUB>-<CLASS>-n<NN>[-rep<R>][-PAR][-n04]

SUB   = LAT (latex) | CRK (cork, Track B2 only)
CLASS = M (1 cm x 2 cm metrology) | A (50 mm x 100 mm architectural)
NN    = 01, 02, 03, 05, 08, 13, 21  (and 04 if optional control)
R     = 1, 2, 3, ...
PAR   = parylene edge-seal sibling only
```

Examples:
- HE-SP-LAT-M-n03-rep2 = latex metrology, 3 layers, replicate 2 (Track A)
- HE-SP-LAT-A-n08-rep1 = latex architectural 50 x 100 mm, 8 layers (Track B1)
- HE-SP-CRK-M-n05-rep1 = cork metrology trial (Track B2)
- HE-SP-LAT-M-n05-rep3-PAR = latex metrology, 5 layers, parylene edge (Track B3)

44. [DESIGN-PROPOSAL] Traveler card per coupon: strain, OD600, date/time of each layer, RH/T during dry-down, defects, mass m0..mn, operator.

---

## 11. QC checkpoints

Stop/fail rules are [DESIGN-PROPOSAL] unless noted.

| Gate | When | Pass | Fail / action | Tag |
|------|------|------|---------------|-----|
| Q0 strain | before coating | wild-type B. subtilis, OD600 35-40 | do not coat | target [LITERATURE-CONFIRMED]; gate [DESIGN-PROPOSAL] |
| Q1 substrate | after cut/roughen/wash | 10 x 20 mm; 0.5 mm latex; no tears | scrap | size/material [LITERATURE-CONFIRMED]; gate [DESIGN-PROPOSAL] |
| Q2 PLL | after PLL dry | continuous wet-out, no bare patches | re-coat once or scrap | [DESIGN-PROPOSAL] |
| Q3 layer k | after each spore dry-down | face covered; no mud-cracks / flakes | freeze coupon as failure specimen | [DESIGN-PROPOSAL] |
| Q4 high-n | n >= 8, every layer | same as Q3 plus edge lift check | expected failure mode; keep specimen | [DESIGN-PROPOSAL] |
| Q5 equilibrate | after 24 h | RH log >= 95% for 24 h | restart 24 h | RH/time [LITERATURE-CONFIRMED]; gate [DESIGN-PROPOSAL] |
| Q6 identity | before storage | ID matches traveler; photos filed | do not test | [DESIGN-PROPOSAL] |

[LITERATURE-CONFIRMED] Interpretation context, not a QC number: Birch found n=1 too weak to deflect 0.5 mm latex against gravity, and angle plateau at n=4 with force still rising (DOI 10.3390/su13074030). A Track A n=1 coupon that does not lift the strip is consistent with literature, not an automatic process failure.

---

## 12. Optional DESIGN-PROPOSAL add-ons (kept off Track A)

### 12.1 Optional n = 4 Birch-plateau control

45. [DESIGN-PROPOSAL] Fabricate HE-SP-LAT-M-n04 replicates with the same Track A method. Purpose: recover Birch's published angle plateau (~43 deg, force still rising) before interpreting n=5..21. The required Fibonacci seven do not include 4.

### 12.2 Track B1 — architectural latex coupon (50 mm x 100 mm)

46. [DESIGN-PROPOSAL] Cut 50 mm x 100 mm from the same 0.5 mm latex. Roughen, wash, PLL, pipette+rock, RT / ~42% RH dry, 24 h / >95% RH — same chemistry as Track A.
47. [DESIGN-PROPOSAL] Use V_B1 = 415 uL per coating step (Section 3.3). Spreading 415 uL uniformly by hand-rock is harder than 16.6 uL; a gentle rocking shaker (Bioinspir. Biomim. 2024 class of method) is allowed on B1 if recorded.
48. [DESIGN-PROPOSAL] Expect more warping during dry-down. Chen 2015 used ~90% RH drying for long wavy HYDRAs to prevent premature curvature (DOI 10.1038/ncomms8346). If B1 coupons curl while coating, a high-RH dry-down is a Chen-class option, but it is a method change relative to Birch's ~42% RH inter-layer dry and must be labelled.
49. [DESIGN-PROPOSAL] Do not claim B1 is a facade panel. It is a larger coupon.

### 12.3 Track B2 — optional cork substrate trial

No published cork + spore actuator protocol is in the verified brief. This entire subsection is [DESIGN-PROPOSAL].

50. [DESIGN-PROPOSAL] If cork is tried, run it as a parallel series (HE-SP-CRK-...), never as a replacement for Track A latex.
51. [DESIGN-PROPOSAL] Start with 1 cm x 2 cm cork coupons so the only changed variable is the substrate. Suggested first thickness: 1-2 mm experimental sheet. AI-CONTEXT / Discovery-03 3-5 mm cork is unverified and is likely too stiff for a 3 um-class coat to bend.
52. [DESIGN-PROPOSAL] Do not assume poly-L-lysine + pipette+rock transfers. Cork is porous; dose may sink. Record whether the face stays a surface film or disappears into pores.
53. [DESIGN-PROPOSAL] Same n_layers list only if adhesion actually holds through n=1 and n=2. Otherwise stop and document failure. That is a valid result.
54. [DESIGN-PROPOSAL] Do not call cork "optimal" in any notebook line. That word in AI-CONTEXT.md is unverified.

### 12.4 Track B3 — optional parylene

See Section 9.2. Repeat: not Birch, not Chen in this survey.

### 12.5 Methods that this protocol rejects for Track A

55. [DESIGN-PROPOSAL] Rejected as Track A defaults (AI-CONTEXT D03 mismatches; see survey Section 10):
    - spin-coating the spore suspension
    - drying at 40 C for 2 h per layer
    - treating 40% RH as 40 C
    - parylene on the only replicate
    - cork as the only substrate
    - cotE gerE or B. thuringiensis as an undeclared swap

---

## 13. Safety

56. [LITERATURE-CONFIRMED] Birch 2021 places B. subtilis in a GRAS / BSL-1 context (DOI 10.3390/su13074030). This is not a licence to skip local biosafety review.
57. [DESIGN-PROPOSAL] Work under the host lab's BSL-1 SOP: no mouth pipetting, no aerosols, no spin-coater on open spore stock, gloves and eye protection, bench disinfection.
58. [DESIGN-PROPOSAL] Autoclave or freshly diluted bleach for contaminated tips, leftover stock, and failed coupons, per local rules.
59. [DESIGN-PROPOSAL] Latex allergy: 0.5 mm natural latex is the Birch substrate. Offer nitrile gloves and a non-latex handling path. Do not switch the coupon material to synthetic "latex-like" film without creating a new series.
60. [DESIGN-PROPOSAL] Poly-L-lysine: follow the supplier SDS.
61. [DESIGN-PROPOSAL] Wire wool: eye protection; keep grit out of the spore stock.
62. [DESIGN-PROPOSAL] Architectural implication, not a lab SOP: Birch lists germination control and real-environment durability as open gaps. Do not install living or dormant spore coupons on a building in this protocol.

---

## 14. What is deliberately not in this document

- No claim that any coupon exists.
- No theta_max, force, or cycle-life result.
- No humidity-chamber measurement procedure (next ROLE 03 file: test-protocol.md).
- No alternative non-spore actuators (later ROLE 03 file: alternatives.md).
- No Octopus-system content.

---

## 15. Work order (when someone later executes this)

Suggested sequence, still a protocol, not a log:

1. Lock strain and OD600 (Section 4).
2. Cut and QC Track A latex metrology set, n_rep = 3, n = 1,2,3,5,8,13,21 (plus optional n=4).
3. PLL and spore stacks, lowest n first so early failures do not waste high-n stock.
4. 24 h / >95% RH equilibration.
5. Only then consider Track B1 (50 x 100 mm), B2 (cork), B3 (parylene).
6. Hand coupons to the test protocol. Do not interpret theta_max(n) until that protocol exists.

If execution never happens, this file remains a protocol.
