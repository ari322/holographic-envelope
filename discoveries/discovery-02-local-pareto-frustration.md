# Discovery 02 — Local Pareto Topology as Architectural Frustration

## Status: Computationally supported analogy — upgradeable to L1 with Wallacei run
## Evidence level: L0 → L1 pending

---

## The gap in current knowledge

Multi-objective facade optimisation studies (e.g. NSGA-II for energy + daylight + cost) treat the Pareto front as a smooth continuous curve. Designers are advised to pick a point on the curve.

A 2025 arXiv paper (arXiv 2606.16792) on Pareto fronts in multi-objective topology optimisation makes a novel finding: Pareto fronts in topology optimisation are NOT smooth. They consist of disconnected local segments, each corresponding to a qualitatively different design topology. The front is nonconvex and piecewise discontinuous.

The paper states explicitly: "the optimal design changes abruptly along the frontier" and "local optima in single-objective topology optimisation are part of local Pareto frontiers in multi-objective topology optimisation."

---

## The original contribution

This project is the first (to the knowledge of this research) to connect this Pareto topology finding to:
1. Spin-glass frustration in condensed matter physics
2. Adaptive architectural facade optimisation specifically

### The structural equivalence

In a spin-glass system:
- The energy landscape has many local minima separated by barriers
- The system cannot reach the global minimum because competing interactions create frustration
- Different realisations of the system (with same global parameters) land in different local minima

In a multi-objective facade Pareto front with topology discontinuities:
- The performance landscape has many local Pareto segments separated by gaps
- No design can simultaneously optimise all four objectives
- Different starting populations in Wallacei converge to different Pareto segments
- The segments correspond to qualitatively different facade typologies (e.g. deep reveal vs flat aperture vs rotation-dominant)

### The falsifiable prediction

If the facade optimisation in Step 8 produces a Pareto front with:
- At least two disconnected or clearly separated clusters
- Each cluster dominated by a different primary gene (e.g. panel_depth vs aperture_ratio)
- Cluster membership stable across multiple Wallacei runs with different random seeds

Then the spin-glass frustration analogy is computationally supported at L1.

If the front is smooth and unimodal across all runs, the analogy is disconfirmed.

---

## Why this matters for architecture

If the prediction is confirmed, the practical implication is profound:
**there is no single optimal facade design — there are families of near-equivalent solutions with no continuous path between them.**

This means:
- Designers who stop optimisation early will land in one attractor basin, possibly missing a qualitatively different and equally valid solution family
- Parametric design tools that assume smooth Pareto fronts may systematically miss disconnected regions
- The design process should explicitly explore multiple attractor basins, not converge on one

This is directly actionable design knowledge, not just a physics metaphor.

---

## Connection to existing literature

- Novel insights into Pareto fronts in multiobjective topology optimisation (arXiv 2606.16792, 2025): establishes mathematical basis for disconnected local Pareto frontiers in topology optimisation.
- From a Pareto Front to Pareto Regions (Semantic Scholar, Rebello & Martins): extends Pareto concept to regions rather than fronts.
- Spin-glass optimisation (PhD thesis, TDX 0803/692475): formal connection between spin-glass models and combinatorial optimisation.

No paper connects all three: spin-glass physics + discontinuous Pareto topology + adaptive architectural facade design.
