# IS-STATUS-NOTES — P1 SYNTHETIC_DEMO fidelity only
stamp: 2026-09-23 AEST  
run_id: `p1-20260923-synth-demo-v1`  
climate: SYNTHETIC_DEMO recipe=v1 + hotspell t∈[30,36]  
**scope:** status at this demo fidelity only — not EPW, not hardware, not intelligence proof

| Idea | Status | Basis (this demo only) |
|---|---|---|
| IS-0001 | **supported** | T3 two-history |Δθ|>ε with T2 control |Δθ|≤ε at SYNTHETIC_DEMO fidelity |
| IS-0002 | **supported** | T4 shows memory + higher gate Y than T5 control; designed hetero used at this fidelity |
| IS-0003 | **supported** | T6 ≠ T3 on collective proxy (Moran_I and/or hysteresis_loop_area); coupling_k=0.35; see agg/T6.json vs T3.json — SYNTHETIC_DEMO only |
| IS-0005 | **supported** | T3 two-history |Δθ|>ε with T2 control |Δθ|≤ε at SYNTHETIC_DEMO fidelity (same probe as IS-0001 at P1) |
| IS-0006 | **supported** | T7 Y-count=2<3 under honest scoring — open-loop hygromorph stays kinetic/interactive as expected |

## Two-history deltas (mean over 4×4 at x*)

| treat | mean\|Δθ\| (deg) | mean\|Δaperture\| | >εθ=0.5? |
|---|---|---|---|
| T2 | 0.000000 | 0.000000 | False |
| T3 | 90.000000 | 1.000000 | True |
| T4 | 50.625000 | 0.562500 | True |

## T5 documentation
- Mode: `memoryless_threshold_per_cell_matched_mean_var` (memoryless per-cell thresholds; seed=42)
- Matched T4 G_hi mean/std ≈ 317.500/49.213; G_lo ≈ 125.625/32.829

## Explicit non-claims
No validated_result · no intelligence proved · no holographic/RSB/spin-glass equivalence · no EPW Sydney invention.
