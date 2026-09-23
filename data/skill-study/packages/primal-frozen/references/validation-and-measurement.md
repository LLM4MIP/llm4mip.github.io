# Original-Model Acceptance and Measuring "Faster"

## 1. Keep the two acceptance paths distinct

**Construction or repair:** Fix the integer choices, leave continuous recourse or explicitly selected discrete variables free, and reoptimize. The result is a new vector. This procedure does not establish feasibility of the original input vector.

**Checking a submitted vector:** Reload the final serialized `.sol` file, apply the documented convention for omitted variables, fix every variable to its submitted value, and check the untouched original model. In addition to a solver fixed-point check, substitute the vector into every row through an independent code path. The MIPLIB GMP checker can be reused for ordinary MPS models. Models with indicators, SOS constraints, or other extensions require a checker that implements their semantics; never omit unsupported constructs silently.

Record all of the following:

- Model file, solution file, checker version or source, and SHA-256. Keep the compressed-file hash separate from the hash of its decompressed contents.
- Reject NaN/Infinity, duplicate variables, unknown variables, and malformed input. Whether omitted sparse variables default to 0 is determined by the file format;
- Check bounds and every applicable domain, including integer, binary, semi-integer, and SOS domains. Check all original ordinary, ranged, indicator, and other applicable constraints.
- Recompute the objective from the original decimal coefficients and the final vector, including the objective sense and constant.
- Record the largest row, bound, and integrality violations, the tolerances, and the arithmetic used by the checker.
- For each candidate, report both its search status and the independent acceptance status of that exact vector.

Recheck a repaired vector from scratch. Do not round a nearly integral vector and then declare it feasible. For `gmut-76-50`, rounding the lower-objective point still leaves a material flow violation. If a standard checker uses nonzero tolerances, `passed` supports feasibility only at those stated tolerances.

A zero computed with finite-precision `Decimal` arithmetic is not automatically a fully rational proof. If arithmetic may round, report the precision and error treatment. When mathematical zero tolerance is required, use `Fraction`, integer scaling, interval enclosures, or sufficient provable precision. A feasible point for a rational system need not have a terminating decimal representation, so arbitrary truncation of fractions is invalid.

Source: [the repository's 22-candidate validation protocol](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/comparisons/miplib-v36-primal-copt-validation-20260908/README.md). Its GMP checks use `1e-5` for linear rows and the objective and `1e-4` for integrality; COPT uses `1e-9`. Passing either check does not turn the 22 results into mathematical zero-error certificates.

## 2. Objective comparison and strict-improvement thresholds

Let `s=+1` for minimization and `s=-1` for maximization. Define improvement as `s*(z_old-z_new)` and require it to be positive. Define relative improvement as `improvement/max(1,abs(z_old))`; never divide by a negative objective value.

When no finite baseline is known, report `first_feasible` and the time of first feasibility. Do not report an infinite improvement percentage. Ordinary numerical optimization may use a predeclared absolute or relative significance threshold, but keep that threshold separate from validation error. For small differences, recompute both old and new objectives from the same original coefficients. If reporting objective intervals, require the intervals to be strictly separated before claiming improvement.

If it has been proved that the objective, or some optimal representative, lies in `a+g Z`, the next lattice point can define the better-objective target. Do not assume `UB-1` merely because the data look integral. For `liu`, the proof that an optimum can be even is enough to reduce the better-feasibility target to 1080; it does not mean that every nonminimal continuous layout must have an even side length.

Use two independent classification axes:

- **Result type:** `first_feasible`, `discrete_improvement`, `recourse_improvement`, `numerical_polish`, `repair_only`, or `no_improvement`.
- **Provenance:** `project_construction`, `solver_generated`, `transferred`, `external`, `external_derived`, or `reproduction`.

A large recourse gain with the same integer pattern can still be valuable. Do not dismiss every same-pattern improvement as insignificant polishing. The label for `sing17` is supported by its particular magnitude and history, not merely by its unchanged integer pattern.

## 3. Minimum fields for a persistent ledger

Store the following for every experiment: `run_id, seed, backend/version, model/start hashes, method, hypothesis, scope, cutoff, free/fixed variables, anchor, start_s, wall_s, workers, status, candidate, next_action`.

`scope` must reconstruct the actual neighborhood: for example, the center solution SHA, period `[7,9]`, fixed extraction states, and whether the final pit is fixed. Merely writing `radius=3` is insufficient. Record stopped/incomplete/closed status, including completed unsuccessful searches that produced no new candidate.

`candidate.audit` must come from actual checker output, not a model-authored claim of passing. The summary tool only aggregates records and cannot establish feasibility. Its simplified input is:

```json
{"type":"meta","instance":"example","model_sha256":"actual 64-hex-digit model SHA-256","sense":"min","baseline":"100","min_improvement":"0.001"}
```

Follow it with one experiment object per line, for example. Replace every hash placeholder with the actual 64-digit hexadecimal value:

```json
{
  "type":"experiment", "run_id":"window-01", "method":"coupled-window",
  "start_s":"60", "wall_s":"40", "workers":2, "status":"TIME_LIMIT",
  "scope":{"center_sha256":"actual hash", "free_periods":[7,8,9], "outside_fixed":true},
  "candidate":{
    "objective":"98.5", "verified_at_s":"99", "category":"discrete_improvement",
    "solution_sha256":"actual 64-hex-digit solution SHA-256",
    "audit":{
      "passed":true, "all_original_constraints_checked":true,
      "model_sha256":"actual 64-hex-digit model SHA-256", "solution_sha256":"actual 64-hex-digit solution SHA-256",
      "recomputed_objective":"98.5", "grade":"numerical",
      "row_tolerance":"1e-9", "integrality_tolerance":"1e-9",
      "report":"validation/window-01.json"
    }
  }
}
```

Serialize each JSONL object on one line. Omit `candidate` when none exists. `verified_at_s` is the acceptance-completion time measured from the task start; it must fall within the corresponding experiment's start/end interval, and `wall_s` must include validation. Supported grades are `exact_rational`, `decimal_zero`, and `numerical`. The summarizer does not open `audit.report`, validate real file hashes, or check model constraints. Always retain its output alongside the original validation files.

A numerical improvement smaller than the predeclared `min_improvement` remains in the best trajectory; it simply does not trigger the threshold-reaching time for the first baseline improvement. If several small improvements cumulatively reach the threshold, compute their cumulative change from the baseline correctly.

## 4. How to test whether the skill is faster

The repository contains heterogeneous research records with different algorithms, seeds, CPUs, starts, and budgets. Neither 22/112 nor 23/112 establishes a GPT success rate. Dividing 10 hours for one complete workflow by 188 seconds for a different reduced model does not establish a speedup.

Use the following design for a controlled comparison:

1. Hold fixed the untouched original model, accessible initial solution, hardware, thread count, budget, and acceptance standard. When comparing the skill policy itself, also hold the solver and version fixed. If one side falls back from COPT to Gurobi or cuOPT, report the result as a whole-system comparison or isolate fallback as a separate factor; do not attribute the entire difference to the skill. If external search or preprocessing is allowed, allow it on both sides and report its cost separately. Do not leak a stronger target solution to only one side.
2. Compare a cold baseline, a solver baseline with the same start, and the skill policy separately. This distinguishes the value of a stronger seed from faster search after the seed.
3. Make the primary outcome the best-primal trajectory over the same full budget and the final verified best at the budget limit. Also record the times of the first verified feasible solution, first strict improvement, and first predeclared threshold-reaching improvement. First improvement is a metric, not a stopping condition; both sides continue until the common total budget or another valid termination condition.
4. Retain unsuccessful runs as right-censored at the budget limit instead of deleting them from timing averages. Report success counts, full-instance distributions, and time curves, not only the mean over successful cases.
5. Record time spent on input, structural analysis, GPT tokens or API calls, construction, solving, lifting, validation, and human preparation. Operator wall time multiplied by worker count is an allocation estimate rather than observed CPU time. Do not add concurrent wall intervals.
6. Split training or development and test data by underlying instance family. Do not place related `nj` or FHNW A/B formulations across the split. Use multiple seeds to assess stability.
7. Run ablations without sibling transfer, structural neighborhoods, kicks, and persistent negative-result memory. Compare independently verified primal values rather than solver-reported values alone.

This skill's utility tests check only retrieval and accounting behavior. They are not the optimization performance experiment described above.
