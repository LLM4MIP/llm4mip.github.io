# Source and reproduction notes

Comparison date: 2026-09-13.

## Published input snapshots

- `sources/no-skill-report.md`: Markdown source of the user-designated run without `milp-structure-research`.
- `sources/skill-report.zh.md`: consolidated report of the user-designated skill run.
- `sources/skill-summary.csv`: 20-row machine-readable summary of the skill run.
- Historical skill: [frozen entrypoint](../../experiment-handoff-20260920/evidence/historical-SKILL.md); SHA-256 `f8a09b104f0af3786b2e702f60dde3de7fd54a1aac581dff9bdd8a3325c84b4f`. The live skill was changed to COPT-first on 2026-09-20; retrieve the full historical skill directory from commit `a5919b51192b4f4493e77ae0fefb71f085e0820d` when reproducing the old workflow.

The published text snapshots use repository-normalized line endings, so their byte hashes differ from the original Windows working copies. `audit.json` records both the original-input hashes and the published-snapshot hashes.

## Source PDF

The no-skill report was also supplied as `miplib20_vs_copt_report.pdf`:

- bytes: `189424`
- SHA-256: `c8dfe7590ce5723a81bbca1a5aa2ebf9912c033b86a1ad83f8cef5331522d0b9`
- metadata title: `MIPLIB 20-instance primal/dual comparison with the COPT table`
- pages: `21`, A4 landscape
- producer: ReportLab
- creation timestamp in metadata: `2026-09-13 20:04:08`

All 21 pages were rendered and visually inspected. The tables, conclusions, and appendix agree with the Markdown source; no clipped table or obvious missing layout content was found. The PDF is not duplicated in this repository because the Markdown snapshot contains the same report content.

## Recompute

Run from the repository root:

```powershell
python .\docs\comparisons\milp-structure-skill-effect-20260913\compare_skill_effect.py `
  --no-skill-report .\docs\comparisons\milp-structure-skill-effect-20260913\sources\no-skill-report.md `
  --skill-summary .\docs\comparisons\milp-structure-skill-effect-20260913\sources\skill-summary.csv `
  --skill-report .\docs\comparisons\milp-structure-skill-effect-20260913\sources\skill-report.zh.md `
  --skill-file .\docs\experiment-handoff-20260920\evidence\historical-SKILL.md `
  --csv-out .\docs\comparisons\milp-structure-skill-effect-20260913\comparison.generated.csv `
  --audit-out .\docs\comparisons\milp-structure-skill-effect-20260913\audit.generated.json
```

The generated CSV must have SHA-256 `18f14dc58129789881d26c44b01c5514cb6007d8c52a74c01a07d7fc58a746f2` and 20 data rows.

## Scope

This is a historical, non-randomized paired comparison. It is suitable for auditing observed outputs and workflow compliance, but not for estimating a causal effect of the skill independently of compute budget, machine, solver state, random seeds, baselines, or research decisions.
