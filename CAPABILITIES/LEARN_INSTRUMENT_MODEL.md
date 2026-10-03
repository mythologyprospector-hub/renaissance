# Learn Instrument Model

**Status:** Architectural model v0.1  
**Capability:** Learn  
**Purpose:** define the smallest inspectable responsibility needed to turn a learning intention into demonstrated capability growth.

## Architectural finding

The missing responsibility is not "serve educational content."

It is to coordinate and preserve a bounded learning process in which a learner can move from a stated goal, through practice and feedback, to demonstrated transfer with less scaffolding.

The smallest reusable model is:

```
goal
  → capability target
  → baseline
  → learning activity
  → performance
  → feedback / reflection
  → adaptation
  → transfer task
  → capability evidence
```

This model is deliberately smaller than a learning platform, tutoring agent, curriculum engine, or learner-management system.

## Minimum objects

### Learner Goal

What the learner is trying to become able to do or understand.

A goal is supplied by or legitimately established with the learner. The instrument must not silently replace it with an engagement, retention, or system-optimization objective.

### Capability Target

A concrete description of what successful learning would make the learner able to do.

It should be expressible as a demonstration or transfer task rather than only as content exposure.

### Baseline

A bounded observation of what the learner can currently demonstrate under stated conditions.

Baseline is not a permanent label or universal measurement of the person.

### Learning Activity

An explanation, example, exercise, investigation, simulation, construction task, question sequence, or other bounded experience intended to develop the target capability.

The activity is an instrument, not the outcome.

### Performance

A learner-produced response or artifact under stated conditions.

Performance records what happened in that task. It does not by itself establish durable capability.

### Feedback

Information returned to the learner about the performance, including correction, explanation, counterexample, question, or reflection prompt.

Feedback must preserve relevant epistemic status and source distinctions.

### Adaptation

A bounded change to subsequent scaffolding, activity, difficulty, or sequence in response to demonstrated performance.

Adaptation must remain subordinate to the learner's legitimate goal.

### Transfer Task

A materially different task requiring the target capability with reduced or changed scaffolding.

Transfer is the critical boundary between repeating a taught interaction and demonstrating increased capability.

### Capability Evidence

An inspectable record connecting the target capability to demonstrated performance across appropriate conditions, especially transfer.

It is evidence about a bounded demonstration, not a universal judgment about the learner.

## Minimum record requirements

A conforming implementation should be able to preserve, where relevant:

- learner goal;
- capability target;
- baseline conditions;
- activity and instructional material;
- source/provenance of material;
- learner performance;
- feedback;
- adaptation;
- transfer task and conditions;
- resulting capability evidence;
- uncertainty, disagreement, or limitations;
- identity/version of consequential generated material or tools.

No universal learner score or hidden learner profile is required.

## What the instrument owns

The Learn instrument owns the **learning process boundary**:

- establishing the target;
- representing bounded learner state relevant to the current goal;
- sequencing learning experiences;
- observing performance;
- providing or routing feedback;
- adapting scaffolding;
- constructing credible transfer checks;
- preserving the distinction between exposure, performance, and capability.

It does not need to own the underlying knowledge, search algorithms, artifact construction, execution runtime, or domain expertise.

## What it does not own

- **Understand / Episteme:** epistemic authority, source knowledge, evidence, contradiction analysis.
- **Explore:** exploration spaces and traversal mechanisms.
- **Create / AI Foundry:** general artifact construction or AI-system engineering.
- **Praxis:** problem framing, intervention selection, real-world decision/evidence boundaries.
- **Organs:** generic runtime, execution, communication, memory, telemetry, or safety mechanisms.

These may be used by Learn.

## First implementation test

Before creating a repository, an implementation should demonstrate one complete bounded workflow:

1. establish a learner goal and capability target;
2. establish a baseline;
3. deliver one bounded learning activity;
4. capture learner performance;
5. provide feedback;
6. adapt the next activity;
7. run a materially different transfer task with reduced scaffolding;
8. produce bounded capability evidence;
9. show that epistemic/provenance distinctions survive the workflow.

Failure to demonstrate transfer should remain a valid result.

## Architectural consequence

A generic learning repository is **not yet justified merely by this model**.

The model identifies a coherent missing responsibility. The next step is a concrete vertical prototype/test of the model. If that test survives, the resulting boundary can become the basis of a Renaissance Learn instrument.

The likely first implementation should be domain-light and orchestration-focused rather than attempting to become a universal education system.

**Unknown remains a valid result.**
