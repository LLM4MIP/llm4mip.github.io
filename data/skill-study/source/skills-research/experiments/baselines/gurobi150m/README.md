# Gurobi 20-instance run

Started 2026-09-20 approximately 01:14 China time on euler4 as wyc.
Remote directory: `/data1/wyc/gurobi20_20260920T011104`.

Five batches, in the user-provided order, four instances each. Every model uses Gurobi 13.0.2, Threads=8 and TimeLimit=9000 seconds. Default search settings and Seed=0; original MPS only, no warm starts or previous cuts. A batch barrier waits for all four processes before starting the next batch. Total maximum solver time is approximately 12.5 hours plus loading, output, and resource-wait overhead; early termination may reduce this.

CPU affinity selects 16 relatively idle physical cores on each socket at every batch start. Four nonoverlapping groups each contain eight distinct physical cores within one socket, with only one SMT sibling selected per core. Binding is best-effort and does not exclude other users. See batches/batch_N_allocation.json for actual logical CPU IDs and physical-core topology. User explicitly accepted this limitation.

Memory protection: SoftMemLimit=56 and NodefileStart=8 (Gurobi decimal GB) per process. New batches wait if available RAM is below 260 GB. Memory exhaustion can end an instance before its time limit; the status is preserved.

Outputs:
- `summary.csv` and `summary.json`: final status, primal objective, dual bound, gap, solver runtime, wall time, thread allocation, and memory.
- `instances/NAME/primal.sol`: incumbent variable values if a feasible incumbent was found.
- `instances/NAME/NO_PRIMAL_SOLUTION.txt`: produced instead if no incumbent was found.
- `instances/NAME/dual_bound.json`: global MIP ObjBound and ObjBoundC, not a dual multiplier vector or exact certificate.
- `instances/NAME/gurobi.log`, `console.log`, `parameters.prm`, `result.json`, and `progress.json`.
- `state.json`: coordinator and worker process state.

The model's numerical solution-quality violations are saved with the final result when an incumbent exists. No independent exact certificate is claimed.

`sync_results.ps1` polls status and summaries every five minutes and downloads all instance outputs after remote completion. It requires the local machine to remain awake and connected; remote computation continues independently. `SYNC_COMPLETE.txt` indicates successful final download. The script can be restarted safely if the local machine sleeps or reboots.

Read remote progress: `ssh euler4 'cat /data1/wyc/gurobi20_20260920T011104/state.json'`.
