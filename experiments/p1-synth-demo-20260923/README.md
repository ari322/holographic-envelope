# P1 SYNTHETIC_DEMO results (2026-09-23)

**run_id:** `p1-20260923-synth-demo-v1`  
**climate_tag:** `SYNTHETIC_DEMO` only — not EPW, not validated weather.

## Claim discipline

- This package is a **SYNTHETIC_DEMO** only.
- It does **not** prove intelligence, holographic equivalence, RSB, or spin-glass identity.
- Gate labels are kinetic / interactive / **candidate** (candidate = ≥3/5 with named controls).

## Gate summary (Y/5)

| Treatment | Y/5 | Label |
|-----------|-----|-------|
| T0 Fixed closed | 0 | kinetic |
| T1 Fixed open | 0 | kinetic |
| T2 Homogeneous memoryless | 2 | interactive |
| T3 Homogeneous hysteretic | 4 | **candidate** |
| T4 Heterogeneous hysteretic | 4 | **candidate** |
| T5 Random heterogeneous | 2 | interactive |
| T6 Coupled | 4 | **candidate** |
| T7 (control / other) | 2 | interactive |

Candidates at ≥3/5: **T3, T4, T6**.

## Caveats

- Moran self-org proxy ≈ 0 where reported (no strong spatial self-organization claim).
- Two-history instrumented only for T2/T3/T4.
- Local RECEIPT sha256: `02ea605cb073563f51df29159f42568b9dbb20a1721657f1210c82e7586e279f`

## Layout

- `scripts/p1_synth_sim.py` — simulator
- `climate/synthetic_v1.csv` — synthetic climate
- `csv/` — cell rows T0–T7 + twohist T2/T3/T4
- `agg/` — per-treatment JSON + gate_summary
- `P1-GATE-SCORECARD-FILLED.md`, `IS-STATUS-NOTES.md`, `RECEIPT.md`, `SHA256SUMS.txt`
