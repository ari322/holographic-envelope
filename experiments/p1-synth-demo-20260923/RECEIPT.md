# RECEIPT — P1 SYNTHETIC_DEMO
stamp: 2026-09-23 AEST  
run_id: `p1-20260923-synth-demo-v1`  
artifact_root: `/workspace/octopus-hq/wiring/INTELLIGENT-SUPERSTRUCTURES-20260923/P1-RESULTS-20260923`

## Claims discipline
- All climate / cell rows labelled **SYNTHETIC_DEMO**.
- No EPW Sydney data invented.
- No validated_result / intelligence / holographic / RSB / spin-glass equivalence claimed.
- Gate labels kinetic / interactive / candidate only; candidate requires ≥3/5 with controls.
- Local artifacts only; no GitHub push from this executor.

## Key parameters
- Grid: 4×4, neighbor_graph=von_neumann_4, theta_units=deg, K_bins=5
- ε_theta=0.5 deg, ε_aperture=0.02
- T2 G_thresh=200; T3 G_hi/G_lo=(350.0, 150.0); T6 k=0.35; T5 seed=42
- Regime shift: hotspell t∈[30,36] (G×1.35, RH−10)

## Treatments gate Y-count / label
- T0: 0/5 → kinetic
- T1: 0/5 → kinetic
- T2: 2/5 → interactive
- T3: 4/5 → candidate
- T4: 4/5 → candidate
- T5: 2/5 → interactive
- T6: 4/5 → candidate
- T7: 2/5 → interactive

## Two-history (mean |Δθ| deg)
- T2: 0.000000
- T3: 90.000000
- T4: 50.625000

## Artifact list (sha256 in SHA256SUMS.txt)
- scripts/p1_synth_sim.py
- climate/synthetic_v1.csv
- csv/p1_cells_T0.csv … T7.csv
- csv/p1_twohist_T2.csv, T3, T4
- agg/T0.json … T7.json
- P1-GATE-SCORECARD-FILLED.md
- IS-STATUS-NOTES.md
- RECEIPT.md
- SHA256SUMS.txt
