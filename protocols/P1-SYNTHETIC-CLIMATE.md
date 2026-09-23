# P1 SYNTHETIC Climate Recipe — 48 h @ 1 h
stamp: 2026-09-23 ~19:07 AEST  
**label every row / every run:** `SYNTHETIC_DEMO`  
status: boot climate for smoke tests — **not** EPW truth · **not** publish weather claim

---

## Purpose

Provide a deterministic, reproducible 48-hour hourly drive so operators can stand up the logging pipeline before Sydney EPW is wired. Prefer EPW when available; keep this recipe for regression.

## Column contract (climate chronicle)

| Column | Unit | Notes |
|---|---|---|
| `t` | h | 0..47 |
| `G_rad` | W/m² proxy | Clear diurnal bump; night ≈ 0 |
| `RH` | % | Night high / day lower with mild noise-free sinusoid |
| `T_air` | °C | Diurnal lag behind radiation |
| `occ_proxy` | 0..1 | Weekday-like occupancy pulse 08–18 local |

Optional meta row in notes: `SYNTHETIC_DEMO;recipe=v1;tz=Australia/Sydney`.

## Deterministic formulas (v1)

Let hour-of-day `h = t % 24` (t = 0..47). Use radians `φ = 2π (h - 6) / 24` so peak radiation near solar noon ≈ 12–13.

```
G_rad(t) = max(0, 750 * sin(π * clamp(h - 6, 0, 12) / 12)^1.2)
           # night hours (h<6 or h>=18): 0

T_air(t) = 18 + 7 * sin(2π * (h - 8) / 24)
           # cool morning, warm afternoon

RH(t)    = clamp(55 + 25 * sin(2π * (h - 2) / 24), 30, 95)
           # higher overnight

occ_proxy(t) =
  0.85  if 8 <= h < 18
  0.15  if 6 <= h < 8 or 18 <= h < 21
  0.05  otherwise
```

`clamp(x,a,b) = min(max(x,a),b)`.

Day 2 (t=24..47) **repeats** day 1 exactly (no drift) so two-history and recovery tests share a stable second day.

## Regime-shift slot (optional, for Adaptation gate)

If testing criterion 5, on day 2 only (`t=24..47`) apply:

```
G_rad' = 1.35 * G_rad   for t in [30, 36]   # 6 h “hot spell”
RH'    = RH - 10        for same window (floor at 30)
```

Document in `notes`: `SYNTHETIC_DEMO;regime_shift=hotspell_t30_36`.

## Patch-shock slot (optional)

At `t=20`, for corner cells `(i,j) ∈ {(0,0),(0,1),(1,0),(1,1)}` only, set `G_rad_cell = G_rad + 400` for one hour. Global climate row stays unshocked; cell-level override logged in `notes`: `PATCH_SHOCK_CORNER`.

## CSV snippet header (climate-only helper)

```
t,G_rad,RH,T_air,occ_proxy,notes
```

Generate with any short script; do **not** hand-invent random weather. Publish neither this series nor results as real Sydney climate.

## Explicit non-claims

- Not EPW · Not measured · Not validation of hygromorph physics · Not intelligence evidence by itself.
