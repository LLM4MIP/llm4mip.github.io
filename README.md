# LLM4MIP — How Much Can LLMs Help Solve MIPs?

## Research website

**[Open the LLM4MIP research website →](https://llm4mip.github.io/)**

Research website for the `MIPLIB_openproblem` project. An LLM-assisted benchmark evaluated 112 open MIP problems and certified optimality or infeasibility for 30 instances (28 optimal and two infeasible), produced 21 primal-bound improvements relative to MIPLIB v36 plus four first finite primal bounds, and produced 41 dual-bound improvements relative to a frozen historical COPT table.

Two of the 21 incumbent improvements use an attributed external `fastxgemm` construction; the project contribution there is truncation, mapping, and strict verification rather than authorship of the parent construction.

The site is organized around one question: how much can language models help solve difficult mixed-integer programs? It separates the LLM's role in structural analysis, reduction design, falsification, checker construction, and workflow coordination from the role of solvers and deterministic proof systems. The reported result counts overlap and are descriptive, not a causal success-rate estimate.

The closest 20-instance comparison is deliberately reported as a mixed result: the structure-focused workflow more often produced the better primal bound and certified global optimality for two instances, while the comparison workflow more often produced the stronger numerical dual bound. Exact solvers, exhaustive computations, SAT/LRAT checking, and audits against the original MPS determine which results are classified as verified.

## Site structure

- `index.html` — brief interactive benchmark overview
- `instances/` — searchable 112-instance catalogue; every instance has a generated `summary.md` and a downloadable results bundle
- `skill/` — downloadable `milp-structure-research` skill and the 20-instance skill-effect study
- `solver-replacement/` — analysis based on benchmark results of whether LLMs can fully replace optimization solvers
- `technical-report.pdf` — verification-classified technical report
- `technical-report.tex` — editable LaTeX source
- `downloads/` — skill, experiment, and reconciliation-audit packages

The instance bundles retain research reports, scripts, artifacts, solutions,
derived proof models, logs, runs, and proof traces present in each instance
directory. They omit only official raw
`input/*.mps*` benchmark models, whose sizes and SHA-256 hashes are recorded in
each package manifest. The historical `rmine14` calibration is excluded from
the 112-instance catalogue.

## Rebuild generated data

From this repository, with the sibling `MIPLIB_openproblem` checkout present:

```sh
python3 scripts/build_site_data.py
```

This regenerates the catalogue JSON/JavaScript, all 112 summaries and
deterministic archives, the skill download, the comparison data, and the two
18 September reconciliation audits bundled for publication. The source snapshot is commit
`89a8abd` plus the explicitly disclosed working-tree reconciliation. A fresh
checkout of `89a8abd` alone is not sufficient to reproduce the current output;
the reconciled sibling working tree (or a later source commit containing those
reviews) is required.

## Publish with GitHub Pages

Published text and downloadable research archives are provided in English.
See [English translation provenance](docs/english-localization.md) and
[`data/english-localization-manifest.json`](data/english-localization-manifest.json)
for original and translated file hashes. Translated frozen skills are not
byte-identical to the original experimental versions. After rebuilding data or
archives, run `python scripts/check_english_content.py` before publishing;
upstream research snapshots may contain Chinese text.

GitHub Pages is configured from the `main` branch root. The public site is available at [llm4mip.github.io](https://llm4mip.github.io/).

Suggested repository topics: `llm`, `mixed-integer-programming`, `mip`, `miplib`, `optimization`, `operations-research`, `ai-for-optimization`.

## Local update based on latest website

Website baseline: GitHub main `b48994ab3cb51808a4d94a3d8c1b46caadd9bc6f` (PR #7). Original page titles, narrative and design are retained. Campaign data expands to 132 cases: 32 optimal (including two tolerance closures), 2 infeasible, 29 primal updates, and 66 dual improvements. The upstream outcome grouping is retained: 32 certified conclusions, 94 feasible/open, 2 numerically optimal and 4 without a feasible solution.

The skill table opens with combined gap versus no-skill AI. Its solver comparison selects minimum valid primal and maximum valid dual across recorded Gurobi and COPT runs, without a solver selector: 16 wins (including one feasibility win), 1 tie, 3 losses; mean reduction 18.9091 percentage points over 19 finite gap pairs. It is a post-hoc best-bound comparison, not a single solver run. The unchanged narrative below describes the original archived workflow; the table identifies the dedicated primal/dual runs separately.

Run `python scripts/build_site_data.py` to regenerate campaign and dedicated-skill data from checked-in snapshots. `data/upstream-source.json` records the latest website's changed-file blob hashes; `data/upstream-catalogue-b48994a.json` supplies original metadata and archive hashes. Research data and frozen skills retain their separate source commit in `data/skill-study/source-manifest.json`. All original upstream summaries and research archives are retained.
