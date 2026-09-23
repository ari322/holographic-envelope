DESIGN DOCUMENT — When (not now) to connect holographic-envelope to Octopus

Status: FUTURE DESIGN. ROLE 06 final output. Not implemented.
Scope: this repository only. No Octopus repository, code, architecture, or config
is written or modified. This page does not authorise a connection.

---

## Verdict

Do not implement the connection now.

The right time to connect is after three independent things are true at once:

    1. The architecture research can stand on its own (facade math tested,
       not only defined).
    2. The CRITIC record of unsupported claims exists and has been read.
    3. An owner GO covers this design pack (TFE, H_coord, BIR, this page).

Until then the Octopus link stays design-only: Way 1 / Way 2 / Way 3 as
written in `agents/GROK-AGENT-MASTER.md`, mapped in this folder, unused
as wiring.

---

## What would be connected (reminder, not a plan to build)

    Way 1  TFE-for-agents.md         output-stream entropy (alphabet A, FLEET/TRACE)
    Way 2  hamiltonian-for-agents.md H_coord cost; genes; hypothetical J
    Way 3  BIR-for-agents.md         H_space / H_interior ratio on API vs interior

These are analogies to D01, D02, D04. They are not a fifth discovery.
They are not Octopus features.

---

## Preconditions (all required)

    P1  Architecture research independently exercised
        - D01 falsification path exists (TFE on static / rule / adaptive
          envelopes) and has been run or explicitly waived by the owner
          with the gap named.
        - D02 RSB protocol is treated as PREDICTED, not confirmed, until
          Hartigan / GMM results exist. Do not export "RSB" into Octopus
          language before that.
        - D04 BIR has a facade measurement path (sensors + panel log) or
          a written reason it is still L1-only.
        GROK-AGENT-MASTER already says: validate the architecture research
        independently, then design the bridge. The bridge is now designed.
        Validation has not been done in this change.

    P2  CRITIC unsupported-claims.md (ROLE 07 task 1) exists
        Owner or a reader has the list of claims that still lack data.
        Connecting before that list exists hides which analogies are still
        free-floating.

    P3  Owner review of this design pack
        Files to review:
          agents/octopus-bridge/TFE-for-agents.md
          agents/octopus-bridge/hamiltonian-for-agents.md
          agents/octopus-bridge/BIR-for-agents.md
          agents/octopus-bridge/integration-proposal.md
        Review means: accept, reject, or send back. It does not mean
        "wire Octopus."

    P4  No new orchestrator
        A later GO, if it ever happens, still does not create a second
        broker, database, or scheduler. Scoring, if any, stays a post-hoc
        read of logs.

If P1–P3 are incomplete, the only correct next action is wait.

---

## Risks of early connection

    R1  Unvalidated metrics become live knobs.
        TFE, H_coord, and BIR would look like health scores. High TFE is
        not automatically exploration; high BIR is not automatically
        intelligence; H_coord minima are not confirmed RSB.

    R2  Analogy leakage.
        AdS/CFT, Bekenstein-Hawking, and facade J^arch numbers get copied
        into agent ops. AI-CONTEXT forbids treating BIR as string theory
        and forbids treating J^arch as exact. Early wiring makes those
        mistakes operational.

    R3  Coupled failure.
        If Octopus and holographic-envelope are joined before either is
        falsifiable on its own, a bad agent week can be blamed on TFE
        and a flat Wallacei run can be blamed on agents. Neither mapping
        can be rejected (see each design doc's falsification section).

    R4  Scope breach.
        Touching Octopus repos, prompts, routing, or config to "help BIR"
        violates ROLE 06 and the prime directive. Missing traces are
        data_absent, not a reason to add telemetry.

    R5  False product claims.
        Sentences of the form "RSB confirmed" or "D01–D04 validated"
        must not travel into another system. They are false today.

---

## What remains design-only until owner GO

    - All four files in agents/octopus-bridge/
    - Any later scoring script, dashboard, or reward that mentions TFE,
      H_coord, or BIR for agents
    - Any Octopus-side change of any kind

Allowed now (this repo only): critique, owner comments, CRITIC / validation
work on the facade side, and edits to these design docs.

Forbidden now: implementation, simulation-as-proof, Octopus writes,
declaring a winner among coordination families, using H_coord or BIR as
a live controller.

---

## One-line rule

First validate the architecture research and review this pack.
Then, only on an explicit owner GO, consider a log-only experiment.
Do not implement the connection in this pull request or the next idle wait.
