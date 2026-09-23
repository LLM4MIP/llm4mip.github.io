# fhnw-schedule-paira200

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -19.369961204645204 (new strict incumbent)
- **Best bound or certificate:** -19.369961204645204 (Gurobi + audited valid cuts)
- **Study result:** Computational optimum; independent rerun and original-MPS audit

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -19.369961204645205810
- **Main method:** portable exact branch-and-dual certificate with frozen or rebuilt strengthening, untouched-original-MPS audit, and paired-formulation cross-check where available
- **Verification category:** PE — Portable exact certificate
- **Earlier source-table status:** computational optimality verification; original-MPS and cross-formulation audits, no portable formal MIP proof
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
- **Source README SHA-256:** `09462db7cc705326686ce557fb4491e95cf1d722e21878d9e382914304f3c160`

## Package integrity

- **Archive:** `fhnw-schedule-paira200-findings.tar.gz`
- **Compressed bytes:** `889084`
- **SHA-256:** `a62cdac5a8af22a6a94276de19d3e95d2b32410c39bf3bd2430daca5be73e650`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/fhnw-schedule-paira200/README.md
