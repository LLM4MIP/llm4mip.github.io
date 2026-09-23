# neos-3594536-henty

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 401,092
- **Best bound or certificate:** 401,092 (Gurobi/COPT)
- **Study result:** Computational optimum; exact primal audit, no portable exact lower-bound certificate

## Certified optimality or infeasibility result

- **Conclusion:** OPT approximately 401,092
- **Main method:** exact component-balance/parity reduction + zero-gap Gurobi/COPT
- **Verification category:** NS — Strict primal audit plus floating-point zero-gap solver run
- **Earlier source-table status:** computational optimality verification; no portable exact lower-bound certificate
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
- **Source README SHA-256:** `852dc28839ef3674b391f65ebb5f7d09ff6de60c7124d362a0710f6f9bf7e5ac`

## Package integrity

- **Archive:** `neos-3594536-henty-findings.tar.gz`
- **Compressed bytes:** `216674`
- **SHA-256:** `5b6c27423826b646b5a10142ad361da1eb28d9772dd5a1d5cb11ec01863d5551`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/neos-3594536-henty/README.md
