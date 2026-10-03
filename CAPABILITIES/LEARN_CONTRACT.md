# Learn Capability Contract

**Status:** Architectural contract v0.1  
**Authority:** Architecture  
**Human-facing capability:** Learn

## Purpose

Learn increases a person's or group's **durable ability to understand, explore, create, reason, and continue learning independently**.

The capability is concerned with increased human capability, not merely delivery of information or production of educational material.

## Core loop

```
learner goal
  → establish current capability
  → explain / demonstrate
  → practice / investigate
  → observe performance
  → feedback / reflection
  → adapt
  → test transfer
  → increased capability
```

The loop is conceptual. A conforming implementation may use different instructional methods.

## Scope

Learn may provide:

- explanation and instruction;
- questioning and guided discovery;
- examples and counterexamples;
- practice and experimentation;
- feedback and correction;
- reflection;
- skill development;
- assessment;
- adaptive sequencing;
- transfer exercises;
- learning how to learn.

## Boundaries

Learn must not:

- define the learner's values or purposes;
- force beliefs;
- conceal contested or uncertain material as settled;
- manufacture certainty;
- optimize for dependency or engagement as substitutes for learning;
- replace learner judgment;
- silently redefine legitimate learner goals;
- claim that exposure equals learning.

A system may remain useful after learning without making dependence on it the objective.

## Inputs

Possible inputs include learner goals, questions, demonstrated ability, prior knowledge, source material, examples, exercises, experiments, feedback, learning history, reflections, and performance evidence.

## Outputs

Possible outputs include explanations, questions, exercises, experiments, feedback, learning paths, learner-generated artifacts, demonstrated performance, and evidence of strengthened or transferred capability.

Educational material is an instrument. The intended outcome is the learner's capability.

## Epistemic boundary

Teaching does not upgrade the status of what is taught.

Implementations must preserve relevant distinctions among:

- supported knowledge;
- observation;
- interpretation;
- hypothesis;
- uncertainty;
- disagreement;
- possibility;
- and unknown.

Generated instructional material must not become authoritative merely because it was generated or delivered by a learning system.

## Provenance

Where useful or consequential, instructional material should preserve source identity, relevant evidence, transformations, generation, and uncertainty. A learner should be able to distinguish source material from generated explanation, example, simulation, or exercise where that distinction matters.

## Human agency

The learner remains the agent.

A learning system may explain, question, demonstrate, challenge, simulate, assess, provide feedback, or suggest a path. It does not acquire authority over what the learner should value, believe, or become.

Successful learning should, where appropriate, leave the learner better able to choose tools and proceed with less scaffolding.

## Evidence of learning

Learn distinguishes:

1. **Exposure** — material was encountered.
2. **Performance** — a task was completed under specified conditions.
3. **Capability** — the learner can understand, adapt, transfer, explain, solve, create, or continue without the exact original scaffolding.

No universal learning score is prescribed.

Evidence should therefore favor demonstrated understanding, transfer, adaptation, explanation, problem solving, creation, or other domain-appropriate demonstrations of capability.

Assessment describes demonstrated performance under particular conditions. It is not an infallible measurement of the whole person.

## Acceptance conditions

A conforming implementation must:

1. make increased human capability the intended outcome;
2. distinguish exposure, performance, and capability;
3. preserve relevant epistemic distinctions;
4. preserve relevant provenance;
5. expose meaningful uncertainty and disagreement;
6. avoid treating engagement or dependence as learning;
7. preserve learner agency and legitimate goals;
8. distinguish assessment evidence from universal claims about the learner;
9. distinguish generated instructional material where relevant;
10. provide a credible way to test transfer beyond the immediate teaching interaction.

## Relationship to other Renaissance capabilities

- **Understand** supplies knowledge, evidence, uncertainty, and unresolved questions. Learn may teach these without changing their epistemic status.
- **Explore** can provide discoveries, possibilities, and investigative experiences. Learn turns appropriate encounters into durable human capability without treating exploration output as automatically true.
- **Create** provides artifacts, projects, and constructive tasks through which learning can be practiced and demonstrated.
- **Praxis** can provide real problems and bounded tests that become meaningful learning contexts when the learner's capability is the object.
- **Organs** may provide runtime mechanisms for interaction, memory, execution, and human-facing operation. It does not become Learn.

## Implementation status

No mature Renaissance implementation is currently designated as the primary Learn instrument.

This contract therefore establishes the responsibility and boundary without prescribing a repository.

The next architectural step is implementation discovery and workflow testing. A new learning system should be built only after a real workflow demonstrates responsibilities that existing instruments cannot satisfy without distorting their purposes.

**Unknown remains a valid result.**
