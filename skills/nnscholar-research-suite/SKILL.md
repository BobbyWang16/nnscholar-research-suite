---
name: nnscholar-research-suite
description: >
  NNScholar research workflow suite for question mining, literature searching,
  hypothesis generation, domain expert knowledge bases, research planning, ARS
  protocol design, experiment flowchart design, validation feasibility, paper architecture,
  paper figure production, paper table production, paper writing and polishing,
  venue recommendation, submission finalization,
  submission portal workflows, cover letters, reviewer responses, automated
  research execution, and AI research engineering. Use this suite for current
  NNScholar academic research workflows and specialist-aware orchestration for
  clinical/biomedical research, radiology or medical imaging AI, evidence-first
  literature work, AI/ML/LLM/RAG/agent/systems experiments, benchmark and
  evaluation planning, overnight/autonomous experiment loops, repo-to-paper conversion, ARA-style provenance and rigor
  review, high-impact manuscript writing, figures, citations, submission strategy,
  and research deliverables.
---

# NNScholar Research Suite

This is the single Codex-facing router for the NNScholar academic research
workflow. The stage modules live under `workflows/` and use `WORKFLOW.md` as
their entry file, so Codex registers only this root suite skill.

## First Rule

Do not load every workflow by default. Select exactly one workflow for the
current user request, read that workflow's `WORKFLOW.md`, then read only the
referenced templates, scripts, agents, or reference files needed for the current
phase.

If the request spans multiple workflow stages, start with the earliest stage
that would unblock the rest of the work. Stage 2 is intentionally compact:
`nnscholar2-1-research-planning` defines the project plan and Gantt chart;
`nnscholar2-2-ars-plan` defines the experimental/method protocol, executable
experiment flowchart, step-by-step procedure, expected results, validation
route, feasibility audit, pilot plan, go/no-go criteria, and fallback plan; and
`nnscholar2-3-paper-architecture` defines manuscript structure and figure/table
planning. Stage 4 is intentionally compact: `nnscholar4-1-paper-figure`
produces data figures, schematics, graphical abstracts, and multi-panel figure
assemblies; `nnscholar4-2-paper-table` produces manuscript tables; and
`nnscholar4-3-paper-writing` drafts, revises, polishes, and audits manuscript
prose. Experimental flowcharts are a native part of
`nnscholar2-2-ars-plan`.
`nnscholar3-1-experiment-validation-plan` is the automated research execution
and validation loop after 2.2 has produced a protocol.

Use `nnscholar2-2-ars-plan` only after the research question or hypothesis is
sufficiently clear, unless the user explicitly asks for a provisional protocol.

## Companion Skill Bridge

NNScholar is the workflow orchestrator. When a request is clearly domain-specific
or output-specific, keep the selected NNScholar workflow as the spine and use
`references/companion-skill-bridge.md` to decide whether a co-installed
specialist skill should provide stricter domain checks.

Read the bridge after choosing the workflow and before producing substantive
recommendations when the request involves:

- clinical medicine, biomedical research, translational research, omics, or
  medical literature appraisal;
- radiology, medical imaging AI, radiomics, CT/MRI/PET/ultrasound, segmentation,
  ROI/masks, model validation, or imaging reporting checklists;
- current literature, citation verification, evidence matrices, systematic
  searching, or claim-to-source binding;
- Nature/CNS/high-impact manuscript writing, figures, citations, reviewer
  response, or submission strategy;
- AI/data-science, database, systems, ML, NLP, or benchmark/evaluation papers
  where idea viability, technical paper logic, benchmark design, figure design,
  AI-assisted research workflow, or pre-submission reviewer-style checks matter;
- Word, PDF, spreadsheet, slide deck, or other file-format deliverables.

Use the strictest compatible guardrail. A companion skill can refine evidence,
domain norms, reporting standards, or file handling, but it must not override a
locked NNScholar protocol without reopening the relevant upstream workflow.

For Nature/CNS or high-impact manuscript work, use NNScholar's built-in
`references/high-impact-paper-guardrails.md`; do not rely on an external
Nature-style skill unless the user explicitly asks for that separate tool.

## Zotero Example Atlas

When the user asks for top-journal examples, figure/table inspiration, paper
structure, manuscript wording patterns, or "make it look like a high-impact
paper," read `references/zotero-example-atlas.md` after selecting the workflow.
The atlas contains copyright-safe structural pattern cards derived from the
user's Zotero library. Use those cards as inspiration and source pointers, not
as copied figures, captions, tables, or article text.

For visual figure-layout cues, the atlas also points to the CC BY screenshot
manifest at `assets/zotero-figure-examples/manifest.json` and selected JPG
reference crops under `assets/zotero-figure-examples/`. Inspect only the
matching assets needed for the current figure task, then generate original
panels and captions with source/license attribution preserved in the handoff.

## Built-In Supervisor Guardrails

For AI/data-science, database, systems, ML, NLP, benchmark/evaluation, or
technical CS papers, NNScholar has built-in advisor-style guardrails distilled
from Supervisor-Skills. After selecting the workflow, read
`references/supervisor-research-guardrails.md` when the request involves idea
viability, technical paper logic, benchmark paper structure, Introduction
logic, core figure design, AI-assisted research workflow, or pre-submission
review.

These guardrails are internal to NNScholar. Use them before companion skills:
the active NNScholar workflow remains the source of stage order, protocol lock,
artifact naming, and handoff requirements.

## Built-In AI Research Engineering Guardrails

For AI/data-science, ML, LLM, RAG, agent, multimodal, systems,
benchmark/evaluation, model-training, or autonomous experiment projects, also
read `references/ai-research-engineering-guardrails.md` when the request
involves iterative experiments, model training/fine-tuning, benchmark
evaluation, repo-to-paper drafting, citation/venue compliance, long-running
research state, or rigorous release/readiness review.

Use this file to add experiment engineering discipline, not to override
NNScholar's research-stage routing.

## Built-In High-Impact Paper Guardrails

For Nature/CNS, Nature-family, Cell/Science-family, or other high-impact
multidisciplinary outputs, read
`references/high-impact-paper-guardrails.md` after selecting the workflow when
the task involves paper architecture, figure/table production, manuscript
drafting or polishing, venue strategy, finalization, cover letters, or reviewer
response.

Apply its paper-type taxonomy, terminology ledger, high-impact argument chain,
figure contract, caption/table legend discipline, FAIR data/code availability,
citation/source discipline, pre-submission reviewer audit, and reviewer-response
action taxonomy as native NNScholar checks.

## Workflow Router

Choose the workflow by explicit payload, current workflow id, or intent.

### Explicit Payload

The NNScholar desktop UI may send a payload like:

```text
Use $nnscholar-research-suite.

Workflow: nnscholar2-2-ars-plan
Mode: protocol-lock
User request:
...
```

When `Workflow:` is present, route to the matching workflow unless the user
explicitly says the selected workflow is wrong.

### Workflow ID Router

If the user message begins with one of these current workflow ids, strip the id
token and route to the matching workflow.

| Alias | Read first |
|---|---|
| `/nnscholar1-1-question-mining`, `nnscholar1-1-question-mining` | `workflows/nnscholar1-1-question-mining/WORKFLOW.md` |
| `/nnscholar1-2-literature-searching`, `nnscholar1-2-literature-searching` | `workflows/nnscholar1-2-literature-searching/WORKFLOW.md` |
| `/nnscholar1-3-hypothesis-generation`, `nnscholar1-3-hypothesis-generation` | `workflows/nnscholar1-3-hypothesis-generation/WORKFLOW.md` |
| `/nnscholar1-4-domain-expert-knowledge-base`, `nnscholar1-4-domain-expert-knowledge-base` | `workflows/nnscholar1-4-domain-expert-knowledge-base/WORKFLOW.md` |
| `/nnscholar2-1-research-planning`, `nnscholar2-1-research-planning` | `workflows/nnscholar2-1-research-planning/WORKFLOW.md` |
| `/nnscholar2-2-ars-plan`, `nnscholar2-2-ars-plan` | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| `/nnscholar2-3-paper-architecture`, `nnscholar2-3-paper-architecture` | `workflows/nnscholar2-3-paper-architecture/WORKFLOW.md` |
| `/nnscholar3-1-experiment-validation-plan`, `nnscholar3-1-experiment-validation-plan` | `workflows/nnscholar3-1-experiment-validation-plan/WORKFLOW.md` |
| `/nnscholar4-1-paper-figure`, `nnscholar4-1-paper-figure` | `workflows/nnscholar4-1-paper-figure/WORKFLOW.md` |
| `/nnscholar4-2-paper-table`, `nnscholar4-2-paper-table` | `workflows/nnscholar4-2-paper-table/WORKFLOW.md` |
| `/nnscholar4-3-paper-writing`, `nnscholar4-3-paper-writing` | `workflows/nnscholar4-3-paper-writing/WORKFLOW.md` |
| `/nnscholar5-1-journal-conference-recommendation`, `nnscholar5-1-journal-conference-recommendation` | `workflows/nnscholar5-1-journal-conference-recommendation/WORKFLOW.md` |
| `/nnscholar5-2-submission-finalization`, `nnscholar5-2-submission-finalization` | `workflows/nnscholar5-2-submission-finalization/WORKFLOW.md` |
| `/nnscholar5-3-submission-portal-workflow`, `nnscholar5-3-submission-portal-workflow` | `workflows/nnscholar5-3-submission-portal-workflow/WORKFLOW.md` |
| `/nnscholar5-4-cover-letter`, `nnscholar5-4-cover-letter` | `workflows/nnscholar5-4-cover-letter/WORKFLOW.md` |
| `/nnscholar5-5-reviewer-response`, `nnscholar5-5-reviewer-response` | `workflows/nnscholar5-5-reviewer-response/WORKFLOW.md` |

### Intent Router

Use this route table when there is no explicit workflow:

| User intent | Read first |
|---|---|
| Broad topic, research gap, research question, novelty-first candidate question | `workflows/nnscholar1-1-question-mining/WORKFLOW.md` |
| Literature search, source screening, evidence matrix, citation verification | `workflows/nnscholar1-2-literature-searching/WORKFLOW.md` |
| Hypothesis, falsifiability, testable prediction, competing explanations | `workflows/nnscholar1-3-hypothesis-generation/WORKFLOW.md` |
| Reusable domain expert knowledge base from prior outputs or files | `workflows/nnscholar1-4-domain-expert-knowledge-base/WORKFLOW.md` |
| Project research plan, milestones, timeline, work packages, Gantt chart, project-level risks | `workflows/nnscholar2-1-research-planning/WORKFLOW.md` |
| AI/ML/LLM/RAG/agent/systems research project, autonomous experiment loop, research state, experiment trajectory, ARA provenance | `workflows/nnscholar2-1-research-planning/WORKFLOW.md` |
| Experimental protocol, method route, executable experiment steps, experiment flowchart, expected results, validation route, feasibility audit, pilot plan, go/no-go criteria, fallback plan, quality gates | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| Model training, fine-tuning, benchmark, evaluation harness, baseline, ablation, seed, reproducibility, artifact protocol | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| Paper writing plan, manuscript structure, result storyline, figure/table blueprint derived from experiments | `workflows/nnscholar2-3-paper-architecture/WORKFLOW.md` |
| Flowchart, technical route diagram, Mermaid, experimental pipeline | route to `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` unless it is purely a manuscript figure/table blueprint, then use 2.3 |
| Experiment or validation steps, resources, feasibility, pilot plan, go/no-go criteria | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| Execute or monitor a locked protocol, run experiments, manage experiment queues, resume overnight research, audit results, convert results to claims, or run bounded review-fix-review loops | `workflows/nnscholar3-1-experiment-validation-plan/WORKFLOW.md` |
| Paper figure production: structured data plot, chart selection, scientific schematic, graphical abstract, mechanism/model/workflow diagram, image prompt, multi-panel figure assembly, caption, legend, export audit | `workflows/nnscholar4-1-paper-figure/WORKFLOW.md` |
| Paper table production: manuscript table, Word table, Markdown/HTML/LaTeX table, statistical/regression table, benchmark table, literature comparison table, table notes, abbreviations | `workflows/nnscholar4-2-paper-table/WORKFLOW.md` |
| Paper writing: manuscript brief, first draft, section writing, figure/table integration, codebase/logs/results to claim-evidence draft, polishing, revision, risky-claim audit, venue/style adaptation | `workflows/nnscholar4-3-paper-writing/WORKFLOW.md` |
| Journal or conference recommendation and submission strategy, including AI/ML/NLP/systems/benchmark venues | `workflows/nnscholar5-1-journal-conference-recommendation/WORKFLOW.md` |
| Final submission package, compliance checklist, author statements | `workflows/nnscholar5-2-submission-finalization/WORKFLOW.md` |
| Submission portal fields, uploads, declarations, final human submit checklist | `workflows/nnscholar5-3-submission-portal-workflow/WORKFLOW.md` |
| Cover letter, presubmission inquiry, editorial pitch | `workflows/nnscholar5-4-cover-letter/WORKFLOW.md` |
| Reviewer response, rebuttal, revision plan, point-by-point replies, baseline/ablation/reproducibility/artifact critique | `workflows/nnscholar5-5-reviewer-response/WORKFLOW.md` |

## Routing Discipline

- If a user provides only a vague paper topic and asks to write a paper, start
  with `nnscholar1-1-question-mining` before drafting or architecture.
- If a user provides reviewer comments, route to `nnscholar5-5-reviewer-response`
  unless they explicitly ask to polish the revised manuscript body first.
- If a user provides structured data and asks for both a figure and manuscript
  text, route first to `nnscholar4-1-paper-figure`, then hand off to
  `nnscholar4-3-paper-writing`.
- If evidence, citation, data, or venue requirements are current or external,
  verify them with source links instead of relying on memory.
- Preserve the user's output language for author-facing planning notes. Use
  polished academic English for manuscript-facing text unless the user or venue
  asks otherwise.
- If a specialist domain bridge is used, record the bridge in the final handoff
  and name the stricter guardrails that affected the recommendation.

## Handoff Contract

Each workflow keeps its original local templates and handoff rules. When a
workflow produces an artifact for a later workflow, include a final section:

```text
## NNScholar Suite Handoff

From workflow:
To recommended next workflow:
Project/topic:
Locked decisions:
Open questions:
Files/artifacts created or used:
Evidence boundary:
Companion skill bridge used:
Risks requiring human confirmation:
```

Do not invent citations, data, statistics, ethics approvals, author
declarations, venue requirements, or reviewer outcomes. Mark uncertain items as
`needs verification`.
