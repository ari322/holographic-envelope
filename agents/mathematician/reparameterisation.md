# Reparameterisation of (eps, ms, wr)
# Agent: MATHEMATICIAN
# Date: 2026-09-23
# Status: PROPOSAL (verification-adjacent; not a confirmed discovery)
# Depends on: frustration-proof.md, coupling-matrix-derivation.md

## Purpose

Propose a change of variables for the control genes (eps, ms, wr) that
removes the *narrative* frustrated triangle and reduces objective-level
conflict between responsiveness, smoothness, and radiation weighting.

Context from frustration-proof.md:
  Under locked H = -sum J sigma sigma and Phi, neither J_pub nor J_der
  gives Phi=-1 on (eps,ms,wr). The "eliminate frustrated triangle" task
  is therefore interpreted as:
    (T1) eliminate the convention-dependent AF-triangle narrative, and
    (T2) reduce the f1/f2 vs f4 tension that motivated positive J(eps,ms).

Falsification condition:
  Implement the map below in the simulator gene layer. Recompute empirical
  J_emp on the new coordinates. The proposal FAILS if
    (a) Phi_emp on every 3-subset of new control coordinates is unchanged
        in the sense that the same AF-narrative text still applies, AND
    (b) Wallacei multi-start still needs the old (eps,ms) pair to reach
        the same Pareto coverage (HV drop > 10% at equal budget).

RSB not claimed.

---

## 1. Old coordinates

  eps in [0.01, 0.15]   hysteresis band
  ms  in [0.05, 0.30]   maxStep
  wr  in [0.2,  0.8]    radiation weight

Normalised: sigma_eps, sigma_ms, sigma_wr in [-1,+1].

---

## 2. Proposal A — (rho, eta, wr)  [recommended default]

Separate "how fast we may move" from "how much chatter we tolerate".

Define:
  rho = ms / max(eps, eps_floor)     # step-per-band ratio (responsiveness)
  eta = eps * ms                     # product proxy for actuation aggressiveness
  wr  = wr                           # unchanged

with eps_floor = 0.01 (lower end of eps domain).

Inversion (for implementation):
  Given (rho, eta) with rho > 0, eta > 0:
    eps = sqrt( eta / rho )
    ms  = sqrt( eta * rho )
  then clamp to the legal box [0.01,0.15] x [0.05,0.30].

Normalise rho, eta to [-1,+1] with project-chosen bounds after a pilot
sweep (SIMULATOR). Until bounds exist, treat Proposal A as a symbolic map.

Why this attacks the narrative triangle:
  J_pub tied frustration to the pair (eps, ms) both coupling positively
  to each other and to wr. Replacing the pair by (rho, eta) makes the
  primary conflict one coordinate (eta ~ wear / chatter) versus wr,
  i.e. a 2-gene trade-off, not a 3-cycle of antiparallel preferences.

CLAIM R1: In coordinates (rho, eta, wr), any Phi 3-cycle that used the
(eps,ms) bond as one edge is undefined; the AF-triangle sentence in
discovery-02 Sec 3.5 cannot be copied verbatim.
  Falsify: rewrite discovery-02 with an explicit 3-cycle among
  (rho, eta, wr) under locked H and Phi=-1.

---

## 3. Proposal B — (tau, wr) hard reduction

Collapse control to two genes:
  tau = characteristic response time proxy = eps / ms
  wr  = radiation weight

Set ms = ms_ref (constant, e.g. midpoint 0.175) and eps = tau * ms_ref,
clamped. This literally deletes one spin from H, so no 3-triangle remains
among control genes.

Cost: loses independent exploration of the eps-ms Pareto edge.

CLAIM R2: Proposal B eliminates any control-only 3-triangle by dimension
reduction. Falsify: show a required design family that needs independent
eps and ms variation beyond tau at fixed ms_ref (e.g. >5% HV loss).

---

## 4. Proposal C — orthogonalise against f4

Keep three genes but rotate in (eps, ms) plane using the empirical
gradient of f4 from a pilot DOE:
  u_parallel = unit vector along (df4/deps, df4/dms)
  u_perp     = orthogonal unit in the (eps, ms) plane
  alpha = projection of (eps, ms) on u_parallel   # wear-aligned
  beta  = projection on u_perp                    # wear-neutral
  wr    unchanged

Then J between beta and wear-sensitive objectives should shrink if the
DOE gradient is accurate.

CLAIM R3: Proposal C is conditional on a measured (df4/deps, df4/dms).
Without that vector it is not implementable. Falsify by supplying the
vector from simulation and showing ||J_emp(beta, wr)|| not smaller than
||J_emp(eps, wr)|| and ||J_emp(ms, wr)||.

---

## 5. Recommendation

Ship Proposal A as the default reparameterisation candidate for SIMULATOR.
Use Proposal B only if gene-budget must drop to 5.
Defer Proposal C until DOE gradients exist.

Do not edit MATH-SKELETON gene list until SIMULATOR reports a pilot
comparison. MATHEMATICIAN proposes; does not silently change canon.

---

## 6. Claims locked

CLAIM R1: Proposal A breaks verbatim 3-cycle narrative on (eps,ms,wr).
CLAIM R2: Proposal B eliminates control 3-triangle by deleting a gene.
CLAIM R3: Proposal C needs empirical f4 gradients.
CLAIM R4: None of A/B/C confirms RSB or claims a new physical discovery.
