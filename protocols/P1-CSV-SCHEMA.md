# P1 CSV Schema — cell tick log
stamp: 2026-09-23 ~19:07 AEST  
canonical header file: `protocols/p1_cells.csv.header`  
claim_type discipline: rows are **measurements / protocol logs**, not validated science claims

---

## Cell tick CSV (required)

One row per cell per timestep. Encoding: UTF-8, comma-separated, LF newlines, header on first line.

| Column | Type | Required | Description |
|---|---|---|---|
| `run_id` | string | yes | Stable id, e.g. `p1-20260923-t3-a` |
| `treat_id` | enum | yes | `T0`…`T7` |
| `t` | int | yes | Hour index from chronicle start (0-based) |
| `i` | int | yes | Row index 0..3 |
| `j` | int | yes | Col index 0..3 |
| `theta` | float | yes | Panel angle (deg or rad — declare in run meta); NaN forbidden |
| `aperture` | float | yes | ∈[0,1] effective openness |
| `G_rad` | float | yes | Incident radiation proxy at cell (W/m² or normalised — declare) |
| `RH` | float | yes | Relative humidity % |
| `T_air` | float | yes | Air temperature °C |
| `occ` | float | yes | Occupancy proxy ∈[0,1] |
| `H_space` | float | yes | Spatial Shannon entropy of aperture field at `t` (same value on all 16 rows for that `t`) |
| `mean_abs_dtheta` | float | yes | Mean \|Δθ\| across cells vs previous `t` (0 at t=0) |
| `notes` | string | yes | Must include climate tag `SYNTHETIC_DEMO` or `EPW_…`; free text after |

### Exact header line

```
run_id,treat_id,t,i,j,theta,aperture,G_rad,RH,T_air,occ,H_space,mean_abs_dtheta,notes
```

Identical content lives in `p1_cells.csv.header` (no trailing newline required beyond single LF).

---

## Aggregate JSON (per treatment, companion)

Suggested keys (not CSV):

```json
{
  "run_id": "p1-…",
  "treat_id": "T3",
  "climate_tag": "SYNTHETIC_DEMO",
  "neighbor_graph": "von_neumann_4",
  "theta_units": "deg",
  "K_bins": 5,
  "response_time_h": null,
  "recovery_time_h": null,
  "hysteresis_loop_area": null,
  "Moran_I": null,
  "two_history_delta_theta": null,
  "gate_scores": {"sensing": null, "memory": null, "feedback": null, "self_org": null, "adaptation": null}
}
```

Leave nulls until measured. Do not invent numbers.

---

## Two-history companion CSV (optional separate file)

Same columns as cell tick; set `notes` to include `TWO_HISTORY;hist=A|B;xstar=…`. See `P1-TWO-HISTORY.md`.

## Validation rules (operator)

1. Exactly 16 rows per `(run_id,treat_id,t)`.
2. `treat_id` ∈ {T0,T1,T2,T3,T4,T5,T6,T7}.
3. `i,j` cover full grid with no duplicates per `t`.
4. `notes` contains climate tag.
5. No empty required fields.

## Non-goals

Schema does not encode BIR, RSB, holography, or market fields.
