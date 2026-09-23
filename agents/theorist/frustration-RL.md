# Frustrated Triangle and Exploration-Exploitation

THEORIST wake note (ROLE 04, task 3). Grounded in `AI-CONTEXT.md` D02 and Open Question 5, `MATH-SKELETON.md` Sections 2.4 and 3, `research/formal-model.md` (hysteresis gate), and Discovery 02 (`discoveries/discovery-02-coupling-matrix.md`, `discovery-02-mathematics.md`). No Wallacei run exists; `J^arch` is a physically motivated approximation, not a calibrated matrix. RSB is predicted, not confirmed. Critic has not written `unsupported-claims.md`. This note proposes a mapping; it does not add a discovery.

**Short answer.** [CONFIRMED] The repo names `(eps, Delta_s, wr)` as a triangle of positive (conflict) couplings among hysteresis, max step, and radiation weight. [SPECULATIVE] That triple is the facade's native form of the exploration-exploitation dilemma, but it is three-way, not two-way: smoothness, tracking speed, and which sensory reward to trust cannot be jointly satisfied. Vanilla RL `eps_greedy` is a one-parameter collapse of a richer conflict already written into `B(t)`.

---

## 1. What the triangle is [CONFIRMED]

Gene vector (`AI-CONTEXT` D02; MATH-SKELETON 3.1):

```
sigma = [s_d, s_a, s_r, s_eps, s_Delta_s, s_wr]    in [-1, +1]^6
```

The last three coordinates are controller genes, not geometry:

- `eps` — hysteresis dead-band (`epsilon` in the formal model)
- `Delta_s` — `maxStep`, the largest allowed change of open-ratio per time step
- `wr` — radiation weight in the panel map

Formal model of the gate:

```
o_i(t) = clamp( wr*R_i + wt*T_i + wc*C_i + wu*U_i , 0, 1 )
delta  = o_i(t) - o_i(t-1)
if |delta| < eps:   hold
else:               step by min(|delta|, Delta_s) * sign(delta)
```

Typical starting values in that file: `eps = 0.05`, `maxStep = 0.10`. The weights on `R, T, C, U` are declared to sum to 1, so raising `wr` lowers the other channels by construction.

`AI-CONTEXT` lists the triangle couplings as all positive:

```
J(eps, Delta_s) = +0.50     responsiveness vs smoothness
J(eps, wr)      = +0.25     weak frustration
J(Delta_s, wr)  = +0.25     weak frustration
```

Verbal meaning in D02: a positive `J` is a conflict coupling (genes do not help the same objectives when both increase). The three pairwise conflicts are:

1. **`eps` vs `Delta_s`.** Low `eps` plus high `Delta_s` tracks `o_i` tightly (better f1/f2 tracking, worse f4 actuation count). High `eps` plus low `Delta_s` holds and creeps (better f4, worse tracking). Discovery 02 Part II.2 names this as the f4 vs f1/f2 indirect conflict.
2. **`eps` vs `wr`.** High `wr` asks the controller to follow radiation; high `eps` ignores small radiation changes. The dead-band can null the very channel the weight amplifies.
3. **`Delta_s` vs `wr`.** High `wr` produces larger target moves when `R` ramps; low `Delta_s` caps those moves. Radiation priority and slew-rate limit fight.

MATH-SKELETON 2.4 writes the triangle test

```
Phi_ijk = sign(J_ij) * sign(J_jk) * sign(J_ik)
Phi = -1  frustrated
Phi = +1  consistent
```

All three listed `J` are positive, so `Phi(eps, Delta_s, wr) = +1`. The same documents nevertheless call this a classical antiferromagnetic triangle: three anti-alignment preferences cannot be satisfied at once. That is a definitional tension already in Discovery 02 Part III.5 (product `+` vs AFM reading). This note does not repair it. The exploration-exploitation mapping uses the *verbal* D02 claim — the three pairs conflict — not a resolved `Phi`.

Further confirmed limits (`AI-CONTEXT` Section 4): `J^arch` is approximate; RSB is not confirmed; Open Question 5 asks whether the triangle can be eliminated by reparameterisation (MATHEMATICIAN task 4, not done).

---

## 2. What exploration-exploitation is [CONFIRMED]

In reinforcement learning, an agent that only exploits its current value estimate can lock onto a suboptimal policy; an agent that only explores never harvests reward. The dilemma is that a single action cannot fully do both. Standard one-parameter compromises (`eps_greedy`, Boltzmann temperature, UCB bonus, entropy regularisation) pick a point on that trade-off. None of this is a facade measurement. It is the textbook object the ROLE 04 prompt asks to connect.

Two distinctions must stay sharp:

- **`eps_hyst` is not `eps_greedy`.** In the formal model, *larger* `eps` means *less* motion (hold unless `|delta|` is large). In `eps_greedy`, *larger* `eps` means *more* random action. Name collision only.
- **Step-size is not exploration.** A large `Delta_s` (or a large learning rate) is aggressive *use* of the current target or gradient. It can look exploratory because the state jumps, but it is not information-seeking. Classical exploration is trying actions that are not currently believed best.

The facade already has an explicit reward-like scalarisation: f1..f4 in Discovery 02, and `H_facade` as a further scalar energy (`MATH-SKELETON` 3.2). `AI-CONTEXT` Section 3 also allows BIR as a possible RL reward. Those are *what* is optimised. The triangle is *how* `B(t)` is allowed to move while optimising.

---

## 3. Proposed correspondence [SPECULATIVE]

Map the three genes onto three familiar RL knobs:

```
eps      <->  stickiness / inverse exploration of new open-ratios
              high eps  = exploit the current panel state (hold)
              low eps   = follow small target changes (track / churn)

Delta_s  <->  action magnitude / maximum policy step
              high Delta_s = exploit the current target at full slew
              low Delta_s  = conservative update

wr       <->  reward-channel prior (exploitation of radiation)
              high wr = exploit R; starve T, C, U on the simplex
              low wr  = spread credit across channels
```

Under this reading the "dilemma" is not a single explore/exploit slider. It is the incompatibility of three demands:

- **D1 smoothness:** high `eps`, low `Delta_s` (low f4, visually quiet, Axiom A4).
- **D2 tracking:** low `eps`, high `Delta_s` (follow `o_i`, spend actuation).
- **D3 radiation priority:** high `wr` (Sydney field `h_wr = +0.25` in D02).

D3 makes D1 worse (more signal that the dead-band must ignore or the slew must cap) and D2 more expensive (larger `|delta|` when `R` moves). Pairwise, that is exactly the three positive `J` entries. A two-parameter RL agent that only sets `eps_greedy` cannot represent D3; a three-parameter agent that sets `(explore_rate, step_size, reward_weight_R)` can.

This would be falsified if an implemented facade controller, with `eps`, `Delta_s`, and `wr` swept independently on a fixed EPW/occupancy chronicle, showed no pairwise objective conflict: i.e. if there existed a direction in `(eps, Delta_s, wr)` that simultaneously improved (or held) f1, f2, and f4. That is the operational meaning of "the triangle is not a dilemma."

A second, sharper falsifier on the *name* of the map: this would be falsified if logged behaviour showed high `eps_hyst` *increasing* state-space coverage (the `eps_greedy` direction) rather than decreasing actuation and holding. The inverted-epsilon claim would then be wrong and the table above would have to be rewritten.

---

## 4. Why a one-parameter collapse is not a solution [SPECULATIVE]

Open Question 5 asks whether `(eps, Delta_s, wr)` can be reparameterised so the frustrated triangle disappears. MATHEMATICIAN has not written `reparameterisation.md`. A natural RL-flavoured collapse is:

```
(eps, Delta_s, wr)  |--->  lambda_EE
```

for example a single temperature, or a single UCB constant, or a single `eps_greedy`, with `wr` frozen at the Sydney prior. That can remove the *algebraic* triangle from `J^arch` by deleting two coordinates. It does not remove the *objectives* that produced the triangle: f4 vs f1/f2, and radiation vs daylight/occupancy.

This would be falsified if a one-knob controller (one explore/exploit scalar, `wr` fixed) recovered the same set of non-dominated (f1, f2, f4) outcomes as the three-gene controller on the same chronicle — i.e. if the extra two genes were gauge and not payoff-relevant. If the one-knob Pareto set is a strict subset, the collapse hid degrees of freedom that the dilemma was using.

A stronger version, still speculative: any reparameterisation that makes `Phi = +1` *and* all pairwise `J <= 0` among the new coordinates has merely moved the conflict into the definition of the new coordinates (the way `eps_greedy` hides the value-of-information problem inside one scalar). This would be falsified if the new coordinates were independently interpretable *and* a Jacobian rebuild (`MATH-SKELETON` 3.3) still produced a positive-triangle among them.

---

## 5. Landscape reading: policy families, not one policy [SPECULATIVE]

D02 predicts that the frustrated triangle helps produce multiple local minima of `H_facade` and, if the Hartigan protocol fires, `K >= 2` clusters in gene space (RSB-equivalent). The RL translation is: there is no single optimal stationary policy for the Sydney prior; there are families,

- low-actuation / high-hold (exploit current geometry),
- radiation-tracking / high-slew (exploit `R`),
- mixed-channel / moderate-gate (split credit across `R, T, C, U`),

that sit in different basins. That matches Discovery 02's architectural claim that designers should be shown families, not one front. It is *not* an empirical result. `AI-CONTEXT` forbids treating RSB as confirmed.

This would be falsified if the Wallacei protocol in MATH-SKELETON 3.4 returned a unimodal `P_arch(d)` (Hartigan p >= 0.05, GMM `K = 1`) while the triangle couplings remained positive — i.e. if the named AFM triangle did not generate multiple attractors. It would also be falsified if the detected clusters differed only in `(d, a, r)` and not in `(eps, Delta_s, wr)`, which would mean the geometry genes, not the explore/exploit triple, carry the multimodality.

A related, weaker claim: an online RL controller that treats BIR or `-H_facade` as reward will inherit the same multi-basin structure in its *hyperparameter* space `(eps, Delta_s, wr)` even if the policy weights themselves converge. This would be falsified if repeated RL seeds, with those three held in the D02 box constraints, converged to one hyperparameter neighbourhood with no gap in `(f1, f2, f4)`.

---

## 6. What the mapping does *not* say [CONFIRMED]

- It does not say the facade *is* an RL agent. `B(t)` is a deterministic hysteresis map (Axiom A1, formal model). RL is a possible *outer* trainer or a source of vocabulary, not a claim that panels epsilon-greedy the sun.
- It does not confirm RSB, calibrate `J^arch`, or answer Open Question 5.
- It does not identify `eps_hyst` with `eps_greedy`. Doing so inverts the hold-vs-explore direction.
- It does not use BIR as a measured reward. BIR has never been logged; using it as an RL reward remains the future option already written in `AI-CONTEXT` Section 3.
- Sign convention for `J` remains internally tense (Hamiltonian `H = -sum J sigma_i sigma_j` vs D02's "J > 0 means anti-align"). The mapping is attached to the conflict table and the gate equations, which do not need that sign to be repaired first.

---

## 7. Deepened falsifiers (summary)

| Claim | Status | Falsifier |
|---|---|---|
| `(eps, Delta_s, wr)` pairwise-conflict on f1/f2/f4 | [SPECULATIVE] use of listed `J` | Independent sweeps find a joint improvement direction for f1, f2, and f4 |
| High `eps` = hold, not explore | [SPECULATIVE] inverted-epsilon | High `eps` increases, rather than decreases, actuation or state-space coverage |
| Triangle = three-way EE, not one knob | [SPECULATIVE] | One-scalar EE controller matches the three-gene (f1, f2, f4) front |
| Reparameterisation removes only algebra | [SPECULATIVE] | New coordinates are independently readable and a Jacobian rebuild still yields a positive triangle |
| Triangle implies multiple policy families | [SPECULATIVE] | Hartigan/GMM on Wallacei: `K = 1`, or clusters ignore `(eps, Delta_s, wr)` |
| RL seeds inherit the multi-basin | [SPECULATIVE] | Repeated RL trainings collapse to one hyperparameter neighbourhood |

A confirmed negative on the first row would remove the object this note maps. A confirmed negative on the Hartigan row would remove the landscape half and leave only the single-controller dilemma (still a possible EE analogue, just without RSB flavour). None of these tests has been run. None is a Critic finding.

---

## 8. Position

[CONFIRMED] The repo already encodes a three-gene conflict among dead-band, slew limit, and radiation weight, sitting in the same gate that Axiom A4 requires for stability. That is the concrete mechanism. Exploration-exploitation is the nearest named dilemma in adjacent theory.

[SPECULATIVE] The right correspondence is inverted-epsilon (hold vs track), step-size, and reward-channel prior — a *triangle*, not a single `eps_greedy`. Collapsing it to one RL knob would answer Open Question 5 only algebraically. This would be falsified if the tests in Section 7 went the other way, in particular if a one-knob controller reproduced the three-gene payoff front or if Wallacei multimodality lived only in geometry genes.

Until those tests exist, THEORIST's claim is limited to: the frustrated triangle is the project's already-written explore/exploit structure, and RL vocabulary is useful only if `eps_hyst` is not confused with `eps_greedy` and the third vertex (`wr`) is not dropped.
