# NNScholar Research Suite

Codex-native packaging of the NNScholar academic research workflow suite.

This repository exposes one installable Codex skill:

```text
skills/nnscholar-research-suite/
  SKILL.md
  manifest.json
  agents/openai.yaml
  references/
  workflows/
    nnscholar1-1-question-mining/
      WORKFLOW.md
      references/
      agents/
    ...
```

The 16 NNScholar workflow modules live under `workflows/` and use
`WORKFLOW.md` instead of `SKILL.md`. This keeps Codex registration clean: users
see one skill, `$nnscholar-research-suite`, while the desktop UI can still send
structured `Workflow: <id>` payloads.

## Install

Install from this repository path:

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo BobbyWang16/nnscholar-research-suite \
  --ref main \
  --path skills/nnscholar-research-suite \
  --method git
```

On Windows, use your Codex bundled Python path or any Python 3 interpreter:

```powershell
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" `
  "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo BobbyWang16/nnscholar-research-suite `
  --ref main `
  --path skills/nnscholar-research-suite `
  --method git
```

Restart Codex or open a new Codex conversation after installation so the skill
cache can refresh.

## Usage

Invoke the suite directly:

```text
Use $nnscholar-research-suite.

Workflow: nnscholar2-2-ars-plan
User request:
Design and lock an executable research protocol for this hypothesis.
```

Current workflow aliases are routed by the root skill:

```text
/nnscholar4-3-paper-writing draft a manuscript from these notes
```

## Workflow Map

| Stage | Workflow |
|---|---|
| 1.1 | `nnscholar1-1-question-mining` |
| 1.2 | `nnscholar1-2-literature-searching` |
| 1.3 | `nnscholar1-3-hypothesis-generation` |
| 1.4 | `nnscholar1-4-domain-expert-knowledge-base` |
| 2.1 | `nnscholar2-1-research-planning` |
| 2.2 | `nnscholar2-2-ars-plan` |
| 2.3 | `nnscholar2-3-paper-architecture` |
| 3.1 | `nnscholar3-1-experiment-validation-plan` |
| 4.1 | `nnscholar4-1-paper-figure` |
| 4.2 | `nnscholar4-2-paper-table` |
| 4.3 | `nnscholar4-3-paper-writing` |
| 5.1 | `nnscholar5-1-journal-conference-recommendation` |
| 5.2 | `nnscholar5-2-submission-finalization` |
| 5.3 | `nnscholar5-3-submission-portal-workflow` |
| 5.4 | `nnscholar5-4-cover-letter` |
| 5.5 | `nnscholar5-5-reviewer-response` |

Stage 2 is compact: `2.2` now owns ARS protocol design, experimental
flowcharts, validation routes, feasibility audits, pilot plans, go/no-go
criteria, and fallback plans. Stage 4 is compact: `4.1` owns data figures,
schematics, graphical abstracts, and multi-panel figure assembly; `4.2` owns
tables; `4.3` owns drafting, revision, polishing, and manuscript audits.

## Specialist Guardrails

The suite includes built-in and companion guardrails under `references/`:

- `companion-skill-bridge.md` maps NNScholar stages to co-installed specialist
  skills for medicine, imaging AI, evidence work, file formats, and technical
  papers.
- `supervisor-research-guardrails.md` adds advisor-style checks for
  AI/data-science, database, systems, ML, NLP, and benchmark papers.
- `ai-research-engineering-guardrails.md` adds experiment engineering,
  reproducibility, model-training, benchmark, autonomous-loop, and release
  readiness discipline.
- `high-impact-paper-guardrails.md` adds Nature/CNS-style paper architecture,
  figure, table, citation, availability, and reviewer-response checks.

NNScholar remains the stage orchestrator. Companion skills can refine evidence,
domain norms, reporting standards, or file handling, but they should not
override a locked NNScholar protocol without reopening the relevant upstream
workflow.

## Zotero Example Atlas

The suite includes a copyright-safe example atlas derived from the user's
Zotero library:

```text
skills/nnscholar-research-suite/references/zotero-example-atlas.md
```

It provides structural example cards for workflow tasks and 12
chart/figure-generation examples for `nnscholar4-1-paper-figure`. The cards
preserve Zotero keys, venue names, DOI/URLs, and reusable structure patterns,
but they do not copy source figures, captions, tables, or long article text.

For figure-layout inspiration, the suite bundles 12 low-resolution CC BY visual
reference crops and a manifest:

```text
skills/nnscholar-research-suite/assets/zotero-figure-examples/manifest.json
```

Use these screenshots only as layout references for generating original
figures, and preserve source/license attribution in project handoffs.

## Validation

Run the no-dependency structure test:

```bash
python scripts/validate_suite.py
```

The validator checks:

- only the root suite is exposed as `SKILL.md`
- all 16 workflows exist and use `WORKFLOW.md`
- manifest workflow IDs match the filesystem
- every workflow alias appears in the root router
- referenced local `references/` and `scripts/` files exist
- stale workflow names from older split-stage packages are absent
- root skill frontmatter follows the Codex `name` + `description` convention
- Zotero atlas coverage includes examples for current workflows and at least
  ten figure examples for `nnscholar4-1-paper-figure`
- Zotero figure screenshot assets exist and use reusable CC BY licensing

## Design Notes

This package intentionally separates three concepts:

- Codex skill registration: one suite skill
- Workflow modules: 16 internal NNScholar workflow folders
- UI buttons: desktop workflow presets that send `Workflow: <id>` payloads

That separation keeps the skill registry stable while preserving rich button
interaction in the desktop client.
