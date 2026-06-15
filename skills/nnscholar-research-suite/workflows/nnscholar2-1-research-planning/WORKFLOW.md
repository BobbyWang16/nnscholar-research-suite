---
name: nnscholar2-1-research-planning
description: Use when NNScholar needs to turn a selected research question, literature-search output, hypothesis report, or domain knowledge base into an executable research plan. Trigger for research planning, project planning, study execution plans, timelines, milestones, work packages, dependency sequencing, feasibility/risk audits, next research steps, or recovery plans for active projects.
---

# NNScholar 2.1 Research Planning

This skill turns an already chosen research direction into an executable research plan. It acts as a research project manager: clarify the current state, define scope, break the work into packages, sequence dependencies, estimate a realistic timeline, identify risks, and decide the next concrete actions.

It is inspired by `research-planning`, `ars-plan`, `research-ideation`, and `scientific-critical-thinking`, but is narrower: do not continue literature searching, invent new hypotheses, write manuscript prose, or design detailed protocols unless those are needed to make the plan coherent.

Version: `0.2.0`. Stage: `research setting / research planning`. Legacy workflow alias: `$nnscholar2-1-research-planning`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar2-1-research-planning` / `/nnscholar2-1-research-planning`.
- Keep the title format as `NNScholar 2.1 Research Planning`.
- Name generated folders and files with English ASCII kebab-case slugs, preferably `phase-step-yyyy-mm-dd-topic`, regardless of the report language.

### Input and Language Policy

- Accept free-form user input, upstream NNScholar outputs, local files, pasted tables, figures, reviewer comments, and target-venue instructions when relevant.
- For research planning, literature, experiment, figure/table planning, audits, and author-facing notes: output in the user's input language unless the user requests another language.
- For manuscript-facing text, including titles, abstracts, manuscript sections, figure legends, table titles/notes, cover letters, submission statements, and reviewer responses: default to polished academic English unless the user or target venue explicitly asks for Chinese, bilingual, or another language.
- Preserve identifiers in their standard form: database names, DOI/PMID/arXiv IDs, trial IDs, gene/protein symbols, chemical formulas, datasets, benchmarks, model names, scales, laws, policies, and citation keys.
- Search strings and database queries should normally be formulated in English, then explained in the output language.

### Multidisciplinary and Revision Standard

- First classify the discipline and study family: clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, engineering, or interdisciplinary.
- Use field-appropriate evidence, methods, reporting norms, and terminology. Do not force biomedical templates onto non-biomedical work.
- Every substantive output should include, when applicable: assumptions, missing information, author queries, risk/audit notes, and a revision-ready checklist.
- Do not fabricate citations, ethics approvals, registrations, sample sizes, statistics, experimental results, author declarations, or venue requirements. Mark uncertain items as `needs verification`.
- When revising or polishing, preserve scientific meaning, numeric values, methods, and claim strength unless the user supplies evidence and explicitly asks for a change.

## Core Rule

Produce a plan only after the research object, output goal, and execution constraints are clear enough. If one of these is missing, ask the smallest useful set of questions instead of producing a polished but unstable plan.

Default minimum questions when the user only clicks the button or provides a vague topic:

1. What is the research question or topic?
2. What is the target output: paper, proposal, thesis, grant, pre-experiment, protocol, or internal project?
3. What is the expected time window and what materials/data are already available?

If the user supplies enough information, proceed without asking.

## Language, Filename, and Formatting Rule

Match the user's input language in all user-facing output. If the user writes Chinese, output Chinese. If the user writes English, output English. Keep database names, trial IDs, variable names, model names, method names, citation keys, and file paths in their original scholarly form.

File names must always use English ASCII slugs:

```text
research-plan-2026-06-11-sclc-immunotherapy.md
research-plan-2026-06-11-ccta-diabetes-risk.md
research-plan-2026-06-11-llm-evaluation-benchmark.md
```

Use clean Markdown with compact tables. Keep chat turns short and decision-oriented. Put the complete plan in a saved report when file output is requested or when the plan is long.

## Template Rule

Use `references/research-planning-output-template.md` as the structural template for full reports. The template defines structure, not output language. Localize headings and field labels to the user's language in the final report.

Use `references/discipline-planning-guide.md` when the discipline, study family, or work-package pattern matters. Load only the relevant section and adapt it to the user's available evidence.

Use `references/research-planning-test-cases.md` for quick behavior checks and regression examples.

## Input

Accept:

- a research topic or question;
- `nnscholar1-1-question-mining` output;
- `nnscholar1-2-literature-searching` output;
- `nnscholar1-3-hypothesis-generation` output;
- `nnscholar1-4-domain-expert-knowledge-base` output;
- local notes, protocols, literature tables, PDF summaries, datasets, manuscript outlines, or user constraints.

Do not assume the newest upstream file belongs to the current topic. Match files by topic keywords, date, project name, disease/model/dataset, and user intent.

## Evidence Discovery

When the user does not provide exact files:

1. Search the current workspace for likely NNScholar outputs and local project files.
2. Prefer matching 1.3 hypothesis output, then 1.2 literature output, then 1.1 question-mining output, then 1.4 knowledge base, then local notes.
3. Use file names, headings, and content snippets to identify the right topic.
4. If multiple plausible evidence bundles exist, present the top 1-3 choices and ask the user to confirm.

Evidence priority:

1. Locked or user-confirmed hypothesis from `1.3`.
2. Literature evidence and research gaps from `1.2`.
3. Research question and novelty rationale from `1.1`.
4. Domain constraints, reviewer risks, bias notes, and design hints from `1.4`.
5. User-provided constraints in the current conversation.

If evidence is weak, mark the plan as `provisional` and identify the upstream stage that should be run before execution.

## Planning Maturity Assessment

Classify the project before planning:

| Level | State | Planning behavior |
|---|---|---|
| S0 Topic only | Broad topic, no question | Ask for target output and scope; create exploratory plan only |
| S1 Question selected | Research question exists | Create question-to-evidence-to-method plan |
| S2 Hypothesis locked | Testable hypothesis exists | Create execution plan with design, data, endpoints, and analysis dependencies |
| S3 Materials available | Data, cohort, corpus, model, or PDFs exist | Create task-level plan with deliverables and validation steps |
| S4 Manuscript target known | Journal, thesis, proposal, or conference known | Include writing and submission-prep dependencies |
| S5 Active project | Work already started | Create recovery plan, backlog, risk audit, and next sprint |

## Workflow

### Step 1: Intake and Scope

Extract:

- target output;
- research question or hypothesis;
- discipline and article/project type;
- available evidence, data, materials, models, code, or corpus;
- time window and resource constraints;
- target venue, funder, course, thesis committee, or internal stakeholder if relevant.

Ask at most 1-3 clarifying questions if any required field is missing.

### Step 2: Define Planning Boundary

State what the plan will and will not cover. Separate:

- research execution;
- data or experiment work;
- analysis/statistics/evaluation;
- manuscript/proposal writing;
- submission or review preparation.

Do not merge every possible downstream task into one giant plan. Keep only tasks needed for the user's current output goal.

### Step 3: Create Work Packages

Break the project into 4-7 work packages. Each work package must include:

- goal;
- input materials;
- method or activity;
- output/deliverable;
- dependencies;
- owner/role if known;
- evidence or quality gate.

Avoid vague tasks like "do analysis" or "write paper". Replace them with checkable tasks such as "build variable dictionary", "define primary endpoint", "screen 30 candidate papers", "run baseline model", or "draft Methods from finalized protocol".

Select work packages by discipline. For clinical projects, include cohort/endpoint/statistics/ethics readiness. For wet-lab or materials projects, include synthesis or experimental reproducibility, controls, characterization, and safety. For AI or computational projects, include dataset governance, baselines, metrics, ablations, leakage checks, and reproducibility. For education, psychology, and social science projects, include theory/construct mapping, instrument validity, recruitment, consent, confounding, and mixed-methods or qualitative rigor when relevant.

### Step 4: Sequence Dependencies

Order tasks by dependency, not by wishful chronology. Typical dependency chain:

```text
Question/hypothesis -> Evidence and scope -> Data/material readiness -> Method/protocol -> Analysis/evaluation -> Figures/tables -> Manuscript/proposal -> Review/submission
```

Identify which tasks can run in parallel and which tasks block later work.

### Step 5: Build Timeline and Milestones

Create a realistic timeline using the user's time window. If no time window is given, propose a default and label it:

- quick sprint: 2 weeks;
- short project: 4-6 weeks;
- standard paper plan: 8-12 weeks;
- thesis/grant: 3-6 months.

Each milestone must have an observable deliverable.

### Step 6: Risk and Feasibility Audit

Check:

- evidence gaps;
- unavailable data/materials;
- sample size, power, or dataset limitations;
- ethics, IRB, privacy, licensing, or safety constraints;
- method mismatch;
- timeline overreach;
- reviewer or committee objections;
- dependency bottlenecks.

For every high-risk item, provide a mitigation or fallback path.

### Step 7: Output and Handoff

Return a concise planning brief in chat. For full reports, follow the template and include:

- current state assessment;
- scope and output goal;
- research question/hypothesis;
- work packages;
- task dependency map;
- timeline and milestones;
- risks and fallbacks;
- quality gates;
- next 3 actions;
- downstream handoff to `research-scheme`, `paper-architecture`, or `flowchart-design` when appropriate.

## Interaction Pattern

Use short micro-rounds:

- Ask at most 1-3 questions per round.
- Prefer choices when ambiguity is common.
- After major choices, show a compact "planning card":

```text
Planning card:
Target output:
Research object:
Current maturity:
Main constraint:
Next decision:
```

Do not ask questions already answered by local files or the user's message.

## Quality Gates

Before finalizing, verify:

- The plan is connected to a specific question or hypothesis.
- The output goal is explicit.
- Every work package has a concrete deliverable.
- Timeline matches available resources.
- Blocking dependencies are visible.
- Risks have mitigation or fallback.
- The next 3 actions are small enough to start immediately.

If a gate fails, mark the plan as provisional and explain what must be clarified.

## Non-goals

Do not:

- run a full literature search unless the user asks to switch to `nnscholar1-2-literature-searching`;
- generate new hypotheses unless the plan reveals that `nnscholar1-3-hypothesis-generation` is needed;
- draft manuscript prose;
- pretend missing data, approvals, or citations exist;
- create an over-detailed protocol when the user only needs a project timeline.
