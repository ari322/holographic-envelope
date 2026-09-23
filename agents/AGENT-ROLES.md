# AGENT ROLES
# One role per Grok agent instance

> Assign one agent to one role. Roles do not overlap.
> If you are not sure which role you have, read the agent deployment instructions.

---

## ROLE 01 — MATHEMATICIAN

**Folder:** `agents/mathematician/`
**Mission:** Audit, extend, and formalise all mathematical content.

**Current tasks:**
  1. Verify the 6×6 coupling matrix J^arch by re-deriving each entry from the objective Jacobian.
     Write derivation to: `agents/mathematician/coupling-matrix-derivation.md`
  2. Verify the frustrated triangle condition for (ε, Δs, wr).
     Write proof to: `agents/mathematician/frustration-proof.md`
  3. Derive the complexity function Σ(e) for H_facade (how many local minima at energy e).
     Write to: `agents/mathematician/complexity-function.md`
  4. Propose a reparameterisation of (ε, Δs, wr) that eliminates the frustrated triangle.
     Write to: `agents/mathematician/reparameterisation.md`

**Do NOT:** Run simulations. Write code. Touch any file outside `agents/mathematician/`.

---

## ROLE 02 — SIMULATOR

**Folder:** `agents/simulator/`
**Mission:** Write all simulation code and pseudocode. Prepare everything for Grasshopper execution.

**Current tasks:**
  1. Complete the Grasshopper node sequence for all 5 steps (steps 02, 03, 05 are missing detail).
     Write to: `agents/simulator/grasshopper-complete.md`
  2. Write a standalone Python simulation of the facade controller (no Grasshopper required).
     Inputs: EPW weather data, gene vector σ.
     Outputs: panel angle time series, f1, f2, f3, f4, TFE.
     Write to: `agents/simulator/facade-sim.py`
  3. Write the RSB detection script (using sklearn GMM + Hartigan dip test).
     Make it self-contained and runnable.
     Write to: `agents/simulator/rsb-detection.py`
  4. Generate synthetic Wallacei output (5 runs × 50 solutions) to test the RSB script.
     Write synthetic data to: `agents/simulator/synthetic-pareto.json`
     NOTE: label it clearly as SYNTHETIC — not real simulation data.

**Do NOT:** Claim RSB is confirmed from synthetic data. Modify math files.

---

## ROLE 03 — MATERIALS SCIENTIST

**Folder:** `agents/materials/`
**Mission:** Develop the D03 bacterial spore panel concept into a complete fabrication specification.

**Current tasks:**
  1. Survey all published data on Bacillus subtilis spore actuators.
     Compile: response time, reversibility, lift capacity, substrate compatibility.
     Write to: `agents/materials/spore-data-survey.md`
  2. Design the fabrication protocol for 7 test panels (n = 1,2,3,5,8,13,21 layers).
     Write step-by-step protocol to: `agents/materials/fabrication-protocol.md`
  3. Specify the humidity chamber test protocol for measuring θ_max vs n_layers.
     Write to: `agents/materials/test-protocol.md`
  4. Propose 3 alternative actuator materials (not spores) that could replace D03 if spores fail.
     Write to: `agents/materials/alternatives.md`

**Do NOT:** Claim fabrication results. Panels have not been built. Be explicit about what is literature vs what is proposed.

---

## ROLE 04 — THEORIST

**Folder:** `agents/theorist/`
**Mission:** Extend the theoretical framework. Find connections to other fields.

**Current tasks:**
  1. Write a 1000-word argument connecting TFE to Kolmogorov complexity.
     Is TFE a lower bound on the Kolmogorov complexity of the facade's behaviour?
     Write to: `agents/theorist/TFE-Kolmogorov.md`
  2. Develop the AdS/CFT analogy more carefully.
     Where exactly does the analogy break down? What would need to be true for BIR = 1 to be exact?
     Write to: `agents/theorist/BIR-limits.md`
  3. Propose a connection between the frustrated triangle (ε, Δs, wr) and the
     exploration-exploitation dilemma in reinforcement learning.
     Write to: `agents/theorist/frustration-RL.md`
  4. Write a speculative (clearly labelled) section on what a BIR > 1 building would mean.
     Write to: `agents/theorist/BIR-greater-than-one.md`

**Do NOT:** Present speculation as confirmed theory. Label all speculative sections clearly.

---

## ROLE 05 — WRITER

**Folder:** `agents/writer/`
**Mission:** Produce publication-ready text. Target journals and conferences.

**Current tasks:**
  1. Write the full abstract (250 words) for a paper titled:
     "Holographic Envelopes: A Spin-Glass Information Framework for Adaptive Architectural Skins"
     Target journal: Building and Environment (Elsevier)
     Write to: `agents/writer/abstract-v1.md`
  2. Write the Introduction section (800 words) for the same paper.
     Write to: `agents/writer/introduction-v1.md`
  3. Write a 500-word popular science summary of the four discoveries.
     Target: Dezeen, Architectural Review, or ArchDaily.
     Write to: `agents/writer/press-summary.md`
  4. Write a conference abstract (300 words) for ACADIA 2027 or eCAADe 2027.
     Write to: `agents/writer/conference-abstract.md`

**Do NOT:** Change any mathematics. If you need a number, take it from MATH-SKELETON.md.

---

## ROLE 06 — OCTOPUS BRIDGE ARCHITECT

**Folder:** `agents/octopus-bridge/`
**Mission:** Design the FUTURE connection between holographic-envelope and Octopus.
             DO NOT touch Octopus. Write design documents only.

**Current tasks:**
  1. Read AI-CONTEXT.md section 3 (Octopus Connection) carefully.
  2. Write a design document: how would TFE be computed for an Octopus agent?
     What is the "panel state" of an agent? What is the "time window"?
     Write to: `agents/octopus-bridge/TFE-for-agents.md`
  3. Write a design document: how would H_facade become a multi-agent coordination cost?
     What are the "genes" for an Octopus agent? What are the "objectives"?
     Write to: `agents/octopus-bridge/hamiltonian-for-agents.md`
  4. Write a design document: what would BIR mean for an Octopus agent?
     What is the agent's "boundary"? What is the agent's "interior"?
     Write to: `agents/octopus-bridge/BIR-for-agents.md`
  5. FINAL OUTPUT: Write a one-page integration proposal.
     When is the right time to connect the two systems?
     What are the risks?
     Write to: `agents/octopus-bridge/integration-proposal.md`

**CRITICAL: DO NOT WRITE TO ANY OCTOPUS REPOSITORY.**
**CRITICAL: DO NOT MODIFY OCTOPUS CODE OR ARCHITECTURE.**
**This role produces DESIGN DOCUMENTS ONLY.**

---

## ROLE 07 — CRITIC

**Folder:** `agents/critic/`
**Mission:** Find weaknesses. Challenge every claim. This is the most important role.

**Current tasks:**
  1. Read all four discovery files and list every claim that is NOT yet supported by data.
     Write to: `agents/critic/unsupported-claims.md`
  2. Identify the three most likely ways this project could fail.
     Be specific. Not "the math might be wrong" — identify WHICH equation and WHY.
     Write to: `agents/critic/failure-modes.md`
  3. Find the weakest point in the AdS/CFT analogy (BIR).
     Write to: `agents/critic/BIR-critique.md`
  4. Find the weakest point in the spin-glass analogy (D02).
     Write to: `agents/critic/spin-glass-critique.md`
  5. Write a one-page "devil's advocate" paper review as if you were a hostile referee.
     Write to: `agents/critic/hostile-review.md`

**Style:** Be direct. Be specific. No softening. A weak critique is useless.

---

## STATUS BOARD

All agents update this file when they complete a task:
`agents/STATUS-BOARD.md`

Format:
```
| Agent | Last completed | Next task | Blocked |
|-------|---------------|-----------|--------|
| MATHEMATICIAN | [task] | [task] | [yes/no] |
| SIMULATOR     | [task] | [task] | [yes/no] |
| MATERIALS     | [task] | [task] | [yes/no] |
| THEORIST      | [task] | [task] | [yes/no] |
| WRITER        | [task] | [task] | [yes/no] |
| OCTOPUS-BRIDGE| [task] | [task] | [yes/no] |
| CRITIC        | [task] | [task] | [yes/no] |
```
