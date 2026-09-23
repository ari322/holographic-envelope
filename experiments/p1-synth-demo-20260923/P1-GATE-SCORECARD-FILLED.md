# P1 Intelligence Gate Scorecard — FILLED (SYNTHETIC_DEMO)
stamp: 2026-09-23 ~19:30 AEST
rule: Claim “intelligent structure **candidate**” only if ≥3/5 **with named controls**. Else label kinetic / interactive.
**Never** claim intelligence proved. Octopus = exemplar only. Spin-glass equivalence = PARK.

run_id: `p1-20260923-synth-demo-v1`
climate_tag: `SYNTHETIC_DEMO` (recipe=v1 + regime_shift=hotspell_t30_36)
operator: Grok Bot executor (P1 SYNTHETIC_DEMO)
date_AEST: 2026-09-23

> Scores derived from measured CSV/JSON under this demo only. Not EPW. Not validated_result. Not intelligence proof.

## T0 — Fixed closed

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | N | `csv/p1_cells_T0.csv + agg/T0.json; corr_G_rad_mean_aperture=None (fixed state)` |
| 2 | Memory — two-history Δθ > noise? | N/A | `agg/T0.json:memory; not instrumented in this demo (twohist only T2/T3/T4)` |
| 3 | Feedback — prior structure state in update? | N | `agg/T0.json:feedback; memoryless or open-loop / fixed — no prior-state feedback` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T0.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | N | `agg/T0.json:adaptation; recovery_time_h=0.0 (fixed; not adaptive)` |

Subtotal Y: **0** / 5 · Label: **kinetic** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T0.json

## T1 — Fixed open

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | N | `csv/p1_cells_T1.csv + agg/T1.json; corr_G_rad_mean_aperture=None (fixed state)` |
| 2 | Memory — two-history Δθ > noise? | N/A | `agg/T1.json:memory; not instrumented in this demo (twohist only T2/T3/T4)` |
| 3 | Feedback — prior structure state in update? | N | `agg/T1.json:feedback; memoryless or open-loop / fixed — no prior-state feedback` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T1.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | N | `agg/T1.json:adaptation; recovery_time_h=0.0 (fixed; not adaptive)` |

Subtotal Y: **0** / 5 · Label: **kinetic** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T1.json

## T2 — Homogeneous memoryless threshold (control)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T2.csv + agg/T2.json; corr_G_rad_mean_aperture=0.913199` |
| 2 | Memory — two-history Δθ > noise? | N | `csv/p1_twohist_T2.csv; twohist mean|Δθ|=0.000000 (expect ≤ε=0.5); control OK=True` |
| 3 | Feedback — prior structure state in update? | N | `agg/T2.json:feedback; memoryless or open-loop / fixed — no prior-state feedback` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T2.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T2.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **2** / 5 · Label: **interactive** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T2.json

## T3 — Homogeneous hysteretic (IS-0001 / IS-0005)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T3.csv + agg/T3.json; corr_G_rad_mean_aperture=0.913531` |
| 2 | Memory — two-history Δθ > noise? | Y | `csv/p1_twohist_T3.csv; twohist mean|Δθ|=90.000000 mean|Δa|=1.000000 εθ=0.5` |
| 3 | Feedback — prior structure state in update? | Y | `agg/T3.json:feedback; hysteresis hold / coupling uses prior aperture` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T3.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T3.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **4** / 5 · Label: **candidate** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T3.json

## T4 — Heterogeneous hysteretic designed (IS-0002)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T4.csv + agg/T4.json; corr_G_rad_mean_aperture=0.901901` |
| 2 | Memory — two-history Δθ > noise? | Y | `csv/p1_twohist_T4.csv; twohist mean|Δθ|=50.625000 mean|Δa|=0.562500 εθ=0.5` |
| 3 | Feedback — prior structure state in update? | Y | `agg/T4.json:feedback; hysteresis hold / coupling uses prior aperture` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T4.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T4.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **4** / 5 · Label: **candidate** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T4.json

## T5 — Random heterogeneous matched mean/var (IS-0002 control)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T5.csv + agg/T5.json; corr_G_rad_mean_aperture=0.94702` |
| 2 | Memory — two-history Δθ > noise? | N/A | `agg/T5.json:memory; not instrumented in this demo (twohist only T2/T3/T4)` |
| 3 | Feedback — prior structure state in update? | N | `agg/T5.json:feedback; memoryless or open-loop / fixed — no prior-state feedback` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T5.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T5.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **2** / 5 · Label: **interactive** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T5.json

## T6 — Neighbor-coupled k>0 on T3 base (IS-0003)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T6.csv + agg/T6.json; corr_G_rad_mean_aperture=0.915941` |
| 2 | Memory — two-history Δθ > noise? | N/A | `agg/T6.json:memory; T6 inherits T3 hysteresis but twohist not required in runbook for T6` |
| 3 | Feedback — prior structure state in update? | Y | `agg/T6.json:feedback; hysteresis hold / coupling uses prior aperture` |
| 4 | Self-organization — collective ≠ independent? | Y | `agg/T6.json:self_org; Moran_I T6=0.0 vs T3=0.0; hyst_loop T6=308.39256 vs T3=173.340394` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T6.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **4** / 5 · Label: **candidate** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T6.json

## T7 — Open-loop RH hygromorph only (IS-0006)

| # | Criterion | Y/N/NA | Evidence pointer |
|---|---|---|---|
| 1 | Sensing — corr(input, state) significant? | Y | `csv/p1_cells_T7.csv + agg/T7.json; corr_RH_mean_aperture=0.999403` |
| 2 | Memory — two-history Δθ > noise? | N/A | `agg/T7.json:memory; not instrumented in this demo (twohist only T2/T3/T4)` |
| 3 | Feedback — prior structure state in update? | N | `agg/T7.json:feedback; memoryless or open-loop / fixed — no prior-state feedback` |
| 4 | Self-organization — collective ≠ independent? | N | `agg/T7.json:self_org; no neighbor coupling (or not T6)` |
| 5 | Adaptation — proxy recovery after regime shift? | Y | `agg/T7.json:adaptation; recovery_time_h=0.0` |

Subtotal Y: **2** / 5 · Label: **interactive** · Notes: SYNTHETIC_DEMO only; corr/Moran/recovery from agg/T7.json

## Cross-treatment summary

| treat_id | Y-count | Label | Linked IS status note |
|---|---|---|---|
| T0 | 0 | kinetic | null baseline |
| T1 | 0 | kinetic | null baseline |
| T2 | 2 | interactive | memoryless control |
| T3 | 4 | candidate | IS-0001/0005: see IS-STATUS-NOTES.md |
| T4 | 4 | candidate | IS-0002: see IS-STATUS-NOTES.md |
| T5 | 2 | interactive | IS-0002 control |
| T6 | 4 | candidate | IS-0003: see IS-STATUS-NOTES.md |
| T7 | 2 | interactive | IS-0006: see IS-STATUS-NOTES.md |

## Explicit refusals (sign)

- [x] No BIR>1 / hologram claim written
- [x] No RSB / Wallacei claim written
- [x] No spin-glass formal equivalence (PARK)
- [x] No market / NCC activation
- [x] OPEN Jacobian + frustration conflicts left OPEN

**Discipline:** Do not upgrade any `candidate` label to “intelligence proved”. Candidate = ≥3/5 under this synthetic fidelity with named controls only.
