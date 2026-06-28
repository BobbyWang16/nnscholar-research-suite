# Discipline Schematic Atlas

Use this reference when deciding how to structure a schematic figure for a discipline.

## Clinical Medicine

Common schematic types:
- patient journey, clinical workflow, diagnostic/prediction model pipeline, treatment decision support, cohort data pipeline.

Recommended structure:
- left: population/data source;
- center: exposure, treatment, model, or workflow;
- right: endpoint, decision, validation, or clinical action;
- bottom strip: time window or validation checkpoints.

Avoid:
- implying treatment benefit before validation;
- mixing radiation pneumonitis, CIP, and rechallenge risk without clear decision nodes.

## Basic Biomedicine

Common schematic types:
- cellular mechanism, signaling pathway, perturbation experiment, omics-to-mechanism workflow.

Recommended structure:
- model system -> perturbation/exposure -> molecular pathway -> phenotype/readout -> validation/rescue;
- use different visual layers for cell, tissue, molecular, and experimental readout.

Avoid:
- presenting untested pathway arrows as proven;
- overcrowding with gene names.

## AI / Data Science

Common schematic types:
- data pipeline, model architecture, training/evaluation workflow, agent system, benchmark protocol.

Recommended structure:
- input data -> preprocessing -> model modules -> prediction/output -> evaluation/deployment;
- use separate colors for data, model, evaluation, and user/system interaction.

Avoid:
- fake UI details or impossible module internals;
- mixing training and inference unless clearly separated.

## Materials / Chemistry

Common schematic types:
- synthesis route, material structure-function mechanism, characterization workflow, application mechanism.

Recommended structure:
- precursor/material -> synthesis/processing -> structure/characterization -> performance/application;
- use clean icons for particles, films, pores, fibers, surfaces, or devices.

Avoid:
- invented exact molecular structures when not specified;
- visual claims of mechanism not supported by characterization.

## Education / Psychology

Common schematic types:
- conceptual framework, intervention process, measurement model, learning/behavior pathway.

Recommended structure:
- intervention/context -> mediator/moderator -> cognitive/behavioral process -> measured outcome;
- separate observed variables from latent constructs.

Avoid:
- overly medical/biological metaphors unless relevant;
- causal arrows for correlational studies.

## Economics / Social Science

Common schematic types:
- identification strategy, causal pathway, policy intervention logic, data linkage workflow.

Recommended structure:
- treatment/exposure -> mechanism channels -> outcome;
- include confounders/control strategy as separate layer;
- for DID/event study, show time and treated/control comparison clearly.

Avoid:
- drawing a direct causal arrow when identification is not established.

## Humanities

Common schematic types:
- corpus construction, interpretive framework, archival workflow, argument map, comparative case structure.

Recommended structure:
- sources/corpus -> selection/coding/reading -> analytical lens -> themes/claims;
- use visual hierarchy rather than causal arrows when the argument is interpretive.

Avoid:
- suggesting quantitative precision if the work is qualitative/interpretive.

## Engineering

Common schematic types:
- system architecture, prototype workflow, control loop, signal/material/energy flow, safety/failure process.

Recommended structure:
- inputs/sensors/material -> core module/prototype -> outputs/actuators/results -> feedback/control/safety;
- label operating conditions and interfaces.

Avoid:
- decorative components that change the implied system design.

