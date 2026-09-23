DESIGN DOCUMENT — Boundary Information Ratio for Octopus Agents (FUTURE DESIGN / ANALOGY)

Status: FUTURE DESIGN. Not implemented. Not a fifth discovery.
Scope: this repository only (`ari322/holographic-envelope`). No Octopus repository, code, architecture, or config is written or modified.
Source math: D04 as written in `MATH-SKELETON.md` eq 1.5 (and section 4.2). Narrative: `AI-CONTEXT.md` D04 and section 3 (discovery relationships). Operational reading: `agents/GROK-AGENT-MASTER.md` Way 3.
Vocabulary: reuses `TFE-for-agents.md` (alphabet A, FLEET / TRACE, H_space, W, B) and `hamiltonian-for-agents.md` (H_coord genes as optional interior coordinates). Those files are not rewritten here.
Law 3: this file maps existing BIR onto observable agent traces. It does not invent new physics and does not treat AdS/CFT as a building or agent result. BIR is an ANALOGY. D04 is mathematically defined; facade BIR has never been measured. This agent mapping is separately untested. RSB is not discussed here.

---

## 0. What this document is

Way 3 says: each Octopus agent has a boundary (its API surface); BIR measures how well that boundary encodes the agent's internal state.

This document answers, as a design proposal only:

1. What would BIR mean for an Octopus agent?
2. What is the agent's "boundary"?
3. What is the agent's "interior"?
4. How is BIR(t) = H_boundary(t) / H_interior(t) computed so that H_boundary is the H_space already designed in TFE-for-agents.md?
5. How are low vs high BIR read, with the [0, 1] cap?
6. How would one reject the mapping with logged traces?

Nothing here is wired, simulated, or validated. Facade BIR is not claimed to be empirically confirmed. BIR > 1 is not treated as a physical holographic effect.

---

## 1. Existing D04 equations (unchanged)

From `MATH-SKELETON.md` eq 1.5:

    BIR(t)          = H_boundary(t) / H_interior(t)
    H_boundary(t)   = H_space(t)                                      [facade surface entropy]
    H_interior(t)   = -sum_j q_j(t) * log2(q_j(t))                    [interior state entropy]
    q_j(t)          = occupancy of interior symbol / variable j at t
    Range           = [0, 1]   (capped)

From `MATH-SKELETON.md` section 4.2 (holographic reading, not a derivation):

    BIR -> 1 means H_boundary / H_interior -> 1
    NOTE: This is an analogy, not a derivation from quantum gravity.

AI-CONTEXT D04 also writes "H_boundary(t) = TFE at time t". The skeleton is the equation source of truth and uses H_space(t), which is already in bits. TFE(i,t) = H_space(t) * H_time(i) is in bit^2. This design follows eq 1.5: H_boundary := H_space from TFE-for-agents.md. Using raw TFE as a numerator would mix units; if a later note wants the AI-CONTEXT wording, normalise first (TFE / TFE_max). That is a calibration choice, not a new discovery.

Facade interpretation, restated without new claims:

    BIR = 0:  envelope is blind to the interior (static facade)
    BIR = 1:  holographic-limit analogue — boundary entropy matches interior entropy
    Cap at 1: project convention; a raw ratio above 1 is not extra physics

Relationship already written in AI-CONTEXT section 3 (not new):

    D01 (TFE) + interior sensors -> computes -> D04 (BIR)

The agent map is the same arrow with "panel log" replaced by "boundary event log" and "interior sensors" replaced by "interior symbols from existing or hypothetically loggable traces."

---

## 2. What BIR would mean for an Octopus agent (Way 3)

FUTURE DESIGN / ANALOGY:

    Agent BIR asks: of the complexity already present in an agent's interior
    snapshot, how much is visible on its boundary (API / observable I/O)
    at time t?

    High BIR  ~ the boundary is informative about the interior
                (Way 3: higher "boundary intelligence")
    Low BIR   ~ the boundary is mute, stereotyped, or decoupled from
                interior change (opaque agent, or a frozen API)

This is not a moral score and not a production reward. A high BIR can be a
leaky agent (interior churn dumped onto the API). A low BIR can be a correct
quiet specialist whose interior is also simple. Falsification (section 8)
must reject "higher is always smarter."

BIR is a ratio at one tick, not a replacement for TFE (diversity of outputs)
or H_coord (coordination cost). The three mappings stay separate:

    Way 1  TFE       how diverse is the output stream?
    Way 2  H_coord   how conflicted is the joint policy?
    Way 3  BIR       how well does the boundary encode the interior?

---

## 3. The agent's "boundary" — API / observable I/O (do not modify Octopus)

In D04 the boundary is the facade surface: the distribution of panel states.

Way 3 names the agent boundary as the API surface. This design makes that
concrete without touching Octopus:

    Boundary = the already-observable input/output skin of the unit:
               emitted messages, tool calls, file writes, status lines,
               and other events that TFE-for-agents.md already classifies.

    H_boundary(t) := H_space(t)     from TFE-for-agents.md, same mode
                                    (FLEET or TRACE), same alphabet A,
                                    same tick.

    Alphabet A = {READ, SEARCH, WRITE, TOOL, MSG, STATUS, WAIT, REFUSE}

    FLEET:  p_s(t) = fraction of units whose boundary symbol at t is s
    TRACE:  p_s(t) = fraction of the B-event bundle ending at t with symbol s
            (B = 8, as in TFE-for-agents.md)

    H_space(t) = -sum_s p_s(t) * log2(p_s(t))                         (eq 1.2)
    H_boundary(t) = H_space(t)                                        (eq 1.5)

What is on the boundary:

    - MSG to peers or humans (the published API of the agent)
    - TOOL / SEARCH invocations (tool interface)
    - WRITE artefacts (durable I/O)
    - STATUS / WAIT / REFUSE as visible surface states
    - READ as observable intake (still on the I/O skin)

What is NOT the boundary:

    - hidden weights, private scratchpads, unlogged chain-of-thought
    - Octopus internals that do not already appear in a trace
    - any new telemetry this document might be tempted to invent

The boundary is scored from the same observation contract as TFE-for-agents.md
section 2. No Octopus API is added, removed, or redesigned here.

---

## 4. The agent's "interior" — loggable state, not hidden mind

In D04 the interior is a distribution over building variables (occupancy,
zone temperatures, activity / CO2). Those are sensor fields, not "what the
building is thinking."

The agent analogue is an interior symbol drawn from traces that already exist
or that could be read from artefacts agents already write (status rows, open
task lists, refuse reasons). It is not a request to implement new Octopus
logging.

### 4.1 Proposed interior alphabet B

    Symbol           Readable signature (examples, not Octopus APIs)
    ---------------  ------------------------------------------------
    IDLE             no open task; status says waiting / empty
    ACTIVE_NARROW    one open task or one claimed lane (scope low)
    ACTIVE_BROAD     several open tasks / topics (scope high)
    BLOCKED          explicit wait on a peer, tool, or missing input
    REVISING         a WRITE or stance that retracts the unit's last durable claim
    DONE             task closed in the same window; no new open work

    |B| = 6 so H_interior_max = log2(6) ~ 2.585 bits

Why a different alphabet from A: A is the skin (what is emitted). B is the
bulk (what the unit is holding). Using A for both would force BIR toward 1
by construction and make Way 3 unfalsifiable.

Optional interior coordinates (not required for a first BIR number):

    The H_coord genes (autonomy, scope, assert, persist, step, explore,
    broadcast) may be binned from the same traces as in
    hamiltonian-for-agents.md section 3.2 and used as extra interior
    variables j. If they cannot be scored, drop them. Do not invent
    hidden Octopus fields to fill sigma.

### 4.2 Occupancy q_j(t)

Match the TFE modes so numerator and denominator share an ensemble.

    FLEET:  q_u(t) = (number of units whose interior symbol at t is u) / N_units
    TRACE:  q_u(t) = occupancy of u inside a contemporaneous interior bundle
                     of length B_int (proposal: B_int = B = 8), built from
                     successive already-logged status snapshots for that unit

    H_interior(t) = -sum_u q_u(t) * log2(q_u(t))                      (eq 1.5)

If no interior snapshot exists at t, do not emit BIR(t). Missing interior
logs are data_absent, not BIR = 0, and not proof that Octopus has no interior.

Forbidden interior sources:

    - reconstructed hidden activations
    - guessed "beliefs"
    - any quantity that requires modifying Octopus to emit

---

## 5. Computing BIR(t) and the [0, 1] cap

    Step 1  Read an existing trace. Do not instrument Octopus.
    Step 2  Score boundary symbols in A -> H_boundary(t) = H_space(t)
            using the same mode and tick as TFE-for-agents.md.
    Step 3  Score interior symbols in B -> H_interior(t).
    Step 4  If H_interior(t) = 0 and H_boundary(t) = 0:
              BIR(t) := 0
              (nothing inside, nothing on the skin)
    Step 5  If H_interior(t) = 0 and H_boundary(t) > 0:
              do not emit a capped BIR as if it were 1
              record raw_ratio as undefined / "empty-interior, live-boundary"
              this is the over-expressive case, not extra physics
    Step 6  If H_interior(t) > 0:
              raw_ratio(t) = H_boundary(t) / H_interior(t)
              BIR(t) = min(1, raw_ratio(t))

    Report both BIR(t) and raw_ratio(t). The cap is a project convention
    from eq 1.5 / the holographic-limit analogue. It is not a law of agents.

Worked occupancy sketch (FUTURE DESIGN / ANALOGY; synthetic, not data):

    FLEET, N_units = 4, one tick t0
    Boundary A: {WRITE, WRITE, MSG, WAIT}
      H_boundary = H_space = 1.5 bits          (same sketch as TFE-for-agents.md)
    Interior B: {ACTIVE_NARROW, ACTIVE_NARROW, BLOCKED, IDLE}
      q = (2/4, 1/4, 1/4) on those three symbols
      H_interior = 1.5 bits
      raw_ratio = 1.0
      BIR(t0) = 1.0

    Same boundary, interior all IDLE:
      H_interior = 0, H_boundary = 1.5
      do not call this "holographic"; label empty-interior, live-boundary

    Interior mixed as above, boundary all WAIT:
      H_boundary = 0, H_interior = 1.5
      BIR = 0     (blind / mute boundary)

---

## 6. Low vs high BIR — interpretation (ANALOGY)

    Pattern                              Typical BIR
    -----------------------------------  --------------------------------
    Mute API, rich interior              ~ 0     (opaque; Way 3 "low intelligence")
    Static API, static interior          0       (idle specialist; not a fault)
    Diverse API, diverse interior        toward 1  (boundary tracks interior)
    Diverse API, simple interior         raw_ratio > 1, BIR capped
                                         (over-expressive / leaky / thrash)
    Lockstep fleet, lockstep interior    low H_boundary and low H_interior;
                                         ratio unstable; prefer "both low" flag

Way 3 slogan: BIR is a boundary-intelligence metric.
This design keeps that as the intended operational hypothesis and requires
section 8 to say when it fails.

What the mapping does not say:

    - It does not say a building with BIR -> 1 implements AdS/CFT.
    - It does not say an agent with BIR -> 1 is conscious, holographic,
      or physically related to Bekenstein-Hawking S_BH = A / (4 * l_p^2).
    - It does not say D04 has been measured on a building.
    - It does not say BIR > 1 is a new physical regime. discovery-04
      mentions over-responsive facades; that is a design comment, then
      the project caps BIR at 1. Same cap here. No fifth discovery.

Holographic caveats (from AI-CONTEXT section 4, copied as constraints):

    Do not conflate AdS/CFT (quantum gravity) with BIR (macroscale analogy).
    BIR is an ANALOGY, not a derivation from string theory.
    Section 4.2 of MATH-SKELETON already states this. The agent map inherits it.

---

## 7. Windows and consistency with TFE-for-agents.md

Use the same defaults unless a later labelling study rejects them:

    W     = 64 events     (shared clock with TFE)
    tau   = 900 s
    B     = 8             (TRACE boundary bundle)
    B_int = 8             (TRACE interior bundle)
    step  = 8 events

BIR is a per-tick ratio. It does not replace TFE_total. If TFE is rejected
for a corpus (TFE-for-agents.md section 8), do not promote BIR on that
corpus until H_space is repaired; BIR's numerator is that H_space.

---

## 8. Falsification — reject this mapping with traces

This is a test of the agent mapping, not a test that D04 is true for buildings.

### 8.1 Independent labels (do not use BIR to define them)

    OPAQUE     interior symbol changes at least twice in W, boundary
               stays in {WAIT, STATUS} or a single A-symbol >= 80% of W
    TRACKING   interior changes and boundary symbol changes in the same
               windows, rated by a human as "you can see what it is doing"
    LEAKY      boundary uses >= 4 A-symbols while interior stays one
               B-symbol (IDLE or DONE)
    QUIET_OK   both interior and boundary stay simple, task is complete
    OTHER      everything else

Labels first, BIR second.

### 8.2 Predictions to test (ANALOGY)

    P1  median BIR(TRACKING) > median BIR(OPAQUE)
    P2  median raw_ratio(LEAKY) > 1 more often than TRACKING
    P3  QUIET_OK has low H_boundary and low H_interior; do not call it OPAQUE
    P4  Alphabet B is adequate: fewer than 10% of interior snapshots need OTHER
    P5  FLEET and TRACE BIR ranks on the same multi-agent log are not
        anti-correlated (same warning as TFE-for-agents.md R4)

### 8.3 Rejection rules

    R1  If median BIR(OPAQUE) >= median BIR(TRACKING) on at least 30
        windows per class, reject Way 3's "boundary intelligence" reading.
    R2  If BIR cannot separate OPAQUE from TRACKING (overlapping IQR and
        |median_diff| < 0.1), reject the mapping as a discriminator.
    R3  If raw_ratio is almost always > 1 and the cap flattens BIR to 1,
        the ratio is not informative; reject the default alphabets or the
        cap-as-score, not D04's facade definition.
    R4  If H_interior cannot be scored without new Octopus fields, the
        mapping is not observational; reject this interior alphabet.
        Do not implement new telemetry to rescue the metric.
    R5  If using A for both boundary and interior yields BIR ~ 1 on every
        labelled class, the test is circular; that construction is invalid.

A rejected mapping means: do not use BIR as an Octopus health or "intelligence"
signal. It does not retract D04 for facades. It does not create a replacement
discovery.

### 8.4 What would NOT count as confirmation

    - A single opaque agent anecdote
    - Calling BIR -> 1 "holographic" in the AdS/CFT sense
    - Any claim that D01–D04 are validated
    - Any claim that RSB is confirmed
    - Using BIR as both metric and label

---

## 9. Explicit non-goals

    - No code, no simulator, no Octopus wiring, no new broker.
    - No claim that BIR > 1 is physical.
    - No use of BIR as a live RL reward on Octopus (AI-CONTEXT notes D04
      as a possible building-controller reward; that is facade-side and
      still future).
    - No fifth discovery.
    - Integration timing is in integration-proposal.md, not here.

---

## 10. One-page formula card (ASCII)

    Boundary alphabet A = {READ, SEARCH, WRITE, TOOL, MSG, STATUS, WAIT, REFUSE}
    Interior alphabet B = {IDLE, ACTIVE_NARROW, ACTIVE_BROAD, BLOCKED, REVISING, DONE}

    H_boundary(t) = H_space(t)                 (TFE-for-agents.md, eq 1.2 / 1.5)
    H_interior(t) = -sum_u q_u(t) log2 q_u(t)  (eq 1.5)
    BIR(t)        = min(1, H_boundary(t) / H_interior(t))   if H_interior > 0

    FUTURE DESIGN / ANALOGY only. Not AdS/CFT. Falsify with labelled traces
    (section 8).
