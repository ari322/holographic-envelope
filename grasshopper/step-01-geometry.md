# Grasshopper Step 01 — Base Geometry

## Goal
Build the parametric facade geometry: 80 pivoting panels on a 10×8 grid.

## Node Sequence

```
[Number Slider] panel_depth = 50..300 mm
    → [Unit Z] scale Z by panel_depth
    → feeds into [Box] component as height

[Surface] 10m × 8m rectangle
    → [Divide Surface] u=10, v=8
    → 80 centre points + 80 normal vectors

[Construct Point] offset each centre by -panel_depth/2 in normal direction
    → [Box] width=1m, height=1m, depth=panel_depth
    → 80 panel boxes

[Line] top edge of each panel box
    → [Rotate 3D] axis = top edge, angle = rotation_gene
    → 80 rotated panels

[Gene_rotation] from Wallacei gene slot 3
    → [Remap] from [0,1] to [0,90] degrees
    → feeds into [Rotate 3D] angle input
```

## Parameters Exposed to Wallacei
- Gene 1 → panel_depth slider
- Gene 2 → aperture_ratio slider (controls panel opening fraction)
- Gene 3 → rotation_angle slider
- Genes 4,5,6 → controller parameters (used in Step 03)

## Output
- Geometry: 80 rotated panel Breps
- Panel centre points (for radiation analysis)
- Panel normal vectors (for Ladybug)
