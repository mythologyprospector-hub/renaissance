# Learn Model Test

**Status:** Architectural test  
**Capability:** Learn  
**Purpose:** Test whether the Learn contract describes a real responsibility without prematurely selecting an implementation.

## Scenario

A new person wants to become capable of using Episteme to investigate a scientific question.

The objective is not that the person can follow a tutorial once. The objective is that the person can later perform a comparable investigation with substantially less scaffolding and can recognize what remains uncertain.

This is a useful test because Episteme already provides the subject matter and inquiry instrument while providing no dedicated learning system.

## Contract mapping

### Learner goal

The learner wants to independently:

- represent a question;
- identify known and unknown material;
- distinguish evidence from interpretation;
- inspect provenance;
- formulate a bounded hypothesis;
- identify a useful next investigation.

### Establish current capability

The learning workflow first records what the learner can already do.

This prevents the system from confusing exposure with progress.

### Instruction and guided practice

The learner receives:

- explanations of relevant Episteme concepts;
- worked examples;
- counterexamples showing epistemic mistakes;
- a guided investigation using explicit scaffolding.

The material must preserve Episteme's distinctions rather than flattening them into simplified assertions.

### Performance

The learner performs a new, bounded investigation.

The result records what was demonstrated and what support remained necessary.

Performance is evidence about this task under these conditions, not a universal claim about the learner.

### Transfer

The learner then receives a materially different question and performs the investigation with reduced or removed scaffolding.

A successful transfer demonstration is stronger evidence of capability than repeating the original exercise.

### Reflection

The learner explains:

- what they did;
- why they treated particular material as evidence, interpretation, or unknown;
- what they would investigate next;
- where their own reasoning remains uncertain.

This tests whether the learner can operate the method rather than merely reproduce its vocabulary.

## What this test establishes

The Learn model survives a concrete workflow because its central object is different from the objects of the existing instruments:

- Episteme manages inquiry and epistemic state.
- The learner is the object whose capability should increase.
- Instruction is an instrument.
- Performance is a bounded observation.
- Transfer is evidence relevant to durable capability.
- Assessment does not become authority over the person.

The test also exposes responsibilities not currently owned by Episteme, AI Foundry, Praxis, or Organs:

- learner-state representation;
- instructional sequencing;
- scaffolding;
- practice design;
- feedback;
- transfer assessment;
- learner reflection;
- adaptation to demonstrated capability.

## What this test does not establish

It does not establish:

- a learning algorithm;
- a pedagogical theory as Renaissance canon;
- a repository boundary;
- a universal learner model;
- a universal assessment metric;
- a particular AI model or interface;
- that every educational workflow requires a new system.

## Architectural result

The minimum reusable shape is:

```
learner goal
    → current capability
    → guided experience
    → demonstrated performance
    → feedback / adaptation
    → transfer test
    → capability evidence
```

The important abstraction is therefore **capability growth with transfer**, not content delivery.

That gives Renaissance a meaningful implementation boundary to test without yet inventing a Learning repository.

**Unknown remains a valid result.**
