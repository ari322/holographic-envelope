# Non-spore actuator alternatives if D03 fails
# ROLE 03 - MATERIALS SCIENTIST (task 4 of 4)
# Date: 2026-09-23
# Status: PROTOCOL / PROPOSAL ONLY. No HE panels or coupons have been built.
#         None of the three alternatives has been fabricated for holographic-envelope.

Claim tags used throughout:
- [LITERATURE-CONFIRMED] = published fact from a named paper with a real DOI
  (spore baseline: verified literature brief 2026-09-23; alternatives: Holstov /
  Reichert / Formentini / Fiorito / JFDE / Actuators 2024 / Cheng 2024 as named
  in the ROLE 03 alternatives brief).
- [DESIGN-PROPOSAL] = HE project choice: how a later campaign might use the
  material as a D03 replacement. Not a built result.

Plain ASCII. Three alternatives only. No invented DOIs. No Octopus content.
No claim that any of these have been built for HE.

---

## 0. Why this file exists

ROLE 03 task 4: propose exactly three non-spore actuators that could replace
D03 (programmable bacterial spore panels) if the spore path fails.

Sibling ROLE 03 files (not in this PR):
- spore-data-survey.md     - PR #6
- fabrication-protocol.md  - PR #6
- test-protocol.md         - PR #8

This file does not add spore data. It does not rewrite the fabrication or
humidity-chamber protocols. It proposes fallback actuators only.

---

## 1. Spore baseline weaknesses (what a replacement must survive)

These four weaknesses are the comparison axes. They come from the verified
spore literature brief and from spore-data-survey.md (PR #6). They are not
new discoveries.

### 1.1 Angle plateau near 4 monolayers

[LITERATURE-CONFIRMED] Birch 2021 tested 1, 2, 3, and 4 monolayers on
0.5 mm natural latex. Deflection angle rose from 1 to 3 monolayers, then
showed diminishing returns / plateau at 4 monolayers (~43 deg), attributed
to the spore contraction limit of about 12%. Force (Stoney) still rose
linearly from 2 to 4 monolayers, up to 26.7 N/m
(DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] n = 1 did not supply enough force to deflect that
0.5 mm latex against gravity (DOI 10.3390/su13074030).

[DESIGN-PROPOSAL] AI-CONTEXT.md D03 writes theta_max = f(n_layers) as an
unbounded monotone map and names a Fibonacci set n = 1, 2, 3, 5, 8, 13, 21.
That encoder is not literature-supported past ~4 layers. A replacement
actuator should offer a programming axis that does not saturate at four
thin coats.

### 1.2 Cycle-life substrate mismatch

[LITERATURE-CONFIRMED] Birch 2021: 10 hydration/dehydration cycles on latex,
no performance loss (DOI 10.3390/su13074030). Birch cites Chen for 1e6-cycle
context; Birch does not itself demonstrate 1e6 cycles on latex.

[LITERATURE-CONFIRMED] Chen 2015: after 1,000,000 humidity cycles and 80 days,
HYDRA elongation was reduced only slightly. Substrate = ~8 um polyimide tape.
Some samples used cotE gerE mutant spores. Response time of those strips
~3 s (DOI 10.1038/ncomms8346).

[LITERATURE-CONFIRMED] Chen 2015 does not say "100% stable". AI-CONTEXT.md
D03's "100% stable over 1,000,000 cycles" is overstated and
substrate-mismatched (latex/cork is not polyimide HYDRA).

[DESIGN-PROPOSAL] A replacement should either (a) already have outdoor or
multi-month facade-class durability data, or (b) have a documented fatigue
caveat that HE can test without confusing two substrates.

### 1.3 Germination / living-material gap

[LITERATURE-CONFIRMED] Birch 2021 states remaining architectural gaps:
longer-term real-environment studies, germination control for architectural
durability, and broader substrates beyond latex (DOI 10.3390/su13074030).

[LITERATURE-CONFIRMED] Birch prefers wild-type B. subtilis for cycle
resilience; cotE gerE expands more but lacks repeated-cycle resilience
(DOI 10.3390/su13074030).

[DESIGN-PROPOSAL] Any non-living replacement automatically removes the
germination-control requirement. That is an architectural advantage, not
a claim that the replacement is maintenance-free.

### 1.4 Cork substrate unverified

[LITERATURE-CONFIRMED] Published spore-actuator substrates in the verified
brief are silicon, elastomer, polyimide, and latex (Chen 2014
DOI 10.1038/nnano.2013.290; Chen 2015 DOI 10.1038/ncomms8346; Birch 2021
DOI 10.3390/su13074030). None is cork.

[DESIGN-PROPOSAL] AI-CONTEXT.md D03 names cork (Quercus suber) as the 2025
optimal substrate. That is unverified. A replacement must not inherit cork
as a hidden dependency.

---

## 2. Alternative 1 - Wood / wood-composite hygromorphs

Named cites: Holstov / Bridgens / Farmer; Reichert / Menges / Correa
(HygroScope, HygroSkin).

### 2.1 Mechanism

[LITERATURE-CONFIRMED] Wood shrinks and swells anisotropically with moisture
content. A bilayer (active wood veneer + stiffer or orthogonally oriented
restricting layer) converts that differential hygroexpansion into bending,
twisting, or opening, analogous to conifer-cone scales (Holstov, Bridgens
and Farmer 2015, DOI 10.1016/j.conbuildmat.2015.08.136; Holstov, Farmer
and Bridgens 2017, DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Reichert, Menges and Correa 2015: humidity-responsive
veneer-composite elements use quarter-cut wood veneer so adsorption /
desorption changes the distance between microfibrils and produces a
programmed shape change. Sensor, motor, and structure are the same
material (DOI 10.1016/j.cad.2014.02.010).

[LITERATURE-CONFIRMED] Menges and Reichert 2015: HygroScope and HygroSkin
are weather-responsive wood systems that replace machines with physically
programmed wood elements (DOI 10.1002/ad.1956).

### 2.2 Trigger

[LITERATURE-CONFIRMED] Ambient relative humidity, plus direct wetting by
rain or condensate. Air temperature, solar irradiation, and wind speed
modulate moisture-exchange rate (Holstov et al. 2017, DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] No operational electricity, sensors, or motors are
required for the material response (Reichert et al. 2015,
DOI 10.1016/j.cad.2014.02.010; Holstov et al. 2015,
DOI 10.1016/j.conbuildmat.2015.08.136).

### 2.3 Response-time band

[LITERATURE-CONFIRMED] Holstov et al. 2017: samples respond faster to
wetting than to ambient-humidity change; 80% of total curvature change
on wetting occurs within the first 20-30 minutes
(DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Holstov et al. 2017: thin panels can follow diurnal
humidity cycles and short precipitation; thicker panels follow longer
humidity patterns and may reach a full dry shape only after prolonged
dry periods. Response band spans a few minutes (thin, wet) to hours /
seasonal (thick) (DOI 10.3390/su9030435).

[DESIGN-PROPOSAL] For an HE desk coupon, budget minutes-to-hours, not
Birch's <3 min on 0.5 mm latex and not Chen's ~3 s on polyimide HYDRAs.
Do not advertise wood as a second-scale actuator.

### 2.4 Durability notes

[LITERATURE-CONFIRMED] Holstov et al. 2017 report a one-year full-weathering
study of hygromorphic wood composites on a roof in Newcastle upon Tyne:
24 glued 50 mm x 125 mm samples plus cladding modules. No wind detachment
in gusts exceeding 25 m/s; minor snow (~20 mm) did not reset pre-programmed
shape; no progressive delamination beyond production-stage bond damage
(DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Same study: thin 1 mm birch active layers lost about
10% curvature range by one year; grain-direction cracks near fixings from
about four months; surface erosion on wood-outward faces from about nine
months. Projected outdoor usability ~1 year for perishable species
(birch); two years or more for thicker, naturally durable oak / larch
heartwood if capacity is to stay roughly constant. Indoor or rain-protected
use is expected to last longer (DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Standard film-forming wood preservatives reduce
hygroscopicity and are therefore unsuitable if they block moisture exchange
(Holstov et al. 2017, DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Reichert et al. 2015 document full-scale
meteorosensitive constructions (HygroSkin pavilion class) as architectural
precedent, not as a multi-decade durability certificate
(DOI 10.1016/j.cad.2014.02.010; DOI 10.1002/ad.1956).

### 2.5 Fab path (desk-scale, AU research context)

[LITERATURE-CONFIRMED] Holstov et al. 2017 compare layer bonds: glue,
mechanical fixing, spot-glue, and fibre-composite passive layers
(wood, fibreglass, jute). Grain angle programs bend vs twist
(DOI 10.3390/su9030435; Holstov et al. 2015,
DOI 10.1016/j.conbuildmat.2015.08.136).

[DESIGN-PROPOSAL] HE first coupon (not built):
- Active: 0.5-1.0 mm quarter-sawn veneer (birch for speed; oak/larch if
  outdoor life is the question).
- Restricting: 1-3 mm plywood, GFRP, or a second veneer with grain at 90 deg.
- Bond: waterproof wood glue or mechanical rivets; do not film-coat the
  active face.
- Cut: laser or CNC available in an architecture workshop
  (materials/selection-matrix.md already lists 3 mm plywood bilayer
  as a 1:5 fallback).
- Size: start 50 mm x 125 mm (Holstov outdoor-sample class), not
  150 mm x 300 mm.

[DESIGN-PROPOSAL] Programming axis instead of spore n_layers: grain angle,
active-layer thickness, perforation of the passive layer (Holstov speed
control), and inverse layer stack (open vs close on wetting).

### 2.6 Why it could replace D03

[DESIGN-PROPOSAL] Same passive humidity trigger as spores, so the D03
zero-energy / no-sensor story survives.

[DESIGN-PROPOSAL] Architectural scale is already demonstrated (HygroSkin;
Holstov cladding modules). Spore literature in the brief stops at 1 cm x
2 cm latex coupons plus 2024 aperture prototypes.

[DESIGN-PROPOSAL] No germination control. No BSL-1 spore stock. No cork
dependency. No 4-monolayer angle cap.

[DESIGN-PROPOSAL] One-year outdoor data exist. Spore latex data in the
brief are 10 cycles.

[DESIGN-PROPOSAL] Trade-off: slower than Birch latex (<3 min) and much
slower than Chen HYDRAs (~3 s). Acceptable if HE's first need is a
visible, reversible facade motion, not a 3-minute spore-speed claim.

### 2.7 Failure modes

[LITERATURE-CONFIRMED] Fungal mould (worse on birch than oak/larch);
UV lignin loss and surface erosion of thin veneers; grain cracks at
fixings; visual ageing (grey / extractive bleed); thickness-dependent
mismatch to diurnal vs seasonal climate (Holstov et al. 2017,
DOI 10.3390/su9030435).

[LITERATURE-CONFIRMED] Coatings that stop moisture exchange kill the
actuator (DOI 10.3390/su9030435).

[DESIGN-PROPOSAL] Additional HE risks: Australian UV and termite /
decay climate may shorten Holstov's UK outdoor life; fire class of thin
untreated veneer; grain-to-grain variability so identically specified
coupons do not share one theta.

### 2.8 Citations (Alternative 1)

- Holstov, A., Bridgens, B. and Farmer, G. Hygromorphic materials for
  sustainable responsive architecture. Construction and Building Materials
  98, 570-582 (2015). DOI 10.1016/j.conbuildmat.2015.08.136
- Holstov, A., Farmer, G. and Bridgens, B. Sustainable materialisation of
  responsive architecture. Sustainability 9, 435 (2017).
  DOI 10.3390/su9030435
- Reichert, S., Menges, A. and Correa, D. Meteorosensitive architecture:
  biomimetic building skins based on materially embedded and
  hygroscopically enabled responsiveness. Computer-Aided Design 60, 50-69
  (2015). DOI 10.1016/j.cad.2014.02.010
- Menges, A. and Reichert, S. Performative wood: physically programming
  the responsive architecture of the HygroScope and HygroSkin projects.
  Architectural Design 85(5), 66-73 (2015). DOI 10.1002/ad.1956

---

## 3. Alternative 2 - SMA / Nitinol facade actuators

Named cites: Formentini; Fiorito; Journal of Facade Design and Engineering
(Vercesi / Speroni / Mainini / Poli); Actuators 2024 (Stelzmann et al.).

### 3.1 Mechanism

[LITERATURE-CONFIRMED] Ni-Ti (Nitinol) is a shape-memory alloy. Heating
through the austenite start/finish temperatures recovers a trained shape
(reverse martensitic transformation). Cooling through martensite
start/finish returns the low-temperature phase. Under bias load the
cycle produces usable stroke (Formentini and Lenci 2017,
DOI 10.1016/j.autcon.2017.10.006; Stelzmann et al. 2024,
DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Fiorito et al. 2016 review SMA, SMP, and SMH as
candidate actuators/sensors for shape-morphing solar shadings, including
solar-radiation / thermal activation (DOI 10.1016/j.rser.2015.10.086).

[LITERATURE-CONFIRMED] Facade implementations use the same wire or spring
as both sensor and actuator: Formentini and Lenci, Nitinol wire on an
aluminium ventilated-facade panel (DOI 10.1016/j.autcon.2017.10.006);
Vercesi et al., SMA spring driving a 180 deg twist of cylindrical
shading elements (DOI 10.7480/jfde.2020.1.4700); Stelzmann et al.,
SMA wire in a solar collector driving 90 deg louvres
(DOI 10.3390/act13030085).

### 3.2 Trigger

[LITERATURE-CONFIRMED] Temperature, usually from solar radiation on the
facade or on a collector - not humidity (Formentini and Lenci 2017,
DOI 10.1016/j.autcon.2017.10.006; Vercesi et al. 2020,
DOI 10.7480/jfde.2020.1.4700; Stelzmann et al. 2024,
DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Vercesi et al. 2020: in a Cfa temperate climate,
they correlate SMA-spring activation with a 50 C transition temperature
and incident solar radiation >300 W/m^2 (DOI 10.7480/jfde.2020.1.4700).

[LITERATURE-CONFIRMED] Formentini and Lenci 2017: summer heat opens the
ventilated-facade panel (cavity ventilation); winter cold leaves it
closed (still-air insulation). No electrical supply is required for the
thermal-sensing / actuation function
(DOI 10.1016/j.autcon.2017.10.006).

[LITERATURE-CONFIRMED] Stelzmann et al. 2024: a solar collector (PMMA
tube + black aluminium, greenhouse effect) raises the SMA above outdoor
air temperature so switching temperatures can be set independently of
ambient air. The 1:1 demonstrator is designed to run without electricity;
Joule heating was used only as a development tool
(DOI 10.3390/act13030085).

### 3.3 Response-time band

[LITERATURE-CONFIRMED] SMA phase change itself is fast once the alloy
reaches As-Af. Facade-scale time is set by how fast the wire/spring is
heated: solar collector and radiation, not the millisecond metallurgy
(Stelzmann et al. 2024, DOI 10.3390/act13030085; Fiorito et al. 2016,
DOI 10.1016/j.rser.2015.10.086).

[LITERATURE-CONFIRMED] Stelzmann et al. 2024: effective on clear summer
days; challenged under overcast conditions when the collector does not
reach the switching temperature (DOI 10.3390/act13030085).

[DESIGN-PROPOSAL] HE desk band: seconds (Joule-heat bench test) to
minutes (solar / hot-air gun / sun lamp). Do not claim humidity-speed
parity with Birch latex. This alternative is a temperature/radiation
actuator.

### 3.4 Durability notes

[LITERATURE-CONFIRMED] Fiorito et al. 2016 treat SMA durability / high
hysteresis-cycle count (under stated conditions) as a reason SMAs are
preferred over many other smart materials for shading
(DOI 10.1016/j.rser.2015.10.086). Vercesi et al. 2020 repeat that
durability argument (DOI 10.7480/jfde.2020.1.4700).

[LITERATURE-CONFIRMED] Stelzmann et al. 2024: Clausius-Clapeyron shift  - 
mechanical stress raises As, Af, Ms, Mf. Wind loads and friction can
therefore move the switching temperatures. They designed a counterweight
to keep SMA stress more constant (DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Stelzmann et al. 2024: bending the wire over
small rollers, or clamping that necks the wire, risks microcracks from
the volume change of the martensitic transformation and long-term
fracture (DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Stelzmann et al. 2024 selected
Ni42.5 Ti49.8 Cu7.5 Cr0.2 wire, diameter 0.7 mm, and required
Mf_sigma > 20.0 C so the sunshade still opens on tropical nights
(DOI 10.3390/act13030085).

[DESIGN-PROPOSAL] HE must treat SMA fatigue, hysteresis (As vs Ms gap),
and stress-shifted temperatures as first-class test items. Do not import
a "million-cycle" number from Chen 2015 HYDRAs or from an unsourced SMA
catalogue.

### 3.5 Fab path (desk-scale, AU research context)

[LITERATURE-CONFIRMED] Demonstrated geometries: straight Nitinol wire
(Formentini and Lenci 2017; Stelzmann et al. 2024) and helical SMA spring
(Vercesi et al. 2020).

[DESIGN-PROPOSAL] HE first coupon (not built):
- Buy a documented NiTi wire or bias-spring with a published Af near
  40-55 C (Vercesi 50 C class) or a lower-Af wire if the bench uses
  modest heat.
- Bias: steel return spring or gravity counterweight
  (Formentini / Stelzmann class).
- Fin: laser-cut aluminium or 3D-printed PLA/PETG shutter, 150 mm x 50 mm
  class, not a full louver wall.
- Heat source for lab: sun lamp or hot-air; optional low-voltage Joule
  heat only as a labelled development tool (Stelzmann used this split).
- Do not design a 2 m collector on the first coupon.

[DESIGN-PROPOSAL] Programming axis instead of spore n_layers: trained
stroke, wire length, pulley radius (Stelzmann Eq. relating l_SMA * eps
to 90 deg rotation), number of parallel wires, and Af alloy choice.

### 3.6 Why it could replace D03

[DESIGN-PROPOSAL] If spores fail on germination, latex cycle life, cork,
or the 4-layer angle cap, SMA still gives reversible geometric motion
on a facade-class fin.

[DESIGN-PROPOSAL] Force is the SMA advantage. Spore Birch lift is
>=150% of coupon mass on 4-layer latex (DOI 10.3390/su13074030). SMA
wires are used to move aluminium panels and coupled louvre sets
(Formentini 2017; Stelzmann 2024). A D03 "programmable angle" story
can be rebuilt as a discrete open/close or 0-90 deg louver, which is
enough for TFE > 0 if different panels have different Af or different
pulley ratios.

[DESIGN-PROPOSAL] Trigger mismatch is explicit: temperature / radiation,
not humidity. That is acceptable if D03's job is "passive adaptive
geometry" rather than "humidity encoder".

[DESIGN-PROPOSAL] Fail-safe is worse than wood or spores: selection-
matrix.md already scores SMA fail-safe as 1/3. A power-free SMA still
needs a bias spring / gravity path so the default state is defined when
the alloy is cold.

### 3.7 Failure modes

[LITERATURE-CONFIRMED] Overcast / low-radiation days: collector never
reaches Af (Stelzmann et al. 2024, DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Stress-shifted transformation temperatures;
wind on louvres (Stelzmann et al. 2024, DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Wire fracture at bends, rollers, and necked
clamps (Stelzmann et al. 2024, DOI 10.3390/act13030085).

[LITERATURE-CONFIRMED] Thermal hysteresis: open and close do not occur
at the same temperature (Fiorito et al. 2016, DOI 10.1016/j.rser.2015.10.086;
Stelzmann et al. 2024, DOI 10.3390/act13030085).

[DESIGN-PROPOSAL] HE-specific: NiTi cost and sourcing in Australia;
fire is not the weak point (metal) but electrical Joule-heat shortcuts
must stay SELV if used; a humidity-chamber test-protocol.md does not
qualify an SMA coupon.

### 3.8 Citations (Alternative 2)

- Formentini, M. and Lenci, S. An innovative building envelope (kinetic
  facade) with Shape Memory Alloys used as actuators and sensors.
  Automation in Construction 85, 220-231 (2018).
  DOI 10.1016/j.autcon.2017.10.006
- Fiorito, F., Sauchelli, M., Arroyo, D., Pesenti, M., Imperadori, M.,
  Masera, G. and Ranzi, G. Shape morphing solar shadings: a review.
  Renewable and Sustainable Energy Reviews 55, 863-884 (2016).
  DOI 10.1016/j.rser.2015.10.086
- Vercesi, L., Speroni, A., Mainini, A.G. and Poli, T. A novel approach
  to shape memory alloys applied to passive adaptive shading systems.
  Journal of Facade Design and Engineering 8(1) (2020).
  DOI 10.7480/jfde.2020.1.4700
- Stelzmann, M., Zakner, F., Navarro de Sosa, I., Nemati, A., Kahnt, A.,
  Maass, B. and Drossel, W.-G. Development of a self-regulating solar
  shading actuator based on the thermal shape memory effect.
  Actuators 13, 85 (2024). DOI 10.3390/act13030085

---

## 4. Alternative 3 - Cellulose 4D-printed hygromorphic bilayers

Named cite: Cheng et al., Nature Communications 2024,
DOI 10.1038/s41467-024-54808-8 (already listed in
materials/selection-matrix.md as the architectural-scale cellulosic
hygromorph).

### 4.1 Mechanism

[LITERATURE-CONFIRMED] Cheng, Tahouni, Sahin, Ulrich, Lajewski, Bonten,
Wood, Ruhe, Speck and Menges 2024: fused-filament-fabrication (FFF)
4D-printing of a swellable cellulose/polyketone biocomposite actuating
layer plus a UV-resistant ASA restricting layer, mesostructured like a
pine-cone scale. Differential hygroexpansion produces programmed
curvature (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Filament: native cellulose powder in a partially
biobased polyketone matrix at 35/65 mass ratio, compounded and extruded
to 1.75 mm filament. Restricting filament: off-the-shelf ASA
(DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] A third cross-patterned biocomposite layer
sandwiches the ASA restrictor to reduce delamination
(DOI 10.1038/s41467-024-54808-8).

### 4.2 Trigger

[LITERATURE-CONFIRMED] Relative humidity and temperature together.
High RH produces high curvature (open / curled, depending on the
programmed shade logic). At 80% RH, Cheng et al. report mean curvature
~0.0155 mm^-1 independent of the tested temperatures. At low RH,
temperature matters: ~no curvature at 30 C; ~0.011 mm^-1 at 10 C
(DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Designed for a temperate climate (Freiburg /
livMatS Biomimetic Shell): flatten (more shade) in hot, dry conditions;
curl (more opening) in cold, humid conditions
(DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Energy-autonomous. No motors. Occupant override
is possible by closing facade vents so the cavity no longer equalises
to outdoor RH (DOI 10.1038/s41467-024-54808-8).

### 4.3 Response-time band

[LITERATURE-CONFIRMED] Cheng et al. 2024: full transformation between
30% RH and 90% RH within 30 minutes in lab absorption / desorption
tests (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Authors judge that 30 min is fast enough relative
to natural weather RH cycles (DOI 10.1038/s41467-024-54808-8).

[DESIGN-PROPOSAL] HE desk band: ~30 min for a Cheng-class 75 mm x 20 mm
print. Thicker or larger prints may be slower. Do not claim Birch <3 min
or Chen ~3 s.

### 4.4 Durability notes

[LITERATURE-CONFIRMED] Cheng et al. 2024: 170 humidity cycles
(30% <-> 90% RH). Curvature at 30% RH stayed consistent for all 170
cycles. At 90% RH a slight curvature reduction occurred in the first
10 cycles, then stayed generally consistent for the next 160
(DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] UV chamber (DIN EN ISO 4892-2/-3 class exposure,
60 C dry heat, 96 h): high-RH curvature almost unchanged
(<0.001 mm^-1 vs control); low-RH curvature decreased more when the
active face was exposed (0.006 mm^-1), which is the direction desired
for shading (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Facade-system mock-up monitored 13 months
(June 2022-July 2023) under real weather (RH range 10-91%). No
noticeable reduction in actuation and no mechanical damage reported
for that period. Summer: daily open/close, up to ~90% shade coverage
on hot dry days. Winter: mostly open (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Authors state that 170 lab cycles are still
small versus a building lifetime (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Full-scale demonstrator: 424 unique modules on
the livMatS building facade in Freiburg; 4 FFF printers; 17 days;
7% reprint for print flaws, 1.4% reprint after motion QC
(DOI 10.1038/s41467-024-54808-8).

### 4.5 Fab path (desk-scale, AU research context)

[LITERATURE-CONFIRMED] Cheng lab coupons: 75 mm x 20 mm, FFF dual-head
printer, dry print climate 30% RH / 20-23 C, 0.7 mm nozzle (biocomposite)
and 0.4 mm nozzle (ASA). Print paths program curl direction
(DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Cheng's actuating filament is a custom
compounded 35/65 cellulose/PK, not a random off-the-shelf "wood PLA"
(DOI 10.1038/s41467-024-54808-8).

[DESIGN-PROPOSAL] HE first coupon (not built):
- Track C-lit: if a cellulose/PK or documented hygromorphic cellulose
  filament can be sourced, reprint the 75 mm x 20 mm Cheng coupon
  geometry on a dual-extruder FDM (architecture-school class).
- Track C-proxy: off-the-shelf wood-filled PLA + ASA or PETG restrictor.
  This is a method change and must be labelled. Do not call a wood-PLA
  print a Cheng 2024 replicate.
- Do not start at 424 unique modules. One geometry, n_rep = 3.
- Humidity box already specified in test-protocol.md (PR #8) can be
  reused at 30% and 90% RH (Cheng set-points), but those are not the
  Birch 42% / >95% spore set-points. Do not pool the two campaigns.

[DESIGN-PROPOSAL] Programming axis instead of spore n_layers: extrusion
path direction, actuating/restricting path offset, flap tessellation
(Cheng programmed 424 unique curl directions), and optional vent
override.

### 4.6 Why it could replace D03

[DESIGN-PROPOSAL] Closest "same job, better evidence" replacement:
passive hygromorph, programmable geometry, zero operational energy,
already run at building-facade quantity.

[DESIGN-PROPOSAL] Addresses all four spore weaknesses:
- Angle / programming: print-path programming does not inherit Birch's
  4-layer plateau (DOI 10.3390/su13074030).
- Cycle life: 170 lab cycles + 13-month outdoor mock-up vs Birch's 10
  latex cycles and Chen's polyimide-only 1e6 result.
- Germination: none. Cellulose/PK and ASA are non-living.
- Cork: unused. Substrate is the printed bilayer itself.

[DESIGN-PROPOSAL] materials/selection-matrix.md already named this
paper as the architectural hygromorph fallback. This file makes that
a ROLE 03 replacement path, not a built HE prototype.

[DESIGN-PROPOSAL] Remaining gap vs spores: Cheng 30 min vs Birch <3 min
on latex. If HE's D03 selling point is "faster than wood", Cheng is in
the wood-like time band, not the spore-latex band.

### 4.7 Failure modes

[LITERATURE-CONFIRMED] First-10-cycle curvature settling at high RH
(Cheng et al. 2024, DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] UV-driven curvature drop on the active face at
low RH; long-term UV mechanism not fully mapped (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Authors flag mechanical wear over a building
lifetime as future work (DOI 10.1038/s41467-024-54808-8).

[LITERATURE-CONFIRMED] Direct rain is avoided in Cheng's design by
hanging the prints in a vented double-skin cavity
(DOI 10.1038/s41467-024-54808-8). Exposed outdoor prints are not the
published configuration.

[DESIGN-PROPOSAL] HE-specific: custom filament compounding is not
desk-scale (twin-screw extruder). A wood-PLA proxy may delaminate,
creep, or lose hygro-stroke. Hot-humid Australian summers invert
Cheng's temperate "dry-hot = closed" assumption (Cheng discussion
already names tropical climates as unproven). Fire class of printed
biocomposite / ASA is not a Cheng result and must not be invented.

### 4.8 Citations (Alternative 3)

- Cheng, T., Tahouni, Y., Sahin, E.S., Ulrich, K., Lajewski, S.,
  Bonten, C., Wood, D., Ruhe, J., Speck, T. and Menges, A.
  Weather-responsive adaptive shading through biobased and bioinspired
  hygromorphic 4D-printing. Nature Communications 15, 10366 (2024).
  DOI 10.1038/s41467-024-54808-8

Spore-baseline papers used only for the comparison columns:

- Chen, X., Mahadevan, L., Driks, A. and Sahin, O. Bacillus spores as
  building blocks for stimuli-responsive materials and nanogenerators.
  Nature Nanotechnology 9, 137-141 (2014). DOI 10.1038/nnano.2013.290
- Chen, X. et al. Scaling up nanoscale water-driven energy conversion
  into evaporation-driven engines and generators. Nature Communications
  6, 7346 (2015). DOI 10.1038/ncomms8346
- Birch, E., Bridgens, B., Zhang, M. and Dade-Robertson, M. Bacterial
  spore-based hygromorphs: a novel active material with potential for
  architectural applications. Sustainability 13, 4030 (2021).
  DOI 10.3390/su13074030

---

## 5. Comparison table vs spore baseline weaknesses

Values in the spore column are [LITERATURE-CONFIRMED] from the verified
brief (see Section 1). Alternative columns are [LITERATURE-CONFIRMED]
where a number or fact is taken from the named paper, and
[DESIGN-PROPOSAL] where the cell is an HE interpretation.

| Weakness (spore D03) | Spore baseline | Alt 1 Wood / wood-composite | Alt 2 SMA / Nitinol | Alt 3 Cellulose 4D print |
|----------------------|----------------|-----------------------------|---------------------|--------------------------|
| Angle / programming plateau | Angle plateaus ~4 monolayers (~43 deg); force may still rise (Birch 2021, DOI 10.3390/su13074030) [LITERATURE-CONFIRMED] | Programming by grain, thickness, perforation, inverse stack - no 4-layer coat cap [DESIGN-PROPOSAL] using Holstov/Reichert mechanism [LITERATURE-CONFIRMED] | Programming by Af, wire length, pulley, parallel count; discrete 90 deg or 180 deg strokes (Stelzmann 2024; Vercesi 2020) [LITERATURE-CONFIRMED] | Programming by FFF path and flap tessellation (424 unique modules, Cheng 2024) [LITERATURE-CONFIRMED] |
| Cycle-life / substrate mismatch | Latex: 10 cycles (Birch 2021). 1e6 cycles = polyimide HYDRA, slight loss, not "100% stable" (Chen 2015) [LITERATURE-CONFIRMED] | 1-year roof weathering; ~10% stroke loss on 1 mm birch; oak/larch better (Holstov 2017) [LITERATURE-CONFIRMED] | SMA chosen in reviews for cycle durability, but facade papers emphasise fatigue at bends, stress-shifted temps, overcast miss (Fiorito 2016; Stelzmann 2024) [LITERATURE-CONFIRMED] | 170 lab cycles (settle in first 10 at 90% RH) + 13-month outdoor mock-up, no reported mechanical damage (Cheng 2024) [LITERATURE-CONFIRMED] |
| Germination / living-material gap | Explicit Birch gap: germination control + real-environment durability (DOI 10.3390/su13074030) [LITERATURE-CONFIRMED] | Non-living; decay/mould replace germination (Holstov 2017) [LITERATURE-CONFIRMED] | Non-living metal; fatigue/fracture replace germination [LITERATURE-CONFIRMED] | Non-living cellulose/PK + ASA; no germination (Cheng 2024) [LITERATURE-CONFIRMED] |
| Cork unverified | No cork+spore actuator data in the brief; literature substrates = latex, polyimide, silicon, elastomer [LITERATURE-CONFIRMED] | Veneer + plywood / GFRP / jute; cork not required (Holstov 2015/2017) [LITERATURE-CONFIRMED] | Aluminium / polymer fin + NiTi; cork not required (Formentini 2017; Stelzmann 2024) [LITERATURE-CONFIRMED] | Printed bilayer is the substrate; cork not required (Cheng 2024) [LITERATURE-CONFIRMED] |
| Trigger | Humidity / water activity (Chen 2014/2015; Birch 2021) [LITERATURE-CONFIRMED] | Humidity + wetting (Holstov; Reichert) [LITERATURE-CONFIRMED] | Temperature / solar radiation (Formentini; Fiorito; Vercesi; Stelzmann) [LITERATURE-CONFIRMED] | Humidity + temperature (Cheng 2024) [LITERATURE-CONFIRMED] |
| Response-time band | ~3 s (polyimide HYDRA, Chen 2015); <3 min (0.5 mm latex, Birch 2021) [LITERATURE-CONFIRMED] | 20-30 min to 80% stroke on wetting; hours to seasonal if thick (Holstov 2017) [LITERATURE-CONFIRMED] | Seconds if Joule-heated; minutes if solar-collector heated; overcast may never switch (Stelzmann 2024) [LITERATURE-CONFIRMED] / [DESIGN-PROPOSAL] for the seconds band as a bench tool | Full 30<->90% RH stroke within 30 min (Cheng 2024) [LITERATURE-CONFIRMED] |
| Architectural precedent | 1 cm x 2 cm latex (Birch); 2024 aperture prototypes; no HE panel [LITERATURE-CONFIRMED] | HygroSkin / HygroScope; Holstov cladding modules and Kielder proposal (Reichert 2015; Holstov 2017) [LITERATURE-CONFIRMED] | Ventilated-facade panel prototype (Formentini); 1:1 louver demonstrator (Stelzmann); twisting-cylinder apparatus (Vercesi) [LITERATURE-CONFIRMED] | 13-month mock-up + 9.37 m^2 / 424-module livMatS facade (Cheng 2024) [LITERATURE-CONFIRMED] |
| Desk-scale HE fab (AU workshop) | Pipette + PLL + latex is literature; cork/spin-coat/40 C/parylene is not [LITERATURE-CONFIRMED] / [DESIGN-PROPOSAL] | Laser-cut veneer bilayer is workshop-feasible [DESIGN-PROPOSAL] | Buy NiTi wire/spring + cut a fin; collector optional later [DESIGN-PROPOSAL] | Dual-extruder FFF is workshop-feasible; Cheng filament is custom (proxy must be labelled) [DESIGN-PROPOSAL] |
| Built for HE? | No [DESIGN-PROPOSAL] | No [DESIGN-PROPOSAL] | No [DESIGN-PROPOSAL] | No [DESIGN-PROPOSAL] |

---

## 6. Suggested replacement order if D03 fails (proposal only)

This section is entirely [DESIGN-PROPOSAL]. It is not a selection result
and it does not retire spores.

1. If the failure is germination, BSL, cork, or 10-cycle latex vs 1e6
   HYDRA confusion: prefer Alternative 3 (Cheng cellulose 4D print) as
   the nearest documented facade hygromorph, then Alternative 1 (wood)
   if FFF cellulose filament cannot be sourced.
2. If the failure is force / inability to move anything larger than a
   1 cm x 2 cm latex strip: prefer Alternative 2 (SMA / Nitinol).
3. If the failure is "we need a humidity encoder with no custom filament
   and no alloy": prefer Alternative 1 (wood bilayer).
4. Do not mix the three into one coupon. Do not put spores on Cheng
   prints or NiTi on veneer and call it D03.

materials/selection-matrix.md already scored mechanical metamaterials
highest as a general prototype family. That family is not one of the
three ROLE 03 alternatives requested here. It remains a separate
project recommendation, not a fourth D03 replacement in this file.

---

## 7. What this file does not claim

- No HE wood, SMA, or cellulose coupon has been fabricated or tested.
- No theta, force, cycle, or shade-coverage number is an HE result.
- No DOI was invented. Alternative DOIs are the named Holstov / Reichert /
  Formentini / Fiorito / JFDE / Actuators 2024 / Cheng 2024 papers.
  Spore DOIs are only those in the 2026-09-23 verified literature brief.
- No Octopus-system content.
- No new discovery. Law 3: no new discoveries until CRITIC writes
  unsupported-claims.md.

If a later campaign never builds these coupons, this file remains a
proposal.

---

## 8. Pointers

- Spore metrics and AI-CONTEXT.md D03 mismatches:
  `agents/materials/spore-data-survey.md` (PR #6)
- Spore coupon fabrication:
  `agents/materials/fabrication-protocol.md` (PR #6)
- Spore humidity-chamber protocol (not for SMA):
  `agents/materials/test-protocol.md` (PR #8)
- Project material scores (includes Cheng 2024 as hygromorph fallback):
  `materials/selection-matrix.md`
- Project D03 one-liner (contains unverified cork / 1e6 / monotone lines):
  `AI-CONTEXT.md` section D03
