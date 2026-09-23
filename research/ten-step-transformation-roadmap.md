# Ten-Step Scientific Transformation Roadmap

Preserved from repo-root `ROADMAP.md` so the P0 discovery-machine `ROADMAP.md` can occupy the seed path. Program source of truth for mission and season is [`CHARTER.md`](../CHARTER.md).

This document defines the 10 sequential steps that move the project from conceptual framework to verifiable scientific contribution.

Each step has a concrete deliverable, a clear evidence class, and a falsifiability criterion.

---

## Step 1 — Boundary Axioms (Theory)

**What:** Write a formal axiomatic statement of the project's core thesis.

> *An architectural envelope is a boundary function B(t) that maps a vector of environmental and occupancy inputs to a vector of panel states, such that B is measurable, reproducible, and its outputs correlate with at least one performance metric.*

**Deliverable:** `research/boundary-axioms.md`

**Evidence class:** Conceptual → Literature-supported

**Falsifiability:** If no correlation between inputs and performance outcomes can be measured, the core thesis fails.

---

## Step 2 — Literature Map (Evidence Base)

**What:** Build a structured map of peer-reviewed literature for five pillars:
- Adaptive envelopes and kinetic facades
- Phase change materials in buildings
- Mechanical metamaterials and deployable structures
- Hygromorphic systems
- Multi-objective parametric optimization in architecture

**Deliverable:** `research/literature-map.md` with DOI links, claim classification, and evidence grade per source

**Evidence class:** Literature-supported

**Falsifiability:** If no peer-reviewed support exists for the core mechanism, the material or analogy must be downgraded.

---

## Step 3 — Formal Input-Output Model (Mathematics)

**What:** Write the formal mathematical model of the panel state controller.

The mapping function for panel i:

    o_i(t) = clamp( w_r * R_i + w_t * T_i + w_c * C_i + w_u * U_i , 0, 1 )

Hysteresis gate:

    if |o_i(t) - o_i(t-1)| < epsilon: hold state
    else: step toward target by maxStep

State machine:

    CLOSED -> radiation high, occupancy low
    SHADED -> radiation high, occupancy high
    VENTILATE -> CO2 or temperature above threshold
    OPEN -> comfortable conditions
    SAFE -> sensor failure, wind above limit, or power loss

**Deliverable:** `research/formal-model.md`

**Evidence class:** Computationally reproducible

**Falsifiability:** Model output can be compared numerically to a baseline controller.

---

## Step 4 — Parametric Workflow (Grasshopper)

**What:** Build the full Grasshopper definition and document it.

Component chain:

    Surface
    → Divide Domain2
    → Isotrim
    → Area (panel centers)
    → Surface Frames
    → LB Incident Radiation
    → Remap Numbers 0..1
    → GhPython state controller
    → Scale or Rotate aperture
    → Join or Bake

Also document:
- Data Tree structure
- Ladybug EPW connection
- Honeybee daylight check
- Kangaroo structural constraints (optional)

**Deliverable:** `grasshopper/workflow.md` + `.gh` file

**Evidence class:** Computationally reproducible

**Falsifiability:** Workflow must run without errors on a standard EPW file and produce a panel state output that changes with radiation input.

---

## Step 5 — Material Selection Experiment

**What:** Narrow from five candidate material families to one primary and one fallback for a 1:5 prototype.

Selection criteria:
- Trigger (thermal, humidity, mechanical, electrical)
- Response type (movement, thermal, optical)
- Fabrication at desk scale
- Durability (cycles, UV, fire class)
- Cost and sourcing in Australia
- Fail-safe behavior

**Deliverable:** `materials/selection-matrix.md` with scored comparison table and final recommendation

**Evidence class:** Literature-supported + experimentally grounded

**Falsifiability:** Selected material must demonstrate at least 100 reversible actuation cycles at target conditions.

---

## Step 6 — Simulation Baseline (Energy and Daylight)

**What:** Run Ladybug incident radiation analysis and compare:
- Static closed facade
- Static open facade
- Proposed adaptive facade

Metrics:
- kWh/m2 incident radiation
- Useful Daylight Illuminance (UDI 100-2000 lux)
- Open-area ratio over time
- Actuation frequency per day

**Deliverable:** `validation/simulation-baseline.md` with result tables and charts

**Evidence class:** Computationally simulated

**Falsifiability:** Adaptive facade must show at least 10% improvement over static closed facade on the primary metric. If it does not, the control logic must be revised.

---

## Step 7 — Physical Prototype 1:5

**What:** Build a small-scale panel demonstrator.

Minimum viable prototype:
- 3 to 5 panels
- One actuator type (servo, SMA wire, or passive hygromorphic)
- One sensor (light or temperature)
- Manual override switch
- Safe default position on power loss

**Deliverable:** `validation/prototype-log.md` with photos, materials list, build notes, and measured actuation range

**Evidence class:** Physical prototype

**Falsifiability:** Prototype must respond to sensor input and return to safe state on simulated sensor failure.

---

## Step 8 — Frustration Landscape as Optimization Analogy

**What:** Formalize the spin-glass analogy as a bounded multi-objective optimization problem.

Four competing objectives:

    f1 = incident solar gain (minimize)
    f2 = daylight deficit (minimize)
    f3 = fabrication complexity (minimize)
    f4 = actuation energy (minimize)

Gene variables:
- panel depth
- aperture ratio
- rotation angle
- response threshold

Solver: Galapagos (single score) or Wallacei (Pareto front)

This step makes the spin-glass analogy falsifiable: if the Pareto front of real facade performance does not show multi-modal clusters, the analogy loses its explanatory power.

**Deliverable:** `grasshopper/optimization-setup.md`

**Evidence class:** Computationally reproducible

**Falsifiability:** Optimization must produce a Pareto front with at least two non-dominated solutions that differ meaningfully on f1 vs f2.

---

## Step 9 — Comparative Evidence Report

**What:** Write a structured evidence report that classifies every major claim in the project.

Format for each claim:

    Claim: [statement]
    Source: [citation or experiment]
    Evidence class: [Level 0-4]
    Status: [confirmed / partial / unverified / rejected]

This document is the scientific accountability layer of the entire repository.

**Deliverable:** `validation/evidence-report.md`

**Evidence class:** Comparative evidence

**Falsifiability:** Any claim rated Level 0 with no path to Level 1 must be removed from the main research narrative.

---

## Step 10 — Research Paper Draft

**What:** Write a structured academic paper draft.

Sections:
1. Introduction: adaptive envelope as boundary function
2. Conceptual framework: bounded analogies from physics
3. Formal model: input-output mapping and state machine
4. Computational workflow: Grasshopper and Ladybug implementation
5. Material strategy: selection and prototype
6. Results: simulation vs baseline
7. Discussion: what the analogies explain and what they do not
8. Conclusion: verified contributions and open questions

Target venue: ACADIA, eCAADe, or a building physics journal.

**Deliverable:** `research/paper-draft-v1.md`

**Evidence class:** Full scientific output

**Falsifiability:** Paper must distinguish clearly between empirically supported claims and open hypotheses.

---

## Progress tracker

| Step | Name | Status |
|------|------|--------|
| 1 | Boundary Axioms | not started |
| 2 | Literature Map | not started |
| 3 | Formal Model | partial — see `research/formal-model.md` |
| 4 | Parametric Workflow | partial — GhPython controller exists |
| 5 | Material Selection | partial — families documented |
| 6 | Simulation Baseline | not started |
| 7 | Physical Prototype | not started |
| 8 | Frustration Landscape | not started |
| 9 | Comparative Evidence | partial — framework exists |
| 10 | Research Paper | not started |
