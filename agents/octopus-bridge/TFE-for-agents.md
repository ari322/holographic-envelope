DESIGN DOCUMENT — Temporal Facade Entropy for Octopus Agents (FUTURE DESIGN / ANALOGY)

Status: FUTURE DESIGN. Not implemented. Not a fifth discovery.
Scope: this repository only (`ari322/holographic-envelope`). No Octopus repository, code, architecture, or config is written or modified.
Source math: D01 as written in `MATH-SKELETON.md` eqs 1.1–1.4 (and `AI-CONTEXT.md` D01).
Operational reading: `agents/GROK-AGENT-MASTER.md` Way 1 (TFE as agent communication entropy).
Law 3: this file maps existing TFE equations onto observable agent traces. It does not invent new physics. Any claim-like sentence below is a mapping to be tested, not a confirmed result. D01 itself is mathematically defined; facade validation is still pending. This agent mapping is separately untested.

---

## 0. What this document is

Way 1 says: each Octopus agent's output stream has a TFE equivalent; low TFE means the agent is stuck in a loop; high TFE means the agent is exploring.

This document answers, as a design proposal only:

1. How would TFE be computed for an Octopus agent from logs that already exist?
2. What is the "panel state" analogue? (a discrete alphabet of observable outputs)
3. What is the time window T, and how should it be chosen?
4. How are H_space(t) and H_time(i) estimated so that TFE(i,t) = H_space(t) * H_time(i)?
5. How would one reject the mapping with logged traces?

Nothing here is wired, simulated, or validated. RSB is not discussed in this file. Facade TFE is not claimed to be empirically confirmed.

---

## 1. Existing D01 equations (unchanged)

From `MATH-SKELETON.md`:

    H(X)        = -sum_i p_i * log2(p_i)                         (eq 1.1)
    H_space(t)  = -sum_{s=1}^{N} p_s(t) * log2(p_s(t))           (eq 1.2)
    H_time(i)   = -sum_{s=1}^{T} p_s(i) * log2(p_s(i))           (eq 1.3)
    TFE(i, t)   = H_space(t) * H_time(i)                         (eq 1.4)
    TFE_total   = (1/N_units) * sum_i (1/N_ticks) * sum_t TFE(i,t)

    Range: [0, log2(N) * log2(T)]

Index hygiene (the skeleton uses i in two roles; this design keeps them separate):

    s        = discrete state symbol (panel state in D01; output class here)
    i        = unit index (panel in D01; agent or coordination unit here)
    t        = time index (tick or event-bin)
    N        = number of distinct states in the alphabet (eq 1.2)
    T        = number of distinct occupied states in the temporal occupancy
               histogram for unit i (eq 1.3: "number of distinct time-states observed")
    N_units  = number of units in the spatial ensemble
    W        = window length used to estimate occupancies (design parameter)

Convention: terms with p = 0 are omitted (standard Shannon). log2 is base-2; units are bits for each entropy and bit^2 for the product TFE.

D01 interpretation, restated without new claims:

    TFE = 0:     all units identical in space and unchanging in time
    TFE = max:   maximally diverse states across space and time
    Prediction on facades (pending, not used as agent evidence):
      TFE_optimised > TFE_rule-based > TFE_static = 0

Way 1 analogue (FUTURE DESIGN / ANALOGY, not a discovery):

    low TFE  ~ stuck / looping / idle-homogeneous
    high TFE ~ exploring / heterogeneous activity

High TFE is not automatically "healthy". White-noise thrashing also raises entropy. Falsification in section 8 must be able to reject a naive "higher is better" reading.

---

## 2. Observation contract — logs only, no Octopus internals

TFE for agents is a post-hoc function of an already-written event log. The design does not require changing Octopus state machines, prompts, tools, or routing.

Minimum log record (observable fields only):

    event = (unit_id, t_stamp, action_type, tool_class, message_genre, status_flag)

    unit_id        = which agent or coordination unit emitted the event
    t_stamp        = existing timestamp or monotone event index
    action_type    = coarse verb already visible in the trace (read, write, search, ...)
    tool_class     = family of tool, if a tool was called; else NONE
    message_genre  = addressee / genre already visible (peer, human, status, none)
    status_flag    = WAIT / REFUSE / OK if the trace already records it

Classifier C maps one event to one symbol in alphabet A. C is deterministic and inspectable. C is not an Octopus code change; it is a log-scoring rule living in this research repo if it is ever implemented later.

Forbidden for this mapping:

    - reading hidden planner state, weights, or private memory
    - inventing new Octopus telemetry
    - treating missing LAN ports or missing traces as proof that agents have no TFE
      (that is body_not_on_this_host / data_absent, not TFE = 0)

---

## 3. Panel-state analogue — discrete alphabet A

In D01 a panel occupies one of a finite set of discrete states (or a discretised open-ratio bin). The agent analogue is the observable output class of one event, not an internal activation.

Proposed alphabet A (8 symbols). Concrete, closed, and built only from observable outputs:

    Symbol     Observable signature (examples, not Octopus APIs)
    --------   -------------------------------------------------
    READ       inspect / open / list existing context or files; no mutation
    SEARCH     query / grep / retrieve over a corpus or index
    WRITE      propose or emit a file patch, draft, or durable artefact
    TOOL       invoke a non-search tool (browser, calculator, ticket, ... )
    MSG        address a peer agent or a human with task content
    STATUS     heartbeat, board row, progress, or "still working" note
    WAIT       idle, blocked, retry-backoff, or empty tick
    REFUSE     constraint hit, rejection, or explicit no-op on policy

Why this alphabet (design justification, not a discovery):

    1. It is discrete, so eq 1.1 applies without inventing a continuous entropy.
    2. It is observable: a reviewer can label a raw trace with these 8 tags.
    3. It separates "doing work" (READ/SEARCH/WRITE/TOOL/MSG) from
       "not progressing" (WAIT/STATUS/REFUSE), which is what Way 1 needs
       in order to talk about loops vs exploration.
    4. |A| = 8 so H_max per factor is log2(8) = 3 bits and TFE_max = 9 bit^2
       when both spatial and temporal occupancies are uniform on all 8.
    5. It does not copy facade states {CLOSED, SHADED, VENTILATE, OPEN, SAFE}.
       Those are building-physics states. Copying them would be a false isomorphism.

Optional refinement (still the same D01 formula, not a new metric):

    Split MSG into MSG_PEER and MSG_HUMAN, or split TOOL by tool_class,
    only if a pilot labelling study shows the 8-symbol alphabet collapses
    distinct behaviours into one bin. Alphabet growth is a calibration choice.
    It is not a new discovery.

What is NOT a panel-state analogue:

    token embeddings, hidden chain-of-thought, Octopus role IDs as "spins",
    or any quantity that requires modifying Octopus to emit.

---

## 4. Unit i and the two observation modes

Eq 1.4 needs a spatial ensemble (to form p_s(t)) and a per-unit history (to form p_s(i)).

### 4.1 FLEET mode (direct facade analogue)

    unit i     = one Octopus agent (or one named coordination unit)
    N_units    = number of agents present in the log during the window
    At tick t  = one symbol per unit (last event in the tick, or majority vote)

    p_s(t)     = (number of units whose symbol at t is s) / N_units
    H_space(t) = Shannon entropy of that occupancy                         (eq 1.2)

This is the closest structural map: agents are panels; the fleet is the facade.

Degeneracy: if N_units = 1, then p_s(t) is a point mass and H_space(t) = 0,
so TFE(i,t) = 0 for every t. That is mathematically correct and operationally useless
for a singleton. Use TRACE mode for a single agent.

### 4.2 TRACE mode (single-agent spatial slice)

FUTURE DESIGN / ANALOGY: treat a short contemporaneous bundle of B events
from the same agent as the "panel array" at time t.

    B          = micro-batch size (proposal: B = 8)
    bundle(t)  = the B events ending at t (event-indexed) or falling in tick t
    p_s(t)     = (count of symbol s in bundle(t)) / B
    H_space(t) = entropy of that bundle                                    (eq 1.2)
    unit i     = the one agent
    H_time(i)  = entropy of that agent's symbols over the long window W    (eq 1.3)

B is not a fifth parameter of nature. It is a binning choice, analogous to
choosing how many panels you photograph in one facade snapshot.

Proposal: report both modes when a fleet log exists; report TRACE mode when it does not.
Do not mix modes in one number without saying which mode was used.

---

## 5. Time window T — how to choose it

Two different "T"s must not be confused.

    T_states  = support size of the temporal occupancy histogram for unit i
                (this is T in eq 1.3 and in the D01 range formula)
    W         = number of events or ticks used to estimate that histogram
    tau       = optional wall-clock length of the same window

### 5.1 Proposed default window

    Event window (primary):   W = 64 events per unit
    Clock window (secondary): tau = 900 seconds of wall time
    Tick size:                one event, or 15-second bins if clocks are coarse
    Micro-batch for TRACE:    B = 8 events

Why these numbers (design, not measured optima):

    1. Occupancy estimates need counts. A rule of thumb is W >= 4 * |A| = 32
       so that a uniform explorer can visit every symbol a few times.
       W = 64 is one doubling above that floor.
    2. W < 2 * |A| is rejected as "window too short"; do not emit a TFE number.
    3. 900 s is long enough to cover a stuck retry loop and short enough
       that a shift from exploration to idle is not averaged away.
    4. If the log is event-rich, prefer W (event window) over tau (clock window),
       because idle gaps would otherwise dominate p_WAIT.
    5. If the log is clock-regular (heartbeats every few seconds), use tau
       so that WAIT is visible.

Sliding vs tumbling:

    Default: sliding window, step = 8 events (or 1 tick).
    This produces a TFE(i,t) surface, matching D01's heatmap over (unit, time).
    Tumbling windows are allowed for a single daily summary TFE_total.

### 5.2 How T_states is obtained

After the window is chosen, build the temporal occupancy for unit i:

    n_s(i)   = number of events of symbol s for unit i inside the window
    p_s(i)   = n_s(i) / W
    T_states = number of symbols with n_s(i) > 0

    H_time(i) = -sum_{s: n_s(i)>0} p_s(i) * log2(p_s(i))                 (eq 1.3)

T_states is observed, not chosen. Choosing W and A is what the designer does.

---

## 6. Estimating H_space(t), H_time(i), and TFE(i,t)

Procedure (design only; no implementation in this change):

    Step 1  Read an existing agent event log. Do not instrument Octopus.
    Step 2  Map each event through C to a symbol in A.
    Step 3  Choose mode (FLEET or TRACE) and window (W, tau, B).
    Step 4  For each tick t in the reporting interval:
              form p_s(t) from the spatial ensemble at t
              H_space(t) = -sum_s p_s(t) * log2(p_s(t))                  (eq 1.2)
    Step 5  For each unit i:
              form p_s(i) from unit i's symbols in the window ending at t
              H_time(i) = -sum_s p_s(i) * log2(p_s(i))                   (eq 1.3)
    Step 6  TFE(i,t) = H_space(t) * H_time(i)                            (eq 1.4)
    Step 7  Optional scalar: TFE_total as in MATH-SKELETON eq 1.4.

Worked occupancy sketch (FUTURE DESIGN / ANALOGY; synthetic counts, not data):

    Suppose FLEET mode, N_units = 4, A as in section 3, one tick t0:
      symbols at t0 = {WRITE, WRITE, STATUS, WAIT}
      p_WRITE(t0) = 2/4, p_STATUS(t0) = 1/4, p_WAIT(t0) = 1/4
      H_space(t0) = -(0.5*log2(0.5) + 0.25*log2(0.25) + 0.25*log2(0.25))
                  = 1.5 bits

    Suppose unit i=1 spent a W=8 window as {WRITE, WRITE, WRITE, WRITE,
      WRITE, WRITE, WRITE, WRITE}:
      H_time(1) = 0 bits
      TFE(1, t0) = 1.5 * 0 = 0

    Suppose unit i=2 spent W=8 as one of each of 8 symbols:
      H_time(2) = 3 bits
      TFE(2, t0) = 1.5 * 3 = 4.5

These numbers illustrate the product. They are not measurements.

---

## 7. Interpretation (Way 1) — labelled ANALOGY

D01: a static envelope has TFE = 0; a diverse adaptive envelope can approach the range max.

Way 1 mapping (FUTURE DESIGN / ANALOGY):

    Pattern                         Typical (H_space, H_time, TFE)
    ------------------------------  ------------------------------------------
    All agents idle / same WAIT     H_space ~ 0, H_time ~ 0, TFE ~ 0
    One agent looping one action    H_time(i) ~ 0, TFE(i,*) ~ 0
    Fleet lockstep same action      H_space ~ 0, TFE ~ 0 even if H_time > 0
    Heterogeneous exploring fleet   both factors high, TFE high
    Random thrash / tool-storm      both factors high, TFE high (not "good")

So:

    TFE ~ 0 is evidence of homogeneity, not automatically of failure.
    A successful coordinated WRITE by every agent at once also has low H_space.

Way 1's slogan "low TFE = stuck; high TFE = exploring" is therefore a one-sided
reading of the product. This design keeps the slogan as the intended operational
hypothesis and requires falsification (section 8) to say when it fails.

What this mapping does not say:

    - It does not say D01 is empirically validated on facades.
    - It does not say agent TFE is a new scientific discovery.
    - It does not say high TFE should be a reward in an Octopus controller
      (that would be an implementation decision, forbidden here).

---

## 8. Falsification — reject this mapping with logged traces

This is a test of the agent mapping, not a test that D01 is true for buildings.

### 8.1 Independent labels (do not use TFE to define the labels)

From raw traces, mark windows with an independent rule or a human rater:

    IDLE     majority WAIT/STATUS, no WRITE/TOOL/MSG
    LOOP     a short symbol n-gram (n=4 or 5) repeats >= 3 times, or
             one symbol occupies >= 80% of W while a task remains open
    EXPLORE  >= 4 distinct symbols in W, no dominant n-gram, and at least
             one WRITE or MSG that is not a repeat of the previous WRITE/MSG
    MIXED    everything else

Labels may be produced by a second rater. TFE is computed only after labels exist.

### 8.2 Predictions to test (ANALOGY to D01 ordering)

    P1  median TFE(EXPLORE) > median TFE(MIXED) > median TFE(LOOP)
    P2  median TFE(IDLE) is near 0 relative to TFE(EXPLORE)
        (propose: TFE(IDLE) <= 0.1 * TFE_max, with TFE_max = log2(|A|) * log2(|A|))
    P3  FLEET lockstep (all units same symbol) has H_space < 0.5 bits
    P4  Alphabet A is adequate: fewer than 10% of events need an "OTHER" bin
        (if OTHER is added during labelling, the alphabet failed)

### 8.3 Rejection rules

    R1  If median TFE(LOOP) >= median TFE(EXPLORE) on a labelled corpus
        of at least 30 windows per class, reject Way 1's low/high reading.
    R2  If TFE(IDLE) is not distinguishable from TFE(EXPLORE)
        (e.g. two-sided test p >= 0.05 or overlapping interquartile ranges
        with effect size |median_diff| / TFE_max < 0.1), reject the mapping
        as a discriminator.
    R3  If changing W over {32, 64, 128} reverses the P1 ordering,
        the mapping is window-fragile; reject the default window, not D01.
    R4  If TRACE mode and FLEET mode disagree on the same multi-agent log
        (rank correlation of per-tick TFE_total < 0), do not treat TFE as
        mode-invariant; report the failure and keep D01's facade formula intact.
    R5  If a corpus of known diverse traces collapses to one or two symbols
        under C, reject alphabet A; do not invent a new entropy.

A rejected mapping means: do not use TFE as an Octopus health signal.
It does not retract D01 for facades. It does not create a replacement discovery.

### 8.4 What would NOT count as confirmation

    - Pretty heatmaps without labels
    - A single anecdotal looping agent
    - Any statement that "RSB is confirmed"
    - Using TFE as both the metric and the label (circular)

---

## 9. Explicit non-goals

    - No code, no simulator, no Octopus wiring.
    - No BIR in this file (ROLE 06 next task: BIR-for-agents.md).
    - No new coupling matrix, no new Hamiltonian (see hamiltonian-for-agents.md).
    - No claim that this is Discovery 05.
    - No claim that facade TFE or this analogue has been measured.

---

## 10. One-page formula card (ASCII)

    Alphabet A = {READ, SEARCH, WRITE, TOOL, MSG, STATUS, WAIT, REFUSE}
    C: event -> A                         (log-only classifier)
    p_s(t) = occupancy of symbol s at tick t over the spatial ensemble
    p_s(i) = occupancy of symbol s for unit i inside window W
    H_space(t) = -sum_s p_s(t) log2 p_s(t)
    H_time(i)  = -sum_s p_s(i) log2 p_s(i)
    TFE(i,t)   = H_space(t) * H_time(i)

    FUTURE DESIGN / ANALOGY only. Falsify with labelled traces (section 8).
