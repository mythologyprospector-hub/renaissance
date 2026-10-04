# Learn Vertical Test

**Status:** Architectural vertical test v0.1  
**Capability:** Learn  
**Model under test:** `CAPABILITIES/LEARN_INSTRUMENT_MODEL.md`

## Purpose

Test the minimum Learn instrument against one complete, domain-light learning episode without depending on a particular teaching technology or educational theory.

The test uses a small reasoning skill: distinguishing a source-supported statement from an interpretation and an unresolved question.

The subject matter is deliberately simple. The test is about learning-process integrity, not domain difficulty.

## Test episode

### 1. Goal

Learner goal:

> Become able to examine a short information packet, separate what is directly supported from what is inferred, and state what remains unresolved.

The instrument records the goal rather than replacing it with completion, engagement, or retention.

### 2. Capability target

The learner should be able to:

- identify source-supported statements;
- label an interpretation as interpretation;
- identify an unresolved question;
- explain the basis for each classification;
- perform the same reasoning on materially different material.

### 3. Baseline

The learner receives a short unfamiliar packet and performs the classification without instruction.

Record:

- task/version;
- available material;
- instructions;
- learner response;
- support provided: none;
- observed performance;
- uncertainty in assessment.

The baseline is a bounded observation, not a learner label.

### 4. Learning activity

Provide:

- one explanation of the distinctions;
- one worked example;
- one counterexample;
- one short guided exercise.

The instructional record identifies which material is supplied source material and which is generated or authored instruction.

No statement becomes more authoritative because it appears in the lesson.

### 5. Practice performance

The learner performs a new classification task.

Record:

- task/version;
- response;
- conditions;
- scaffolding;
- observed strengths/errors;
- learner explanation where relevant.

The result is performance evidence, not yet capability evidence.

### 6. Feedback

Feedback identifies the reasoning difference between the learner's response and the task's stated criteria.

It may:

- correct an error;
- ask a question;
- provide a counterexample;
- expose an ambiguity;
- point back to source material.

Feedback must not conceal uncertainty merely to make the lesson feel decisive.

### 7. Adaptation

The next activity changes according to demonstrated performance.

Examples:

- if the learner confuses inference with source support, provide a contrasting example;
- if classification is correct but unexplained, require justification;
- if the learner demonstrates the target cleanly, reduce scaffolding.

The adaptation is tied to the current capability target, not to maximizing interaction time.

### 8. Transfer

Provide a materially different information packet with:

- different subject matter;
- different wording;
- no worked example from the lesson;
- reduced scaffolding.

The learner repeats the classification and explanation task.

This is the decisive test.

A learner who succeeds only when the original examples or prompts are reproduced has demonstrated performance, but not sufficient transfer evidence for the target capability.

### 9. Capability evidence

Produce a bounded record containing:

- capability target;
- baseline performance;
- learning activity;
- practice performance;
- feedback/adaptation history;
- transfer task;
- transfer performance;
- remaining uncertainty and limitations.

The record may support the bounded conclusion:

> Under the recorded conditions, the learner demonstrated the target reasoning skill on both the practice task and a materially different transfer task with reduced scaffolding.

It must not silently become:

> This learner understands reasoning.

## Failure tests

A conforming instrument must reject or preserve the distinction in these cases:

### Exposure without performance

The learner reads the lesson but completes no task.

Result: exposure only.

### Performance without transfer

The learner succeeds on a rehearsed exercise but fails the materially different task.

Result: performance demonstrated; durable capability remains unresolved.

### Generated lesson presented as source

An AI-generated explanation is presented without distinguishing it from supplied source material.

Result: provenance/epistemic boundary violation.

### Correct answer by unsupported guess

The learner reaches the expected classification but cannot provide the requested basis.

Result: outcome alone does not establish the intended capability.

### Engagement substituted for learning

The learner completes many activities but shows no evidence of increased capability.

Result: activity count is not learning evidence.

### Learner goal silently changed

The system changes the target because another objective is easier to optimize.

Result: human-agency violation.

## Architectural result

The vertical test demonstrates that the minimum model has a real, nontrivial boundary.

The essential state is not a content library. It is the relationship among:

```
goal
→ target
→ baseline
→ activity
→ performance
→ feedback
→ adaptation
→ transfer
→ bounded capability evidence
```

Three things become especially clear:

1. **Transfer is a first-class object.** It cannot safely be inferred from lesson completion or repeated performance.
2. **Assessment is bounded evidence.** It describes demonstrations under conditions rather than classifying the whole learner.
3. **Learning provenance matters.** The system must preserve distinctions between supplied knowledge, generated instruction, learner performance, and assessment interpretation.

## Boundary decision

The test is sufficient to justify a dedicated **Learn instrument** as an architectural responsibility.

It is not yet sufficient to prescribe:

- a repository name;
- a particular AI tutor;
- a database;
- a learner model;
- a curriculum engine;
- a scoring algorithm;
- a UI;
- or an autonomous teaching architecture.

The next implementation should therefore be a minimal, inspectable vertical slice whose sole purpose is to execute and preserve this loop:

```
goal → baseline → activity → performance → feedback → adaptation → transfer → evidence
```

If that slice cannot remain domain-light and preserve the boundaries above, the architecture should be revised before it grows.

**Unknown remains a valid result.**
