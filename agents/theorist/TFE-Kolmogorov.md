# Is TFE a Computable Lower Bound on Kolmogorov Complexity?

THEORIST wake argument. Grounded in `AI-CONTEXT.md`, `MATH-SKELETON.md` Sections 1.1-1.4, Axiom A1 (`research/boundary-axioms.md`), and the discrete panel log in `grasshopper/step-04-TFE.md`. No simulation has been run; nothing below is an empirical discovery. Critic has not yet produced `unsupported-claims.md`; this note stays inside existing definitions plus standard algorithmic-information facts.

**Short answer.** [CONFIRMED] As defined, Temporal Facade Entropy (TFE) is a computable product of two empirical Shannon entropies. It is not a lower bound on the Kolmogorov complexity `K` of a facade panel-state time series. The mismatch is independent in three places: units, functional form, and the gap between histogram entropy and program length of one finite string.

---

## 1. Objects under comparison [CONFIRMED]

Let the recorded envelope be a finite array `X` of size `N_panels x T_steps`. Grasshopper Step 04 treats a typical log as 80 panels by 8760 hours, then bins each continuous angle into five states. Write `X(i,t)` for the discrete state of panel `i` at time `t`. This array is the "facade panel-state time series."

Prefix Kolmogorov complexity `K(X)` is the length, in bits, of a shortest self-delimiting program that prints `X` and halts. `K` is a property of one concrete string (the flattened log), not of a distribution.

MATH-SKELETON 1.2-1.4 defines TFE from two empirical histograms, not from `K`:

```
H_space(t) = - sum_s p_s(t) * log2(p_s(t))
H_time(i)  = - sum_s q_s(i) * log2(q_s(i))
TFE(i,t)   = H_space(t) * H_time(i)
TFE_total  = (1/N) sum_i (1/T) sum_t TFE(i,t)
```

Here `p_s(t)` is the fraction of panels in state `s` at time `t`, and `q_s(i)` is the fraction of time panel `i` spends in state `s`. The stated range is `[0, log2(N_states) * log2(T_states)]`. The scalar summary factorises:

```
TFE_total = <H_space>_t * <H_time>_i
```

That identity follows from the written sums; it is not an extra assumption. TFE therefore records how mixed the spatial histogram is, times how mixed a panel's temporal histogram is. It does not score the shortest program for `X`.

---

## 2. What is actually known about `K` and Shannon entropy [CONFIRMED]

Three textbook facts fix the comparison. They are not project measurements.

First, `K` is uncomputable: no algorithm, given every finite string, returns `K` of that string. Any total computable statistic of `X` — including TFE — therefore cannot equal `K(X)` on all logs.

Second, a computable compressor yields an *upper* bound: if a program of length `L` prints `X`, then `K(X) <= L`. Histogram entropy does not automatically yield a matching *lower* bound on that same `X`. A string that uses two symbols equally can be periodic (`000...111`) with `K ~ log(T)`, or incompressible with `K ~ T`. The empirical binary entropy is 1 bit in both cases.

Third, the Shannon-Kolmogorov link is an *expectation* statement about a computable source `P`:

```
H(P)  <=  sum_x P(x) K(x)  <=  H(P) + K(P) + O(1)
```

So `H(P)` lower-bounds the *average* program length of draws from `P`, once `P` itself is fixed and computable. It does not lower-bound `K` of one observed facade log, and it does not license replacing `H(P)` by a product of two marginal empirical entropies.

---

## 3. Three reasons TFE is not a lower bound on `K(X)` [CONFIRMED]

### 3.1 Units

`K(X)` is a bit length. Each of `H_space(t)` and `H_time(i)` is a Shannon entropy in bits. Their product is in `bits^2`. MATH-SKELETON states the range as a product of two logarithms, which is the same dimension. A number in `bits^2` cannot sit below a number in bits unless the project adds a conversion (a reference scale, a logarithm, or an extensive factor such as `T` or `N_panels`). No such conversion is defined. Without it, "`TFE <= K(X)`" is not even a typed inequality.

### 3.2 Product of marginals is not joint entropy

The quantity that would enter a typical-set argument for the whole log is a joint / process entropy of `X`, not `H_space * H_time`. The two factors discard order and discard space-time dependence: they are histograms. A travelling wave, a global lockstep cycle, and a spatially white but temporally i.i.d. field can be tuned to similar histogram pairs and therefore similar TFE, while their program lengths differ by large additive amounts (a short generator versus an incompressible table).

The extensive surrogates `T * H_time(i)` and `N_panels * H_space(t)` are still not `K(X)`: they estimate path or snapshot complexity only under i.i.d. models. TFE multiplies two non-extensive scalars and averages them. That is a diversity index, not a coding-length bound.

### 3.3 The controller makes the i.i.d. source model false

Axiom A1 writes the envelope as a deterministic map `B(t) : X_in(t) -> S(t)`. The formal model adds hysteresis (`epsilon`, `maxStep`) and a finite state machine. Therefore `X` is a deterministic function of the input chronicle `X_in` (climate, occupancy, overrides) and of a short description of `B`:

```
K(X)  <=  K(B) + K(X_in) + O(1)
```

If `B` is a small program — the intended case — then `K(X)` tracks weather and occupancy, not TFE. A lockstep facade can have `H_space ~ 0` and therefore `TFE ~ 0` while `K(X)` is still `K` of one climate-driven path. A high-TFE spore gradient (MATH-SKELETON 5.2) can still come from a short rule plus a slow humidity series, so `K(X)` stays small.

TFE = 0 does imply a spatially and temporally degenerate histogram (static, uniform envelope). That is *consistent* with small `K`, but `0 <= K(X)` is true of every string and is not a TFE-specific bound.

---

## 4. What TFE *is* allowed to claim [CONFIRMED]

Inside the repo, TFE is a performance metric on state *distributions*: TFE = 0 for a static envelope; the design aspiration is TFE_optimised > TFE_rule-based > TFE_static = 0 (`AI-CONTEXT` D01). That ranking does not mention `K`. It is also computable from a finite log: count bins, evaluate the two Shannon sums, multiply, average. Computability of TFE is not in doubt. What fails is the further claim that this computable number is a lower bound on `K(X)`.

A weaker, still definitional, reading is available: large TFE is *incompatible* with the most trivial programs (print one constant state). That is an informal complexity *hint*, not a bound. Compressors (gzip, context weighting, a generator that replays `B` on `X_in`) remain the correct computable *upper* bounds on `K(X)`.

---

## 5. Speculative repairs [SPECULATIVE]

The question can be salvaged only by changing the object or the inequality. None of the following is licensed by `TFE = H_space * H_time`.

**Extensive Shannon as an expected-K estimator.** Replace TFE by `H_hat(X) = T * <H_time>_i` (or a fitted entropy rate) and read `H_hat` as an estimator of `E[K]` under a declared source, not as `K(X)`. This would be falsified if a short replay of `B` on recorded `X_in` beat `H_hat` as a description length while histograms stayed high.

**TFE as a monotone proxy.** Claim only that TFE ranks with compressed length across S0/S1/S2. This would be falsified if, for a fixed compressor and discretisation, the TFE ranking and the compressed-length ranking disagreed.

**A typed inequality.** Invent a conversion such as `C(X) = min( TFE_total / log2(N_states), T * <H_time> )` and claim `C(X) <= K(X)`. This would be falsified if any finite log satisfied `C(X) > K_upper(X)` for a known generating program — the only operational stand-in for `K`.

---

## 6. Verdict

[CONFIRMED] TFE is a computable, histogram-based, `bits^2`-valued diversity functional of the panel-state log. Kolmogorov complexity of that log is an uncomputable bit length. Standard inequalities relate `K` to Shannon entropy only in expectation, for a declared source, and for the entropy of that source — not for a product of two empirical marginals. Deterministic boundary dynamics (`B(t)`) further cap `K(X)` by `K(B) + K(X_in)`, independent of TFE.

[SPECULATIVE] TFE may still *correlate* with compressed length across static, lockstep, and gradient-actuated families, and an extensive rewrite of TFE might become an expected-K estimator under extra independence assumptions. This would be falsified if those families, once logged, produced a TFE ranking that did not match a fixed compressor ranking, or if a short `B`-replay described a high-TFE log far more tightly than any extensive Shannon rewrite.

Until such a test exists, the honest theoretical position is: TFE is not a computable lower bound on `K` of the facade time series; it is a computable stand-in for distributional richness of panel states in space and time.
