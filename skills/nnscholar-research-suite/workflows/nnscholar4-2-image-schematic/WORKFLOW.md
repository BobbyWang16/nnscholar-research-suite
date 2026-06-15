---
name: nnscholar4-2-image-schematic
description: Use when NNScholar needs to create scientific schematic figures, graphical abstracts, mechanism diagrams, workflow illustrations, model architecture visuals, clinical process diagrams, experimental route visuals, or concept diagrams using Image2 / gpt-image-2 image generation. Guides the user from upstream research outputs to a structured visual blueprint, Image2-ready prompt, generated figure, caption, and revision loop. Works across clinical medicine, biomedicine, AI/data science, materials/chemistry, education/psychology, economics/social science, humanities, and engineering.
---

# NNScholar 4.2 Image Schematic

This skill turns research plans, mechanisms, workflows, and conceptual relationships into publication-oriented schematic images using Image2 (`gpt-image-2`) via the built-in `image_gen` tool.

Version: `0.2.0`. Stage: `paper output / image schematic`. Legacy workflow alias: `$nnscholar4-2-image-schematic`, routed through `$nnscholar-research-suite`.

## NNScholar Unified Operating Standard

This skill follows the shared NNScholar contract. If older local wording conflicts with this section, this section wins.

### Naming and Invocation

- Keep the workflow id, folder name, and legacy alias as `nnscholar4-2-image-schematic` / `/nnscholar4-2-image-schematic`.
- Keep the title format as `NNScholar 4.2 Image Schematic`.
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

Do not jump directly to image generation. First create a scientific visual blueprint, then convert it into an Image2-ready prompt, then generate or iterate the image.

Image2 is good for polished schematic visuals, composition, visual metaphors, and graphical abstracts. It is less reliable for dense exact text, tiny labels, equations, or strict diagram geometry. For text-heavy figures, use short labels, numbered callouts, and a caption/legend outside the image.

## Boundary

Use this skill for:

- graphical abstract / visual summary;
- mechanism or pathway schematic;
- study workflow or experiment route illustration;
- model/pipeline architecture illustration;
- clinical diagnostic/treatment process illustration;
- materials synthesis and function schematic;
- education/psychology conceptual framework;
- economics/social-science identification logic illustration;
- humanities conceptual/corpus workflow illustration;
- engineering system/prototype/process schematic.

Do not use this skill for:

- data-driven charts from structured tables; use `nnscholar4-1-data-figure`;
- manuscript tables; use `nnscholar4-4-table-formatting`;
- exact journal flow diagrams with many labels/counts where Mermaid/SVG is safer, unless the user explicitly wants a polished raster version;
- official logos, real institutional branding, or copyrighted figure recreation.

## Image2 Policy

When actual image generation is requested, use the default built-in `image_gen` tool path from the `imagegen` skill. Treat this as the Image2 / `gpt-image-2` route.

- Do not use the older `scientific-schematics` Nano Banana/OpenRouter path unless the user explicitly asks for it.
- Do not use CLI fallback unless the user explicitly asks for CLI/API/model controls.
- If the image is for the project, save the final selected image under `figures/` and report the path.
- If exact text matters, keep in-image text minimal and provide a separate editable caption/label map.
- If the user provides a reference image, inspect it first when available and specify its role: style reference, layout reference, or edit target.

## Upstream Priority

Use local or conversation outputs in this order:

1. `nnscholar2-3-paper-architecture`: planned figure slots and story order.
2. `nnscholar2-4-flowchart-design`: route diagram, Mermaid flowchart, Figure 1 logic.
3. `nnscholar3-1-experiment-validation-plan`: experiment/validation steps and readouts.
4. `nnscholar2-2-ars-plan`: Aim/Route/Specification and protocol lock.
5. `nnscholar1-4-domain-expert-knowledge-base`: domain terms and accepted mechanisms.
6. `nnscholar4-1-data-figure`: any generated data figure context that must be visually aligned.
7. User-provided sketch, prompt, image, manuscript draft, or current request.

When files are not specified, search `references/`, `reference/`, `docs/`, `outputs/`, `figures/`, and `images/` for figure plans, Mermaid diagrams, graphical abstract notes, sketches, and manuscript architecture.

## Interactive Micro-Rounds

Ask at most 1-3 questions per round.

### Round 0: Visual Intake

Return a short card:

```text
Detected discipline / study family:
Intended figure type:
Scientific message:
Likely visual structure:
Image2 suitability:
Missing information:
Next questions:
```

If the request is vague, ask:

1. What should this image explain: mechanism, workflow, model architecture, study design, graphical abstract, or concept framework?
2. Which discipline or study family is this?
3. Should the output be a polished Image2 raster image, a Mermaid/SVG blueprint first, or both?

Use `references/discipline-schematic-atlas.md` if discipline-specific conventions are unclear.

### Round 1: Content and Accuracy Check

Inspect or request:

- required components/nodes;
- arrows or causal/process relationships;
- exact labels that must appear;
- what must not appear;
- target venue or style: journal, conference, poster, slide, grant, graphical abstract;
- orientation and aspect ratio: square, landscape, portrait, single-column, double-column;
- whether prior diagrams or figures should be visually consistent.

### Round 2: Visual Blueprint

Before Image2 generation, produce a concise blueprint:

```text
Figure ID:
Figure type:
Canvas / aspect ratio:
Panel layout:
Main visual objects:
Flow direction:
Required labels:
Color system:
Accuracy constraints:
Avoid:
Caption plan:
```

For text-heavy diagrams, convert labels to short terms or numbered callouts:

```text
In-image label: "1"
External legend: "1. External validation cohort with site-level calibration."
```

### Round 3: Image2 Prompt Package

Use `references/image2-prompt-template.md` to produce:

- final prompt;
- negative constraints;
- exact text/label policy;
- aspect ratio recommendation;
- post-generation review checklist.

If the user asks for direct generation and the blueprint is sufficient, call `image_gen` after producing the prompt package.

### Round 4: Generate and Save

When generating:

- call the built-in `image_gen` tool once for the first version;
- inspect the output for scientific accuracy, readable composition, label issues, and visual clutter;
- if the first version is close, do one targeted iteration rather than rewriting the whole prompt;
- save final project-bound files under:

```text
figures/schematic-YYYY-MM-DD-short-topic/
  schematic.png
  image2_prompt.md
  figure_caption.md
```

- Add a short downstream handoff for `nnscholar4-5-manuscript-drafting`: where the schematic belongs, what introductory or methods sentence should point to it, and which claims must stay outside the manuscript body unless supported elsewhere.

### Round 5: Caption and Revision Handoff

Always provide:

- figure title;
- manuscript caption;
- label map if labels are abbreviated or numbered;
- abbreviation definitions;
- visual legend for symbols, colors, arrows, modules, or numbered callouts;
- evidence boundary note: what is proven evidence, planned workflow, model assumption, or hypothesis;
- source/upstream note if the schematic is derived from 2.2 ARS, 2.4 flowchart, 3.1 validation plan, or uploaded references;
- what the image communicates;
- what it should not be used to claim;
- recommended edits for journal-ready polish.

Use `references/schematic-output-template.md` for a full report.

For downstream manuscript drafting, make sure `figure_caption.md` or the final report includes:

```text
4.5 handoff:
Manuscript placement:
Intro/Methods/Results insertion cue:
Caption-ready figure title:
Caption-ready legend:
Evidence boundary sentence:
Terms/abbreviations to reuse:
```

## Cross-Disciplinary Guardrails

- Clinical medicine: avoid implying causality from observational workflow; show patient journey, data sources, model, decision point, and validation separately.
- Basic biomedicine: distinguish hypothesis mechanism from experimentally proven mechanism; label cell/tissue/animal models clearly.
- AI/data science: show data flow, model modules, training/inference split, evaluation, and deployment; avoid impossible architecture details.
- Materials/chemistry: separate synthesis, characterization, mechanism, and application; do not invent molecular structures or crystal geometry.
- Education/psychology: show constructs, intervention, measurement, and outcome; avoid implying causality without design support.
- Economics/social science: distinguish treatment/exposure, identification logic, confounders, and outcome; do not depict descriptive correlation as causal proof.
- Humanities: show corpus/source selection, interpretive framework, coding/reading process, and argument structure.
- Engineering: label inputs, modules, signals/material/energy/data flow, operating conditions, and failure/safety points.
