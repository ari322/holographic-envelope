# Grasshopper complete node sequence (all 5 steps)

SIMULATOR Role 02 Task 1. Pseudocode for a Rhino 7/8 + Grasshopper definition.
This file fills the missing detail on steps 02 (radiation), 03 (controller),
and 05 (Wallacei). Steps 01 and 04 are restated so the chain is one document.

Plugins: Ladybug Tools 1.7+, Honeybee, GhPython (built-in), Wallacei X.
No `.gh` binary is produced here. Build the canvas from this sequence.
Gene bounds and objectives match `prompts/prompts-algorithmic.md` A01–A04 and
`grasshopper/optimization-setup.md`. Do not treat this as a completed Wallacei run.

Data tree rule: keep one item per panel on `{0;i}` for i = 0..79. Graft and
Entwine only when lists go out of sync.

---

## Step 01 — Geometry (10 x 8 = 80 panels)

Source: `grasshopper/step-01-geometry.md`, prompt A01.

Facade: 10 m x 8 m rectangle, north-facing in Sydney (southern hemisphere).
Each panel: 1 m x 1 m box, depth = gene `d`, pivot on the top edge,
rotation `theta` in [0, 90] deg.

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 1.1 | Number Slider `panel_depth` | 50..300 mm, named `d` | — | 1.3, 1.5, Wallacei Gene 1 |
| 1.2 | Surface (or Rectangle + Boundary) | 10 m x 8 m in World XY, then Orient to facade plane | Rhino surface or constructed rectangle | 1.4 |
| 1.3 | Unit Z (or Amplitude along facade normal) | length = `d` (convert mm to m: `d / 1000`) | 1.1 | 1.5 |
| 1.4 | Divide Surface | U = 10, V = 8, quad split | 1.2 | points (80), normals (80) |
| 1.5 | Construct Point | offset each centre by `-d/2` along the normal | 1.4 points, 1.4 normals, 1.3 | box origins |
| 1.6 | Box | X=1 m, Y=1 m, Z=`d` (m), plane = Surface Frame at centre | 1.5, 1.1 | 80 panel Breps |
| 1.7 | Surface Frames (or Plane Normal) | Z = facade normal, Y = world up | 1.4 | 80 planes |
| 1.8 | Line | top edge of each box (two corners with max Z in panel plane) | 1.6 | 80 pivot axes |
| 1.9 | Number Slider `rotation_angle` | 0..90 deg, named `r` (manual test) | — | 1.11 |
| 1.10 | Wallacei Gene 3 | same range as 1.9; mute 1.9 when Wallacei is running | Wallacei | 1.11 |
| 1.11 | Stream Filter (or GeneList switch) | item 0 = slider, item 1 = Wallacei | 1.9, 1.10 | 1.12 |
| 1.12 | Rotate 3D | axis = 1.8, angle = 1.11 (radians) | 1.6, 1.8, 1.11 | rotated panel Breps |
| 1.13 | Number Slider `aperture_ratio` | 0.1..0.9, named `a` | — | Step 03 / geometry scale |
| 1.14 | Scale NU (optional aperture) | scale panel opening in-plane by `a` | 1.12, 1.13 | aperture Breps |

Outputs to later steps:

- `panel_breps` (80) → Step 02 mesh
- `panel_centres` (80) → Step 02 / occupancy
- `panel_normals` (80) → Ladybug context
- `pivot_axes` (80) → Step 03 geometry response

---

## Step 02 — Ladybug radiation and Honeybee daylight (was missing)

Source: prompt A02, `grasshopper/workflow.md` Steps B–C,
`validation/simulation-baseline.md`.

This step produces **f1** (mean incident radiation) and **f2** (daylight
deficit). Until this canvas is solved against a real EPW, use the geometric
proxies in `facade-sim.py` only as a stand-in. Do not paste proxy numbers
into a results table as Ladybug/Honeybee output.

### 02A — EPW and sky

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 2.1 | File Path | Sydney Observatory Hill or Bankstown `.epw` (energyplus.net/weather) | — | 2.2 |
| 2.2 | LB Import EPW | location, dry bulb, GHI, DNI, DHI, wind, ground temp | 2.1 | 2.3, 2.4 |
| 2.3 | LB Location | north angle: project north (Sydney facade faces north = 0 deg if model Y is north) | 2.2 location | 2.5 |
| 2.4 | LB Analysis Period | annual HOY 1–8760; optional summer-only 1 Dec–28 Feb | — | 2.5 |
| 2.5 | LB SkyMatrix | sky density = 1 (Tregenza) to start; 2 if time allows | 2.2, 2.3, 2.4 | 2.8 |

### 02B — Incident radiation = f1

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 2.6 | Mesh Brep | meshing = simple, one face per panel if possible | Step 01 `panel_breps` | 2.8 |
| 2.7 | Context mesh (optional) | adjacent buildings / ground | Rhino | 2.8 |
| 2.8 | LB Incident Radiation | geometry = 2.6, sky = 2.5, context = 2.7, offset 10 mm along normal | 2.5, 2.6, 2.7 | per-panel kWh/m2/year (80 values) |
| 2.9 | Mass Addition + Division | sum / 80 | 2.8 | **f1** mean kWh/m2 |
| 2.10 | Panel (readout) | name `f1_mean_radiation` | 2.9 | Wallacei objective 1 |

Notes from `workflow.md`: LB Incident Radiation does not include inter-panel
reflections by default. Keep panel index order identical to Step 01.

### 02C — Honeybee UDI → daylight deficit = f2

Occupied hours: 8:00–18:00 weekdays (prompt A02, simulation-baseline.md).
f2 = fraction of occupied hours with zone illuminance **below 300 lux**.

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 2.11 | Extrude / Cap | extrude facade inward 6 m to a closed room (min Honeybee Room) | Step 01 surface | 2.12 |
| 2.12 | HB Room from Solid | name `HE_zone`, program = Office | 2.11 | 2.14 |
| 2.13 | HB Aperture | add window on facade face; area fraction = gene `a` (or fixed 0.4 for first run) | 1.13 | 2.14 |
| 2.14 | HB Model | rooms + apertures + shade = Step 01 panels as orphaned shades | 2.12, 2.13, 1.12 | 2.16 |
| 2.15 | HB Sensor Grid from Rooms | offset 0.8 m, spacing 0.5 m | 2.12 | 2.16 |
| 2.16 | HB Wea from EPW | same file as 2.1 | 2.2 | 2.17 |
| 2.17 | HB Annual Daylight | Radiance params `-ab 2 -ad 5000` for first pass | 2.14, 2.15, 2.16 | ill_result |
| 2.18 | HB Annual Daylight Metrics | UDI low threshold = 300 lux; schedule = weekdays 8–18 | 2.17, occupancy schedule | UDI_low per sensor |
| 2.19 | Average | mean UDI_low across sensors (fraction of occupied hours < 300 lux) | 2.18 | **f2** |
| 2.20 | Panel | name `f2_daylight_deficit` | 2.19 | Wallacei objective 2 |

If Honeybee is too slow inside a Wallacei loop: compute f2 once per
individual with a coarser grid (`-ab 1`) or cache Wea. Do not silently
replace f2 with the `facade-sim.py` lux proxy inside a results claim.

### 02D — Hourly radiation list for the controller

LB Incident Radiation is annual-cumulative. The Step 03 controller needs
**hourly** per-panel irradiance.

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 2.21 | LB Direct Sun Hours or LB Incident Radiation with `cumulative_ = False` / HOY loop | analysis period = 2.4; if annual 8760 is too heavy, run a representative week first | 2.5, 2.6 | `radiation[panel][hour]` |
| 2.22 | GHPython flatten | reshape to list-of-lists length 80 x T | 2.21 | Step 03 `radiation` |

Alternative (no Ladybug hourly): feed `agents/simulator/facade-sim.py`
weather arrays into a GhPython node. Label that path **proxy**, not Ladybug.

---

## Step 03 — State controller (was missing)

Source: `grasshopper/ghpython_state_controller.py`,
`research/formal-model.md`, `grasshopper/workflow.md` Steps D–F.

GhPython does not keep memory across solutions. Persist `previous` with a
Data Recorder, Hoopsnake, or an external hourly loop (Anemone / GHPython
`for t in hours`).

### 03A — Occupancy (synthetic unless sensors exist)

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 3.1 | Construct Point (or Populate 3D) | occupant points inside the room, weekday 8–18 denser | — | 3.2 |
| 3.2 | Distance | from each occupant cloud to each panel centre | 3.1, Step 01 centres | 3.3 |
| 3.3 | Remap Numbers | 0 at 0 m → 1, far → 0, then invert so near = high occupancy | 3.2 | `occupancy` list [0,1] x 80 |
| 3.4 | Boolean (weekday and hour) | hour in [8, 18) and weekday < 5; else scale occupancy by 0.1 | clock / HOY | gate on 3.3 |

Workflow.md notes occupancy is currently synthetic.

### 03B — Gene-driven controller parameters

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 3.5 | Number Slider `epsilon` | 0.01..0.15 | — | 3.8 / Wallacei Gene 4 |
| 3.6 | Number Slider `maxStep` | 0.05..0.30 | — | 3.8 / Wallacei Gene 5 |
| 3.7 | Number Slider `wr` | 0.2..0.8 | — | 3.8 / Wallacei Gene 6 |
| 3.8 | Expression | `wu = 1 - wr` (GhPython uses wr + wu only) | 3.7 | 3.9 `wu` |

### 03C — GhPython controller node

Paste `grasshopper/ghpython_state_controller.py`. Inputs (type hint: float
list or item):

| Input | Type | Source |
|-------|------|--------|
| `radiation` | list[float] | Step 02 hourly (2.22), one value per panel |
| `occupancy` | list[float] | 3.3 |
| `previous` | list[float] | 3.11 recorder (or 0.5 x 80 on first tick) |
| `wr` | float | 3.7 / Wallacei Gene 6 |
| `wu` | float | 3.8 |
| `threshold` | float | 3.5 (`epsilon`) |
| `maxStep` | float | 3.6 |

Output `a` = `states` in [0, 1], length 80.

Formal-model extras (optional, not in the current GhPython file):

- SAFE: if wind from EPW > 15 m/s, set all states to 0 (closed).
- Mapping: `o = clamp(wr*R + wt*T + wc*C + wu*U)`. The checked-in GhPython
  uses `solar_response = 1 - R` (high radiation closes). Keep that sign so
  the canvas matches `facade-sim.py` and the existing node.

### 03D — Time loop and geometry response

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 3.9 | Anemone Loop Start (or GHPython `for t`) | T = 168 (week) or 8760 (year) | HOY series | 3.10 |
| 3.10 | GhPython controller | code from 03C | radiation_t, occupancy_t, previous | `states_t` |
| 3.11 | Data Recorder / Loop End | record `states_t` as previous | 3.10 | next tick + archive |
| 3.12 | Remap | state 0 → 0 deg, state 1 → gene `r` deg | 3.10, 1.11 | `panel_angle_series` [80][T] |
| 3.13 | Rotate 3D | same axes as 1.8, angle = 3.12 | Step 01 boxes | animated panels |
| 3.14 | Scale | in-plane opening *= gene `a` | 3.13, 1.13 | shaded aperture |

Actuation count for **f4**: in the same GhPython, increment a counter when
`abs(state - previous) > 0` after the hysteresis gate. Mean daily events
per panel = total moves / (T / 24). Output that scalar as Wallacei
objective 4.

**f3** unique geometries: with one gene vector, all 80 panels share
`(d, a, r)` so f3 = 1. If a D03 layer list is grafted later, f3 = number of
unique `n_layers`. Output as Wallacei objective 3.

---

## Step 04 — TFE

Source: `grasshopper/step-04-TFE.md`, prompt A03, MATH-SKELETON 1.4.

| # | Component | Parameters | Incoming | Outgoing |
|---|-----------|------------|----------|----------|
| 4.1 | GHPython TFE | paste prompt A03 | `panel_states` = angle/90, shape [80][T] | `TFE_total`, `H_space`, `H_time` |
| 4.2 | Bins | 5 bins: [0–18], [18–36], [36–54], [54–72], [72–90] deg | encoded in A03 as `n_bins = 5` on [0,1] | — |
| 4.3 | Negative | `f_TFE_neg = -TFE_total` | 4.1 | optional extra objective (Wallacei minimises) |

Expected ranges (step-04-TFE.md; not measured here): static ≈ 0;
rule-based ≈ 0.1–0.5. A03 `TFE_total` is the mean of `H_space(t) * H_time(i)`.

Wallacei A04 lists four objectives (f1–f4), not TFE. Compute TFE as a
diagnostic on the controller log. Only wire `f_TFE_neg` if a fifth
objective is explicitly added later.

---

## Step 05 — Wallacei X (was missing)

Source: prompt A04, `grasshopper/optimization-setup.md`,
AI-CONTEXT.md RSB protocol.

### 05A — Genome (6 continuous sliders → Wallacei Gene List)

| Slot | Name | Range | Units | Also wired to |
|------|------|-------|-------|----------------|
| Gene 1 | `panel_depth` / `d` | 50–300 | mm | Step 01 box depth |
| Gene 2 | `aperture_ratio` / `a` | 0.1–0.9 | — | Step 01 scale, HB aperture |
| Gene 3 | `rotation_angle` / `r` | 0–90 | deg | Step 01 / 03 rotate |
| Gene 4 | `hysteresis_epsilon` / `eps` | 0.01–0.15 | — | Step 03 `threshold` |
| Gene 5 | `maxStep` / `ms` | 0.05–0.30 | — | Step 03 `maxStep` |
| Gene 6 | `radiation_weight` / `wr` | 0.2–0.8 | — | Step 03 `wr` |

Connect sliders to **Wallacei Gene List** in this order. Disable the
manual Stream Filter (1.11) so Wallacei owns the six values during a run.

### 05B — Objectives (all minimise)

| Slot | Name | Source component | Unit |
|------|------|------------------|------|
| f1 | mean incident radiation | 2.9 | kWh/m2 |
| f2 | daylight deficit | 2.19 | fraction 0–1 |
| f3 | unique panel geometry types | Step 03 f3 (usually 1) | count |
| f4 | mean daily actuation events per panel | Step 03 f4 | events/day |

Connect to **Wallacei Fitness Values** in this order. Wallacei minimises
each. Do not invert f1–f4.

### 05C — Solver settings (prompt A04)

| Setting | Value |
|---------|--------|
| Population | 50 |
| Generations | 100 |
| Crossover | 0.9 |
| Mutation | 0.1 |
| Algorithm | NSGA-II (Wallacei X default) |
| Independent runs | 5 |
| Seeds | 42, 137, 256, 891, 1024 |

Procedure: set the Wallacei random seed, Run, Export, change seed, repeat.
Do not reuse a single export as five runs.

### 05D — Exports required for RSB detection

After each run, export from Wallacei (CSV or JSON):

1. Full Pareto set: 6 genes + 4 objectives per individual.
2. Convergence / standard deviation plots (Wallacei UI is enough).
3. Keep run id and seed in the filename, e.g. `wallacei_seed042.csv`.

Downstream (not Grasshopper):

```
python agents/simulator/rsb-detection.py --input <real-or-synthetic>.json
```

Distance used by the detector (MATH-SKELETON 3.4):

    d(g_a, g_b) = ||g_a - g_b||_2 / sqrt(6)

`agents/simulator/synthetic-pareto.json` is a **SYNTHETIC** 5 x 50 fixture
for testing that script. It is not a Wallacei export. A dip-test / GMM hit
on that file is not confirmation of RSB or Discovery 02.

### 05E — Canvas checklist before the first real run

1. EPW path resolves (Sydney Observatory Hill or Bankstown).
2. 80-panel tree is aligned across geometry, radiation, occupancy, states.
3. Controller loop writes `previous` (otherwise f4 = 0 and states freeze).
4. Four fitness numbers update when sliders move (smoke test before Wallacei).
5. Five seeds recorded; exports labelled with seed and date.

---

## End-to-end data flow

```
Step 01 geometry (d, a, r)
    -> Step 02 Ladybug f1 + Honeybee f2 + hourly radiation
    -> Step 03 occupancy + GhPython hysteresis (eps, maxStep, wr)
         -> panel_angle_series [80][T]
         -> f3 geometries, f4 actuations
    -> Step 04 TFE diagnostic (A03)
    -> Step 05 Wallacei: genes 1-6, minimise f1-f4, 5 seeds
         -> export Pareto JSON/CSV
         -> agents/simulator/rsb-detection.py  (real export only for D02 test)
```

Python stand-in while the `.gh` file is unbuilt: `agents/simulator/facade-sim.py`.
That module does not replace Steps 02 or 05 on a real EPW Wallacei run.
