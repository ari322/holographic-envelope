# Validation Framework

## Goal

Move the project from conceptual language to evidence.

## Claim ladder

### Level 0 — Conceptual analogy
A statement is used only as a bounded conceptual guide.

### Level 1 — Computational mapping
The concept is implemented as a reproducible parametric or control logic model.

### Level 2 — Performance simulation
The model is tested against measurable outputs such as radiation, daylight, aperture ratio, or actuation frequency.

### Level 3 — Physical prototype
A small-scale prototype demonstrates the relevant mechanism.

### Level 4 — Comparative evidence
The adaptive system outperforms a baseline static facade in one or more defined metrics.

## Minimum metrics

- Incident radiation reduction
- Daylight adequacy or useful daylight illuminance
- Open-area ratio
- Number of unique panel states
- Energy or actuation demand
- Fail-safe behavior under sensor error or shutdown

## Baselines

Every test should compare against:
- a static facade,
- a simple rule-based adaptive facade,
- the proposed adaptive logic.

## Failure tests

- sensor noise
- missing data
- threshold oscillation
- extreme weather input
- actuation limit reached
- manual override
