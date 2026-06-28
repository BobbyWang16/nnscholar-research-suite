# NNScholar 3.1 Auto Research Guardrails

Distilled from `wanshuiyin/Auto-claude-code-research-in-sleep` and adapted for NNScholar. Use these rules when `nnscholar3-1-experiment-validation-plan` is acting as the automated research execution and validation loop.

## Core Position

3.1 is the execution layer after 2.2:

- 2.1 plans project milestones and resources.
- 2.2 locks the experimental protocol, validation route, metrics, baselines, feasibility gates, and fallback logic.
- 3.1 executes or orchestrates the locked protocol, monitors progress, audits results, iterates with bounded review, and prepares evidence for figures and manuscript drafting.

Do not use 3.1 to invent a new hypothesis, silently change the protocol, or judge its own work as good enough.

## Companion Skill Routing

Use these installed skills when the local task matches:

| Need | Companion skill |
|---|---|
| Full autonomous lifecycle from idea to results to paper handoff | `research-pipeline` |
| Turn a refined proposal into claim-driven run order | `experiment-plan` |
| Implement/run a small number of jobs | `run-experiment` |
| Batch, multi-seed, multi-config, or phased GPU jobs | `experiment-queue` |
| Check active jobs, logs, screens, W&B, or queue status | `monitor-experiment` |
| Parse result files and summarize metrics | `analyze-results` |
| Convert supported results into paper claims | `result-to-claim` |
| Check result integrity before claims | `experiment-audit` |
| Plan decisive ablations | `ablation-planner` |
| Improve work through bounded review-fix-review rounds | `auto-review-loop` |
| Improve paper artifacts after drafting | `auto-paper-improvement-loop` |

Keep NNScholar as the spine: companion skills can execute or audit subtasks, but 3.1 owns stage order, artifacts, gates, and handoff.

## Acceptance Discipline

- Separate executor outputs from acceptance verdicts.
- A stage is `done` when the executor writes the artifact.
- A stage is `accepted` only when its deterministic verifier or independent reviewer gate passes.
- Never let a heartbeat, scheduler, or the same executor self-acquit quality.
- If the evidence is incomplete, mark claims provisional rather than filling gaps.

## External Cadence

Use background or scheduled wakeups only for visibility and stall recovery:

- OK: detect dead processes, stale queues, missing outputs, or no-progress ticks.
- OK: nudge a structurally different next attempt after repeated stagnation.
- Not OK: decide that a paper, experiment, result, or claim is good enough on a timer.

Quality verdicts must come from the relevant gate: result file verification, experiment audit, review loop, or human approval.

## Run State

For long-running 3.1 work, require a run state artifact with:

- run id, topic, protocol source, selected validation route;
- phase statuses: `pending`, `running`, `done`, `accepted`, `failed`, `skipped`;
- artifact paths and timestamps;
- budget and compute usage;
- blockers and next action;
- reviewer/audit verdict handles when available.

Prefer resumable runs. On resume, revalidate any `done` but unaccepted stage.

## Integrity Gates

Before converting results into claims, check:

- ground truth provenance;
- score normalization and metric definitions;
- claimed numbers versus result files;
- dead code or unused metrics;
- actual scope versus wording such as "comprehensive" or "robust";
- seeds, splits, baselines, ablations, and compute environment;
- leakage, cherry-picking, and missing failed runs.

If an integrity gate fails, continue only with explicit warning tags and downgraded claim strength.

## Handoff Minimum

A completed 3.1 handoff should include:

- locked protocol source;
- executed run manifest or action log;
- result summary and raw result paths;
- experiment audit status;
- claim-evidence table;
- unresolved weaknesses and failed attempts;
- recommended next workflow: usually `nnscholar4-1-paper-figure` for result figures, `nnscholar2-3-paper-architecture` for paper architecture updates, or `nnscholar4-3-paper-writing` for drafting and polishing.
