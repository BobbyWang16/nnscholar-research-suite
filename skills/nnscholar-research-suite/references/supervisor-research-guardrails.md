# Supervisor Research Guardrails

Use this file as an internal NNScholar reference when the project is an
AI/data-science, database, systems, ML, NLP, benchmark/evaluation, or technical
CS paper, or when the user asks for advisor-style critique, top-conference
paper logic, figure quality, AI-assisted research workflow, or pre-submission
review.

Keep the active NNScholar workflow as the stage authority. These guardrails add
reviewer-style checks; they do not replace NNScholar stage order, upstream
protocol locks, evidence boundaries, or handoff contracts.

## Trigger Map

| Request signal | Apply guardrail |
|---|---|
| idea viability, novelty check, feasibility, "is this worth pursuing" | Idea Evaluation Gate |
| paper skeleton, technical paper logic chain, advisor meeting template | Technical Paper Logic Gate |
| benchmark/evaluation paper, dataset paper, evaluation taxonomy | Benchmark Paper Gate |
| Introduction logic, running example, contribution alignment | Introduction Gate |
| motivated example, solution overview, experiment figure, chart choice | Core Figure Gate |
| final paper review, LaTeX check, AI-tone scan, before deadline | Pre-Submission Review Gate |
| how to use AI for research, Vibe Coding/Figure/Writing, tool choice | AI Collaboration Integrity Gate |

## Idea Evaluation Gate

Use in 1.1, 1.3, 2.1, and 2.2 before committing months of work.

1. Position the idea as Novel Problem, Novel Method, New Setting, Benchmark, or
   Application/Validation.
2. Run a fatal-flaws audit before scoring:
   - already solved or dominated by a recent benchmark/method;
   - novelty depends only on swapping model names or datasets;
   - no accessible data, labels, samples, compute, or evaluation route;
   - contribution cannot be falsified or measured;
   - claim requires causal/mechanistic evidence the design cannot provide.
3. Score the strongest contribution dimensions from 1-10:
   - Higher: effectiveness, accuracy, quality, validity.
   - Faster: efficiency, latency, workflow acceleration.
   - Stronger: robustness, generalization, noise tolerance.
   - Cheaper: lower annotation, data, compute, or operational cost.
   - Broader: cross-domain transfer, unification, new setting coverage.
4. Check lifecycle and capability fit against user resources: hours, timeline,
   compute, data access, engineering skill, collaborator support.
5. Probe paradigm-shift potential:
   - hidden assumption challenged;
   - field-level pain point addressed;
   - technology-cycle shift makes the route newly feasible;
   - solving it would meaningfully change the field.
6. Verdict:
   - Strong Accept: at least two high dimensions, no fatal flaw, feasible route.
   - Accept with Revisions: promising but needs scope, evidence, or route repair.
   - Reject and Pivot: critical flaw or unfixable resource/lifecycle mismatch.

## Technical Paper Logic Gate

Use in 2.3 and 4.3 for technical CS papers.

1. Choose one paper positioning:
   - Technique Paper: key idea/mechanism is the main contribution.
   - New Problem/Setting Paper: problem definition or setting is the contribution.
2. Fill the logic chain:
   - background and motivation;
   - at most three specific limitations;
   - one-sentence key idea or goal;
   - at most three challenges derived from implementing the idea;
   - one methodology module per challenge;
   - three or four contributions mapped to manuscript sections.
3. Run four consistency checks:
   - limitations -> key idea/goal;
   - key idea/goal -> challenges;
   - challenges -> methodology modules;
   - methodology modules/results -> contributions.
4. Mark any break as CRITICAL and send the user back to 2.2 or 2.3 before
   drafting prose.

## Benchmark Paper Gate

Use when the work is a benchmark, evaluation, dataset, leaderboard, or
capability-boundary paper.

1. Audit five pillars:
   - Research Gap: which evaluation dimension is missing?
   - Construction Pipeline: how is data built with quality control?
   - Evaluation Framework: what metrics, tiers, rubrics, or taxonomies diagnose
     the gap?
   - Empirical Findings: what capability boundaries or failure modes are shown?
   - Companion Method: optional method/model/tool that demonstrates actionability.
2. Build the benchmark introduction chain:
   - background plus running example;
   - existing benchmark limitations, no more than three;
   - research questions;
   - design considerations;
   - benchmark proposal;
   - contributions.
3. Require Section 2-7 planning:
   - task/design goals;
   - construction pipeline;
   - optional companion method;
   - experiments by RQ;
   - discussion/research opportunities;
   - related benchmark comparison.
4. Do not let a benchmark paper read like a method paper unless the companion
   method is genuinely central and separately validated.

## Introduction Gate

Use in 2.3 and 4.3 when Introduction logic matters.

1. Use a six-part outline:
   - background and running example;
   - prior-work limitations;
   - problem essence and goal;
   - key challenges;
   - solution overview;
   - contributions.
2. Keep limitations and challenges at no more than three each.
3. Ensure the running example in paragraph 1 reappears in the solution overview,
   case study, or result narrative.
4. Map each challenge to one module or result block.
5. Map each contribution to a section number and avoid vague claims such as
   "comprehensive experiments" unless the specific evidence is named.

## Core Figure Gate

Use in 2.3 and canonical Stage 4 figure/table/writing workflows.

1. Classify the figure:
   - Motivated Example: shows the concrete failure or gap readers should care
     about.
   - Solution Overview: explains method modules and data/control flow.
   - Experimental Results: supports a claim with measured data.
   - Benchmark Construction/Evaluation: shows pipeline, taxonomy, or RQ results.
2. Select chart/layout based on the claim, not aesthetics.
3. Require concrete labels; avoid placeholder module names.
4. Audit:
   - vector-first export for diagrams and plots;
   - readable fonts after scaling;
   - color-blind-safe palette and non-color encoding;
   - honest axes and uncertainty;
   - self-contained caption with the main finding in the first sentence;
   - no chartjunk or misleading 3D effects.

## Pre-Submission Review Gate

Use in 4.3, 5.1, 5.2, and 5.5 within one week of submission or after a major
rewrite.

Review findings must be severity-tagged:

- CRITICAL: blocks submission, such as broken contribution-method-result logic,
  missing baseline, missing figure/table evidence, page-limit violation, or
  unsupported claim.
- MAJOR: likely reviewer complaint, such as weak topic sentences, unclear
  running example, inconsistent terminology, raster final figure, incomplete
  artifact checklist, or repeated AI-tone wording.
- MINOR: polish, grammar, local phrasing, small formatting issues.

Check:

1. Macro logic: Introduction, contributions, methods, results, and claims align.
2. Writing details: topic sentences, paragraph length, transitions, redundancy.
3. Grammar and style: articles, agreement, tense, long sentences, Chinglish.
4. LaTeX/formatting: equations, labels, citations, references, figure/table
   captions, anonymity, page limits.
5. Figure quality: vector/raster, font size, caption, axis honesty, consistency.
6. AI-tone scan: flag repeated inflated wording such as innovative,
   revolutionary, transformative, superior, unprecedented, breakthrough,
   remarkable, notably, underscores, paves the way, or similar hype language.
7. Em dash policy: replace sentence-connector em dashes if the project or venue
   style forbids them.

Every CRITICAL finding needs a concrete fix suggestion.

## AI Collaboration Integrity Gate

Use whenever NNScholar plans AI-assisted coding, plotting, figure generation, or
writing.

1. AI may accelerate literature organization, code/debugging, figure rendering,
   formatting, and language polish.
2. The researcher owns research questions, core ideas, experimental design,
   technical path, conclusions, and novelty claims.
3. Verify every AI-generated passage against actual evidence, experiments, and
   project files.
4. Do not fabricate citations, data, results, approvals, or reviewer outcomes.
5. Respect venue or institution AI-disclosure rules; mark as `needs verification`
   if unknown.
6. Keep an audit trail for generated code, plots, figures, manuscripts, and
   submission assets when they support claims.

## Handoff Addendum

When these guardrails changed the output, add to the NNScholar handoff:

```text
Supervisor guardrails used:
Gates applied:
Critical issues found:
Revisions required before next stage:
Items needing author verification:
```
