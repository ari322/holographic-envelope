# P1 Operator Runbook — 4×4 Grasshopper / Python logging
stamp: 2026-09-23 ~19:07 AEST  
source: `P1-HYPOTHESIS/P1-4x4-PACK.md`  
status: protocols only — discovery machine; no law / no intelligence proved  
Octopus: computational exemplar ONLY

---

## 0. Preconditions (check before first tick)

| # | Check | Pass if |
|---|---|---|
| 0.1 | claim_type discipline | No holographic / RSB / market language in run notes |
| 0.2 | OPEN math conflicts | J-arch + frustration remain OPEN; do not narrate spin-glass equivalence |
| 0.3 | Climate labelled | Rows use `SYNTHETIC_DEMO` or `EPW_SYDNEY_EXCERPT` in `notes` / climate meta |
| 0.4 | Schema locked | CSV matches `protocols/P1-CSV-SCHEMA.md` + `p1_cells.csv.header` |
| 0.5 | Treatments list | T0–T7 all scheduled (or explicit skip with reason in scorecard) |
| 0.6 | Memory probe | Two-history protocol file present; T3/T4 mandatory |

**Blockers that do NOT stop this runbook:** Jacobian conflicts (block D02 spin-glass interpretation only).  
**Blockers that DO stop a “validated_result” claim:** missing controls, unlabelled climate, no scorecard.

---

## 1. Geometry & state (once)

1. Build **4×4** cell array (N=16). Indices `i,j ∈ {0,1,2,3}` row-major.
2. Neighbor graph: **4-connected (von Neumann)**; record in run meta `neighbor_graph=von_neumann_4`.
3. Per-cell state: angle `theta` in K=5 discrete bins (match HE TFE docs) and/or continuous `aperture ∈ [0,1]`.
4. Export path: one CSV per treatment (or one CSV with `treat_id` column). Prefer one file per `run_id`.

---

## 2. Climate drive

1. Prefer Sydney EPW excerpt when available.
2. Else load **SYNTHETIC_DEMO** from `protocols/P1-SYNTHETIC-CLIMATE.md` (48 h @ 1 h).
3. Smoke duration: ≥48 h @ 1 h. Target report: 168 h (1 week) when EPW ready.
4. Patch-shock optional after baseline: spike `G_rad` on corner 2×2 for 15 min; log recovery.

---

## 3. Treatment loop (execute in order T0→T7)

For each treatment ID:

1. Reset cell state to agreed IC (document IC in `notes`).
2. Load rule map for treatment (see pack table).
3. For each hour `t`:
   - Read climate row `(G_rad, RH, T_air, occ_proxy)`.
   - Update each cell per rule (T6 uses neighbor mean).
   - Append 16 CSV rows (one per cell) matching header.
4. After climate chronicle completes:
   - Write aggregate JSON stub: `response_time`, `recovery_time`, `hysteresis_loop_area` (T3/T4), `Moran_I` (T6).
5. If treatment is T3 or T4: run **Two-history probe** (`protocols/P1-TWO-HISTORY.md`) and append probe rows or separate `*_twohist.csv`.
6. Fill one blank row-block on `protocols/P1-GATE-SCORECARD.md` for that treatment.

### Treatment quick-ref

| ID | Rule | Idea link |
|---|---|---|
| T0 | Fixed closed | null |
| T1 | Fixed open | null |
| T2 | Homogeneous memoryless threshold | control |
| T3 | Homogeneous hysteretic thresholds | IS-0001 / IS-0005 |
| T4 | Heterogeneous hysteretic map (designed) | IS-0002 |
| T5 | Random heterogeneous (matched mean/var to T4) | IS-0002 control |
| T6 | Neighbor-coupled update (k>0) on T3 base | IS-0003 |
| T7 | Open-loop RH hygromorph curve only | IS-0006 |

---

## 4. Gate scorecard (after all treatments)

Score each treatment Y/N with evidence pointer (CSV row range or plot path):

1. Sensing — corr(input, state) significant vs null?
2. Memory — two-history \|Δθ\| > noise band? (N/A for T0/T1/T2/T5/T7 unless instrumented)
3. Feedback — prior structure state in update equation?
4. Self-organization — T6 metrics ≠ T3 independence?
5. Adaptation — proxy recovered after climate regime shift?

Label “intelligent structure candidate” **only if ≥3/5** with named controls. Else `kinetic` / `interactive`.  
**Never** claim intelligence proved; never claim Octopus ownership of HE.

---

## 5. Falsification bookkeeping

| Outcome | Action |
|---|---|
| Memory treatments fail two-history | Mark IS-0001/0005 `inconclusive` or `refuted` at this fidelity |
| T6 ≡ T3 on corr/recovery | IS-0003 fails self-org at P1 |
| T4 ≤ T2 and T5 on proxies | IS-0002 heterogeneity unused |
| T7 scores ≥3/5 under honest scoring | Revise gate (too loose) per IS-0006 falsification |

---

## 6. Deliverables checklist (operator)

- [ ] GH definition **or** Python exporter compatible with facade-sim angles
- [ ] CSV set matching schema (+ two-history files)
- [ ] One animation/timelapse (optional but preferred)
- [ ] Completed gate scorecard (T0–T7)
- [ ] Status notes for IS-0001…0003,0005,0006 (supported/refuted/inconclusive) — local only until PR
- [ ] All climate rows labelled SYNTHETIC_DEMO or EPW

## 7. Explicit non-goals

No RSB / Wallacei archive · No BIR>1 holographic claims · No Octopus-as-owner language · No market/NCC · No spin-glass formal equivalence (PARK).

## 8. Next after this runbook

Execute logging pipeline on hardware/GH session; bind results under a future `P1-RESULTS-YYYYMMDD/` — **not** invented here.
