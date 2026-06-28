# Zotero Top-Journal Example Atlas

Use this atlas when the user asks for reference examples, figure/table
inspiration, manuscript structure, journal-style prose, or "make it look like a
top-journal paper." The examples below are derived from the user's Zotero
metadata and are written as original structural pattern cards. Do not copy
figures, captions, tables, or long text from the source papers into outputs or
into this repository.

## Copyright-Safe Use

- Treat each source as a pointer and design pattern, not as reusable content.
- Cite the Zotero key, title, venue, year, and DOI/URL when a source directly
  influences a generated structure.
- Generate original diagrams, captions, section plans, and prose.
- If an actual source figure is required, verify its license first. Otherwise
  link to the article and describe the reusable pattern in your own words.
- For bundled screenshot assets, use only the crops listed in
  `assets/zotero-figure-examples/manifest.json`; they were selected from
  sources recorded as CC BY 4.0 or equivalent. Treat them as low-resolution
  visual references, not manuscript-ready panels.

## Figure Screenshot Assets

When a figure workflow needs concrete visual layout cues, inspect the manifest
first, then open only the JPGs that match the requested figure type. Each asset
keeps a Zotero key, source DOI, figure label, pattern tag, and license field.

- `figref-01-radimagenet-workflow`: S04, Figure 1, dataset curation +
  pretraining + transfer-learning workflow, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-01-radimagenet-workflow.jpg`.
- `figref-02-radimagenet-performance`: S04, Figure 3, small-dataset
  performance comparison with uncertainty, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-02-radimagenet-performance.jpg`.
- `figref-03-tme-study-design`: S13, Figure 1, cohort design with CT/IHC
  linkage and validation, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-03-tme-study-design.jpg`.
- `figref-04-tme-model-performance`: S13, Figure 2, ROC/distribution/confusion
  matrix performance panel, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-04-tme-model-performance.jpg`.
- `figref-05-mr-deltanet-design`: S15, Figure 1, longitudinal MRI study
  design and biology-interpretation route, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-05-mr-deltanet-design.jpg`.
- `figref-06-mr-deltanet-performance`: S15, Figure 3, multi-cohort ROC and
  score-distribution validation, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-06-mr-deltanet-performance.jpg`.
- `figref-07-flare-overall-design`: S16, Figure 1, multimodal
  missing-modality foundation-model design, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-07-flare-overall-design.jpg`.
- `figref-08-flare-framework`: S16, Figure 3, multi-branch model framework with
  modality-specific encoders, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-08-flare-framework.jpg`.
- `figref-09-crcfound-overview`: S17, Figure 1, 3D CT foundation-model
  pretraining and downstream tasks, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-09-crcfound-overview.jpg`.
- `figref-10-crcfound-performance`: S17, Figure 2, cross-validation
  performance bars plus ROC comparison, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-10-crcfound-performance.jpg`.
- `figref-11-lung-pathology-subtyping`: S26, Figure 4, diagnostic downstream
  algorithm development and validation, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-11-lung-pathology-subtyping.jpg`.
- `figref-12-lung-pathology-prognostic`: S26, Figure 6, AI-derived prognostic
  parameter quantification with visual examples, `CC BY 4.0`,
  `assets/zotero-figure-examples/figref-12-lung-pathology-prognostic.jpg`.

## Source Bank From Zotero

- S01 `MDABN3I7`: Tan et al., "Characterization of tumour heterogeneity through segmentation-free representation learning on multiplexed imaging data," Nature Biomedical Engineering, 2025, DOI `10.1038/s41551-025-01348-1`.
- S02 `JSTRRMB5`: Ding et al., "A multimodal whole-slide foundation model for pathology," Nature Medicine, 2025, DOI `10.1038/s41591-025-03982-3`.
- S03 `B8YSYQF3`: Gao et al., "A lung CT vision foundation model facilitating disease diagnosis and medical imaging," Nature Communications, 2025, DOI `10.1038/s41467-025-66620-z`.
- S04 `MEHDNDLE`: Mei et al., "RadImageNet: An Open Radiologic Deep Learning Research Dataset for Effective Transfer Learning," Radiology: Artificial Intelligence, 2022, DOI `10.1148/ryai.210315`.
- S05 `NZYTX36P`: Kou et al., "A Serial MRI-based Deep Learning Model to Predict Survival in Patients with Locoregionally Advanced Nasopharyngeal Carcinoma," Radiology: Artificial Intelligence, 2025, DOI `10.1148/ryai.230544`.
- S06 `LLFQ54SG`: Prior et al., "Identification of Precise 3D CT Radiomics for Habitat Computation by Machine Learning in Cancer," Radiology: Artificial Intelligence, 2024, DOI `10.1148/ryai.230118`.
- S07 `EU7J4NW3`: Gilad et al., "Radiomics-based Machine Learning Prediction of Neoadjuvant Chemotherapy Response in Breast Cancer Using Physiologically Decomposed Diffusion-weighted MRI," Radiology: Imaging Cancer, 2025, DOI `10.1148/rycan.240312`.
- S08 `QGYBDL8K`: "Class imbalance on medical image classification: towards better evaluation practices for discrimination and calibration performance," European Radiology, 2024, DOI `10.1007/s00330-024-10834-0`.
- S09 `QUHBW6ZM`: "Association of Machine Learning-Based Assessment of Tumor-Infiltrating Lymphocytes on Standard Histologic Images With Outcomes of Immunotherapy in Patients With NSCLC," JAMA Oncology, 2023, DOI `10.1001/jamaoncol.2022.4933`.
- S10 `ZTSPKCPQ`: "A Structured Tumor-Immune Microenvironment in Triple Negative Breast Cancer Revealed by Multiplexed Ion Beam Imaging," Cell, 2018, DOI `10.1016/j.cell.2018.08.039`.
- S11 `AHWV84VV`: "Artificial intelligence for multimodal data integration in oncology," Cancer Cell, 2022, DOI `10.1016/j.ccell.2022.09.012`.
- S12 `CWTDFQ74`: "Artificial intelligence for clinical oncology," Cancer Cell, 2021, DOI `10.1016/j.ccell.2021.04.002`.
- S13 `BJJT2VUD`: "Non-invasive tumor microenvironment evaluation and treatment response prediction in gastric cancer using deep learning radiomics," Cell Reports Medicine, 2023, DOI `10.1016/j.xcrm.2023.101146`.
- S14 `R9FH59H8`: "Spatially aware deep learning reveals tumor heterogeneity patterns that encode distinct kidney cancer states," Cell Reports Medicine, 2023, DOI `10.1016/j.xcrm.2023.101189`.
- S15 `VH3RG3I7`: "MR-DELTAnet: A Longitudinal MRI-Transformer Model Predicting Pathological Complete Response and Revealing Immune Microenvironment via scRNA-seq in Locally Advanced Rectal Cancer," Advanced Science, 2025, DOI `10.1002/advs.202517721`.
- S16 `VM9UW7QT`: "Foundation Model-Enabled Multimodal Deep Learning for Prognostic Prediction in Colorectal Cancer with Incomplete Modalities," Advanced Science, 2026, DOI `10.1002/advs.202510931`.
- S17 `5FWICZ2D`: "CRCFound: A Colorectal Cancer CT Image Foundation Model Based on Self-Supervised Learning," Advanced Science, 2025, DOI `10.1002/advs.202407339`.
- S18 `ZXG7C7Q7`: "Survival Prediction via Hierarchical Multimodal Co-Attention Transformer: A Computational Histology-Radiology Solution," IEEE Transactions on Medical Imaging, 2023, DOI `10.1109/TMI.2023.3263010`.
- S19 `ST9NKPTX`: "3DSAM-adapter: Holistic adaptation of SAM from 2D to 3D for promptable tumor segmentation," Medical Image Analysis, 2024, DOI `10.1016/j.media.2024.103324`.
- S20 `MDQGNJ2K`: "Hover-Net: Simultaneous segmentation and classification of nuclei in multi-tissue histology images," Medical Image Analysis, 2019, DOI `10.1016/j.media.2019.101563`.
- S21 `JWEG6XW6`: "Whole-cell segmentation of tissue images with human-level performance using large-scale data annotation and deep learning," Nature Biotechnology, 2022.
- S22 `VFLKJKAH`: "TotalSegmentator: Robust Segmentation of 104 Anatomic Structures in CT Images," Radiology: Artificial Intelligence, 2023, DOI `10.1148/ryai.230024`.
- S23 `QDBT4GC4`: "HGMSurvNet: A two-stage hypergraph learning network for multimodal cancer survival prediction," Medical Image Analysis, 2025, DOI `10.1016/j.media.2025.103661`.
- S24 `2EI7MG9I`: "A multimodal synergistic model for personalized neoadjuvant immunochemotherapy in esophageal cancer," Cell Reports Medicine, 2025, DOI `10.1016/j.xcrm.2025.102479`.
- S25 `EHQQKU8P`: "Interpretable multi-modal artificial intelligence model for predicting gastric cancer response to neoadjuvant chemotherapy," Cell Reports Medicine, 2024, DOI `10.1016/j.xcrm.2024.101848`.
- S26 `3H2VPXX7`: "Next-generation lung cancer pathology: Development and validation of diagnostic and prognostic algorithms," Cell Reports Medicine, 2024, DOI `10.1016/j.xcrm.2024.101697`.
- S27 `IT73VATY`: "AI-enabled molecular phenotyping and prognostic predictions in lung cancer through multimodal clinical information integration," Cell Reports Medicine, 2025, DOI `10.1016/j.xcrm.2025.102216`.
- S28 `YYMFANQ8`: "Pan-cancer analysis of spatial transcriptomics reveals heterogeneous tumor spatial microenvironment," Cell Reports Medicine, 2026, DOI `10.1016/j.xcrm.2026.102751`.
- S29 `VWBGI8WD`: "Pan-cancer spatial characterization of key immune biomarkers in the tumor microenvironment," Cell Reports Medicine, 2025, DOI `10.1016/j.xcrm.2025.102418`.
- S30 `9LMKACQU`: "Radiomics-Based Unsupervised Clustering Identifies Subtypes Associated With Prognosis and Immune Microenvironment in Clear Cell Renal Cell Carcinoma," Advanced Science, 2025, DOI `10.1002/advs.202506165`.
- S31 `NXPGDSKN`: "Longitudinal MRI-Driven Multi-Modality Approach for Predicting Pathological Complete Response and B Cell Infiltration in Breast Cancer," Advanced Science, 2025, DOI `10.1002/advs.202413702`.
- S32 `TTPCZJ2I`: "Noninvasive Characterization of Tumor Heterogeneity in HNSCC: From Clinical Utility to Biological Correlates," Advanced Science, 2026, DOI `10.1002/advs.75780`.
- S33 `NWJ4GKAF`: "Polarity Prompting Vision Foundation Models for Pathology Image Analysis," IEEE Transactions on Medical Imaging, 2025, DOI `10.1109/TMI.2025.3578492`.

## Workflow Example Cards

### nnscholar1-1-question-mining

- Example 1: Use S11 + S12 to mine a broad AI-oncology topic into a sharper gap: "multimodal integration exists, but which clinical decision point lacks validated evidence?" Output a gap table with decision point, missing modality, and validation barrier.
- Example 2: Use S01 + S10 to turn tumor heterogeneity into questions by scale: cell neighborhood, tissue habitat, patient-level outcome, and treatment response. Reject vague "heterogeneity is important" questions.
- Example 3: Use S04 + S03 to mine foundation-model questions around transferability: pretraining data, target modality, out-of-distribution center, and task-specific finetuning.
- Example 4: Use S08 to turn "class imbalance" into methodological questions about discrimination, calibration, confidence intervals, and clinically meaningful thresholds.
- Example 5: Use S15 + S31 to mine longitudinal imaging questions: what changes over time, what biological signal it may reflect, and what validation would distinguish imaging correlation from mechanism.

### nnscholar1-2-literature-searching

- Example 1: Use S04 as the seed for dataset/pretraining searches; expand by terms `radiologic deep learning dataset`, `transfer learning`, `external validation`, and modality-specific names.
- Example 2: Use S06 + S07 as radiomics search anchors; split search strings into habitat radiomics, delta radiomics, DWI MRI, CT, treatment response, and cancer type.
- Example 3: Use S02 + S33 for pathology foundation-model searches; capture model family, supervision, pretraining corpus, WSI task, and external dataset.
- Example 4: Use S09 + S13 + S25 to collect clinical-response prediction papers; extract cohort, treatment, outcome, modality, comparator, and validation level.
- Example 5: Use S08 as the methods-quality anchor; add search terms for `calibration`, `decision curve`, `class imbalance`, `threshold`, and `confidence interval`.

### nnscholar1-3-hypothesis-generation

- Example 1: From S15, frame a testable hypothesis linking longitudinal MRI representation changes to immune-cell infiltration; require independent biological validation before mechanism claims.
- Example 2: From S01, hypothesize that segmentation-free multiplex-image embeddings capture heterogeneity missed by hand-drawn regions; test with outcome association and robustness checks.
- Example 3: From S18 + S23, hypothesize that histology-radiology co-attention improves survival prediction only when both modalities add nonredundant information; test ablation and missing-modality stress.
- Example 4: From S08, hypothesize that models optimized on imbalanced data may show inflated AUC but poor calibration; test with calibration curves, PR metrics, and threshold analysis.
- Example 5: From S06, hypothesize that habitat-level radiomics produces more stable phenotypes than whole-tumor averages; test across centers, scanner settings, and perturbation analysis.

### nnscholar1-4-domain-expert-knowledge-base

- Example 1: Build an imaging-AI KB from S04, S05, S06, and S08 with fields for modality, label, split, validation, metrics, calibration, and clinical endpoint.
- Example 2: Build a pathology-AI KB from S02, S20, S21, and S33 with fields for WSI tiling, cell segmentation, foundation-model pretraining, and slide-level aggregation.
- Example 3: Build a radiogenomics KB from S15, S30, S31, and S32 with fields for imaging phenotype, omics assay, cell type/pathway, validation, and causal boundary.
- Example 4: Build a clinical oncology AI KB from S09, S13, S24, and S25 with fields for treatment, response endpoint, cohort, comparator, and decision utility.
- Example 5: Build a reporting-quality KB from S08, S22, and S19 with fields for segmentation label source, class imbalance, external validation, segmentation metric, and reproducibility artifact.

### nnscholar2-1-research-planning

- Example 1: Plan a foundation-model project using S03/S04/S17: data inventory, pretraining/fine-tuning route, external test set, baseline models, and compute risk.
- Example 2: Plan a longitudinal MRI project using S05/S15/S31: timepoint definition, missing scans, outcome window, model comparison, and biological follow-up.
- Example 3: Plan a radiomics-response project using S06/S07/S13: ROI protocol, feature stability, model selection, calibration, DCA, and external validation.
- Example 4: Plan a pathology-cell project using S20/S21/S33: annotation budget, cell/nucleus labels, segmentation metric, slide-level aggregation, and stain/domain shift.
- Example 5: Plan a multimodal survival project using S18/S23/S16: modality availability, missing-modality handling, survival endpoint, cross-validation, and interpretability.

### nnscholar2-2-ars-plan

- Example 1: ARS from S08: Aim tests class-imbalance-aware evaluation; Route compares AUC, PR, calibration, and threshold utility; Specification requires stratified patient-level splits.
- Example 2: ARS from S05: Aim predicts survival from serial MRI; Route encodes timepoint-aware imaging; Specification locks endpoint window, censoring rule, and external validation.
- Example 3: ARS from S19/S22: Aim validates segmentation generalization; Route tests promptable or multi-organ segmentation; Specification locks Dice, HD95, organ/lesion categories, and QC review.
- Example 4: ARS from S15/S31: Aim links longitudinal imaging response to immune biology; Route integrates imaging model with scRNA-seq or immune features; Specification marks mechanism claims as associative unless validated.
- Example 5: ARS from S24/S25: Aim predicts neoadjuvant therapy response; Route fuses clinical, imaging, and pathology features; Specification locks comparator, endpoint, calibration, and decision curve.

### nnscholar2-3-paper-architecture

- Example 1: S02-style architecture: unmet need -> foundation model -> broad validation tasks -> external cohorts -> interpretability/limitations -> clinical boundary.
- Example 2: S05-style architecture: clinical survival problem -> serial imaging design -> model development -> validation -> risk stratification -> clinical interpretation.
- Example 3: S13-style architecture: noninvasive TME claim -> radiomics/deep-learning route -> treatment response outcome -> biology association -> translational caution.
- Example 4: S20-style architecture: segmentation problem -> annotation and benchmark -> model design -> quantitative segmentation results -> error analysis -> reusable tool.
- Example 5: S08-style architecture: evaluation problem -> imbalanced-data pitfalls -> metric comparison -> calibration/threshold results -> recommendations for future studies.

### nnscholar2-2-ars-plan experimental flowcharts

- Example 1: S04-inspired dataset flow: source datasets -> modality filtering -> preprocessing -> pretraining -> task-specific fine-tuning -> external tests.
- Example 2: S05-inspired longitudinal flow: baseline MRI -> follow-up MRI -> temporal encoder -> survival model -> risk groups -> Kaplan-Meier validation.
- Example 3: S06-inspired habitat radiomics flow: CT volume -> tumor mask -> habitat computation -> feature extraction -> model selection -> outcome association.
- Example 4: S19-inspired segmentation flow: 2D foundation model -> 3D adaptation -> prompt/label inputs -> segmentation output -> Dice/HD95 evaluation.
- Example 5: S18-inspired multimodal flow: radiology branch + histology branch + clinical covariates -> co-attention fusion -> survival prediction -> ablation.

### nnscholar2-2-ars-plan validation examples

- Example 1: Validate S08-like evaluation claims by comparing AUC, AUPRC, calibration slope, Brier score, and DCA under multiple imbalance ratios.
- Example 2: Validate S06-like radiomics habitat stability through center-held-out testing, scanner perturbation, mask perturbation, and feature reproducibility.
- Example 3: Validate S15-like imaging-immune links with independent immune assays or external transcriptomic cohorts; keep mechanism language bounded.
- Example 4: Validate S19/S22 segmentation models with organ/lesion-wise Dice, HD95, failure-case review, and reader adjudication for ambiguous boundaries.
- Example 5: Validate S02/S03 foundation models with task transfer, low-label settings, OOD center testing, and comparison with strong supervised baselines.

### nnscholar3-1-experiment-validation-plan

- Example 1: Execute an S08-style evaluation audit by running discrimination, calibration, threshold, subgroup, and class-imbalance checks from a locked protocol.
- Example 2: Execute an S06-style radiomics validation loop by tracking mask perturbation, scanner sensitivity, held-out center performance, and reproducibility artifacts.
- Example 3: Execute an S15/S31-style imaging-biology validation loop by separating imaging model performance, immune-assay association, and mechanism-language limits.
- Example 4: Execute an S19/S22-style segmentation validation loop by producing organ/lesion metrics, failure-case panels, annotation notes, and reader-QC decisions.
- Example 5: Execute an S02/S03/S17-style foundation-model benchmark loop by logging transfer tasks, low-label settings, OOD tests, baselines, ablations, and release-readiness gaps.

### nnscholar4-1-paper-figure: data figures

- Figure example 1: S04 pretraining-transfer workflow panel; visual reference
  `figref-01-radimagenet-workflow`. Show source datasets -> modality filtering
  -> pretraining -> downstream tasks -> external tests as a left-to-right
  reproducible pipeline.
- Figure example 2: S04 small-dataset performance panel; visual reference
  `figref-02-radimagenet-performance`. Show target task on x-axis, performance
  delta on y-axis, baseline vs pretrained model, external-test markers, and CI
  whiskers.
- Figure example 3: S13 noninvasive TME study-design panel; visual reference
  `figref-03-tme-study-design`. Combine cohort flow, CT/IHC linkage,
  train/validation/test splits, and the clinical response endpoint.
- Figure example 4: S13 model-performance panel; visual reference
  `figref-04-tme-model-performance`. Pair ROC/AUPRC with score distributions,
  confusion-matrix or threshold views, and a concise validation summary.
- Figure example 5: S15 longitudinal MRI + biology overview; visual reference
  `figref-05-mr-deltanet-design`. Align timepoint MRI inputs, transformer
  feature extraction, pCR prediction, and immune microenvironment interpretation.
- Figure example 6: S15 multi-cohort validation figure; visual reference
  `figref-06-mr-deltanet-performance`. Use cohort-faceted ROC, score
  distribution, calibration, and clinically meaningful subgroup comparison.
- Figure example 7: S16 incomplete-modality multimodal design; visual reference
  `figref-07-flare-overall-design`. Show available/missing modalities, fusion
  route, survival endpoint, and missing-modality stress tests.
- Figure example 8: S16 model-framework schematic; visual reference
  `figref-08-flare-framework`. Use parallel modality encoders, shared latent
  representation, prediction heads, and ablation callouts.
- Figure example 9: S17 3D CT foundation-model overview; visual reference
  `figref-09-crcfound-overview`. Show self-supervised pretraining, downstream
  fine-tuning tasks, cohort partitions, and clinical validation boundary.
- Figure example 10: S17 performance comparison panel; visual reference
  `figref-10-crcfound-performance`. Combine cross-validation bars, ROC curves,
  confidence intervals, and baseline/foundation-model contrasts.
- Figure example 11: S26 pathology diagnostic algorithm panel; visual reference
  `figref-11-lung-pathology-subtyping`. Show slide or region examples,
  diagnostic labels, model outputs, validation cohorts, and error cases.
- Figure example 12: S26 pathology prognostic-feature panel; visual reference
  `figref-12-lung-pathology-prognostic`. Link AI-derived quantitative features,
  representative visual examples, survival stratification, and model evidence.

### nnscholar4-1-paper-figure: scientific schematics

- Example 1: S02-inspired foundation-model schematic: WSI patches -> multimodal encoder -> task heads -> validation cohorts -> interpretability panel.
- Example 2: S03/S17 CT foundation-model schematic: CT volume -> self-supervised pretraining -> fine-tuning tasks -> OOD validation -> clinical use boundary.
- Example 3: S15/S31 radiogenomics schematic: longitudinal MRI -> transformer features -> immune-cell/pathway association -> validation layer -> claim boundary.
- Example 4: S19/S22 segmentation schematic: prompt or anatomical prior -> 3D adaptation -> mask output -> QC loop -> metric dashboard.
- Example 5: S10/S28 spatial biology schematic: tissue image -> cell segmentation -> spatial neighborhoods -> immune-marker map -> outcome association.

### nnscholar4-1-paper-figure: multi-panel assembly

- Example 1: Assemble a 5-panel imaging-AI figure from S05: cohort flow, model overview, ROC/time-dependent ROC, KM risk groups, and calibration.
- Example 2: Assemble a 6-panel radiomics habitat figure from S06/S13: image, ROI, habitat map, feature stability, model result, and biology association.
- Example 3: Assemble a pathology foundation-model figure from S02/S33: WSI overview, patch embedding, task heads, benchmark table, failure cases.
- Example 4: Assemble a segmentation figure from S19/S20/S22: raw images, annotations, masks, quantitative metrics, and reader/QC notes.
- Example 5: Assemble a multimodal oncology figure from S18/S24/S25: modality branches, fusion model, ablation, clinical endpoint, and subgroup analysis.

### nnscholar4-2-paper-table

- Example 1: S05 clinical cohort table. Columns: training/internal/external cohorts; rows: demographics, tumor stage, MRI timepoints, endpoint, censoring, and missingness.
- Example 2: S08 model evaluation table. Rows: model variants; columns: AUC, AUPRC, sensitivity, specificity, calibration slope, Brier score, DCA net benefit, CI.
- Example 3: S06 radiomics feature table. Rows: feature groups/habitats; columns: extraction source, stability filter, selected features, coefficient/rank, biological interpretation.
- Example 4: S19 segmentation table. Rows: organs/lesions or datasets; columns: Dice, HD95, false positive rate, annotation source, and failure mode.
- Example 5: S24/S25 therapy-response table. Rows: clinical-only, imaging-only, pathology-only, multimodal; columns: response endpoint, discrimination, calibration, subgroup performance.

### nnscholar4-3-paper-writing: drafting

- Example 1: S02-style Results order: model scope -> benchmark breadth -> external validation -> interpretability -> limitations. Keep claims tied to provided tasks.
- Example 2: S05-style Methods order: cohort -> imaging timepoints -> preprocessing -> model -> survival endpoint -> statistics -> validation.
- Example 3: S08-style Discussion order: key evaluation finding -> why AUC alone misleads -> calibration/clinical utility -> recommendations -> limitations.
- Example 4: S13/S25-style translational drafting: noninvasive model -> treatment-response endpoint -> biological association -> clinical decision caution.
- Example 5: S19/S20-style method paper drafting: problem -> annotation resource -> architecture -> benchmark -> failure analysis -> reusable implementation.

### nnscholar4-3-paper-writing: polishing

- Example 1: From S05, polish survival claims by replacing "predicts outcome" with evidence-bounded language tied to cohort, endpoint, and validation set.
- Example 2: From S08, add evaluation nuance when prose over-relies on AUC; insert calibration, imbalance, and threshold-utility caveats.
- Example 3: From S15/S31, soften mechanism language: "associated with immune features" unless independent biological validation is supplied.
- Example 4: From S02/S03, strengthen foundation-model prose by naming pretraining data, target tasks, external validation, and failure modes.
- Example 5: From S19/S22, improve segmentation prose by separating annotation protocol, model output, reader QC, Dice/HD95, and clinical-readiness limits.

### nnscholar5-1-journal-conference-recommendation

- Example 1: If the work resembles S05 or S06 and has rigorous validation, consider Radiology: Artificial Intelligence / Radiology: Imaging Cancer fit; check RSNA scope and article type.
- Example 2: If the work resembles S02/S03 and has broad foundation-model validation, consider Nature Medicine / Nature Communications / Nature Biomedical Engineering tiers; verify novelty and generality.
- Example 3: If the work resembles S18/S23 with technical model contribution, consider IEEE TMI / Medical Image Analysis; emphasize method novelty and benchmarks.
- Example 4: If the work resembles S13/S24/S25 with oncology translation, consider Cell Reports Medicine / Cancer Cell-adjacent scope only if biology and clinical value are strong.
- Example 5: If the work resembles S08 as a methods/evaluation critique, target journals that accept methodological standards papers and require clear practice recommendations.

### nnscholar5-2-submission-finalization

- Example 1: For Radiology: AI-like S05/S06 submissions, finalize reporting checklist, external validation wording, data/code availability, IRB/consent, and figure permissions.
- Example 2: For Nature-style S02/S03 submissions, finalize data availability, code/model availability, competing interests, author contributions, and source-data links.
- Example 3: For Cell Reports Medicine-like S13/S25 submissions, finalize clinical ethics, cohort consent, translational relevance, graphical abstract, and STAR-style resource clarity if required.
- Example 4: For IEEE TMI/MEDIA-like S18/S19 submissions, finalize reproducibility, benchmark splits, implementation details, and supplementary ablations.
- Example 5: For any source-derived figure inspiration, verify that no copyrighted source image, caption, or table has been copied into the manuscript package.

### nnscholar5-3-submission-portal-workflow

- Example 1: Radiology-family portal pattern from S05/S06: article type, structured abstract, manuscript files, figure files, supplementary material, data/code statement, checklist.
- Example 2: Nature-family portal pattern from S01/S02/S03: cover letter, manuscript, reporting summary when applicable, data availability, code availability, ethics, competing interests.
- Example 3: Cell-family portal pattern from S10/S13/S24/S25: highlights, eTOC/graphical abstract fields if required, STAR/resource table when applicable, declaration forms.
- Example 4: IEEE/MEDIA portal pattern from S18/S19/S20: double-blind checks if required, graphical abstract optionality, code link, supplementary algorithm details.
- Example 5: Universal portal risk pattern: verify fees, word limits, figure formats, color policy, ethics statements, and required source files from official pages on submission day.

### nnscholar5-4-cover-letter

- Example 1: S02-style cover letter pitch: unmet clinical/pathology bottleneck, broad model capability, external validation breadth, and careful clinical-readiness boundary.
- Example 2: S05-style cover letter pitch: clinically important survival endpoint, serial MRI novelty, patient-level validation, and how the result could support risk stratification.
- Example 3: S06/S13-style pitch: noninvasive habitat/TME quantification, treatment-response relevance, validation strength, and no causal overclaim.
- Example 4: S18/S23-style pitch: technical multimodal fusion novelty, benchmark superiority, ablation evidence, and reproducibility assets.
- Example 5: S08-style pitch: methodological improvement for the field, why current evaluation practice is insufficient, and practical recommendations for reviewers/readers.

### nnscholar5-5-reviewer-response

- Example 1: If reviewers question external validation, use S05/S06-style language: define patient-level split, center-held-out set, and what is not external validation.
- Example 2: If reviewers question class imbalance, use S08-style response: add AUPRC, calibration, threshold analysis, and sensitivity analyses instead of defending AUC alone.
- Example 3: If reviewers question biological mechanism, use S15/S31-style response: distinguish association, validation, and causal mechanism; add cautious wording.
- Example 4: If reviewers question segmentation reliability, use S19/S20/S22-style response: add annotation protocol, inter-reader or QC process, Dice/HD95, and failure-case review.
- Example 5: If reviewers question multimodal model value, use S18/S23/S24-style response: add ablation, missing-modality analysis, modality contribution, and clinical interpretability.
