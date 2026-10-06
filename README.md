# LLM4MIP — How Much Can LLMs Help Solve MIPs?

[Open the research website](https://llm4mip.github.io/).

The complete study covers 217 open MIPLIB instances and reports 52 resolved
instances: 49 optimal, 2 infeasible and 1 unbounded. It records 59 primal-bound
improvements against MIPLIB v36 and 136 dual-bound improvements against the
historical COPT 10-hour baseline. Result snapshot: 6 October 2026.

These categories overlap. Per-instance summaries retain the numerical,
tolerance and source-model qualifications associated with each conclusion.
The results are descriptive comparisons against fixed baselines; they are not
an equal-budget causal comparison or a live MIPLIB leaderboard.

## Website and data

- `index.html`: overview and interactive result charts.
- `instances/`: searchable complete catalogue and current per-instance result bundles.
- `data/campaign-catalogue.json`: 217 current results and comparison decisions.
- `data/campaign-metrics.json`: current headline totals.
- `data/result-provenance.json`: source hashes and baseline definitions.
- `downloads/results-217.json`, `.csv`, `.tar.gz`: complete downloadable results.
- `skill/`: the separately frozen 20-instance skill comparison.
- `solver-replacement/`: workflow discussion and comparison evidence.

Per-instance bundles contain the current summary, result JSON and license.
They link to source research records, which may require repository access;
full experiment logs and proof archives are not embedded in these compact bundles.

## Rebuild and validate

No solver or network access is required to rebuild from the checked-in inputs:

```sh
python scripts/build_site_data.py
python scripts/validate_results.py
python scripts/check_english_content.py
```

The 20-instance experiment has its own source manifest and acceptance criteria.
Updating the full-study catalogue does not change that experiment's results.

GitHub Pages publishes the `main` branch root at https://llm4mip.github.io/.
