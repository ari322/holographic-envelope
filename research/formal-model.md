# Formal Mathematical Model

## Status: Step 3 — Complete

---

## Core mapping function

For each panel i at time t:

    o_i(t) = clamp( w_r*R_i + w_t*T_i + w_c*C_i + w_u*U_i , 0, 1 )

Variables:
- R_i  normalised incident radiation [0,1]
- T_i  normalised external temperature [0,1]
- C_i  normalised CO2 or air quality [0,1]
- U_i  normalised local occupancy density [0,1]
- w_r, w_t, w_c, w_u  tunable weights summing to 1.0

Output o_i(t) = 0 means fully closed, 1 means fully open.

---

## Hysteresis gate

    delta = o_i(t) - o_i(t-1)
    if |delta| < epsilon:   hold current state
    else:                   move by min(|delta|, maxStep) * sign(delta)

Typical starting values:
- epsilon = 0.05  (5% dead band)
- maxStep = 0.10  (max 10% change per time step)

These values must be calibrated against prototype actuation speed and sensor noise floor.

---

## Discrete state machine

    SAFE       <- sensor_failure OR wind > W_limit OR power_loss
    VENTILATE  <- temperature > T_hot AND occupancy > U_crowd
    SHADED     <- radiation > R_high
    OPEN       <- all conditions comfortable
    CLOSED     <- radiation > R_high AND occupancy < U_low

Priority order (highest first): SAFE > VENTILATE > SHADED > OPEN > CLOSED

SAFE is a hard override. When active, all panels move to their mechanically safe default position regardless of any other signal.

---

## Information entropy of the facade

At any time t, the facade state distribution can be described by a Shannon entropy:

    H(t) = - sum_i [ p_i * log2(p_i) ]

where p_i is the normalised open ratio of panel i.

H_max occurs when all panels have different open ratios (maximum spatial variety).
H_min = 0 when all panels are identical.

This is the project's formal link to the holographic information analogy:
a facade with H > 0 encodes spatially differentiated information about the interior state on the boundary surface.
This is measurable, not metaphorical.

---

## Weighted multi-objective score for optimisation

    Score = a*f1 + b*f2 + c*f3 + d*f4

    f1 = mean incident radiation across all panels (kWh/m2) — minimise
    f2 = daylight deficit: fraction of hours below 300 lux — minimise
    f3 = number of unique panel geometries — minimise for fabrication
    f4 = total actuation events per day — minimise for energy and wear

For Pareto optimisation (Step 8), these four objectives are kept separate.
