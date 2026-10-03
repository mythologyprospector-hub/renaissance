# Create Capability Contract

**Status:** Architectural contract v0.1  
**Authority:** Renaissance Architecture  
**Human-facing capability:** Create

## Purpose

Create increases humanity's ability to transform intention, knowledge, possibility, and imagination into **inspectable artifacts, designs, methods, and constructive changes**.

The responsibility begins where a person or group has something they intend to make or change and ends with an artifact or attempted artifact whose lineage, state, evaluation, and remaining limitations can be understood.

Create is not merely generation. It includes the constructive loop:

```
intention
  ↓
requirements / constraints
  ↓
design
  ↓
construction
  ↓
inspection / evaluation
  ↓
revision
  ↓
artifact
```

The loop may be iterative and may involve other Renaissance capabilities.

## Scope

Create may include:

- translating human intent into explicit requirements;
- design and decomposition;
- selecting or developing constructive methods;
- programming and software construction;
- fabrication and prototyping;
- composition and creative production;
- transformation of existing artifacts;
- revision and repair;
- artifact evaluation;
- packaging and reproducibility;
- preserving artifact lineage;
- producing intermediate artifacts when they are useful toward the intended result.

Artifacts may be digital, physical, mathematical, informational, scientific, educational, artistic, or otherwise constructive.

## Boundaries

Create does not:

- decide what humans ought to create;
- invent human goals or values and silently treat them as requirements;
- establish the truth of claims merely because they appear in an artifact;
- turn generated material into evidence without the appropriate epistemic process;
- silently replace human creative or engineering judgment;
- acquire authority merely because it can construct something;
- authorize consequential external actions merely because construction is complete.

A constructed artifact is an artifact, not automatically a validated claim, safe intervention, or authorized action.

## Inputs

Create may receive:

- human intention and goals;
- requirements and constraints;
- designs and specifications;
- knowledge and evidence from Episteme;
- possibilities discovered through exploration;
- candidate interventions from Praxis;
- existing artifacts;
- materials and resources;
- models, simulations, examples, and references;
- evaluation criteria.

Inputs retain their original epistemic and authorization status.

## Outputs

Create may produce:

- designs;
- plans;
- source code;
- programs;
- prototypes;
- documents;
- models;
- datasets or transformations of datasets where creation is the actual responsibility;
- physical or digital artifacts;
- revised artifacts;
- build records;
- evaluation records;
- reproducible construction specifications.

Creation outputs should make clear what was generated, transformed, supplied, measured, or externally sourced where that distinction matters.

## Provenance

Where consequential or useful for reproduction, Create should preserve:

- originating intention or requirement;
- source materials;
- inputs;
- transformations;
- tools and relevant configuration;
- versions;
- contributors;
- generated components;
- evaluation;
- revisions;
- resulting artifact identity.

Provenance records lineage. It does not certify truth, quality, safety, or fitness for purpose.

## Epistemic status

Create must preserve distinctions among:

- source material;
- generated material;
- observation;
- measurement;
- inference;
- hypothesis;
- design assumption;
- test result;
- evaluation;
- and established knowledge.

A successful build does not prove the assumptions that produced it.

A failed build is still a potentially useful result.

Evaluation performed during creation must remain distinguishable from independent evidence or validation where that distinction matters.

## Human agency

The human remains the owner of purpose and consequential judgment.

Create may assist by:

- proposing designs;
- decomposing work;
- constructing artifacts;
- trying alternatives;
- running bounded evaluations;
- identifying defects;
- revising artifacts;
- and exposing tradeoffs.

It must not silently substitute system objectives for the creator's objectives.

Automation may be used for construction, but authority to perform consequential external actions remains governed by the applicable human and runtime controls.

## Relationship to other capabilities

### Episteme / Understand

Episteme can provide knowledge, evidence, unknowns, hypotheses, experiments, and results.

Create may use those materials but does not inherit their epistemic authority.

Create can also produce artifacts or construction results that later become inputs to inquiry.

### Praxis

Praxis can frame a human problem, generate candidate interventions, analyze failure, design tests, and record human decisions and results.

Create may construct an intervention or artifact selected through a legitimate human decision.

Create does not make that decision itself.

### Explore

Explore may expose possibilities, candidate designs, regions of a search space, or previously unknown alternatives.

Create turns selected possibilities or human intentions into artifacts.

Exploration does not authorize creation, and creation does not validate an explored possibility.

### Organs

Organs may provide bounded execution, communication, memory, sandboxing, safety gates, coordination, telemetry, and human-facing operation.

Those mechanisms enable Create but do not become the Create capability.

## Acceptance conditions

A conforming implementation must:

1. preserve the distinction between intention and implementation;
2. keep requirements and constraints inspectable where applicable;
3. preserve relevant artifact lineage;
4. distinguish generated and supplied material where relevant;
5. distinguish construction from validation;
6. preserve meaningful failure and revision history where useful;
7. avoid silently acquiring authority through automation;
8. support human inspection and intervention at appropriate consequential boundaries;
9. remain replaceable behind the capability contract;
10. produce artifacts that can be inspected independently of the system that created them where practical.

## What Create does not require

Create does not require:

- a particular AI model;
- autonomous agents;
- a single repository;
- a graphical editor;
- a distributed runtime;
- automatic deployment;
- autonomous real-world action;
- or a universal artifact format.

A useful implementation may begin as a narrow instrument and broaden only when demonstrated responsibility warrants it.

## Current implementation status

No existing project is designated as the primary Renaissance implementation of Create by this contract.

Existing independent projects may later demonstrate that they already satisfy some or all of this responsibility. Similarity alone does not establish membership.

The next architectural task is therefore **implementation discovery and boundary testing**, not automatic creation of a new repository.

## Status

This contract recognizes Create as a Renaissance system capability while leaving its implementation open.

The capability may be revised, composed with other capabilities, or retired by explicit architectural decision if evidence warrants it.
