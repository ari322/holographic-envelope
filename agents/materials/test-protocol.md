# Humidity-chamber test protocol — theta_max vs n_layers
# ROLE 03 — MATERIALS SCIENTIST
# Date: 2026-09-23
# Status: PROTOCOL ONLY. No coupons have been tested. No panels exist.
# Coupons, if later built, come from agents/materials/fabrication-protocol.md.

Every procedural step is tagged:
- [LITERATURE-CONFIRMED] = published test element from the verified brief
  (Birch 2021 baseline on 0.5 mm latex; Chen 2014/2015 and Bioinspir. Biomim. 2024
  only where the brief supports the fact).
- [DESIGN-PROPOSAL] = project metrology choice not demonstrated in those papers.

Do not read untagged headings as a completed experiment.
Do not treat this file as a lab notebook. No measurement is claimed.

Citation keys (full references in spore-data-survey.md):
- Chen 2014, DOI 10.1038/nnano.2013.290
- Chen 2015, DOI 10.1038/ncomms8346
- Birch 2021, DOI 10.3390/su13074030
- Bioinspir. Biomim. 2024, DOI 10.1088/1748-3190/ad3a4d (secondary; 99% RH / 24 h)

Plain ASCII math.

---

## 0. Purpose and scientific limits

ROLE 03 task 3: specify a humidity-chamber protocol that measures
```
theta_max  vs  n_layers
```
for the fabrication-protocol.md coupon set
```
n_layers in {1, 2, 3, 5, 8, 13, 21}
```
plus the optional n = 4 Birch-plateau control.

[LITERATURE-CONFIRMED] Birch 2021 is the architectural-coupon baseline: 0.5 mm
natural latex (E ~ 3.0 MPa), 1 cm x 2 cm strips, 1-4 monolayers, 24 h
equilibration at >95% RH, switching ~42% RH <-> >95% RH, maximum deflection
in <3 min, reversible bending with no direction hysteresis, angle via
tracing / protractor, force via Stoney from radius of curvature (N/m),
paper-load lift on 4-layer actuators, and a local cycle check of at least
10 hydration/dehydration cycles (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch 2021: deflection angle increased from 1 to 3
monolayers, then showed diminishing returns / plateau at 4 monolayers
(~43 deg), attributed to the spore contraction limit of about 12%. Force
(Stoney) still rose linearly from 2 to 4 monolayers, up to 26.7 N/m.
n = 1 was insufficient to deflect 0.5 mm latex against gravity
(DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Chen 2015 HYDRA strips on ~8 um polyimide respond in
about 3 s and, after 1,000,000 humidity cycles and 80 days, showed elongation
reduced only slightly (DOI 10.1038/ncomms8346). That is context for thin-film
HYDRAs. It is not a latex-coupon specification.

### Hard limits on what this protocol may claim later

- Do not assign Chen 2015's ~3 s response to 0.5 mm latex coupons.
- Do not assign Chen 2015's 1e6-cycle result to latex (or cork) coupons.
- Do not claim "100% stable" cycle life (Chen 2015 does not say that).
- Do not treat n = 5, 8, 13, 21 as a published series. Birch stopped at 4.
- Do not treat cork, 50 mm x 100 mm architectural coupons, ImageJ, or
  crack-scoring rubrics as literature methods. They are DESIGN-PROPOSAL
  branches and run only if those coupons actually exist.
- This file does not report theta_max, force, lift, or cycle numbers.

---

## 1. What is tested (and what is not)

### 1.1 Required series (Track A metrology)

[DESIGN-PROPOSAL] Test the seven Fibonacci coupons specified in
fabrication-protocol.md Section 2.1, IDs HE-SP-LAT-M-n01 .. n21, at least
n_rep = 3 replicates per n_layers when those coupons exist.

| Coupon ID | n_layers | Literature overlap | Tag |
|-----------|----------|--------------------|-----|
| HE-SP-LAT-M-n01 | 1 | Birch tested n=1 (force-poor vs gravity) | n=1 as a tested count [LITERATURE-CONFIRMED]; inclusion in this series [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n02 | 2 | Birch overlap | same |
| HE-SP-LAT-M-n03 | 3 | Birch overlap; last point before published plateau | same |
| HE-SP-LAT-M-n05 | 5 | first point past Birch n=4 plateau | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n08 | 8 | force / crack / delamination probe | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n13 | 13 | force / crack / delamination probe | [DESIGN-PROPOSAL] |
| HE-SP-LAT-M-n21 | 21 | highest stack-integrity risk | [DESIGN-PROPOSAL] |

[DESIGN-PROPOSAL] Optional Birch-plateau control HE-SP-LAT-M-n04 (fabrication-
protocol.md Section 12.1). Strongly recommended: the required Fibonacci set
skips the published plateau point.

### 1.2 Tracks that this protocol may receive

```
TRACK A  — 1 cm x 2 cm, 0.5 mm latex, Birch method
           ONLY track that can be compared to Birch 2021 without a caveat

TRACK B1 — 50 mm x 100 mm latex architectural coupon
           run Section 12 only if those coupons exist

TRACK B2 — cork (Quercus suber) trial
           run Section 13 only if those coupons exist

TRACK B3 — parylene-edge siblings (HE-SP-...-PAR)
           compare sealed vs unsealed siblings if both exist; do not
           treat sealed coupons as the Birch baseline
```

[LITERATURE-CONFIRMED] Track A size, substrate, and RH window match Birch 2021
(DOI 10.3390/su13074030). [DESIGN-PROPOSAL] Tracks B1-B3 and the Fibonacci
extension past n=4.

### 1.3 Prerequisite

1. [LITERATURE-CONFIRMED] Coupons must already have completed the 24 h
   equilibration at >95% RH required by Birch 2021 after the last dried layer
   (DOI 10.3390/su13074030). Fabrication-protocol.md Section 8 owns that step.
2. [DESIGN-PROPOSAL] Do not start this protocol on a coupon that failed
   fabrication-protocol.md QC gates Q0-Q6, except as a documented
   non-actuating failure specimen (crack score only; no theta_max claim).
3. [DESIGN-PROPOSAL] If no coupon exists, stop. This file remains a protocol.

---

## 2. Equipment

Temperatures, RH set-points, and timed responses below are literature values
where tagged; hardware brands and fixture details are DESIGN-PROPOSAL.

### 2.1 Humidity environments

| Item | Set-point / use | Tag |
|------|-----------------|-----|
| Wet enclosure | >95% RH (Birch); 99% RH is also a literature-class wet hold (Bioinspir. Biomim. 2024) | set-point [LITERATURE-CONFIRMED]; box hardware [DESIGN-PROPOSAL] |
| Dry enclosure | ~42% RH | set-point [LITERATURE-CONFIRMED] Birch 2021; how the set-point is made [DESIGN-PROPOSAL] |
| Transfer path | move coupon between wet and dry enclosures (or switch one chamber) | switching ~42% <-> >95% [LITERATURE-CONFIRMED]; transfer method [DESIGN-PROPOSAL] |
| RH/T logger | one logger in each enclosure, logging through equilibration and every cycle | [DESIGN-PROPOSAL] |
| Timer | readable to 1 s | [DESIGN-PROPOSAL] |

4. [LITERATURE-CONFIRMED] The two literature RH set-points for latex testing
   are ~42% RH and >95% RH (Birch 2021, DOI 10.3390/su13074030).
5. [LITERATURE-CONFIRMED] Bioinspir. Biomim. 2024 used 99% RH for a 24 h
   equilibration (DOI 10.1088/1748-3190/ad3a4d). Either >95% or 99% is a
   literature-class wet condition; record the actual RH.
6. [DESIGN-PROPOSAL] Achieve >95% RH with a closed box over liquid water (or
   a fog / humidifier system) that does not drip onto the spore face.
7. [DESIGN-PROPOSAL] Achieve ~42% RH with a second closed box held at that
   set-point (conditioned room, dry-air bleed, or a saturated-salt system).
   Do not invent a Birch "official" salt. Record the method and the logged RH.
8. [DESIGN-PROPOSAL] Do not use a single open bench and guess the RH. If the
   laboratory ambient happens to sit at ~42% RH and is logged as such, that
   ambient may serve as the dry set-point.
9. [DESIGN-PROPOSAL] Reject a session if either logger is off, uncalibrated,
   or shows the "wet" box below 95% RH except for brief door-open transients.

### 2.2 Angle and curvature

| Item | Use | Tag |
|------|-----|-----|
| Graph paper / tracing paper | Birch-class curvature trace | [LITERATURE-CONFIRMED] Birch traced curvature |
| Flexicurve or equivalent spline | hold the side-view profile for tracing | [LITERATURE-CONFIRMED] as a Birch-class tool family (flexicurve / trace) |
| Protractor | read the bend angle from the trace or from the coupon edge | [LITERATURE-CONFIRMED] Birch 2021 angle method family |
| Straight-edge / scale bar | length L, sagitta, photograph scale | [DESIGN-PROPOSAL] |
| Clamp fixture | hold one short edge; free length documented | [DESIGN-PROPOSAL] fixture; Birch vertical-vs-gravity context [LITERATURE-CONFIRMED] |
| Camera (optional) | side-view stills / short video for ImageJ | [DESIGN-PROPOSAL] modernisation |
| ImageJ or equivalent (optional) | digital angle / radius | [DESIGN-PROPOSAL] |

### 2.3 Force, lift, and damage scoring

| Item | Use | Tag |
|------|-----|-----|
| Measured radius of curvature | input to Stoney force per unit width (N/m) | method class [LITERATURE-CONFIRMED] Birch 2021 |
| E_s, t_s of the substrate | Birch latex: E_s ~ 3.0 MPa, t_s = 0.5 mm | [LITERATURE-CONFIRMED] Birch 2021 |
| Analytical balance | coupon mass; paper-load masses | [DESIGN-PROPOSAL] |
| Paper loads | known-mass slips placed on the free arm | lift class [LITERATURE-CONFIRMED] Birch 2021; exact slips [DESIGN-PROPOSAL] |
| Optical / USB microscope | crack and delamination scoring, especially n >= 5 | [DESIGN-PROPOSAL] |
| Traveler cards from fabrication-protocol.md | ID, n_layers, defects, masses | [DESIGN-PROPOSAL] |

10. [DESIGN-PROPOSAL] Do not introduce a load cell as the primary Birch-class
    force number. Birch reported Stoney force from curvature. A load cell, if
    used later, is an extra DESIGN-PROPOSAL channel and must not replace the
    Stoney column.

### 2.4 What this bench is not

11. [LITERATURE-CONFIRMED] Chen 2015 HYDRA metrology (polyimide tape, ~3 s
    stroke, 1e6-cycle endurance) is a different construct (DOI 10.1038/ncomms8346).
    Do not borrow HYDRA fixtures or HYDRA cycle counts for Track A latex.
12. [DESIGN-PROPOSAL] No spin-coater, no 40 C oven, no parylene coater on the
    Track A measurement path. Those are fabrication mismatches, not test tools.

---

## 3. Definitions (report all four, do not collapse them)

Angle convention must be written down before the first coupon is mounted.
Birch reports a maximum deflection of about 43 deg at 4 monolayers but the
verified brief does not freeze a unique geometric definition. Choose one
convention and keep it for the whole series.

13. [DESIGN-PROPOSAL] Fixture datum: 0 deg = the clamped tangent (the
    uncoated / as-mounted strip axis). Positive theta is bending toward the
    coated face.
14. [DESIGN-PROPOSAL] theta(RH) = included angle between the fixture datum
    and the free-end tangent, in degrees. Record the alternative chord-angle
    if a coupon is so curled that a tangent is ambiguous, and say so.
15. [DESIGN-PROPOSAL] Stroke:
    ```
    Delta_theta(n) = |theta_wet(n) - theta_dry(n)|
    ```
    with wet = logged RH >95% (or 99%) and dry = logged RH ~42%.
16. [DESIGN-PROPOSAL] Peak absolute angle used as the Birch-comparable
    "max deflection" column:
    ```
    theta_max(n) = max( |theta_wet(n)|, |theta_dry(n)| )
    ```
    relative to the fixture datum. Report both theta_max and Delta_theta.
    Do not silently swap them.
17. [LITERATURE-CONFIRMED] No direction hysteresis means the same angle at
    the same RH on the hydrate path and the dehydrate path (Birch 2021,
    DOI 10.3390/su13074030). Operational check:
    ```
    |theta_hydrate(RH) - theta_dehydrate(RH)|  <=  theta_repeat
    ```
    [DESIGN-PROPOSAL] theta_repeat = 2 deg as a first recording threshold
    (not a Birch number). If the gap exceeds that, flag hysteresis; do not
    "correct" the angle.

---

## 4. Mounting and orientation

18. [LITERATURE-CONFIRMED] Birch 2021 assessed vertical deflection against
    gravity; n = 1 did not supply enough force to deflect 0.5 mm latex in
    that orientation (DOI 10.3390/su13074030). Track A primary orientation
    is therefore vertical (free end hanging or standing, gravity along the
    long axis).
19. [DESIGN-PROPOSAL] Clamp one 10 mm short edge. Free length L is the
    unclamped 20 mm minus any grip overlap. Record L in mm for every coupon.
    Typical target: L = 15-18 mm if 2-5 mm is in the clamp. Do not treat
    those millimetres as a Birch specification.
20. [DESIGN-PROPOSAL] Coated face orientation: keep it consistent across the
    series (recommend coated face on the side that Birch-style contraction
    will curl toward the camera). Photograph the ID on the back face.
21. [DESIGN-PROPOSAL] A horizontal (gravity-neutral) repeat is allowed as a
    secondary series, labelled as such. It is not the Birch gravity test.
    Use it only after the vertical series, and never pool the two.
22. [DESIGN-PROPOSAL] Reject a mount that twists the strip or covers the
    spore face with the clamp.

---

## 5. RH set-points and dwell times

### 5.1 Pre-test equilibration (mandatory)

23. [LITERATURE-CONFIRMED] Before the first measurement, the coupon has
    already spent 24 h at >95% RH (Birch 2021, DOI 10.3390/su13074030).
24. [LITERATURE-CONFIRMED] Bioinspir. Biomim. 2024: 99% RH for 24 h is an
    acceptable literature-class alternative wet hold (DOI 10.1088/1748-3190/ad3a4d).
25. [DESIGN-PROPOSAL] If the coupon left the wet box for more than a brief
    transfer before mounting, return it to >95% RH for at least 30 min and
    log that recovery. A full 24 h restart is required if the wet logger
    dropped below 95% RH for more than a door-open transient (same rule as
    fabrication-protocol.md Q5).
26. [DESIGN-PROPOSAL] First photograph and first theta reading are taken
    in the wet state, still at >95% RH (or 99% RH), immediately after
    mounting. That is t = 0 for cycle 1, hydrate-end / wet hold.

### 5.2 Switching ~42% RH <-> >95% RH

27. [LITERATURE-CONFIRMED] The actuation stimulus is a switch between
    ~42% RH and >95% RH (Birch 2021, DOI 10.3390/su13074030).
28. [LITERATURE-CONFIRMED] On 0.5 mm latex, Birch reports maximum deflection
    in <3 min after that switch (DOI 10.3390/su13074030).
29. [LITERATURE-CONFIRMED] Chen 2015 ~3 s is the polyimide HYDRA response
    (DOI 10.1038/ncomms8346). Cite it only as context. Do not use 3 s as
    the latex dwell, and do not fail a latex coupon for not moving in 3 s.
30. [DESIGN-PROPOSAL] Observation window per switch: 3 min minimum (Birch
    upper bound on time-to-max). Keep the coupon at the new RH for a total
    dwell of 5 min so a late creep, if any, is visible. The extra 2 min is
    not a Birch number.
31. [DESIGN-PROPOSAL] Suggested time samples after each switch (t = 0 is
    the instant the coupon is in the new RH environment):
    ```
    t = 0, 15 s, 30 s, 60 s, 90 s, 120 s, 180 s, 300 s
    ```
    theta_max for that half-cycle is the plateau value in this window, not
    a single snapshot at an arbitrary time.
32. [DESIGN-PROPOSAL] Do not use the 10 min / 90% RH recipe in
    validation/falsification-protocol.md D03 as the Track A method. That
    project line is substrate-mismatched (cork) and is not Birch 2021.
33. [DESIGN-PROPOSAL] Record enclosure air temperature. Birch's published
    latex times are not a licence to ignore T. If T changes by more than
    about 3 C between wet and dry boxes, flag the session; do not invent
    a Birch temperature correction.

### 5.3 One RH cycle (definition)

34. [LITERATURE-CONFIRMED] A local cycle is one hydration plus one
    dehydration between the two literature set-points (Birch 2021).
35. [DESIGN-PROPOSAL] Standard cycle used in this protocol:
    ```
    wet hold  (>95% RH, already true at start of cycle 1)
      -> switch to ~42% RH, dwell Section 5.2
      -> switch to >95% RH, dwell Section 5.2
    ```
    That closed loop is cycle k. Reverse the order only if the coupon was
    last parked dry, and label the starting direction.
36. [DESIGN-PROPOSAL] Transfer time between boxes counts as part of t = 0
    setup, not as extra dwell. Target transfer < 15 s. If transfer exceeds
    30 s, void that half-cycle and repeat it.

---

## 6. Angle measurement method

Primary method is Birch-class tracing / protractor. Camera + ImageJ is an
optional modernisation and does not replace the hand measurement on Track A.

### 6.1 Birch-class hand method (required on Track A)

37. [LITERATURE-CONFIRMED] Measure bend angle with a protractor / graph-paper
    / flexicurve family method; Birch traced curvature (DOI 10.3390/su13074030).
38. [DESIGN-PROPOSAL] At each listed time sample (or at minimum at t = 180 s
    and t = 300 s):
    a. Align a flexicurve or transparent overlay to the coupon side profile.
    b. Transfer the profile onto graph paper, including the clamp datum.
    c. Draw the fixture tangent and the free-end tangent.
    d. Read theta with a protractor to the nearest 1 deg (0.5 deg if the
       tool allows).
    e. Keep the paper trace. Write coupon ID, cycle, direction, t, RH, T.
39. [DESIGN-PROPOSAL] If the profile is an obvious circular arc, also
    measure sagitta d and chord or free length L on the same trace for the
    radius step in Section 7.
40. [DESIGN-PROPOSAL] Two operators, or one operator reading twice, on the
    t = 180 s wet and dry traces of cycle 1. Record both. Use the mean in
    the summary table; keep the raw pair.

### 6.2 Optional camera + ImageJ workflow

This entire subsection is [DESIGN-PROPOSAL].

41. [DESIGN-PROPOSAL] Fixed camera, optical axis perpendicular to the plane
    of bending. Include a scale bar and the clamp edge in every frame.
42. [DESIGN-PROPOSAL] Still frame at each time sample, or video at >= 1 fps
    for 3 min. Do not use video as the only record; keep the paper trace.
43. [DESIGN-PROPOSAL] In ImageJ (or equivalent): set scale; draw the datum
    line and the free-end tangent; measure the included angle. Optionally
    fit a circular arc and export R.
44. [DESIGN-PROPOSAL] If ImageJ and protractor disagree by more than
    theta_repeat (Section 3), trust the paper trace for the Birch-comparable
    column and file the digital value in a parallel column. Do not overwrite.

---

## 7. Force method (Stoney, report N/m)

45. [LITERATURE-CONFIRMED] Birch 2021 computed force from the Stoney
    formula using radius of curvature, and reported the result in N/m,
    up to 26.7 N/m at the greatest monolayer count tested (4)
    (DOI 10.3390/su13074030). Birch also cites a Chen latex reference of
    about 16 N/m at similar RH.
46. [LITERATURE-CONFIRMED] Substrate constants for the Track A comparison
    are Birch's 0.5 mm natural latex with Young's modulus ~3.0 MPa
    (DOI 10.3390/su13074030).

The verified brief does not reprint Birch's exact algebraic line. Use the
standard thin-film Stoney force per unit width and write the symbols down.
Do not present the algebra as a new discovery.

47. [DESIGN-PROPOSAL] Primary reporting formula (plain ASCII):
    ```
    f = (E_s * t_s^2) / (6 * R)          [N/m]
    ```
    where
    ```
    f    = force per unit width           (N/m)
    E_s  = substrate Young's modulus      (Pa)
    t_s  = substrate thickness            (m)
    R    = radius of curvature            (m)
    ```
    Track A numbers if the coupon is Birch latex and E_s is not re-measured:
    ```
    E_s = 3.0e6 Pa
    t_s = 0.5e-3 m
    f   = (3.0e6 * (0.5e-3)^2) / (6 * R)
        = 0.125 / R                      [N/m]   if R is in metres
    ```
48. [DESIGN-PROPOSAL] Optional Poisson form, recorded in a second column
    only if nu_s is measured or taken from a cited latex datasheet:
    ```
    f_nu = (E_s * t_s^2) / (6 * R * (1 - nu_s))
    ```
    Do not mix f and f_nu in the same plot. Birch's 26.7 N/m must be
    compared to whichever form the operator can show is the closer match
    to Birch's methods text when that paper is read in full. Until then,
    report f from Section 47 and label it "Stoney, no Poisson term".
49. [DESIGN-PROPOSAL] Radius from the same trace used for theta, circular-arc
    approximation:
    ```
    R_sagitta = (L^2) / (8 * d) + d / 2
    ```
    or, if the coupon is treated as a circular arc of included angle
    theta_rad = theta_deg * pi / 180 and arc length ~ L:
    ```
    R_theta = L / theta_rad
    ```
    Record which R is fed to Stoney. Prefer R_sagitta when d is measurable;
    use R_theta only when the profile is an obvious circular arc and d is not.
50. [DESIGN-PROPOSAL] If the coupon is nearly flat, R -> infinity and f -> 0.
    Report f = 0 (or "below resolution") rather than dividing by a guessed R.
    [LITERATURE-CONFIRMED] A near-zero deflection at n = 1 on 0.5 mm latex
    against gravity is consistent with Birch 2021, not an automatic fail.
51. [DESIGN-PROPOSAL] Do not insert t_f (spore-film thickness) into the
    N/m column. Birch's reported quantity is force per unit width. A stress
    ```
    sigma_f = f / t_f
    ```
    is optional and only if t_f is measured. The fabrication-protocol.md
    estimate t_f ~ 3 um * n is a packing guess, not a measured stack.
52. [LITERATURE-CONFIRMED] Interpretation context, not a pass/fail number:
    Birch force rose linearly from 2 to 4 monolayers while angle approached
    a plateau (DOI 10.3390/su13074030). That split is the quantity this
    protocol is built to see again at n >= 5.

---

## 8. Lift test (paper loads)

53. [LITERATURE-CONFIRMED] Birch 2021: 4-monolayer latex actuators lifted
    paper loads equivalent to >=150% of actuator mass; deflection fell
    linearly with load (DOI 10.3390/su13074030).
54. [LITERATURE-CONFIRMED] Chen 2015 HYDRA lift of about 50x strip mass is
    a different, polyimide construct (DOI 10.1038/ncomms8346). Do not use
    50x as the Track A target and do not mix it with Birch's 1.5x result.

55. [DESIGN-PROPOSAL] Weigh the finished coupon (m_act) after the 24 h wet
    equilibration, blot any condensed water, and record mg.
56. [DESIGN-PROPOSAL] Cut paper slips to a known mass series, for example
    ```
    0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 2.00  x  m_act
    ```
    Exact increments are not in the brief. What is required is a load
    axis in units of m_act, including at least one point at 1.50 * m_act
    (the Birch 150% mark) when the coupon can take it.
57. [DESIGN-PROPOSAL] Run lift on the n = 4 control if it exists (Birch
    overlap). Also run n = 3 (last published rising-angle point) and any
    n >= 5 coupon that is still mechanically intact (crack score <= 2 in
    Section 9). Skip lift on coupons that are already flaking; a dropped
    coat is not a lift result.
58. [DESIGN-PROPOSAL] Procedure, one load at a time, same RH switch as
    Section 5:
    a. Mount as in Section 4 (vertical, Birch gravity context).
    b. Place the paper slip on the free arm (not on the clamp).
    c. Switch ~42% <-> >95% RH; dwell the Section 5.2 window.
    d. Record theta_max (and Delta_theta) at that load.
    e. Remove the load; recover one unloaded half-cycle before the next slip.
59. [DESIGN-PROPOSAL] Plot theta (or Delta_theta) vs load / m_act. A
    roughly linear drop with load is the Birch qualitative pattern. Do not
    claim a 150% lift unless the coupon actually raises that slip through
    a measurable angle change. n = 1 is not expected to lift on 0.5 mm latex.
60. [DESIGN-PROPOSAL] Do not hang gram masses from a hook unless the coupon
    is first shown to survive paper slips. Hook fixtures are not Birch.

---

## 9. Crack / delamination scoring (required for n >= 5)

Birch 2021 did not publish a high-n damage rubric; the paper stopped at
4 monolayers. This entire section is [DESIGN-PROPOSAL] except the literature
reason for watching n >= 5.

61. [LITERATURE-CONFIRMED] Birch 2021 angle plateau at 4 monolayers is
    attributed to the ~12% spore-strain limit, not to a measured crack series
    (DOI 10.3390/su13074030). [DESIGN-PROPOSAL] Layers 5-21 are therefore
    an integrity experiment as much as an angle experiment.

62. [DESIGN-PROPOSAL] Score every coupon at three times: (i) after 24 h
    wet equilibration, before cycle 1; (ii) after cycle 1; (iii) after the
    10-cycle block (Section 10). Score n >= 5 after every cycle.

63. [DESIGN-PROPOSAL] Rubric (integer 0-5), mid-span plus both ends,
    coated face, 10-50x:

| Score | Name | Visible state | Actuation handling |
|-------|------|---------------|--------------------|
| 0 | Intact | continuous film, no cracks | full protocol |
| 1 | Hairline | fine cracks, no flake, edges attached | full protocol |
| 2 | Mud-crack | channel cracks, film still attached | full protocol; flag |
| 3 | Edge lift | delamination starting at an edge or clamp | angle + Stoney allowed; skip lift if face is peeling |
| 4 | Flake | patches of coat lost | theta_max may be recorded as "damaged"; do not treat as a programming point |
| 5 | Failed stack | coat gone or coupon torn | stop actuation; keep as failure specimen |

64. [DESIGN-PROPOSAL] Also record a one-line location code: E (edge),
    M (mid-span), C (clamp), X (widespread), and a yes/no for powdering
    onto the paper trace.
65. [DESIGN-PROPOSAL] A coupon that reaches score >= 4 is a stack-integrity
    result. It is not evidence that theta_max(n) has been measured at that n.
66. [DESIGN-PROPOSAL] Photograph each scored state with the coupon ID and
    a scale bar. Do not "repair" a cracked coat to continue the series
    (same rule as fabrication-protocol.md step 30).

---

## 10. Local cycle block (Birch minimum = 10)

67. [LITERATURE-CONFIRMED] Birch 2021: 10 hydration/dehydration cycles on
    the latex hygromorphs, no performance loss (DOI 10.3390/su13074030).
    Ten cycles is the literature minimum for Track A.
68. [LITERATURE-CONFIRMED] Birch 2021 cites Chen et al. for 1e6-cycle
    durability on other constructs; Birch does not demonstrate 1e6 cycles
    on latex (DOI 10.3390/su13074030).
69. [LITERATURE-CONFIRMED] Chen 2015: after 1,000,000 humidity cycles and
    80 days, HYDRA elongation was reduced only slightly, on polyimide,
    including some cotE gerE samples (DOI 10.1038/ncomms8346). Context only.

70. [DESIGN-PROPOSAL] After the first characterisation cycle (Section 5-7),
    run nine further full cycles (Section 5.3) for a logged total of 10.
    Same two RH set-points. Same 3-5 min dwells. No new loads during the
    cycle block (lift is Section 8, run on a separate day or after cycle 10
    recovery).
71. [DESIGN-PROPOSAL] At cycles 1, 2, 5, and 10, record the full time series.
    At the other cycles, record at least the t = 180 s wet and dry angles.
72. [DESIGN-PROPOSAL] "No performance loss" is operationalised, for this
    protocol only, as
    ```
    |theta_max(cycle 10) - theta_max(cycle 1)|  <=  theta_repeat
    ```
    and no increase of crack score by more than 1 grade. This is a recording
    rule, not a Birch statistical test.
73. [DESIGN-PROPOSAL] Stop the cycle block early if crack score reaches 4
    or the latex tears. Early stop is a result (integrity limit), not a
    voided notebook.
74. [DESIGN-PROPOSAL] Do not extend Track A to 1e6 cycles in this protocol.
    Do not write a latex "1e6-cycle plan" that cites Chen 2015 as if it
    were the same device. A later endurance protocol, if written, is a
    new DESIGN-PROPOSAL document.

---

## 11. Recommended run order (still a protocol, not a log)

75. [DESIGN-PROPOSAL] Suggested sequence when coupons later exist:

    1. Confirm IDs, traveler cards, and 24 h / >95% RH log (Section 1.3).
    2. Score cracks (Section 9) and weigh m_act.
    3. Mount Track A n = 1, 2, 3 first (Birch overlap).
    4. Cycle 1 full time series + traces + Stoney (Sections 5-7).
    5. If HE-SP-LAT-M-n04 exists, run it next (published plateau).
    6. Run n = 5, 8, 13, 21 with crack scoring after every cycle.
    7. Complete the 10-cycle block on coupons that are still score <= 3.
    8. Lift test (Section 8) on n = 4 (or n = 3 if no n = 4) and on intact n >= 5.
    9. Only then consider Track B1 / B2 / B3 (Sections 12-14).

76. [DESIGN-PROPOSAL] Do not start on n = 21. High-n coupons are the
    exploratory tail; they do not calibrate the protractor or the boxes.

---

## 12. Track B1 — architectural 50 mm x 100 mm latex (only if built)

This section is idle unless HE-SP-LAT-A-* coupons exist.
The entire section is [DESIGN-PROPOSAL] except the RH window, which remains Birch.

77. [DESIGN-PROPOSAL] If Track B1 coupons exist, use the same two RH
    set-points (~42% <-> >95%), the same 24 h pre-test wet hold, and the
    same <3 min observation window as Track A. [LITERATURE-CONFIRMED] RH
    pair and 24 h wet hold: Birch 2021. [DESIGN-PROPOSAL] applying them
    to a 50 mm x 100 mm coupon.
78. [DESIGN-PROPOSAL] Clamp one 50 mm edge. Record free length. Expect
    more self-weight sag than the 1 cm x 2 cm strip; a n = 1 "no lift
    against gravity" result is even more likely and is not a process fail.
79. [DESIGN-PROPOSAL] Same angle, Stoney, lift, crack, and 10-cycle columns.
    Stoney with E_s ~ 3.0 MPa and t_s = 0.5 mm remains the latex default,
    but self-weight and non-circular bending make f a rougher number.
    Label B1 Stoney values "large-coupon, interpret with caution".
80. [DESIGN-PROPOSAL] Do not call a 50 mm x 100 mm coupon a facade panel.
    Do not start 150 mm x 300 mm mock-ups in this protocol
    (fabrication-protocol.md Section 2.2).

---

## 13. Track B2 — cork trial metrics (only if built)

No published cork + spore actuator curve is in the verified brief.
This entire section is [DESIGN-PROPOSAL] and runs only if HE-SP-CRK-* exist.

81. [DESIGN-PROPOSAL] Do not replace Track A. Cork is a parallel series.
82. [DESIGN-PROPOSAL] Apply the same RH set-points and the same angle /
    cycle / crack columns so the only intentional change is the substrate.
    Do not borrow Birch's 43 deg, 26.7 N/m, <3 min, or 150% lift as cork
    expectations.
83. [DESIGN-PROPOSAL] Extra cork-only notes, recorded every cycle:
    - Did the coat stay a surface film or sink into pores?
    - Did the cork sheet cup, swell, or crack on its own?
    - Is E_s * t_s^2 even roughly known? If not, skip Stoney rather than
      inventing a cork modulus. Report R and theta only.
84. [DESIGN-PROPOSAL] Do not write "cork is optimal" in the notebook.
    That AI-CONTEXT.md D03 line is unverified (spore-data-survey.md Section 10.1).
85. [DESIGN-PROPOSAL] A cork coupon that does not bend is a valid negative
    result. It does not falsify Birch 2021.

---

## 14. Track B3 — parylene siblings (only if built)

86. [DESIGN-PROPOSAL] If HE-SP-*-PAR siblings exist, run them through
    Sections 5-10 beside their unsealed twins. Compare Delta_theta and
    crack score. A sealed coupon that stops exchanging water is a blocked
    actuator, not a durability win.
87. [LITERATURE-CONFIRMED] Birch 2021 does not describe an edge seal.
    Unsealed Track A remains the literature baseline (DOI 10.3390/su13074030).

---

## 15. Data-table schema

No cells are filled. This is the empty schema for a later campaign.

### 15.1 Coupon header (one row per physical coupon)

[DESIGN-PROPOSAL] columns:

```
coupon_id          e.g. HE-SP-LAT-M-n05-rep2
track              A | B1 | B2 | B3
substrate          latex_0.5mm | cork | other
n_layers           1,2,3,4,5,8,13,21
replicate          1..n_rep
strain             wild-type B. subtilis (default) | labelled other
OD600              fabrication-day stock
m0_mg              bare substrate
m_act_mg           after 24 h wet equilibration
L_mm               free length after clamp
E_s_Pa             3.0e6 for Birch latex unless re-measured
t_s_m              0.5e-3 for Track A latex
equil_RH_pct       logged mean during 24 h hold
equil_hours        should be >= 24
operator
date_iso           YYYY-MM-DD (date of test, not a result)
notes
```

### 15.2 Time-series / cycle table (one row per observation)

[DESIGN-PROPOSAL] columns:

```
coupon_id
cycle              1..10 (or early-stop)
direction          dehydrate | hydrate
RH_target          42 | 95 | 99
RH_logged_pct
T_logged_C
t_s                seconds since switch
theta_deg          protractor / trace
theta_imagej_deg   optional; blank if unused
theta_max_deg      peak |theta| this half-cycle (filled at end of dwell)
delta_theta_deg    |theta_wet - theta_dry| this cycle (filled at cycle end)
R_m                radius used in Stoney (blank if flat)
R_method           sagitta | theta | imagej | none
f_Npm              Stoney N/m from Section 7 (blank if R none)
load_x_mact        0 for unloaded cycles; lift-test multiplier otherwise
load_mg
crack_score        0..5
crack_loc          E|M|C|X
hysteresis_flag    Y if |theta_hydrate - theta_dehydrate| > theta_repeat
void_flag          Y if transfer >30 s or RH off-target
filename_trace     paper-trace scan
filename_photo
```

### 15.3 Summary table (one row per coupon, filled only after that coupon is run)

[DESIGN-PROPOSAL] columns:

```
coupon_id
n_layers
theta_max_c1_deg
delta_theta_c1_deg
f_max_c1_Npm
theta_max_c10_deg
delta_theta_c10_deg
cycles_completed
crack_score_end
lift_max_x_mact    blank if lift not run
hysteresis_any     Y/N
integrity_limit    Y if score >= 4 or early stop
spore_strain_flag  Y if Section 16.1 pattern holds for this n
```

### 15.4 Required plots (when data later exist)

88. [DESIGN-PROPOSAL] Plot A: theta_max vs n_layers (mean of replicates,
    error bars = min/max or sample sd). Overlay Birch's qualitative
    pattern: weak n=1, rise through n=3, plateau near n=4.
89. [DESIGN-PROPOSAL] Plot B: f (N/m) vs n_layers on the same x-axis.
90. [DESIGN-PROPOSAL] Plot C: theta_max vs cycle number, one line per n.
91. [DESIGN-PROPOSAL] Plot D (lift): theta vs load / m_act for n = 4
    (and intact higher n).
92. [DESIGN-PROPOSAL] Do not fit a monotone f(n) through n = 21 and call
    it literature. Birch's published points stop at 4.

---

## 16. Falsification criteria

These criteria interpret a future dataset. They are not results.

### 16.1 Spore-strain limit (primary architectural falsifier)

93. [LITERATURE-CONFIRMED] Birch 2021 already reports angle plateau at 4
    monolayers with force still rising, attributed to the ~12% spore
    contraction limit (DOI 10.3390/su13074030).

94. [DESIGN-PROPOSAL] Campaign-level rule for the Fibonacci extension:
    ```
    IF  theta_max(n) is flat (within theta_repeat of the n=4 or n=5 value)
        for all measured n >= 5
    AND f(n) continues to rise beyond n=4
    AND f(n) then plateaus
    THEN the useful programming range of n_layers on this latex is the
         Birch short range, and the cap is the spore-strain limit
         (not a new discovery; a confirmation of Birch's interpretation
         on a longer n list).
    ```
    That outcome falsifies AI-CONTEXT.md D03 as written
    (unbounded monotone theta_max = f(n_layers)). It does not falsify
    Birch 2021. It does not by itself falsify force-based programming.

### 16.2 Stack-integrity limit (distinct from 16.1)

95. [DESIGN-PROPOSAL]
    ```
    IF  theta_max and f both collapse for n >= 5
    OR  crack_score >= 4 on a majority of n >= 5 replicates
    THEN the limit is fabrication / delamination, not the 12% strain cap.
    Do not interpret those n as programmed angles.
    ```

### 16.3 Birch-reproduction checks (Track A only)

96. [LITERATURE-CONFIRMED] Expected qualitative pattern on 0.5 mm latex
    (DOI 10.3390/su13074030): n=1 force-poor vs gravity; angle rising
    through n=2-3; plateau near n=4 if the control exists; no direction
    hysteresis; max deflection inside 3 min; 10 cycles without loss.
97. [DESIGN-PROPOSAL] If n=1 produces a large vertical deflection against
    gravity, the substrate, thickness, or mount is not Birch-class.
    Stop comparing numbers to 43 deg / 26.7 N/m until that is resolved.
98. [DESIGN-PROPOSAL] If direction hysteresis exceeds theta_repeat at
    both set-points, the coupon is not reproducing Birch reversibility.
    Check RH control, clamp slip, and coat damage before discussing n.
99. [DESIGN-PROPOSAL] If time-to-plateau on 0.5 mm latex is many times
    longer than 3 min with RH actually switched, record the curve. Do not
    relabel the coupon as a Chen 2015 3 s HYDRA miss.

### 16.4 Lift

100. [DESIGN-PROPOSAL] Failure of an n=4 latex coupon to move any paper
     slip does not, by itself, falsify Birch if theta_max is also far
     below ~43 deg (the actuator is simply not a Birch-class 4-layer).
     Failure of a Birch-like n=4 (angle near the published plateau, coat
     intact) to lift ~1.5 * m_act is a lift-specific discrepancy and
     should be reported as such.

### 16.5 What these criteria must not do

101. [DESIGN-PROPOSAL] Do not treat a cork negative (Track B2) as a
     falsification of Birch latex.
102. [DESIGN-PROPOSAL] Do not treat a 10-cycle latex fade as a
     falsification of Chen 2015's polyimide 1e6-cycle result.
103. [DESIGN-PROPOSAL] Do not treat a flat theta_max(n>=5) as a failed
     fabrication if Section 16.1 holds. That is the scientifically
     interesting confirmation.

---

## 17. Safety and waste (test bench)

104. [LITERATURE-CONFIRMED] Birch 2021 places B. subtilis in a GRAS /
     BSL-1 context (DOI 10.3390/su13074030). This is not a skip of local
     review.
105. [DESIGN-PROPOSAL] Same BSL-1 handling as fabrication-protocol.md
     Section 13: no aerosols, gloves, bench disinfection, autoclave or
     bleach path for failed coupons and used paper loads that touched
     the coat.
106. [DESIGN-PROPOSAL] Latex allergy: Track A is natural latex. Nitrile
     gloves on the bench. Do not swap coupon material mid-series.
107. [DESIGN-PROPOSAL] Water boxes: keep liquid off electrical loggers
     and off the spore face.
108. [DESIGN-PROPOSAL] Do not install coupons on a building as part of
     this protocol. Birch lists real-environment durability and
     germination control as open gaps (DOI 10.3390/su13074030).

---

## 18. What this document deliberately does not contain

- No claim that any coupon, chamber run, angle, force, or lift exists.
- No filled data tables.
- No cork result, no parylene result, no 50 x 100 mm result.
- No 1e6-cycle latex plan and no 3 s latex claim.
- No alternative non-spore actuators (next ROLE 03 file: alternatives.md).
- No Octopus-system content.
- No new discovery. Law 3 remains: no new discoveries until CRITIC writes
  unsupported-claims.md.

If execution never happens, this file remains a protocol.

---

## 19. Pointers

- Literature numbers and AI-CONTEXT.md D03 mismatches:
  `agents/materials/spore-data-survey.md`
- Coupon fabrication, IDs, Track A/B split, 24 h wet equilibration:
  `agents/materials/fabrication-protocol.md`
- Next ROLE 03 task (not written in this pass):
  `agents/materials/alternatives.md`
- Project D03 one-liner (contains unverified monotone / cork / 1e6 lines):
  `AI-CONTEXT.md` section D03
