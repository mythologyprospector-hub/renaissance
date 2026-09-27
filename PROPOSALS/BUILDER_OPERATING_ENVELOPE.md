# Proposal — Builder Operating Envelope

**Status:** Proposed  
**Authority:** Proposal  
**Date:** 2026-09-27

## Purpose

Define a compact, reusable operating model for Renaissance builders that preserves constitutional and governance safeguards while reducing unnecessary active-context reconstruction.

This proposal does **not** amend the Constitution, Charter, Decisions, Architecture, or established governance.

## Problem

The current grounding procedure is rigorous but operationally expensive. For consequential work it requires reconciliation of current repository state, the current authority set, Decisions, relevant architecture/capability documents, recent history, and the generated snapshot; its authority reading order explicitly names ten repository documents, and it requires considering the full repository tree.

That is appropriate for architectural or constitutional work, but applying the same breadth to routine implementation can consume substantial working context before useful work begins.

The observed Episteme operating pattern and independent review supplied to the Human Gate suggest a different optimization:

> Preserve authority safeguards, but load only the authority and evidence relevant to the current task.

## Proposed operating model

### 1. Repository as durable memory

Git/GitHub is the durable project record. Conversation context is temporary working memory, not a second repository.

### 2. Targeted grounding

For each mission, establish:

- current repository state;
- the task's direct source of truth;
- authority documents relevant to the requested change;
- applicable Decisions;
- affected implementation and tests.

Broader grounding is required when the task crosses an architectural, constitutional, governance, repository-wide, or otherwise consequential boundary.

### 3. Authority map, not authority preload

The builder should know where authority lives without reading every authority document for every task.

The authority index in `AGENTS.md` remains useful as a routing map.

### 4. Settled decisions stay settled

Do not reopen established Decisions, architecture, or boundaries unless the current task presents:

- contradictory evidence;
- a new requirement;
- a test or implementation failure;
- repository drift;
- an explicit request to reconsider; or
- a consequence that crosses an established authority boundary.

### 5. Routine implementation is distinct from architectural work

A routine implementation that follows established architecture should not automatically trigger full constitutional or repository-wide reconstruction.

### 6. Investigation must converge

Investigate until the evidence needed for the current decision is sufficient. Then act, test, verify, document where required, and commit.

Investigation must not become an indefinite substitute for execution.

### 7. Commits are durable checkpoints

A verified commit records a recoverable state. The builder need not carry every intermediate implementation detail forward after it has been durably recorded.

### 8. Human Gate remains authoritative

Targeted grounding does not weaken the Human Gate or change the authority hierarchy.

A single `.` means continue within the established direction; it does not authorize silent constitutional change, waive testing, or convert a proposal/experiment into canon.

## Suggested task classes

The following classification is proposed as an operating aid, not a new authority hierarchy:

### Routine

Examples: implementation of an established requirement, test addition, documentation synchronization, bug fix within established boundaries.

Ground locally and inspect only the applicable authority/source-of-truth material.

### Architectural

Examples: changing interfaces, capability boundaries, cross-project relationships, runtime topology, or established architecture.

Ground the affected architecture and applicable Decisions, plus higher-level authority necessary to verify compatibility.

### Foundational / constitutional

Examples: changing purpose, authority, constitutional constraints, governance, or foundational principles.

Perform broad grounding and use the documented change-control process.

### Uncertain boundary

If the builder cannot determine which class applies, inspect enough authority to resolve the classification rather than guessing.

## Proposed compact execution loop

```text
orient
  -> classify task
  -> target-ground
  -> inspect source of truth
  -> implement or propose
  -> test
  -> verify current state
  -> document when required
  -> commit
  -> continue
```

## Safeguards retained

This proposal retains:

- repository-as-source-of-truth;
- Human Gate authority;
- constitutional and governance hierarchy;
- provenance and epistemic discipline;
- change control;
- applicable Decision review;
- testing and final verification;
- conflict escalation;
- repository hygiene;
- no silent architecture or canon changes.

The proposed change is **where and when information is loaded**, not what authority means.

## Candidate implementation

If accepted as a direction, the next bounded step should be an operating-protocol experiment rather than an immediate rewrite of canon.

The experiment should compare the current grounding procedure with a targeted procedure across representative routine, architectural, and foundational tasks.

It should measure at least:

- documents read;
- approximate active-context volume;
- tool/retrieval operations;
- implementation progress;
- tests and verification;
- authority violations or missed dependencies;
- whether the task had to broaden grounding later.

The experiment should explicitly test the failure mode:

> targeted grounding missed an applicable authority document.

A successful experiment would demonstrate that targeted grounding reduces unnecessary context consumption without weakening the project's existing safeguards.

## Non-goals

This proposal does not:

- remove the Constitution, Charter, Principles, Boundaries, Epistemology, Governance, Change Control, Decisions, or Architecture;
- declare any existing authority document obsolete;
- establish a new constitutional principle;
- define a final universal agent prompt;
- require a particular model, subscription, reasoning mode, or vendor;
- claim that fewer tokens automatically means better engineering;
- replace human judgment with an automated classification system.

## Relationship to existing authority

This proposal is subordinate to the Constitution, Charter, ratified Decisions, established Architecture, and Change Control.

If implementation of this proposal would materially alter an established requirement, that change must be handled through the appropriate Decision/change-control process.

## Recommendation

Treat this as a bounded operational experiment.

Do not optimize for minimum context at the expense of authority awareness. Optimize for the smallest sufficient context that can safely complete the current mission.
