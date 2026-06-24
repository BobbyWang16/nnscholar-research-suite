# NNScholar Research Suite

Codex-native packaging of the NNScholar academic research workflow suite.

This repository exposes one installable Codex skill:

```text
skills/nnscholar-research-suite/
  SKILL.md
  manifest.json
  agents/openai.yaml
  workflows/
    nnscholar1-1-question-mining/
      WORKFLOW.md
      references/
      agents/
    ...
```

The 20 NNScholar workflow modules are kept under `workflows/` and use
`WORKFLOW.md` instead of `SKILL.md`. This keeps Codex registration clean: users
see one skill, `$nnscholar-research-suite`, while the desktop UI can still show
20 task buttons.

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

Workflow: nnscholar1-1-question-mining
User request:
Help me identify research gaps in this topic.
```

Legacy aliases are also routed by the root skill:

```text
/nnscholar4-5-manuscript-drafting draft a manuscript from these notes
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
| 2.4 | `nnscholar2-4-flowchart-design` |
| 3.1 | `nnscholar3-1-experiment-validation-plan` |
| 4.1 | `nnscholar4-1-data-figure` |
| 4.2 | `nnscholar4-2-image-schematic` |
| 4.3 | `nnscholar4-3-figure-assembly` |
| 4.4 | `nnscholar4-4-table-formatting` |
| 4.5 | `nnscholar4-5-manuscript-drafting` |
| 4.6 | `nnscholar4-6-manuscript-polishing` |
| 5.1 | `nnscholar5-1-journal-conference-recommendation` |
| 5.2 | `nnscholar5-2-submission-finalization` |
| 5.3 | `nnscholar5-3-submission-portal-workflow` |
| 5.4 | `nnscholar5-4-cover-letter` |
| 5.5 | `nnscholar5-5-reviewer-response` |

## Specialist Bridge

The suite now includes a lightweight companion-skill bridge:

```text
skills/nnscholar-research-suite/references/companion-skill-bridge.md
```

NNScholar remains the stage orchestrator, but the bridge tells Codex when to
borrow stricter checks from co-installed specialist skills. Examples:

- `radiology-skills` for medical imaging AI, radiomics, validation leakage,
  ROI/masks, CLAIM/CLEAR/RQS/IBSI/TRIPOD+AI/STARD-AI, journal fit, and reviewer
  response.
- `medical-research-*`, `paper-search`, `literature-engineer`, and
  `evidence-binder` for biomedical evidence appraisal, verified literature,
  algorithm matching, and claim-to-source binding.
- `nature-*` skills for high-impact manuscript writing, figure logic,
  citations, submission package checks, and reviewer response discipline.
- `docx`, `pdf`, `xlsx`, and `pptx` skills for file-format deliverables.

The bridge is optional at runtime: if a companion skill is not installed, Codex
falls back to the checkpoints in the reference file and marks specialist
verification as needed.

## Zotero Example Atlas

The suite also includes a copyright-safe example atlas derived from the user's
Zotero library:

```text
skills/nnscholar-research-suite/references/zotero-example-atlas.md
```

It provides at least five structural example cards for every NNScholar workflow
and 12 chart/figure-generation examples for `nnscholar4-1-data-figure`. The
cards preserve Zotero keys, venue names, DOI/URLs, and reusable structure
patterns, but they do not copy source figures, captions, tables, or long article
text.

For figure-layout inspiration, the suite also bundles 12 low-resolution CC BY
visual reference crops, a Markdown gallery that directly embeds them, and a
manifest for automation:

```text
skills/nnscholar-research-suite/references/figure-screenshot-gallery.md
skills/nnscholar-research-suite/assets/zotero-figure-examples/manifest.json
```

Use these screenshots only as layout references for generating original figures,
and preserve source/license attribution in any project handoff. Zotero keys are
kept only as provenance labels; another computer does not need the user's Zotero
library to inspect the bundled reference images.

## Validation

Run the no-dependency structure test:

```bash
python scripts/validate_suite.py
```

The validator checks:

- only the root suite is exposed as `SKILL.md`
- all 20 workflows exist and use `WORKFLOW.md`
- manifest workflow IDs match the filesystem
- every workflow alias appears in the root router
- referenced local `references/` and `scripts/` files exist
- stale workflow names are absent
- root skill frontmatter follows the Codex `name` + `description` convention
- Zotero atlas coverage includes at least five examples per workflow and at
  least ten figure examples for data-figure generation
- Zotero figure screenshot assets are directly embedded in a portable gallery
  and use reusable CC BY licensing

## Design Notes

This package intentionally separates three concepts:

- Codex skill registration: one suite skill
- Workflow modules: 20 internal NNScholar workflow folders
- UI buttons: desktop workflow presets that send `Workflow: <id>` payloads

That separation keeps the skill registry stable while preserving rich button
interaction in the desktop client.
