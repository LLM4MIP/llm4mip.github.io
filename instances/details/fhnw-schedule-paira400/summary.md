# fhnw-schedule-paira400

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -36.27696674236886 (new strict incumbent)
- **Best bound or certificate:** -36.27696674236886 (safe suffix master)
- **Study result:** Computational optimum; two master runs and Pair-A/Pair-B full-row audits

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -36.276966742368865136
- **Main method:** portable exact branch-and-dual certificate with frozen or rebuilt strengthening, untouched-original-MPS audit, and paired-formulation cross-check where available
- **Verification category:** PE — Portable exact certificate
- **Earlier source-table status:** computational optimality verification; independent zero-gap reread and full-row audits, no portable formal MIP proof
- **Reconciliation rule:** The verification category above governs this summary when older instance or table wording differs.

## Experiment workflow

1. Freeze the original model, baseline, objective convention, and acceptance tolerance.
2. Profile the untouched formulation and propose falsifiable structural hypotheses.
3. Run bounded primal, dual, reduction, or certificate experiments with explicit stopping rules.
4. Map useful results back to the original MPS and classify the resulting verification method.

## Download bundle

The sibling `.tar.gz` archive copies the related research material from this instance directory and adds this summary plus a package manifest. Only official raw `.mps`/`.mps.gz` inputs are omitted to avoid redistributing bulky benchmark source files; public solutions, hashes, derived proof models, runs, logs, and any proof traces present in the directory remain included. Files retained externally by hash cannot be embedded here.

## Provenance

Generated from the local `MIPLIB_openproblem` research archive for the LLM4MIP website. Read the source instance README and package manifest before reusing a numerical claim.

- **Source base commit:** `89a8abd0847941bdf774353a1983d5e6a00457a0` plus the disclosed 18 September working-tree reconciliation
- **Source README SHA-256:** `5d689998ff8bb6e375fc800c21dd9646eedd0811526f47b40bdc72d1b0295360`

## Package integrity

- **Archive:** `fhnw-schedule-paira400-findings.tar.gz`
- **Compressed bytes:** `327996`
- **SHA-256:** `88814ef371b96d6971b9b21df58b0998631c0ecc47601af94be3f039f0d9f10a`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/fhnw-schedule-paira400/README.md
