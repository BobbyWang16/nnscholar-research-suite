---
name: nnscholar-research-suite
description: >
  NNScholar research workflow suite for question mining, literature searching,
  hypothesis generation, domain expert knowledge bases, research planning, ARS
  protocol design, paper architecture, flowchart design, experiment validation,
  data figures, image schematics, figure assembly, table formatting, manuscript
  drafting, manuscript polishing, venue recommendation, submission finalization,
  submission portal workflows, cover letters, and reviewer responses. Use this
  suite for NNScholar academic research workflows, legacy aliases such as
  /nnscholar1-1-question-mining through /nnscholar5-5-reviewer-response, and
  specialist-aware orchestration for clinical/biomedical research, radiology or
  medical imaging AI, evidence-first literature work, high-impact manuscript
  writing, figures, citations, submission strategy, and research deliverables.
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
that would unblock the rest of the work. Use `nnscholar2-2-ars-plan` only after
the research question or hypothesis is sufficiently clear, unless the user
explicitly asks for a provisional protocol.

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
- Word, PDF, spreadsheet, slide deck, or other file-format deliverables.

Use the strictest compatible guardrail. A companion skill can refine evidence,
domain norms, reporting standards, or file handling, but it must not override a
locked NNScholar protocol without reopening the relevant upstream workflow.

## Zotero Example Atlas

When the user asks for top-journal examples, figure/table inspiration, paper
structure, manuscript wording patterns, or "make it look like a high-impact
paper," read `references/zotero-example-atlas.md` after selecting the workflow.
The atlas contains copyright-safe structural pattern cards derived from the
user's Zotero library. Use those cards as inspiration and source pointers, not
as copied figures, captions, tables, or article text.

For visual figure-layout cues, the atlas also points to the CC BY screenshot
gallery at `references/figure-screenshot-gallery.md`, the asset manifest at
`assets/zotero-figure-examples/manifest.json`, and selected JPG reference crops
under `assets/zotero-figure-examples/`. These images are bundled with the skill
for portable use on other computers; Zotero keys are provenance labels only.
Inspect only the matching assets needed for the current figure task, then
generate original panels and captions with source/license attribution preserved
in the handoff.

## Workflow Router

Choose the workflow by explicit payload, legacy alias, or intent.

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

### Legacy Alias Router

If the user message begins with one of these aliases, strip the alias token and
route to the matching workflow. These aliases are compatibility shims for the
older multi-skill layout and for desktop workflow buttons.

| Alias | Read first |
|---|---|
| `/nnscholar1-1-question-mining`, `nnscholar1-1-question-mining` | `workflows/nnscholar1-1-question-mining/WORKFLOW.md` |
| `/nnscholar1-2-literature-searching`, `nnscholar1-2-literature-searching` | `workflows/nnscholar1-2-literature-searching/WORKFLOW.md` |
| `/nnscholar1-3-hypothesis-generation`, `nnscholar1-3-hypothesis-generation` | `workflows/nnscholar1-3-hypothesis-generation/WORKFLOW.md` |
| `/nnscholar1-4-domain-expert-knowledge-base`, `nnscholar1-4-domain-expert-knowledge-base` | `workflows/nnscholar1-4-domain-expert-knowledge-base/WORKFLOW.md` |
| `/nnscholar2-1-research-planning`, `nnscholar2-1-research-planning` | `workflows/nnscholar2-1-research-planning/WORKFLOW.md` |
| `/nnscholar2-2-ars-plan`, `nnscholar2-2-ars-plan` | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| `/nnscholar2-3-paper-architecture`, `nnscholar2-3-paper-architecture` | `workflows/nnscholar2-3-paper-architecture/WORKFLOW.md` |
| `/nnscholar2-4-flowchart-design`, `nnscholar2-4-flowchart-design` | `workflows/nnscholar2-4-flowchart-design/WORKFLOW.md` |
| `/nnscholar3-1-experiment-validation-plan`, `nnscholar3-1-experiment-validation-plan` | `workflows/nnscholar3-1-experiment-validation-plan/WORKFLOW.md` |
| `/nnscholar4-1-data-figure`, `nnscholar4-1-data-figure` | `workflows/nnscholar4-1-data-figure/WORKFLOW.md` |
| `/nnscholar4-2-image-schematic`, `nnscholar4-2-image-schematic` | `workflows/nnscholar4-2-image-schematic/WORKFLOW.md` |
| `/nnscholar4-3-figure-assembly`, `nnscholar4-3-figure-assembly` | `workflows/nnscholar4-3-figure-assembly/WORKFLOW.md` |
| `/nnscholar4-4-table-formatting`, `nnscholar4-4-table-formatting` | `workflows/nnscholar4-4-table-formatting/WORKFLOW.md` |
| `/nnscholar4-5-manuscript-drafting`, `nnscholar4-5-manuscript-drafting` | `workflows/nnscholar4-5-manuscript-drafting/WORKFLOW.md` |
| `/nnscholar4-6-manuscript-polishing`, `nnscholar4-6-manuscript-polishing` | `workflows/nnscholar4-6-manuscript-polishing/WORKFLOW.md` |
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
| Executable research plan, milestones, timeline, work packages, risks | `workflows/nnscholar2-1-research-planning/WORKFLOW.md` |
| Aim-Route-Specification plan, protocol lock, study/method/statistical route | `workflows/nnscholar2-2-ars-plan/WORKFLOW.md` |
| Paper architecture, manuscript structure, result storyline, figure/table blueprint | `workflows/nnscholar2-3-paper-architecture/WORKFLOW.md` |
| Flowchart, technical route diagram, Mermaid, PRISMA-style flow | `workflows/nnscholar2-4-flowchart-design/WORKFLOW.md` |
| Experiment or validation steps, resources, feasibility, go/no-go criteria | `workflows/nnscholar3-1-experiment-validation-plan/WORKFLOW.md` |
| Structured data plot, chart selection, publication figure, plotting code | `workflows/nnscholar4-1-data-figure/WORKFLOW.md` |
| Scientific schematic, graphical abstract, mechanism diagram, image prompt | `workflows/nnscholar4-2-image-schematic/WORKFLOW.md` |
| Multi-panel figure assembly from existing panels | `workflows/nnscholar4-3-figure-assembly/WORKFLOW.md` |
| Manuscript table formatting, Word table, table notes, abbreviations | `workflows/nnscholar4-4-table-formatting/WORKFLOW.md` |
| First manuscript draft from upstream outputs | `workflows/nnscholar4-5-manuscript-drafting/WORKFLOW.md` |
| Manuscript polishing, section revision, risky-claim audit, style adaptation | `workflows/nnscholar4-6-manuscript-polishing/WORKFLOW.md` |
| Journal or conference recommendation and submission strategy | `workflows/nnscholar5-1-journal-conference-recommendation/WORKFLOW.md` |
| Final submission package, compliance checklist, author statements | `workflows/nnscholar5-2-submission-finalization/WORKFLOW.md` |
| Submission portal fields, uploads, declarations, final human submit checklist | `workflows/nnscholar5-3-submission-portal-workflow/WORKFLOW.md` |
| Cover letter, presubmission inquiry, editorial pitch | `workflows/nnscholar5-4-cover-letter/WORKFLOW.md` |
| Reviewer response, rebuttal, revision plan, point-by-point replies | `workflows/nnscholar5-5-reviewer-response/WORKFLOW.md` |

## Routing Discipline

- If a user provides only a vague paper topic and asks to write a paper, start
  with `nnscholar1-1-question-mining` before drafting or architecture.
- If a user provides reviewer comments, route to `nnscholar5-5-reviewer-response`
  unless they explicitly ask to polish the revised manuscript body first.
- If a user provides structured data and asks for both a figure and manuscript
  text, route first to `nnscholar4-1-data-figure`, then hand off to
  `nnscholar4-5-manuscript-drafting`.
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
