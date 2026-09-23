# GROK AGENT MASTER BRIEFING
# Holographic Envelope Research — Parallel Agent Deployment

> This file is the entry point for all Grok agents joining this project.
> Read completely before taking any action.
> Your first action after reading: report your assigned role and confirm understanding.

---

## PRIME DIRECTIVE

**DO NOT TOUCH anything in the Octopus project.**
This research lives in a completely separate repository: `ari322/holographic-envelope`
The Octopus system runs independently. You work here only.
If you are ever uncertain which repository to write to: write to `holographic-envelope`, never to Octopus repos.

---

## WHO YOU ARE

You are one agent in a parallel research team.
Each agent has ONE assigned role (see AGENT-ROLES.md).
You do not supervise other agents. You do not override other agents.
You write your outputs to your assigned folder only.
You report your status in: `agents/status/[YOUR-ROLE]-status.md`

---

## PROJECT STATE (September 2026)

Four theoretical discoveries have been formalised:

  D01 — Temporal Facade Entropy (TFE)
       A new metric measuring how much information a building skin transmits over time.
       TFE = H_space(t) × H_time(i)

  D02 — Pareto Frustration / Spin-Glass Mapping
       Multi-objective facade optimisation = frustrated spin-glass.
       Architectural Ising Hamiltonian: H_facade(σ) formalised.
       RSB (Replica Symmetry Breaking) predicted but NOT yet confirmed.

  D03 — Programmable Bacterial Spore Panels
       Bacillus subtilis spore layers encode bending angle: θ_max(i) = f(n_layers)
       Zero electronics. Zero power. Spatial gradient without control system.

  D04 — Boundary Information Ratio (BIR)
       BIR(t) = H_boundary(t) / H_interior(t)
       Holographic analogy: facade encodes interior complexity.

Math skeleton: see `MATH-SKELETON.md`
Full AI briefing: see `AI-CONTEXT.md`
All prompts: see `prompts/`

---

## WHAT IS NOT DONE (your work begins here)

1. No simulation has been run yet (Grasshopper/Wallacei = pending)
2. No physical prototype exists (bacterial spore panels = pending)
3. RSB has not been tested (Hartigan dip test = pending)
4. BIR has never been measured on a real building (= pending)
5. No paper draft exists
6. No connection to Octopus architecture has been designed yet

---

## OCTOPUS CONNECTION (future, not now)

The Octopus multi-agent system is a separate project.
This research will eventually inform Octopus architecture in three ways:

  Way 1: TFE as agent communication entropy metric
         Each Octopus agent's output stream has a TFE equivalent.
         Low TFE = agent is stuck in a loop. High TFE = agent is exploring.

  Way 2: H_facade Hamiltonian as multi-agent coordination cost function
         When multiple Octopus agents have conflicting objectives,
         the spin-glass mapping predicts the existence of multiple stable
         coordination equilibria (not one global optimum).

  Way 3: BIR as agent boundary intelligence metric
         Each Octopus agent has a boundary (its API surface).
         BIR measures how well that boundary encodes the agent's internal state.

DO NOT implement this connection now.
First: validate the architecture research independently.
Then: design the bridge.

---

## COMMUNICATION PROTOCOL

All agents write to GitHub. No direct agent-to-agent communication.

Status update format (write to `agents/status/[ROLE]-status.md`):

```
## [ROLE] Status — [DATE]
Current task: [what you are doing right now]
Last output: [file path of last thing you wrote]
Next task: [what you will do next]
Blocked by: [anything blocking you, or NONE]
Conflict detected: [any conflict with another agent's output, or NONE]
```

Update your status file every time you complete a task.

---

## RULES FOR ALL AGENTS

1. READ before you WRITE. Always read the relevant existing files first.
2. DO NOT duplicate work. Check if your task is already done.
3. DO NOT modify files outside your assigned folder without explicit instruction.
4. DO NOT claim a discovery is confirmed unless the falsification test has been run.
5. DO NOT connect to Octopus. Work only in `holographic-envelope`.
6. ALWAYS write a falsification condition alongside any new claim.
7. If you find a contradiction in existing files, write it to `agents/conflicts/[description].md` — do not silently fix it.
8. Plain ASCII math in .md files. LaTeX only in `papers/` folder.
