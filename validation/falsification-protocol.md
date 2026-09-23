# Falsification Protocol

> Every claim in this project must be falsifiable.
> This file lists each claim and its falsification condition.

---

## D01 — Temporal Facade Entropy (TFE)

**Claim:** TFE_optimised > TFE_rule-based > TFE_static = 0

**Falsification condition:**
  If TFE_rule-based >= TFE_optimised in Wallacei simulation,
  then TFE is not a useful discriminator for adaptive facade optimisation.
  The metric must be redesigned (different discretisation, different time window).

**Experiment:** Run three facade configurations in Grasshopper simulation:
  A: All panels fixed at 45° (static)
  B: All panels follow rule: open if radiation > threshold, close otherwise (rule-based)
  C: Wallacei-optimised gene vector (adaptive)
  Compute TFE for each. Check ordering.

---

## D02 — Pareto Frustration / RSB

**Claim:** Wallacei with different random seeds converges to K ≥ 2 distinct design families.

**Falsification condition:**
  If Hartigan dip test p > 0.05 on pairwise gene distances,
  then P_arch(d) is unimodal and no RSB-equivalent structure exists.
  The analogy to spin-glass frustration is not supported for this problem.

**Experiment:** Run Wallacei 5× with seeds [42, 137, 256, 891, 1024].
  Collect all Pareto solutions. Compute pairwise distances. Apply dip test.
  Fit GMM. Report K, BIC, and cluster centroids.

---

## D03 — Bacterial Spore Layer Encoding

**Claim:** θ_max(i) increases monotonically with n_layers.

**Falsification condition:**
  If θ_max is non-monotone (e.g., reaches a plateau or decreases at high n),
  then the layer-count encoding scheme does not work as a programming language.
  Alternative: encode via spore concentration C rather than layer count n.

**Experiment:** Fabricate 10 cork panels with n = 1, 2, 3, 5, 8, 13, 21 layers.
  Place in humidity chamber at 90% RH. Measure θ after 10 minutes.
  Plot θ vs n. Test for monotonicity.

---

## D04 — Boundary Information Ratio (BIR)

**Claim:** An optimised adaptive facade achieves higher BIR than a static facade.

**Falsification condition:**
  If BIR_static >= BIR_adaptive for any real building dataset,
  then the metric is dominated by interior entropy H_interior
  and facade adaptation does not contribute meaningfully.
  The normalisation of H_interior must be revised.

**Experiment:** Apply BIR computation to one year of sensor data from a building
  with a static facade (baseline) and one with a dynamic shading system.
  Compare BIR time series means.
