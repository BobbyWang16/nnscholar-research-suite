# Companion Skill Bridge

Use this reference after selecting exactly one NNScholar workflow. It helps the
suite borrow stricter domain guardrails from co-installed specialist skills
without turning NNScholar into a loose bundle of unrelated tools.

## Operating Rule

- Keep the selected NNScholar workflow as the source of stage order, handoff,
  protocol lock, and artifact naming.
- Use companion skills only for domain-specific evidence, reporting standards,
  file handling, or venue-specific constraints.
- If a companion skill conflicts with a locked NNScholar upstream artifact, do
  not silently change the downstream output. Reopen the relevant NNScholar stage
  or mark the conflict as `needs author confirmation`.
- If the companion skill is not installed or available in the current Codex
  session, apply the fallback checkpoints in this file and state that the
  specialist skill was unavailable.

## Bridge Map

| Request signal | Prefer companion skill when available | Apply to NNScholar stages | Added checks |
|---|---|---|---|
| Radiology, medical imaging AI, radiomics, CT/MRI/PET/ultrasound, ROI, masks, segmentation, radiogenomics | `radiology-skills` and its focused modules such as `radiology-design`, `radiology-deep-learning`, `radiology-radiomics`, `radiology-stats`, `radiology-reporting`, `radiology-figure`, `radiology-journal`, `radiology-response` | 1.1-1.3, 2.1-2.4, 3.1, 4.1-4.6, 5.1-5.5 | patient-level split, center-held-out vs pooled validation, external validation definition, ROI/mask protocol, reader agreement, leakage, calibration, DCA, CLAIM/CLEAR/RQS/IBSI/TRIPOD+AI/STARD-AI, clinical-utility overclaim |
| Clinical, biomedical, translational, omics, medical paper reading | `medical-research-literature-reader-pro`, `medical-research-gap-finder`, `medical-research-algorithm-matcher`, `research-patient-completion` | 1.1-1.4, 2.1-2.2, 3.1, 4.5-4.6 | evidence-type classification, pseudo-gap rejection, verified algorithm papers, endpoint quality, ethics/privacy, cohort completeness, biological plausibility |
| Literature expansion, citation verification, claim evidence, systematic searching | `paper-search`, `literature-engineer`, `evidence-binder`, `evidence-auditor`, `nature-citation` | 1.2, 2.3, 4.5-4.6, 5.1-5.5 | verified DOI/PMID/arXiv/URL, provenance, dedupe, search strategy, citation-to-claim binding, no fabricated references |
| High-impact manuscript, Nature/CNS style, submission-grade figure, reviewer response | `nature-writing`, `nature-polishing`, `nature-figure`, `nature-data`, `nature-reviewer`, `nature-response`, `nature-paper2ppt` | 2.3, 4.1-4.6, 5.1-5.5 | claim ceiling, figure conclusion logic, data/code availability, reviewer-risk audit, point-by-point response discipline |
| Word, PDF, spreadsheet, slide deck, presentation, table or figure deliverable | `docx`, `pdf`, `xlsx`, `pptx`, `paper-slide-deck`, `radiology-paper2ppt` | 4.1-4.4, 4.5-4.6, 5.2-5.3 | format-specific parsing, layout/rendering checks, table integrity, export readiness, source manifest |

## Imaging AI Fallback Checkpoints

Use these even when `radiology-skills` is unavailable:

1. Identify disease, modality, task, population, endpoint, label source, centers,
   scanner variation, segmentation source, and intended clinical use.
2. Reject image-level, slice-level, or lesion-level random splits as
   patient-level validation unless patient grouping is explicitly preserved.
3. Do not call a pooled multicenter split external validation. Reserve external
   validation for center-, time-, institution-, or dataset-held-out testing.
4. Require metrics compatible with the task: ROC/AUC or PR/AUPRC, sensitivity,
   specificity, calibration, confidence intervals, DCA for clinical utility,
   Dice/HD95 for segmentation, reader agreement when readers or annotations are
   involved.
5. Keep SHAP, GradCAM, saliency, radiomics signatures, and radiogenomics
   associations as explanatory or associative evidence unless validated as a
   mechanism by independent experiments.
6. Check reporting standards: CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI,
   STARD-AI, CONSORT-AI, or SPIRIT-AI as applicable.

## Biomedical Fallback Checkpoints

1. Classify the evidence type before recommending a design: mechanistic,
   observational, interventional, diagnostic, prognostic, algorithmic, omics,
   review/meta-analysis, or translational.
2. Separate hypothesis generation from validation. Do not let exploratory
   omics, public database mining, or retrospective association become causal
   evidence without independent validation.
3. Ask whether samples, cohorts, assays, databases, controls, and endpoints are
   actually available. Mark unavailable resources as blockers.
4. Preserve ethical, consent, privacy, biosafety, animal, and clinical trial
   requirements as `needs verification` unless source documents are supplied.

## Evidence and Citation Fallback Checkpoints

1. Current literature, venue rules, fees, deadlines, impact metrics, guidelines,
   and standards require live verification before final factual claims.
2. Every formal citation recommendation needs a stable identifier or source link.
3. Keep a source manifest when producing manuscripts, evidence matrices,
   submission packages, or reviewer responses.
4. If evidence is missing, produce a search plan or placeholder list, not a
   fabricated citation.

## Handoff Addendum

When a bridge influenced the output, append these fields to the NNScholar Suite
Handoff:

```text
Companion skill bridge used:
Specialist checks applied:
Conflicts with locked upstream artifacts:
Items still needing specialist verification:
```
