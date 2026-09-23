# Non-spore actuator alternatives if D03 fails
# ROLE 03 - MATERIALS SCIENTIST (task 4 of 4)
# Date: 2026-09-23
# Status: PROTOCOL / PROPOSAL ONLY. No HE panels or coupons have been built.

Claim tags:
- [LITERATURE-CONFIRMED] = published fact from a named paper with a real DOI
- [DESIGN-PROPOSAL] = HE project choice, not a built result

Three alternatives only. No invented DOIs. No Octopus content.

---

## 1. Spore baseline weaknesses

### 1.1 Angle plateau near 4 monolayers
[LITERATURE-CONFIRMED] Birch 2021: angle plateaus ~43 deg at 4 monolayers;
force still rises to 26.7 N/m (DOI 10.3390/su13074030).

### 1.2 Cycle-life substrate mismatch
[LITERATURE-CONFIRMED] Birch 2021: 10 cycles on latex (DOI 10.3390/su13074030).
Chen 2015: 1e6 cycles on polyimide HYDRA, not latex (DOI 10.1038/ncomms8346).

### 1.3 Germination gap
[LITERATURE-CONFIRMED] Birch 2021 lists germination control as an open
architectural gap (DOI 10.3390/su13074030).

### 1.4 Cork substrate unverified
[LITERATURE-CONFIRMED] Published substrates = silicon, elastomer, polyimide,
latex. None is cork (Chen 2014/2015; Birch 2021).

---

## 2. Alternative 1 — Wood / wood-composite hygromorphs

[LITERATURE-CONFIRMED] Holstov, Bridgens and Farmer 2015: wood bilayer
converts differential hygroexpansion into bending (DOI 10.1016/j.conbuildmat.2015.08.136).
[LITERATURE-CONFIRMED] Holstov et al. 2017: 80% wet stroke in 20-30 min;
1-year full-weathering roof study, no progressive delamination
(DOI 10.3390/su9030435).
[LITERATURE-CONFIRMED] Reichert, Menges, Correa 2015: HygroScope/HygroSkin
passive humidity-responsive systems (DOI 10.1016/j.cad.2014.02.010).

[DESIGN-PROPOSAL] Addresses all four spore weaknesses. No germination.
No cork dependency. Outdoor precedent exists (Holstov 1-year).
Trade-off: slower than Birch latex (<3 min) — minutes to hours.

---

## 3. Alternative 2 — SMA / Nitinol facade actuators

[LITERATURE-CONFIRMED] Formentini and Lenci 2017: Nitinol wire on aluminium
ventilated-facade panel (DOI 10.1016/j.autcon.2017.10.006).
[LITERATURE-CONFIRMED] Stelzmann et al. 2024: SMA wire driving 90 deg louvres
via solar collector; overcast miss is a documented caveat
(DOI 10.3390/act13030085).
[LITERATURE-CONFIRMED] Fiorito et al. 2016: SMA cycle durability review
(DOI 10.1016/j.rser.2015.10.086).

[DESIGN-PROPOSAL] Temperature/solar trigger — not humidity. Force advantage
over spores. Fail-safe requires bias spring. Useful if D03 fails on force.

---

## 4. Alternative 3 — Cellulose 4D-printed hygromorphic bilayers

[LITERATURE-CONFIRMED] Cheng et al. 2024: FFF 4D-printing of cellulose/PK +
ASA bilayer; 170 humidity cycles; 13-month outdoor mock-up; 424-module
livMatS facade (DOI 10.1038/s41467-024-54808-8).
[LITERATURE-CONFIRMED] Full 30%<->90% RH stroke within 30 min.
No operational electricity required.

[DESIGN-PROPOSAL] Closest "same job, better evidence" spore replacement.
Non-living. No germination. No cork. Programming by FFF path rather than
n_layers. Custom cellulose/PK filament is not off-the-shelf.

---

## 5. Comparison table

| Weakness | Spore | Alt 1 Wood | Alt 2 SMA | Alt 3 Cellulose 4D |
|----------|-------|-----------|-----------|--------------------|
| Angle plateau | ~4 layers, ~43 deg [LC] | No coat cap [DP] | 90/180 deg stroke [LC] | FFF path programming [LC] |
| Cycle life | 10 (latex) [LC] | 1-yr outdoor [LC] | Durability cited; fatigue at bends [LC] | 170 cycles + 13 months [LC] |
| Germination | Open gap [LC] | Non-living [LC] | Non-living [LC] | Non-living [LC] |
| Cork | Unverified [LC] | Not required [LC] | Not required [LC] | Not required [LC] |
| Trigger | Humidity [LC] | Humidity+wetting [LC] | Temperature/solar [LC] | Humidity+temperature [LC] |
| Response | <3 min latex [LC] | 20-30 min [LC] | Seconds-minutes [LC] | 30 min [LC] |
| Arch precedent | 1 cm × 2 cm latex [LC] | HygroSkin; Holstov [LC] | Formentini; Stelzmann [LC] | 424-module livMatS [LC] |

LC = [LITERATURE-CONFIRMED], DP = [DESIGN-PROPOSAL]

---

## 6. No new claims

- No HE coupon has been built for any alternative.
- No DOI was invented.
- No Octopus content.
- No new discovery (Law 3).
