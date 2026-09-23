# fhnw-schedule-pairb400

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -36.27696674236886 (new strict incumbent)
- **Best bound or certificate:** -36.27696674236886 (independent safe suffix master)
- **Study result:** Computational optimum; two safe runs, cross-formulation audit, invalid old cuts explicitly rejected

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -36.276966742368865136
- **Main method:** portable exact branch-and-dual certificate with frozen or rebuilt strengthening, untouched-original-MPS audit, and paired-formulation cross-check where available
- **Verification category:** PE — Portable exact certificate
- **Earlier source-table status:** computational optimality verification; two safe zero-gap runs and full-row audits, no portable formal MIP proof
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
- **Source README SHA-256:** `42634b6c2f6fc2edf99f4526daa31df4abc6346fdff40a84535cd716fc86127e`

## Package integrity

- **Archive:** `fhnw-schedule-pairb400-findings.tar.gz`
- **Compressed bytes:** `124724`
- **SHA-256:** `af6d315f1df4bed8c65287262103a3b5d21cc25d873863ab005358ead9e7c2fd`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/fhnw-schedule-pairb400/README.md
