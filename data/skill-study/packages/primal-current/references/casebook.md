# Mechanisms Behind Success and No-Improvement Controls

All repository links are pinned to `b329d3812c5acf51733e0e9f7baabdda7b1008d2` and were accessed on 2026-09-14. The explanations of why a mechanism may be reusable are mechanism analyses; they are not evidence of the original GPT's decision rationale or of a causal speedup. Reported times are historical records, not timings from the current reproduction.

## Align the Statistics First

- The overall set contains 112 instances from the frozen 2026-09-04 open set. The separate `rmine14` directory is a historical calibration and is excluded from the denominator.
- The September 8 validation bundle contains 22 supplied vectors: 18 numerical improvements, including `sing17`, plus 4 first finite solutions. It validates feasibility and objective values, not novelty or global optimality.
- The latest project primal table contains **23 entries**: adding `dws012-02` changes the count to **19+4**. The earlier "22/22" result cannot be extrapolated into a uniform revalidation of all 23 current entries.
- The approximately `2.47e-11` relative change for `sing17` is numerical polishing. Three external or externally derived `fastxgemm` vectors also improve old public records, but the repository explicitly excludes them from the project's primal contribution count.
- The remaining 86 instances are "not listed in the project's primal table." They include proofs of optimality for known solutions, exact repairs, local results, and unresolved feasibility cases, so they cannot be treated directly as failed trials of a primal algorithm.
- The three `nj` formulations share one underlying partition. Each FHNW Pair A/B pair shares underlying scheduling data. Counts by formulation are not independent sample sizes.

Sources: [latest README results table](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/README.md) and [earlier 22-entry validation report](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/comparisons/miplib-v36-primal-copt-validation-20260908/README.md).

## Mechanisms for All 23 Instances in the Project Table

| Instance | Result | Action That Produced the Improvement | Lesson for GPT / Attribution Boundary |
|---|---|---|---|
| allcolor58 | 258→42 | Started from the public `allcolor10` construction, ran an exact residual configuration search, and released capacity types | Fixed capacities stalled after covering 55/58 stores; allowing capacity changes completed the construction. This was an external seed plus a project construction, so the result cannot be attributed solely to the parity lower bound |
| circ10-3 | 256→242 | Recovered the CIRC10 scheduling encoding, then constructed and validated a 242 witness | Use the original problem literature, constructions, and mappings; there is no need to start from an anonymous MPS alone |
| bley_xs1noM | 3873690.77→3855895.86 | Transferred a sibling solution through identity columns and checked the target model's additional integer upper bounds | Look for strong available solutions in the same data family first; the transfer is not a new native combinatorial construction |
| dws012-02 | 119893.31070966377→119443.31072434435 | Compared 264 design positions, swapped only one selected position with one unselected position, and completed the target model's recourse | Both solutions select 19 positions and overlap on 18; all remaining operating decisions must still satisfy the original rows. The 395 small DEC blocks cannot be solved independently |
| cvrpb-n45k5vrpi | 775→751 | Recovered the B-n45-k5 routes and the original indicator gadget, then lifted the result | An external domain benchmark can provide a strong seed; the vehicle-count optimality argument remains separate from the primal construction |
| cvrpa-n64k9vrpi | 1617→1401 | Recovered the A-n64-k9 data, constructed routes, and filled the complete original-space vector | As above; the original model permits a free fleet, so a fixed nine-vehicle requirement cannot be inferred from the filename alone |
| fhnw-binschedule0 | 16088→15958 | Reduced 319319 variables to a 507-item interval-order core, then constructed loads after matching/path cover | The interval core changes the search object; a lower-bound certificate does not itself produce a complete solution |
| fhnw-binschedule1 | 55198→55158 | Reduced approximately 1.14 million variables to 773 items, then constructed a witness with colored matching | Internal machine loads must be checked in addition to endpoint loads |
| fhnw-schedule-paira200 | -19.2298568218154→-19.369961204645204 | Combined job selection, valid conflict/energy strengthening, and scheduling in the original model | 30 jobs are selected; Pair A and Pair B are different encodings of the same dataset |
| fhnw-schedule-pairb200 | -19.24094384259708→-19.3699612046452058100 | Performed the corresponding selection and reconstruction, then validated every original Pair B row | The solution is shared with A200 and is not a second independent algorithmic success |
| fhnw-schedule-paira400 | -35.54680465280395→-36.27696674236886 | Used a safe 400-binary suffix master and reconstructed a feasible schedule | 60 jobs are selected; the master relaxation requires an independent lift |
| fhnw-schedule-pairb400 | -35.4584→-36.27696674236886 | Independently reconstructed and cross-checked the counterpart of the A400 solution | An early deadline misinterpretation produced invalid cuts; the valid primal may be retained, but the incorrect proof must be withdrawn |
| liu | 1083.984782 headline→1082 | Moved from the official strict 1084 layout to a sequence-pair hint and then to CP-SAT | Even dimensions plus the system of difference constraints show that an optimum can be chosen with even dimensions, allowing a direct search for 1082; `460.253 s` is the runtime of a specific stage |
| neos-3594536-henty | 401223→401092 | Reduced by component balance/parity and recovered free flows through a spanning forest | The reduced model closed in `188.34 s`; this is not the end-to-end time of the full research effort |
| rmine15 | -5018.819990999996→-5018.823005000000004879 | Rearranged periods `[7,9]`, jointly changing 34 mining blocks and 35 bits | This is a small but real discrete improvement; a small magnitude does not imply a numerical artifact |
| neos-5266653-tugela | 65505.2005752763→65257.573990387 | Jointly changed vehicle blocks 3, 11, and 12 and repaired the continuous potential differences | Vehicle columns are interleaved; blocks cannot be selected by slicing contiguous columns |
| supportcase39 | -1085080.906934894→-1085083.856820570460 | Used an 11×11 Gaussian-boundary window to adjust 30 control variables jointly | Single-point, two-point, and 5/7/9 windows all failed to improve; the larger semantic window succeeded |
| nj1 | unknown→382.0606208032 | Used population-balanced connected partitioning, recombination, and kick plus descent | Shares a 595-label partition with `nj2` and `nj3`; first construct a complete feasible solution, then improve it |
| nj2 | unknown→382.0606208032 | Reconstructed root and flow variables from the same partition | This is not a second independent discovery |
| nj3 | unknown→382.0606208032 | Transferred a label-repair construction and later improved the same-source partition | `current` temporarily worsened from `383.6229` to `389.6399` before descending to `382.0606`; a bad kick never overwrote `best` |
| ns1905797 | unknown→13.98258 | Rebalanced a four-block assignment, constructed CP routes, created a complete start, and then applied COPT improvement | The trajectory was `15.03429` → `14.62129` in a 5-second stage → `13.98258` in a 120-second stage; a 900-second continuation found no further improvement |
| nag | 945→930 | Ran a bounded generic COPT solve | The value 930 came from the 2700-second run; do not invent a structural-method explanation for every success |
| sing17 | 36161699.37883251→36161699.3779386893546367410 | Fixed the same integer pattern and reoptimized the continuous variables | Numerical polishing; do not label it as a new discrete pattern |

Per-instance sources and original objective fields are stored in [instances.json](instances.json). The comparison baseline in the table is frozen at v36 and must not be presented as a live leaderboard.

## Primary Evidence Entry Points

- [allcolor58 construction record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/allcolor58/reports/objective-42-certificate.md): the fixed-capacity run covered 55 stores in 53 seconds, and the flexible run covered 58 stores in approximately 40 seconds. These timings come from log-file intervals and exclude earlier research.
- [complete dws012-02 report](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/dws012-02/reports/final_report.md): first rejected a false decomposition, then used a sibling design transplant; the complete research effort took 72 minutes 42 seconds.
- [ns1905797 construction and warm start](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/ns1905797/README.md): progressed from an imbalanced block assignment to a complete feasible point; a candidate that mixed block solutions and violated `R0054` was rejected.
- [rmine15 three-period window](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/rmine15/README.md), [supportcase39 boundary window](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/supportcase39/README.md), and [tugela joint-vehicle source](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/neos-5266653-tugela/experiments/copt_interleaved_block_lns.py).
- [liu representations and lattice structure](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/liu/README.md) and [henty quotient/lift](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/neos-3594536-henty/README.md).
- [latest nj3 local scopes and transfer record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/nj3/README.md): 21 pairs, 39 anchored triples, and 67 anchored quadruples have already been closed locally; the next search must not repeat those fixed scopes.
- [nag run sequence](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/instances/nag/final_report.md) and [FHNW family log analysis](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/fhnw-schedule-pair-results-and-log-analysis-2026-09-08.zh.md).

## Boundaries Learned from Cases Without Improvement

| Situation | Instance Evidence | Skill Action |
|---|---|---|
| Small exchanges have already been explored adequately | `t1722` connected moves of size at most 5; `comp12` bit moves of size at most 10; `sorrell` needs at least 13 removals and 14 additions | Read the recorded scope; change or enlarge the real move and avoid repeating a covered radius |
| One block can be optimized while the global model remains stuck | `sing5/11/17`, `cmflsp`, `bab3` | Optimize jointly across blocks coupled by shared resources; closing one local block does not establish global separability |
| Decomposition labels are misleading | All 395 small `dws012-02` blocks contain only linking variables | Check private variables and coupling rows before using a decomposition; do not begin independent subproblems from the DEC labels alone |
| Audit rejects a nominal improvement | `bley`, `gmut-76-50`, `polygonpack`, `minutedispatchstrategy` | Normalize integer variables, optimize recourse, and recompute on the original model before deciding whether the result improved |
| A relaxed or partial solution looks strong | `supportcase30` reaches 987/1024; `datt256` reaches 470/480 | Preserve the near-feasible point and continue repair; do not report it as a primal bound |
| A stronger lower bound does not produce a new solution | `graph40`, `scpl/scpk/scpj`, `genus`, `mining` | In a primal task, use the bound only as a target signal and do not expand into a long proof campaign by default |
| The known solution is already optimal or the model is infeasible | `graph40` matches the existing solution; `fhnw-binpack/pythago` is infeasible | After verification, stop unproductive primal search; the structure may still be reusable, but it does not count as a new primal result |
| Interface work or analysis consumes the search budget | Early `allcolor` work spent substantial time repairing extractors and producing huge outputs | Retain negative-result memory, create a compact structure card, and begin actual construction promptly instead of accumulating analysis logs |

The existing [milp-structure-research](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/skills/milp-structure-research/SKILL.md) skill covers a wider range of structural, dual, and proof research. This skill reuses its evidence discipline and adds routing centered on time to a verified primal, construction seeds, warm starts, adaptive neighborhoods, stopping conditions, and negative-result memory.
