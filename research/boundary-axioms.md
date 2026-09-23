# Boundary Axioms

## Status: Step 1 — Theory

This document defines the formal axiomatic foundation of the project.
Every major claim in this repository must be traceable to one or more of these axioms.

---

## Axiom A1 — Envelope as Boundary Function

An architectural envelope is a boundary function:

    B(t) : X(t) -> S(t)

Where:
- X(t) = input vector at time t, including radiation R, temperature T, CO2 concentration C, occupancy density U, wind speed W
- S(t) = output state vector, one state per panel i: { open ratio, rotation angle, mode }
- B is deterministic and reproducible given the same X(t)

This is the project's core falsifiable claim.
If no measurable correlation between X(t) and S(t) can be established, the project's empirical basis fails.

---

## Axiom A2 — Performance Consequence

The envelope's state S(t) must produce a measurable change in at least one building performance metric:
- incident solar gain (kWh/m2)
- useful daylight illuminance UDI (lux-hours)
- open-area ratio (m2/total m2)
- actuation energy demand (Wh)

Without this, the adaptive envelope is indistinguishable from a static facade in terms of scientific evidence.

---

## Axiom A3 — State Discretisation

The continuous output of B(t) can be discretised into a finite state machine with at least five states:

    CLOSED      -> high radiation, low occupancy
    SHADED      -> high radiation, high occupancy
    VENTILATE   -> CO2 or temperature above threshold
    OPEN        -> comfortable conditions, demand for view or daylight
    SAFE        -> sensor failure, wind above limit, or power loss

SAFE is a hard constraint. It overrides all other states.
This discretisation enables physical prototyping with finite actuator positions.

---

## Axiom A4 — Hysteresis as Stability Requirement

The boundary function B(t) must include a hysteresis gate to prevent oscillation:

    if |o_i(t) - o_i(t-1)| < epsilon: hold
    else: move toward target by at most maxStep per time unit

Without this gate, small sensor fluctuations cause rapid repeated actuation, reducing actuator lifespan and creating visual noise.
Epsilon and maxStep are tuneable parameters; their optimal values are determined by simulation and prototype testing.

---

## Axiom A5 — Bounded Analogy

Conceptual transfers from physics are permitted only under the following conditions:

1. The analogy is explicitly bounded and named as an analogy.
2. The analogy generates a testable prediction or design decision.
3. The analogy is not used to imply direct physical equivalence.

Allowed transfers under these conditions:
- Holographic principle -> information analogy: interior state is readable on the boundary
- Phase transition -> state logic: envelope switches between discrete or continuous modes
- Spin-glass frustration -> multi-objective optimisation landscape with no single global minimum

Disallowed:
- Claiming the facade implements black-hole physics
- Claiming SYK dynamics are materially present in building components
- Claiming quantum effects are simulated by Grasshopper geometry

---

## Axiom A6 — Prototype Falsifiability

Every claim in this project should eventually be classifiable at one of four evidence levels:

    L0  conceptual analogy, not yet testable
    L1  computationally reproducible model
    L2  simulated performance outcome
    L3  physical prototype demonstration
    L4  comparative evidence against a static baseline

A claim at L0 with no defined path to L1 or above must be marked speculative and excluded from the main research narrative.
