DESIGN DOCUMENT — H_facade as a Multi-Agent Coordination Cost (FUTURE DESIGN / ANALOGY)

Status: FUTURE DESIGN. Not implemented. Not a fifth discovery.
Scope: this repository only (`ari322/holographic-envelope`). No Octopus repository, code, architecture, or config is written or modified.
Source math: D02 as written in `MATH-SKELETON.md` section 3 (and section 2 for frustration / overlap templates). Narrative: `AI-CONTEXT.md` D02; `agents/GROK-AGENT-MASTER.md` Way 2.
Law 3: this file maps the existing architectural Ising structure onto agent coordination. It does not invent new condensed-matter results. Architectural numbers (J^arch entries, Sydney h, predicted sigma*) are facade quantities. They are not facts about agents. Any numeric J or h shown for agents is HYPOTHETICAL.
RSB is PREDICTED for the facade problem and is NOT confirmed. This file does not confirm RSB for agents.

---

## 0. What this document is

Way 2 says: when multiple Octopus agents have conflicting objectives, the spin-glass mapping predicts multiple stable coordination equilibria, not one global optimum.

This document answers, as a design proposal only:

1. How would H_facade become a coordination cost H_coord?
2. What are the "genes" sigma for an agent / coordination unit?
3. What are the objectives f_k whose conflicts create couplings?
4. How is the coupling matrix J constructed and read?
5. What does frustration imply for coordination?
6. How would one reject the mapping?

The architectural Hamiltonian remains the source object:

    H_facade(sigma) = -sum_{i<j} J^arch_ij * sigma_i * sigma_j
                      - sum_i h_i * sigma_i
                      + lambda * P(sigma)                                 (eq 3.2)

This file proposes an analogue H_coord with the same algebraic shape.
Same shape is not the same system.

---

## 1. Existing D02 structure (unchanged)

From `MATH-SKELETON.md` section 3:

    sigma_k = 2 * (g_k - g_k_min) / (g_k_max - g_k_min) - 1              (eq 3.1)
    sigma   in [-1, +1]^6                                                 (facade k = 6)

    H_facade(sigma) = -sum_{i<j} J^arch_ij * sigma_i * sigma_j
                      - sum_i h_i * sigma_i
                      + lambda * P(sigma)                                 (eq 3.2)

    J^arch_ij = (1/M) * sum_{k=1}^{M} (d f_k / d sigma_i) * (d f_k / d sigma_j)
    M = number of objectives (M = 4 on the facade)                        (eq 3.3)

    d(g_a, g_b) = (1 / sqrt(6)) * ||g_a - g_b||_2
    P_arch(d) = distribution of d over Pareto pairs
    RSB flagged if Hartigan dip test p < 0.05 and K >= 2                  (eq 3.4)
    (flagged means "test would support the analogy"; it has not been run)

Frustration template from section 2.4:

    Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik)
    Phi_ijk = -1 : frustrated triangle
    Phi_ijk = +1 : consistent triangle

    Note from D02 write-ups: an all-positive (antiferromagnetic) triangle
    is also treated as a classical frustrated triangle, because three
    pairwise "prefer opposite" bonds cannot be satisfied at once.

Edwards-Anderson template (eq 2.1) is the parent form. H_facade is the
architectural instance. H_coord, if ever used, would be a third instance
of the same template, not a new physical law.

---

## 2. Coordination Hamiltonian — same template, new names

FUTURE DESIGN / ANALOGY:

    H_coord(sigma) = -sum_{i<j} J^coord_ij * sigma_i * sigma_j
                     - sum_i h_i * sigma_i
                     + lambda * P(sigma)

    sigma in [-1, +1]^k          (k proposed below; k need not be 6)
    J^coord                      constructed by eq 3.3, not copied from J^arch
    h                            a task-type prior, not the Sydney EPW field
    P(sigma)                     penalty for infeasible coordination, not
                                 infeasible panel geometry
    lambda                       non-negative penalty weight (design knob)

Reading:

    Lower H_coord = cheaper coordination under the current scalarisation.
    Because of frustration (section 6), "cheaper" is local: several sigma
    can be local minima. Way 2's point is exactly that there is not one
    global coordination optimum.

H_coord is a cost function for comparing already-observed or already-proposed
coordination parameter vectors. It is not an Octopus scheduler, broker, or
new orchestrator. Implementing a minimiser against live Octopus agents is
out of scope and not authorised by this document.

---

## 3. Genes sigma — a normalised vector in [-1, +1]^k

### 3.1 Why k is not 6

Facade k = 6 because the building problem is parameterised by

    [depth, aperture, rotation, hysteresis, maxStep, radiation_weight].

Those are physical / controller genes. Copying k = 6 onto agents would pretend
that "aperture" has an agent meaning. It does not.

This design uses k = 7: the smallest set that covers (who decides, how wide,
how hard, how sticky, how large a move, explore vs exploit, how much is shared)
without importing facade geometry. k = 7 is a proposal, not a measured rank.

### 3.2 Proposed coordination genes

Raw knobs g_k are whatever an observer can already score from traces or from
a written policy card. Each is then normalised by eq 3.1.

    k   name          g-domain (proposal)     sigma = -1                  sigma = +1
    --  ------------  ----------------------  --------------------------  --------------------------
    1   autonomy      [0, 1]                  wait for consensus          act without peers
    2   scope         [0, 1]                  narrow specialist lane      broad / overlapping work
    3   assert        [0, 1]                  yield / defer on clash      overwrite / insist
    4   persist       [0, 1]                  flip stance easily          hold stance (hysteresis)
    5   step          [0, 1]                  tiny incremental edits      large jumps per turn
    6   explore       [0, 1]                  exploit the current lane    try new actions / tools
    7   broadcast     [0, 1]                  keep context local          flood peers with state

Normalisation (eq 3.1, identical algebra):

    sigma_k = 2 * (g_k - g_k_min) / (g_k_max - g_k_min) - 1
    If g_k in [0, 1], this is simply sigma_k = 2*g_k - 1
    sigma in [-1, +1]^7

How g_k could be read from observable traces (FUTURE; no Octopus change):

    autonomy   fraction of actions taken with no prior peer MSG in the window
    scope      fraction of distinct artefact / topic IDs touched vs a role list
    assert     fraction of conflicts where this unit's WRITE stood last
    persist    mean run length of the same stance / symbol (see TFE alphabet)
    step       mean normalised size of WRITE diffs or plan revisions
    explore    fraction of previously unseen tool_class or topic IDs in the window
    broadcast  fraction of events that are MSG to peers, or bytes shared / bytes kept

These estimators are design sketches. If a later study cannot estimate a gene
from logs, drop that gene (k decreases). Do not invent hidden Octopus fields
to fill the vector.

### 3.3 Coordination unit

sigma may be attached to:

    (a) one agent, or
    (b) one role-level coordination unit (e.g. "writer", "critic") if several
        processes share a role.

H_coord is a function of one sigma vector (the joint policy of the unit),
or, in a later extension that still uses eq 3.2, a concatenation of several
units' genes. This document uses one sigma per unit and studies a fleet by
comparing several sigma's pairwise distances (section 7), not by enlarging
k without bound.

---

## 4. Objectives f_k — conflicts that create couplings

Facade D02 uses M = 4 building objectives (radiation, daylight deficit,
geometry uniqueness, actuation count). Those are not agent objectives.

Proposed coordination objectives (M = 4, all MINIMISE, same count as D02
so that eq 3.3 is used with a familiar M; the quantities are different):

    f1 = f_latency     time from task-open to first useful WRITE or MSG
                       (seconds or event counts)
    f2 = f_conflict    pairwise contradiction rate: fraction of peer pairs
                       whose durable artefacts disagree on a shared claim
    f3 = f_coverage    fraction of required roles / checklist items untouched
    f4 = f_cost        observable spend: turns + tool calls (+ tokens if logged)

Why these four (design justification):

    They are visible in traces. They conflict. That is all eq 3.3 needs.
    They are not a claim that Octopus "should" optimise them in production.

Conflict structure (FUTURE DESIGN / ANALOGY; qualitative, not measured):

    f1 vs f2   DIRECT. Higher autonomy / assert can cut latency and raise
               contradiction. Waiting for consensus can cut contradiction
               and raise latency.

    f3 vs f4   DIRECT. Covering more roles costs more turns and tools.

    f3 vs f2   INDIRECT. Broader scope / overlapping coverage can reduce
               missed items and increase contradictions.

    f1 vs f4   INDIRECT. Extra TOOL / retry spend can cut latency and
               raise cost.

This is the same logical shape as D02 section 2.2 (direct and indirect
conflicts, no single g* minimises all f_k). It is not the same physical
system and it is not a new discovery.

Optional fifth objective (do not add unless a study shows M = 4 hides a
dominant safety axis):

    f5 = f_safety   count of REFUSE-worthy constraint hits that were ignored
    Adding f5 changes M in eq 3.3. It does not change the template.

---

## 5. Coupling matrix J^coord

### 5.1 Construction (eq 3.3, not copied numbers)

    J^coord_ij = (1/M) * sum_{k=1}^{M} (d f_k / d sigma_i) * (d f_k / d sigma_j)

    J^coord is symmetric, zero diagonal.
    M = 4 unless f5 is added.

Sign reading (same as D02 / coupling-matrix write-up):

    J_ij < 0   cooperative / ferromagnetic analogue:
               raising sigma_i and sigma_j together tends to help the same
               objectives (product of Jacobian columns has negative mean)
    J_ij > 0   frustrating / antiferromagnetic analogue:
               the two genes pull objectives in opposing ways
    J_ij = 0   decoupled at this scalarisation

Do not paste J^arch into J^coord. J^arch entries such as J(d,a) = -0.50
are facade approximations. Using them as agent facts would be a category error.

How the Jacobian would be estimated later (design, not code):

    1. Score sigma and f_k on many windows of existing multi-agent logs, or
       on replayed traces with recorded policy cards.
    2. Standardise f_k.
    3. Estimate d f_k / d sigma_i by regression or finite difference across
       nearby windows. This is an observational Jacobian, not a controlled
       derivative, and must be labelled as such.
    4. Insert into eq 3.3. Regularise small entries to 0.

If logs cannot support a Jacobian, J^coord remains unspecified.
A missing matrix is not an invitation to reuse J^arch.

### 5.2 HYPOTHETICAL example J (illustration only)

The following signs and magnitudes are invented to show the shape of a
write-up. They are not measured. They are not J^arch. They must not be
cited as results.

HYPOTHETICAL sign sketch (rows/cols: autonomy, scope, assert, persist, step, explore, broadcast):

    gene:        aut   scp   asr   per   stp   exp   brd
    f1 latency   [-]   [+]   [-]   [+]   [-]   [+]   [+]
    f2 conflict  [+]   [+]   [+]   [-]   [+]   [+]   [-]
    f3 coverage  [+]   [-]   [0]   [0]   [0]   [-]   [-]
    f4 cost      [+]   [+]   [+]   [0]   [+]   [+]   [+]

    [-] = increasing this gene decreases this objective (helps, since we minimise)
    [+] = increasing this gene increases this objective (hurts)
    [0] = negligible in this sketch

HYPOTHETICAL sparse J^coord entries consistent with that sketch
(magnitudes are placeholders, |J| in {0.25, 0.50}):

    J(autonomy, assert)   = +0.50    frustrating: both cut latency, both raise conflict
    J(autonomy, persist)  = +0.25    weak frustration: wait-vs-hold vs go-alone
    J(scope, broadcast)   = -0.50    cooperative on coverage
    J(scope, explore)     = +0.25    weak frustration: breadth vs novelty spend
    J(persist, step)      = +0.50    frustrating: stickiness vs jump size
    J(persist, explore)   = +0.50    frustrating: hold vs wander
    J(step, explore)      = +0.50    frustrating: large jumps vs new lanes
    J(assert, broadcast)  = -0.25    weak cooperation on resolving clashes in public
    J(explore, broadcast) = -0.25    weak cooperation on sharing new findings
    all unspecified pairs = 0 in this sketch
    diagonal              = 0

This matrix is HYPOTHETICAL. If a later Jacobian disagrees, the sketch is discarded.
It has no authority over Octopus.

### 5.3 External field h (task prior, not climate)

Facade h is a Sydney EPW climate prior. Do not reuse

    h_facade = [+0.30, -0.20, +0.15, -0.10, -0.10, +0.25]

for agents.

HYPOTHETICAL task prior examples (not measurements):

    Incident-response task:   bias autonomy and step up, explore down
      h ~ [+0.3, 0, +0.2, +0.1, +0.2, -0.2, 0]     (order as section 3.2)
    Audit / critic task:      bias autonomy down, persist and broadcast up
      h ~ [-0.3, -0.1, -0.2, +0.2, -0.2, 0, +0.3]
    Open exploration task:    bias explore and scope up, persist down
      h ~ [0, +0.2, 0, -0.2, 0, +0.3, +0.1]

h is a prior over genes, not a reward hack and not a claim about Octopus defaults.

---

## 6. Frustration and multiple coordination equilibria

### 6.1 Frustrated triangle (ANALOGY, not the facade triangle)

Facade D02 highlights (eps, maxStep, wr) as a frustrated triangle.
That triangle is about controller responsiveness, smoothness, and radiation weight.
It is not an agent fact.

ANALOGUE candidate in the HYPOTHETICAL J of section 5.2:

    (persist, step, explore)

    J(persist, step)    > 0
    J(step, explore)    > 0
    J(persist, explore) > 0

    All-positive triangle: each pair "prefers opposite".
    No assignment of {persist, step, explore} in {-1, +1} satisfies all
    three antiparallel preferences. This is the D02 reading of an
    antiferromagnetic triangle, applied here as ANALOGY.

Phi product on signs (+,+,+) is +1, so the strict eq 2.4 product test does
not fire; D02 already treats this all-positive case as classical frustration.
A later measured J^coord may instead produce a Phi = -1 triangle on a
different triple. Either pattern is enough, if real, to expect multiple
local minima of H_coord. Neither pattern is claimed as measured.

### 6.2 What "multiple equilibria" means for agents (Way 2)

If H_coord is frustrated:

    - Two fleets with the same task prior h and the same f_k can settle
      at distinct sigma vectors with similar H_coord.
    - Example families (illustrative labels only):
        "consensus-heavy":   autonomy -, persist +, broadcast +, step -
        "fast-split":        autonomy +, assert +, broadcast -, persist -
        "explorer-mesh":     explore +, scope +, persist -, broadcast +
    - Choosing among those families is a design / governance decision,
      not something a single scalar run should hide.

This is the Way 2 sentence: not one global coordination optimum.
It is a predicted consequence of the mapping, not an observed Octopus law.

### 6.3 Penalty P(sigma)

P(sigma) >= 0 marks combinations treated as infeasible for the task, e.g.:

    all units with autonomy = +1 and broadcast = -1 while f_coverage must be 0
    step = +1 and persist = +1 beyond a stated stability rule

P is a design constraint, analogous to eq 3.2's geometry penalty.
It is not a new physical potential.

---

## 7. Overlap / multiplicity test (template of eq 3.4)

Do not claim RSB. The facade protocol is PREDICTED and unrun. Agents inherit
only the test template.

FUTURE protocol (logs or offline replay; no Octopus modification):

    1. Collect R independent coordination traces for the same task family
       (different seeds, start times, or human kickoffs). R >= 5 if possible.
    2. Score one sigma per trace (or per stable window).
    3. Distances:
         d(sigma^a, sigma^b) = (1 / sqrt(k)) * ||sigma^a - sigma^b||_2
         (eq 3.4 with 6 replaced by k)
    4. Histogram P_coord(d).
    5. Hartigan dip test. Fit a Gaussian mixture. Read K.

Classification (same table shape as D02, applied to this mapping only):

    K = 1 and dip p >= 0.05   unimodal: multiplicity not supported
    K = 2 and dip p < 0.05    two basins: weak support for Way 2
    K >= 3 and dip p < 0.01   many basins: stronger support for Way 2
    clusters stable across R  still not "RSB confirmed"; say
                              "multimodal coordination attractors in this corpus"

Predicted ground-state numbers from the facade (sigma* ~ [+0.4, +0.3, 0.0, ...])
must not be reused as predicted agent equilibria.

---

## 8. Falsification protocol for the coordination-Hamiltonian mapping

This rejects the agent mapping. It does not reject D02 for facades.

    F1  Jacobian collapse.
        If every estimated |d f_k / d sigma_i| is consistent with noise,
        eq 3.3 yields J ~ 0. Then H_coord is only an external-field model.
        Reject the "couplings from objective conflict" story for this corpus.

    F2  No frustration.
        If the estimated J^coord has no Phi = -1 triangle and no all-positive
        triangle of material bonds (|J| above a stated threshold, e.g. 0.2),
        reject "frustration guarantees multiple coordination equilibria"
        for this gene set.

    F3  Single attractor.
        If P_coord(d) is unimodal (Hartigan p >= 0.05, K = 1) across R >= 5
        independent traces of the same task, reject Way 2's multiplicity
        claim for that task. The mapping may still be a useful scalar cost
        with one basin; it is not a spin-glass-like coordinator.

    F4  Architectural-number leak.
        If a model that uses J^arch's numeric entries (padded or truncated
        to k) predicts f_k or basin labels as well as or better than the
        log-estimated J^coord, treat that as a failed domain transfer:
        the agent problem is not inheriting facade numbers. Discard the
        copied matrix. Do not promote J^arch to an agent fact.

    F5  Reparameterisation.
        If a change of coordinates on (persist, step, explore) — or whichever
        triple was blamed — removes all frustrated triangles and the landscape
        of H_coord becomes single-basin under F3, then the multiplicity was
        a parameterisation artefact. Reject "intrinsic multiple equilibria".
        (This parallels the open facade question of reparameterising
        (eps, maxStep, wr); it does not answer that facade question.)

    F6  Circular energy.
        If H_coord is used both to select "equilibria" and to define the
        labels of those equilibria, the test is invalid. Labels must come
        from task outcomes or human family names, not from H_coord itself.

What would NOT count as confirmation:

    - Drawing a pretty J matrix by hand (section 5.2 is not evidence)
    - Saying "agents are spins" without eq 3.3 estimates
    - Any sentence of the form "RSB is confirmed"
    - A single multi-agent anecdote

---

## 9. Explicit non-goals

    - No implementation, no optimiser, no Octopus wiring, no new broker.
    - No claim that D02 or RSB is confirmed on facades or on agents.
    - No BIR in this file (next ROLE 06 task: BIR-for-agents.md).
    - No fifth discovery.
    - Do not minimise H_coord on a live system on the strength of this text.

---

## 10. One-page formula card (ASCII)

    sigma_k = 2*(g_k - g_min_k)/(g_max_k - g_min_k) - 1
    sigma   in [-1, +1]^7
            = (autonomy, scope, assert, persist, step, explore, broadcast)

    f = (f_latency, f_conflict, f_coverage, f_cost)     all MINIMISE

    J^coord_ij = (1/M) * sum_k (d f_k / d sigma_i) * (d f_k / d sigma_j)
    H_coord(sigma) = -sum_{i<j} J^coord_ij * sigma_i * sigma_j
                     - sum_i h_i * sigma_i
                     + lambda * P(sigma)

    J^coord is estimated, not copied from J^arch.
    Example numbers in this file are HYPOTHETICAL.
    FUTURE DESIGN / ANALOGY only. Falsify with F1–F6.
