# MILP40 Fresh20 Solver Comparison

This report summarizes the 20 MILP instances run on Altman on November 27, 2026. It gives the final relative gap and elapsed wall-clock time for each custom run alongside the corresponding historical COPT runtime.

## Results and mean runtime

| Method | Instances | Proven optimal | Sum of per-instance times (s) | Mean per-instance time (s) |
|---|---:|---:|---:|---:|
| Altman custom algorithms | 20 | 9 | 95559.77 | **4777.99** |
| Historical COPT benchmark | 20 | 20 | 29830.00 | **1491.50** |

All 20 Altman runs produced a feasible solution verified exactly against the original model and a valid global bound. Nine instances were proven optimal, and 11 reached the 7200 s time limit. The mean uses the unrounded elapsed times for all 20 instances.

## Per-instance results

Instances are sorted by final Altman gap in ascending order, with ties ordered by instance ID. The gap is `abs(P − D) / max(1, abs(P), abs(D))`, where `P` is the verified feasible objective and `D` is the verified global bound.

| ID | Instance | Final Altman gap | Altman time (s) | Historical COPT time (s) | Altman status |
|---:|---|---:|---:|---:|---|
| 14 | `supportcase26` | 0% | 150.7 | 2063 | Proven optimal |
| 17 | `glass4` | 0% | 1165.0 | 76 | Proven optimal |
| 18 | `proteindesign121hz512p9` | 0% | 614.6 | 1922 | Proven optimal |
| 19 | `ns1760995` | 0% | 725.5 | 713 | Proven optimal |
| 20 | `neos-5093327-huahum` | 0% | 2950.2 | 722 | Proven optimal |
| 24 | `roi5alpha10n8` | 0% | 4792.0 | 1010 | Proven optimal |
| 25 | `rocII-5-11` | 0% | 2540.2 | 1197 | Proven optimal |
| 29 | `nursesched-medium-hint03` | 0% | 2732.5 | 3757 | Proven optimal |
| 32 | `neos-1171737` | 0% | 689.0 | 81 | Proven optimal |
| 5 | `gmu-35-50` | 0.059328% | 7200 | 1467 | Time limit |
| 28 | `tr12-30` | 0.099541% | 7200 | 125 | Time limit |
| 40 | `ic97_potential` | 0.177530% | 7200 | 1655 | Time limit |
| 16 | `sing326` | 0.495111% | 7200 | 922 | Time limit |
| 30 | `snp-02-004-104` | 0.747143% | 7200 | 5802 | Time limit |
| 35 | `reblock115` | 0.814756% | 7200 | 699 | Time limit |
| 26 | `neos-873061` | 1.589212% | 7200 | 997 | Time limit |
| 1 | `ran14x18-disj-8` | 9.009808% | 7200 | 109 | Time limit |
| 39 | `physiciansched3-3` | 10.386246% | 7200 | 3886 | Time limit |
| 22 | `uct-subprob` | 21.656051% | 7200 | 130 | Time limit |
| 21 | `comp21-2idx` | 51.764706% | 7200 | 2497 | Time limit |

## Timing and verification

- **Altman** ran custom algorithms. Per-instance wall-clock time includes model analysis, code development, search, and validation. The four batches ran in sequence, with five instances running concurrently in each batch. Wall-clock time from the first batch start to the last batch finish was 28804.58 s, including transitions and cleanup.
- **COPT** runtimes come from the Hans 12-thread benchmark records archived on October 7, 2026. The benchmark used COPT 8.0.3, different hardware, and a different model preprocessing workflow. The SHA-256 hashes of all 20 anonymous input files matched the corresponding files in the archived record. [Hans COPT benchmark results](https://plato.asu.edu/ftp/milp_res12/modified.copt.12threads.7200s.res)
- **Verification** checked the original constraints, variable bounds, and integrality for each reported solution, recomputed its objective, and replayed the global bound certificate. A numerical candidate with a lower objective for instance 1 failed the exact original-model check. Its reported gap uses the best verified feasible objective.

## Evidence files

The Altman experiment directory is `/home/huangyicheng/milp40_fresh20_20261127_v2/`.

- `verified_summary.csv` and `verified_summary.json` contain the unrounded elapsed times, exact objectives, and evidence paths.
- `audit-final.log` records the final replay results. `schedule_validation.json` records batch timing, input checks, and search process cleanup.
