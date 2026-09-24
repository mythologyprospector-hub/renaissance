# Learn Experiment 001 — Transfer, Not Exposure

**Status:** Architectural experiment specification v0.1  
**Authority:** Experiment  
**Capability:** Learn  
**Related contract:** `CAPABILITIES/HUMAN_CAPABILITY_MODEL.md`

## Purpose

Test whether a learning interaction can produce evidence of increased human capability rather than merely exposure to information or successful performance under immediate scaffolding.

This is a deliberately small experiment. It is intended to test the Learn contract, not to establish a universal theory or metric of learning.

## Core question

> After an instructional interaction, can the learner demonstrate a capability that transfers to a meaningfully different task?

## Hypothesis

If the interaction produces genuine learning, then evidence of capability should survive at least some change in task, context, or scaffolding.

Immediate success alone is insufficient evidence.

## Experimental shape

1. **Baseline**
   - Give the learner a small unfamiliar task.
   - Record what the learner can already do without instruction.
   - Do not assume the baseline is zero.

2. **Instruction**
   - Provide a bounded explanation, example, demonstration, or guided discovery sequence.
   - Preserve the epistemic status and provenance of instructional material.
   - Record the support provided.

3. **Immediate task**
   - Ask the learner to perform a task directly related to the instruction.
   - Record performance and the amount/type of scaffolding required.

4. **Transfer task**
   - Change the surface form, context, or problem while preserving the underlying capability being tested.
   - Reduce or remove scaffolding where appropriate.
   - Record whether the learner can recognize and apply the underlying idea.

5. **Reflection**
   - Ask the learner to explain what they think they learned, what remains uncertain, and how they would approach a new problem.

6. **Optional delayed retest**
   - At a later point, repeat a related transfer task without re-teaching the material.
   - Treat retention as additional evidence, not a universal requirement for every learning event.

## Evidence categories

The experiment distinguishes:

- **Exposure:** the learner encountered information or instruction.
- **Performance:** the learner successfully completed a task under specified conditions.
- **Transfer:** the learner applied the capability to a changed situation.
- **Reflection:** the learner can describe, question, or reason about what was learned and what remains uncertain.
- **Retention:** capability remains demonstrable after an interval.

No single category is equivalent to learning in every domain.

## Required records

Where practical, preserve:

- learner goal;
- baseline capability;
- instructional material or provenance;
- instructional transformations or generated content;
- support/scaffolding supplied;
- task conditions;
- observed performance;
- transfer-task conditions;
- learner explanation/reflection;
- uncertainties or unresolved misunderstandings;
- evidence supporting the claimed capability change.

## Architectural tests

The experiment passes its architectural purpose only if:

- exposure remains distinguishable from performance;
- performance remains distinguishable from transfer;
- assessment remains evidence about performance under stated conditions;
- generated instruction does not gain epistemic authority merely by being generated;
- provenance can survive into the learning interaction where relevant;
- uncertainty and misunderstanding can remain explicit;
- the learner remains the agent;
- the system does not optimize for engagement or dependence as substitutes for capability;
- the experiment can report **insufficient evidence of learning** without forcing a positive conclusion.

## Domain neutrality

The protocol intentionally does not prescribe a universal subject, interface, teaching method, learner age, curriculum, or scoring scale.

A later domain-specific experiment may instantiate this protocol for mathematics, programming, science, language, music, or another field.

The domain supplies the appropriate capability and transfer task.

## What this experiment does not establish

This experiment does not establish:

- a universal definition of learning;
- a universal learning score;
- that transfer is required in every possible form of learning;
- that delayed retention is always required;
- that one experimental result proves a learner has permanently acquired a capability;
- that the system has authority to determine whether a person has learned in every context.

## Failure is useful

A result showing exposure without transfer is not a failed system test in the epistemic sense. It is information about the limits of the instructional interaction.

The experiment should preserve that distinction.

## Expected outcome

The desired architectural outcome is not a successful learner score.

It is a clearer answer to:

> **What evidence does Renaissance need before it may reasonably say that a learning interaction increased human capability?**

Unknown remains a valid result.
