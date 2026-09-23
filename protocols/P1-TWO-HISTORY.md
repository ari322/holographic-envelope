# P1 Two-History Memory Probe — mandatory for T3 / T4
stamp: 2026-09-23 ~19:07 AEST  
linked: IS-0001, IS-0005 · also informative for T7  
status: protocol only — positive Δθ is **memory signal**, not learning / intelligence proof

---

## Why mandatory

Memoryless maps (T2) must end at the same state for identical present inputs. Hysteretic maps should not. Without this probe, gate criterion “Memory” is un-scorable.

## Definitions

- **History A / B:** two distinct 12 h climate segments ending at the **same** input vector `x* = (G_rad*, RH*, T_air*, occ*)`.
- **Noise band ε:** operator-declared; default ε = max(0.5° angle, 0.02 aperture) or 1 bin if using K=5 discrete θ. Document ε in run meta.
- **Memory signal:** `|θ(x*|A) − θ(x*|B)| > ε` (or aperture analogue).

## Procedure

1. **Choose x\*** reachable from both histories (recommend mid-range RH≈55%, G_rad≈200, T_air≈22, occ≈0.5). Record exact tuple.
2. **History A (12 h):** drive from IC_A along path A ending at x\*. Log all ticks; tag `TWO_HISTORY;hist=A`.
3. **At meeting point:** record `θ_A`, `aperture_A` per cell (or instrumented subset — full 4×4 preferred).
4. **Reset policy:**
   - Prefer **continue without hard reset** if the material/model carries state naturally.
   - If simulator requires reset: restore **only** environmental inputs schedule, **not** wiping hysteresis state unless testing memoryless control.
   - Document reset choice in `notes`.
5. **History B (12 h):** drive along path B (different RH/radiation trajectory) ending at **same** x\*. Tag `TWO_HISTORY;hist=B`.
6. **Compare:** compute per-cell and mean `|Δθ|`, `|Δaperture|`.
7. **Controls:**
   - Run identical two-history on **T2** (memoryless): expect `|Δθ| ≤ ε`.
   - Optional: T7 open-loop hygromorph — weak memory possible; score honestly.

## Suggested path shapes (SYNTHETIC_DEMO)

Both paths end at hour-local equivalent of x\*:

| Phase | History A | History B |
|---|---|---|
| 0–4 h | High RH wet-up (RH→85) | Dry-down (RH→35) |
| 4–8 h | Moderate G_rad ramp | Low G_rad then spike |
| 8–12 h | Converge to x\* | Converge to x\* |

Use the same `occ_proxy` schedule on both. Exact numbers may follow `P1-SYNTHETIC-CLIMATE.md` slices; paths must differ in ordering, not only in noise.

## Pass / fail (P1-level)

| Result | Interpretation |
|---|---|
| T3/T4 \|Δθ\| > ε and T2 \|Δθ\| ≤ ε | Memory signal supports IS-0001/0005 at this fidelity |
| T3/T4 \|Δθ\| ≤ ε | Memory claim fails → refuted/inconclusive for P1 map |
| T2 \|Δθ\| > ε | Probe broken (IC leak / binning / bug) — fix before scoring |

## Logging

Append to main CSV or write `p1_<run_id>_twohist.csv` with identical header; `notes` must include `TWO_HISTORY;hist=A|B;xstar=G:…,RH:…,T:…,occ:…`.

## Explicit non-claims

Two-history ≠ learning · ≠ intelligence · ≠ holographic encoding · ≠ RSB.
