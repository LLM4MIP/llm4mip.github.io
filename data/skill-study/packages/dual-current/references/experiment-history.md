# Controlled experiment history

Read this reference only when reproducing, comparing, or extending the controlled MIPLIB experiments below. It records historical evidence; it does not override a user's solver choice or the current COPT-first policy.

## 20-instance Dual Skill campaign

- Experiment ID: `miplib20_dual_skill_20260917T0231CST`
- Scope: 20 fixed minimization instances, 150 wall minutes per instance, five ordered batches of four, at most four concurrent instances, 30/60/90/120/150-minute no-backfill checkpoints.
- Historical backend: Gurobi 13.0.2, 8 threads per instance. The skill was frozen before target work; its `SKILL.md` SHA-256 was `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535`.
- Workflow: 300-second reproducible baseline, structural diagnosis, exact/equivalent projections or valid relaxations, globally valid cuts, decomposition and cutoff exclusion, continuous checkpointing, separate numerical and solver-independent certified series, per-route mapping validation, batch barriers, and final artifact audits.
- Outcome: all 20 instances achieved a strict numerical dual improvement over their reproducible baseline; 9 improved the certified-value series; 109 numerical and 51 certified improvements were accepted. `ns1456591` and `neos-3682128-sandon` were closed exactly.
- Canonical source: `summary.csv` SHA-256 `6a10c08ae5287a4f5758d095c0bb2cbd23b4b5d637aedd7cef01457e42612848`; `report.md` SHA-256 `28025a5f3fbb7680274024eb003a8e926846dfb574bd34c447634f8ca2f49bdc`; final audit passed 20/20 and 5/5 batches.
- Warning: the source directory's top-level `report_zh.md` belongs to an earlier controlled/general experiment and is not a canonical result of this campaign.

## COPT terminal-backend replay

- Experiment ID: `miplib20_dual_skill_copt_replay_20260920T0212CST`
- Scope: the 18 non-closed instances only. Each accepted final terminal model from the Gurobi-driven campaign was frozen byte-for-byte; the terminal backend changed to COPT 8.0.4. Per-instance terminal time limit, 8 threads, batch order, mapping, and postprocessing were retained.
- Outcome relative to the source Gurobi strongest bound: COPT/replacement stronger on 2 instances (`graphdraw-grafo2`, `zeil`), equal on 3 (`polygonpack4-10`, `scpm1`, `supportcase22`), and weaker on 13. Twelve retained solver-independent fallbacks were checked; none displaced the COPT terminal value.
- Evidence: all 18 results and five strict batch barriers passed the final end-to-end audit. Canonical `summary.csv` SHA-256 is `6584fb0c16fbad95fc155fe0a0dedad77da1befebf226c6bd8452050527ae0bb`; `comparison.csv` SHA-256 is `74e0ee996f01e9dc1e7bc12400e326e2655b6ed2dec19deaaf7bea4191f96da5`.
- Interpretation: this is a backend replay of routes selected during Gurobi-driven research. It is not a blind solver benchmark. The source used Xeon 8358 / Ubuntu 20.04.6, while the replay used Xeon 8469C / Ubuntu 22.04.3; solver-specific settings were recorded as direct, approximate, unavailable, or model transformations.

## Handoff locations

- AI-facing dossier on altman: `/data/operationgpt/huangyicheng_temp/dual_skill_handoff_20260920T1957CST`
- Full COPT replay on altman: `/data/operationgpt/huangyicheng_temp/miplib20_dual_skill_copt_replay_20260920T0212CST`
- Original full Dual Skill evidence, local snapshot: `D:/sufe/AI4MIP/miplib20_dual_skill_20260917T0231CST`
- Original execution tree recorded by the campaign: `/data1/wyc/miplib20_dual_skill_20260917T0231CST` on `euler4`.

For later general-skill or primal-skill comparisons, join on instance name **and original MPS SHA-256**. Compare minimization dual bounds by larger-is-stronger and primal bounds by smaller-is-better. Keep numerical global bounds, independently certified bounds, and verified primal values in separate fields; compute a joint gap only when both endpoints are valid for the same original model.
