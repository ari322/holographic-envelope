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
(~43 deg; ~12% spore-strain limit) while Stoney force still rises (up to 26.7 N/m).
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

### 2.1 Humidity environments

| Item | Set-point / use | Tag |
|------|-----------------|-----|
| Wet enclosure | >95% RH (Birch) | set-point [LITERATURE-CONFIRMED] |
| Dry enclosure | ~42% RH | set-point [LITERATURE-CONFIRMED] Birch 2021 |
| RH/T logger | one logger in each enclosure | [DESIGN-PROPOSAL] |

### 2.2 Angle and curvature

| Item | Use | Tag |
|------|-----|-----|
| Graph paper / tracing paper | Birch-class curvature trace | [LITERATURE-CONFIRMED] |
| Protractor | read the bend angle | [LITERATURE-CONFIRMED] |
| Camera (optional) | side-view stills for ImageJ | [DESIGN-PROPOSAL] |

---

## 3. Definitions

13. [DESIGN-PROPOSAL] theta(RH) = included angle between fixture datum and free-end tangent.
14. [DESIGN-PROPOSAL] Stroke: Delta_theta(n) = |theta_wet(n) - theta_dry(n)|
15. [DESIGN-PROPOSAL] theta_max(n) = max( |theta_wet(n)|, |theta_dry(n)| )

---

## 4. Falsification criteria

### 4.1 Spore-strain limit

[LITERATURE-CONFIRMED] Birch 2021 reports angle plateau at 4 monolayers
with force still rising, attributed to the ~12% spore contraction limit
(DOI 10.3390/su13074030).

[DESIGN-PROPOSAL] IF theta_max(n) is flat for all n >= 5 AND f(n) continues
to rise, the useful programming range is the Birch short range — a
confirmation of Birch's interpretation, not a new discovery.

---

## 5. What this document does not contain

- No claim that any coupon, chamber run, angle, force, or lift exists.
- No filled data tables.
- No Octopus-system content.
- No new discovery.

If execution never happens, this file remains a protocol.
