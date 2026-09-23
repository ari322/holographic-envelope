# PACKAGING — incomplete large-file push

**stamp:** 2026-09-23 AEST  
**run_id:** `p1-20260923-synth-demo-v1`

## On branch

- README, scorecard, IS-STATUS-NOTES, RECEIPT, SHA256SUMS
- `climate/synthetic_v1.csv`
- `agg/` including T0–T7, gate_summary, twohist_summaries, `_threshold_maps.json`
- ROADMAP one-line pointer (repo root)

## Not yet on branch (MCP payload ceiling)

- `scripts/p1_synth_sim.py` (sha256 `24a805b0bd7dc1172ff2703881122d1efd074e0fe5931f81560e3e3aa2421b21`)
- `csv/p1_cells_T0.csv` … `T7.csv`
- `csv/p1_twohist_T2.csv`, `T3`, `T4`

Local regeneration with the simulator produces CSVs matching `SHA256SUMS.txt` (28/28 ok when script present).

## Non-claims

SYNTHETIC_DEMO only. Not intelligence proved. Not EPW.
