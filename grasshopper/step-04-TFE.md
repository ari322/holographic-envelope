# Grasshopper Step 04 — TFE Computation

## Goal
Compute Temporal Facade Entropy from panel state time series.
This is objective f_TFE which we MAXIMISE (invert for Wallacei which minimises).

## Data Flow

```
[Step 03 controller output]
    → panel_angle_series: list[80][8760]  (angle per panel per hour)
    → normalise: panel_state = angle / 90.0 ∈ [0,1]

[GHPython: TFE node]
    → input: panel_states (list[80][8760])
    → code: paste from prompts/prompts-algorithmic.md A03
    → output: TFE_total (float)

[Negate] TFE_total × (-1)
    → feeds into Wallacei as objective f_TFE_neg
    → Wallacei minimises f_TFE_neg = maximises TFE
```

## Discretisation Note
Panel states are continuous angles [0°, 90°].
For entropy computation, discretise into 5 bins:
  [0-18°], [18-36°], [36-54°], [54-72°], [72-90°]
This gives H_max = log2(5) = 2.32 bits per panel.

## Expected TFE Range
- Static facade (all panels identical, fixed): TFE ≈ 0
- Rule-based facade (all panels move together): TFE ≈ 0.1–0.5
- Optimised adaptive facade: TFE ≈ 1.5–4.0
- Maximum theoretical: TFE = log2(5) × log2(8760/bin_size) ≈ 2.32 × 3.46 ≈ 8.0
