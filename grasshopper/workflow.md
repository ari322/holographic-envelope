# Grasshopper Workflow Documentation

## Status: Step 4 — Complete

---

## Required plugins

- Rhino 7 or 8
- Grasshopper (built-in)
- Ladybug Tools 1.7+ (Ladybug, Honeybee)
- Kangaroo 2 (optional, for structural constraints)
- Wallacei or Galapagos (for Step 8 optimisation)
- GhPython (built-in)

---

## Full component chain

```
Step A — Base geometry
Rhino Surface
  -> Grasshopper: Surface component
  -> Divide Domain2 (U=10, V=20 as starting grid)
  -> Isotrim  -> individual panel surfaces
  -> Area     -> panel centroid points
  -> Surface Frames -> local XYZ axes per panel

Step B — Solar analysis
  -> LB Import EPW   (load local weather file)
  -> LB SkyMatrix    (annual or monthly cumulative)
  -> LB Incident Radiation (mesh = panel centroids, sky = SkyMatrix)
  -> output: radiation list per panel [kWh/m2]

Step C — Daylight check (optional Honeybee)
  -> HB Model from Room surfaces
  -> HB Radiance Simulation
  -> output: UDI per zone [lux-hours]

Step D — Occupancy input
  -> GhPython or Panel component: occupancy values per zone
  -> Point cloud of agent positions -> proximity to panel centroids
  -> Distance -> Remap -> occupancy density list [0,1]

Step E — State controller
  -> GhPython: ghpython_state_controller.py
  -> inputs: radiation, occupancy, previous, wr, wu, threshold, maxStep
  -> output: states list [0,1] per panel

Step F — Geometry response
  -> Remap states to rotation angle (e.g. 0 -> 0 deg, 1 -> 75 deg)
  -> Rotate panel aperture geometry around panel centroid axis
  -> OR Scale aperture opening within panel boundary
  -> Boundary Surface or Brep Join

Step G — Visualisation
  -> Gradient: states -> colour map (blue=closed, red=open)
  -> Custom Preview on panel surfaces
  -> Number readout: H(t) Shannon entropy across facade

Step H — Bake / Export
  -> Bake final geometry for Rhino model
  -> Export panel data as CSV: [panel_id, radiation, occupancy, state, angle]
```

---

## Data Tree structure

```
Panels: {0;0} to {0;N-1}   (N = total panel count)
Each branch: one item per panel

radiation  {0;i}  -> float
occupancy  {0;i}  -> float
states     {0;i}  -> float
frames     {0;i}  -> Plane
```

All lists must be synchronised by index. Use Entwine or Graft carefully to avoid mismatched branches.

---

## EPW file setup

1. Download EPW for your project location from EnergyPlus Weather Data (energyplus.net).
2. For Sydney/Castle Hill area: use Sydney Observatory Hill or Bankstown EPW.
3. Connect file path to LB Import EPW component.
4. LB SkyMatrix: set north angle, analysis period (annual or summer only), sky density.
5. LB Incident Radiation: connect geometry (panel centroids or mesh), sky matrix, and context geometry (adjacent buildings or terrain if available).

---

## Known limitations

- LB Incident Radiation does not account for inter-panel reflections by default.
- Honeybee simulation requires closed Room geometry and takes longer to compute.
- GhPython state list holds no memory between Grasshopper solution cycles; external timer or Human UI slider needed for time-step simulation.
- Occupancy input is currently synthetic; real sensor integration requires Arduino/MQTT bridge or Firefly plugin.
