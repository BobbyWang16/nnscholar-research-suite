---
name: nnscholar3-1-experiment-validation-plan
description: Use when NNScholar needs to execute, monitor, resume, audit, or iteratively improve a locked research protocol after 2.2: automated research execution, overnight experiment loop, ML/LLM/RAG/agent benchmark runs, experiment queue, run manifest, job monitoring, result analysis, integrity audit, result-to-claim conversion, bounded auto-review loop, narrative report, and handoff to figures, paper architecture, tables, or manuscript writing.
---

# NNScholar 3.1 Automated Research Execution

This skill turns a locked or provisional experimental protocol into monitored research action. It is the execution and validation-operations layer: it runs or tracks experiments, preserves run state, audits results, converts evidence into claims, and prepares downstream handoff. It is not the protocol-design authority.

Version: `0.4.1`. Stage: `research execution / automated validation`. Routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id and folder name as `nnscholar3-1-experiment-validation-plan` / `/nnscholar3-1-experiment-validation-plan`.
- Keep the title format as `NNScholar 3.1 Automated Research Execution`.
- Name generated folders and files with English ASCII kebab-case slugs, preferably `phase-step-yyyy-mm-dd-topic`, regardless of the report language.

### Input and Language Policy

- Accept free-form user input, upstream NNScholar outputs, local files, pasted tables, figures, reviewer comments, target-venue instructions, repositories, configs, logs, result files, W&B notes, queue states, and execution constraints when relevant.
- For research planning, experiment execution, monitoring, audits, figure/table planning, and author-facing notes: output in the user's input language unless the user requests another language.
- For manuscript-facing text, including claim sentences, figure legends, Methods provenance sentences, narrative handoff, and reviewer-response-ready wording: default to polished academic English unless the user or target venue explicitly asks for Chinese, bilingual, or another language.
- Preserve identifiers in their standard form: database names, DOI/PMID/arXiv IDs, trial IDs, gene/protein symbols, chemical formulas, datasets, benchmarks, model names, config keys, run IDs, commit hashes, paths, metrics, and citation keys.
- Search strings, API queries, and benchmark names should normally be formulated in English, then explained in the output language.

### Multidisciplinary and Revision Standard

- First classify the discipline and study family: clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, engineering, or interdisciplinary.
- Use field-appropriate execution, evidence, monitoring, audit, and reporting norms. Do not force ML automation language onto non-code laboratory, clinical, fieldwork, or humanities projects.
- Every substantive output should include, when applicable: assumptions, missing information, author queries, risk/audit notes, and a revision-ready checklist.
- Do not fabricate citations, ethics approvals, registrations, sample sizes, statistics, experimental results, server availability, costs, author declarations, or venue requirements. Mark uncertain items as `needs verification`.
- When revising execution plans or claims, preserve scientific meaning, numeric values, methods, and claim strength unless the user supplies evidence and explicitly asks for a change.

## Core Rule

3.1 executes or monitors an evidence-producing plan only after the protocol source is clear enough. The default upstream authority is `nnscholar2-2-ars-plan`: 2.2 locks the question, claim, dataset/sample/materials, comparator, metric, validation route, pilot, go/no-go criteria, and fallback logic; 3.1 runs, tracks, audits, and reports what happened.

Do not silently change the 2.2 claim, dataset, comparator, metric, validation route, or go/no-go criteria. If execution reveals a necessary change, reopen 2.2 or record a protocol-deviation note and mark affected claims provisional.

If the user asks only for validation design, feasibility, pilot, go/no-go criteria, or fallback planning without execution, route to `../nnscholar2-2-ars-plan/WORKFLOW.md`.

## Boundary

Use this skill for:

- executing or monitoring a locked protocol;
- building a run manifest or experiment tracker;
- managing local, remote, Modal, Vast.ai, SSH, screen/tmux, or queue-based jobs;
- resuming long-running or overnight research work;
- checking logs, queue state, result files, failed runs, cost/budget risk, and blockers;
- analyzing result files and preserving raw result provenance;
- auditing experiment integrity before converting results into claims;
- converting supported results into claim-evidence maps;
- running bounded review-fix-review loops after results or draft artifacts exist;
- preparing downstream handoff to 4.1 paper figures, 4.2 paper tables, 2.3 paper architecture, 4.3 paper writing, or 2.2 redesign.

Do not use this skill for:

- broad topic selection or gap mining; use `nnscholar1-1-question-mining`;
- full literature search or citation verification; use `nnscholar1-2-literature-searching`;
- hypothesis invention or falsifiability design; use `nnscholar1-3-hypothesis-generation`;
- project-level Gantt planning; use `nnscholar2-1-research-planning`;
- protocol design, experimental route selection, or validation-route design; use `nnscholar2-2-ars-plan`;
- manuscript section order or result storyline design; use `nnscholar2-3-paper-architecture`;
- paper figure generation; use `nnscholar4-1-paper-figure`;
- paper table generation; use `nnscholar4-2-paper-table`;
- manuscript drafting or polishing; use `nnscholar4-3-paper-writing`;
- final submission, portal work, cover letters, or reviewer response; use 5.x workflows.

## Required References

For automated research, read:

- `../../references/auto-research-3-1-guardrails.md`
- `../../references/ai-research-engineering-guardrails.md` for AI/ML/LLM/RAG/agent, benchmark, model-training, or systems projects
- `../../references/supervisor-research-guardrails.md` for competitive CS/AI paper positioning, idea viability, benchmark design, or pre-submission-style critique

For full reports, use `references/automated-research-output-template.md`.

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output. Keep technical terms, benchmark names, model names, metric keys, run IDs, server aliases, code paths, and citation keys in their original form when clearer.

File and folder names must always use English ASCII slugs:

```text
research-runs/3-1-2026-06-28-llm-eval-benchmark/
research-runs/3-1-2026-06-28-radiomics-validation/
research-runs/3-1-2026-06-28-materials-stability/
```

Use clean Markdown with compact tables, stable headings, and editable checklists. Put long run manifests, trackers, and audit details in files rather than overloading chat.

## Run Modes

| Mode | Trigger | Behavior |
|---|---|---|
| `execute` | Locked protocol plus runnable code/data/resources | Build run state, launch or queue jobs, monitor, analyze, audit, and hand off |
| `monitor` | Running jobs, queue state, logs, W&B, screen/tmux, or resume request | Inspect status, update run state, detect blockers, and recommend next action |
| `audit` | Results exist and user asks whether they support claims | Run integrity checks, analyze results, and create claim-evidence map |
| `review-loop` | Results plus code, claim map, narrative report, or draft exist | Run bounded review-fix-review loop after audit |
| `dry-run` | Protocol is not executable or resources are missing | Produce execution manifest, blockers, budget, and first actions only |

## Upstream Priority

Use local or conversation artifacts in this order:

1. `nnscholar2-2-ars-plan`: protocol lock card, ARS plan, validation route, expected/disconfirming results, pilot/go-no-go, fallback, quality gates.
2. `nnscholar2-1-research-planning`: timeline, resources, milestones, project risks, budget or compute limits.
3. `nnscholar1-3-hypothesis-generation`: claim, mechanism, prediction, falsification rule.
4. `nnscholar1-2-literature-searching`: comparator methods, endpoints, benchmarks, evidence precedents.
5. Repository files: README, configs, scripts, tests, logs, result folders, notebooks, W&B notes, queue states.
6. Installed auto-research artifacts: `refine-logs/EXPERIMENT_PLAN.md`, `refine-logs/EXPERIMENT_TRACKER.md`, `review-stage/AUTO_REVIEW.md`, `NARRATIVE_REPORT.md`, `EXPERIMENT_AUDIT.md`, `CLAIMS_FROM_RESULTS.md`.
7. User message: latest constraints, budget, server, autonomy level, and target output.

When files are not specified, search `research-runs/`, `refine-logs/`, `review-stage/`, `results/`, `outputs/`, `logs/`, `configs/`, `scripts/`, `docs/`, `references/`, and the repository root. Do not assume the newest file belongs to the current topic; match by topic, date, run ID, protocol source, and user intent.

## Workflow

### Step 1: Intake and Mode Selection

Return a compact card:

```text
Detected mode:
Detected discipline / study family:
Protocol source:
Claim / hypothesis:
Runnable assets:
Data/material status:
Compute / environment:
Budget and autonomy boundary:
Missing information:
Next questions:
```

Ask at most 1-3 questions if required fields are missing. If the user asks for unattended execution, state the boundary: monitoring and stall recovery can be automated; quality acceptance still requires deterministic verification, independent review, or human approval.

### Step 2: Evidence and Protocol Check

Verify:

- protocol source and version;
- locked or provisional status;
- claim and metric boundary;
- data/material/code availability;
- comparator/baseline/control;
- expected output files;
- success, failure, and stop/go rules;
- ethics/privacy/licensing/safety constraints;
- budget, compute, server, and timeline constraints.

If there is no usable protocol source, create a dry-run execution plan and hand back to 2.2 for protocol locking.

### Step 3: Build the Run State

Create or update a 3.1 run folder when producing files:

```text
research-runs/3-1-YYYY-MM-DD-short-topic/
  autonomous_research_state.json
  autonomous_research_state.md
  run_manifest.md
  experiment_tracker.md
  result_summary.md
  experiment_audit.md
  claim_evidence_map.md
  narrative_handoff.md
  source_manifest.json
```

For long-running work, record phases as `pending`, `running`, `done`, `accepted`, `failed`, or `skipped`. A phase is `done` when the executor writes the artifact. A phase is `accepted` only when the deterministic verifier, integrity audit, independent reviewer, or human gate passes. On resume, revalidate any `done` phase that lacks an acceptance handle.

### Step 4: Convert Protocol to Execution Manifest

Build a manifest from the protocol:

| Field | Required content |
|---|---|
| Claim tested | claim, hypothesis, or validation question |
| Run/action | command, human action, assay, data extraction, or analysis step |
| Input | data, sample, material, config, code, server, or document |
| Variant | baseline, ablation, comparator, control, seed, split, or condition |
| Expected output | file path, table, figure, log, assay readout, or decision artifact |
| Success criterion | objective threshold or qualitative criterion |
| Failure interpretation | what a negative result means |
| Cost/risk | compute, time, budget, sample, ethics, or dependency risk |
| Gate | continue, revise, stop, or reopen 2.2 |

For AI/ML work, if the protocol is too high-level, use the installed `experiment-plan` skill as the planning subroutine and keep the resulting claim-driven run order inside the 3.1 handoff.

### Step 5: Route Execution

Choose the lightest safe executor:

- Use `run-experiment` for a small number of runnable jobs.
- Use `experiment-queue` for 10+ jobs, multi-seed/multi-config sweeps, phased jobs, teacher-student dependencies, OOM-prone jobs, or crash-safe remote scheduling.
- Use `monitor-experiment` for active jobs and status checks.
- Use `ablation-planner` when the main result is positive but reviewer-belief-changing ablations are missing.
- Use a human-action tracker for wet-lab, clinical, fieldwork, humanities, or social-science work that Codex cannot execute directly.

Before launch, verify environment, data, budget, path, and command assumptions. Do not launch paid cloud/GPU work, destructive scripts, patient-data operations, or external submissions without explicit user instruction.

### Step 6: Monitor, Recover, and Record Deviations

During monitoring:

- update run state and tracker;
- inspect logs, queue state, expected outputs, and failure markers;
- detect dead processes, missing files, stalled queues, OOM, failed preconditions, and budget risk;
- distinguish execution failure from scientific disconfirmation;
- make structural pivots only when the protocol allows them or after reopening 2.2;
- record any protocol deviation with reason, affected claim, and whether author confirmation is needed;
- never mark quality accepted because time passed or no error appeared.

### Step 7: Analyze and Audit Results

When outputs exist:

- use `analyze-results` or equivalent code to parse result files;
- preserve raw result paths and source hashes when feasible;
- run `experiment-audit` or apply its integrity checklist before converting results into claims;
- use `result-to-claim` or the NNScholar claim-evidence format to bind each claim to evidence;
- tag claims as supported, weakly supported, contradicted, provisional, or blocked.

Do not fabricate missing numbers. If a result is not in a file or source artifact, mark it missing.

### Step 8: Bounded Auto-Review Loop

Use `auto-review-loop` only after there is an artifact to review: results, code, claim map, narrative report, or draft.

Rules:

- use a fixed maximum round count;
- preserve reviewer memory, raw review, or trace handles when available;
- implement fixes before re-reviewing;
- separate review verdict from executor summary;
- stop at max rounds with remaining blockers rather than looping forever;
- if new experiments are required, update the run state and return to Step 5.

### Step 9: Output and Handoff

For short chats, return:

- mode and current state;
- protocol source;
- run/monitoring status;
- completed and failed actions;
- result summary;
- integrity audit status;
- claim-evidence status;
- blockers and risks;
- next 3 actions;
- recommended next NNScholar workflow.

For full reports, use `references/automated-research-output-template.md`.

Recommend the next stage:

- `nnscholar4-1-paper-figure` if quantitative results need figures.
- `nnscholar4-2-paper-table` if structured results need manuscript tables.
- `nnscholar2-3-paper-architecture` if the result storyline or figure/table blueprint changed.
- `nnscholar4-3-paper-writing` if claim-evidence and narrative handoff are ready.
- `nnscholar2-2-ars-plan` if execution revealed that the protocol must change.

## Interaction Pattern

Use short micro-rounds:

- Ask at most 1-3 questions per round.
- Prefer status cards and action tables over long prose.
- Do not ask questions already answered by local files or the user's message.
- If the user asks to "just run it," first show the execution boundary and any paid/destructive/ethics-sensitive step requiring explicit confirmation.

After major changes, show a compact 3.1 card:

```text
3.1 card:
Mode:
Protocol status:
Run state:
Accepted evidence:
Blocked evidence:
Integrity status:
Next action:
```

## Discipline Guardrails

- Clinical medicine: do not execute patient-data operations without privacy/ethics constraints; separate internal validation, external validation, calibration, clinical utility, and sensitivity analysis.
- Basic biomedicine: track biological replicates, technical replicates, batch, controls, reagent identity, rescue/orthogonal validation, and negative results.
- AI/data science: require dataset, split, labels, baselines, metric direction, ablations, seeds, config, commit/environment, leakage checks, failed runs, and reproducibility artifacts.
- Materials/chemistry: track synthesis batch, characterization settings, comparator, stability, repeated measurements, and instrument conditions.
- Education/psychology: track recruitment, consent, scale validity, attrition, intervention fidelity, effect sizes, and missing-data handling.
- Economics/social science: track identification strategy, data source, cleaning, fixed effects, standard errors, robustness, and external validity.
- Humanities: track corpus/archive selection, coding rules, source criticism, counterexamples, and interpretive uncertainty.
- Engineering: track prototype version, workload, hardware/software environment, operating conditions, stress/failure tests, and safety constraints.

## Auto Research Skill Integration

For automated or overnight research, read `../../references/auto-research-3-1-guardrails.md`. Use companion skills as subroutines, not as replacements for the 3.1 workflow:

- `research-pipeline` for full autonomous lifecycle only when the user explicitly wants an end-to-end chain.
- `experiment-plan` for claim-driven execution planning when 2.2 is too high-level.
- `run-experiment`, `experiment-queue`, and `monitor-experiment` for execution and monitoring.
- `analyze-results`, `experiment-audit`, and `result-to-claim` for evidence conversion.
- `auto-review-loop` for bounded review-fix-review after artifacts exist.

For AI/ML/LLM/RAG/agent/training/evaluation projects, also read `../../references/ai-research-engineering-guardrails.md`. Require the Two-Loop Research Cycle, Experiment Protocol and Trajectory Gate, Skill Routing and Environment Gate, Evaluation Harness Gate, Repo-to-Paper Evidence Gate, and Rigor Review Gate as applicable.

For technical CS or competitive AI venues, read `../../references/supervisor-research-guardrails.md` and apply fatal-flaw, benchmark, figure, and pre-submission-style checks where they affect execution or claim strength.

## Quality Gates

Before calling 3.1 complete, verify:

- protocol source is named and the protocol status is clear;
- run state is current and resumable if long-running;
- raw result paths are preserved;
- claimed numbers match artifacts;
- failed, negative, skipped, and incomplete runs are visible;
- integrity audit status is visible;
- autonomous review loop is bounded and documented if used;
- protocol deviations are recorded;
- next workflow can trust the claim boundary.

If a critical gate fails, mark the output as provisional and explain the minimum fix.

## Output Rules

Match the user's language. Keep variable names, endpoint names, model names, datasets, benchmark names, server aliases, run IDs, paths, and software names in their original form when clearer.

Default output files:

```text
research-runs/3-1-YYYY-MM-DD-short-topic/
  autonomous_research_state.json
  autonomous_research_state.md
  run_manifest.md
  experiment_tracker.md
  result_summary.md
  experiment_audit.md
  claim_evidence_map.md
  narrative_handoff.md
  source_manifest.json
```

For downstream manuscript or figure work, make sure `narrative_handoff.md` or the chat handoff includes:

```text
4.1 figure handoff:
Figure candidates:
Raw result paths:
Supported visual claims:
Uncertainty/variance notes:

4.2 table handoff:
Table candidates:
Raw result paths:
Metric definitions:
Sample size / split / seed notes:

2.3 handoff:
Updated result storyline:
Changed figure/table blueprint:
Claim boundary:

4.3 handoff:
Claim-evidence map:
Methods/provenance sentences:
Limitations sentence:
Unresolved evidence gaps:
```

Always end with:

```text
## NNScholar Suite Handoff

From workflow: nnscholar3-1-experiment-validation-plan
To recommended next workflow:
Project/topic:
Locked decisions:
Protocol source:
Run state:
Accepted evidence:
Provisional or failed evidence:
Integrity audit status:
Claim-evidence files:
Open questions:
Files/artifacts created or used:
Evidence boundary:
Companion skill bridge used:
Risks requiring human confirmation:
```

## Non-goals

Do not:

- invent hypotheses, baselines, datasets, approvals, citations, sample sizes, statistics, costs, or results;
- replace 2.2 protocol design;
- run paid GPU/cloud work without user permission;
- run destructive scripts without explicit confirmation;
- self-accept experiment quality;
- hide negative, failed, skipped, or incomplete runs;
- submit papers, portals, reviews, or external forms automatically;
- convert provisional evidence into manuscript claims without audit labels.
