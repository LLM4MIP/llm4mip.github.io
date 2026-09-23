# fhnw-schedule-paira100

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -15.113116512593402 (strict)
- **Best bound or certificate:** -15.113116512593402 (Gurobi + audited valid cuts)
- **Study result:** Computational optimum; official lower headline is nonintegral, so no numerical primal improvement is claimed

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -15.113116512593401992
- **Main method:** portable exact branch-and-dual certificate with frozen or rebuilt strengthening, untouched-original-MPS audit, and paired-formulation cross-check where available
- **Verification category:** PE — Portable exact certificate
- **Earlier source-table status:** computational optimality verification; original-MPS and row-semantic audits, no portable formal MIP proof
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
- **Source README SHA-256:** `2843e2c13cc2d03b0e9df8665f841c4673b13f69a858780d8c3005931fd8e7c8`

## Package integrity

- **Archive:** `fhnw-schedule-paira100-findings.tar.gz`
- **Compressed bytes:** `508081`
- **SHA-256:** `41885bcf6518a0f349648a517da4ca234ed5667bb2b942141fb72fe738d8684a`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/fhnw-schedule-paira100/README.md
