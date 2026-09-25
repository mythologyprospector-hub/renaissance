# Renaissance — Grounding Protocol

**Status:** Operational guidance  
**Authority:** Implementation / operating procedure  
**Relationship to canon:** This document does not establish or amend Renaissance canon. It implements the existing onboarding, change-control, provenance, and authority requirements.

## Purpose

A returning Architect/Builder must not rely on conversational memory as the source of truth.

The repository is the source of truth.

Grounding is therefore a repeatable operating procedure for restoring current project context before consequential work.

## Grounding rule

Before consequential work, the working agent MUST reconcile:

1. current repository state;
2. current authority documents;
3. current recorded decisions;
4. current architectural and capability documents relevant to the task;
5. recent repository history;
6. any generated grounding snapshot available in the repository.

If these disagree, stop and resolve the discrepancy before treating the disagreement as settled fact.

## Mandatory grounding moments

Re-ground:

- at the beginning of a new work session;
- after a substantial conversation or context transition;
- after another builder, Codex, or contributor may have changed the repository;
- after pulling or fetching new repository state;
- when moving between major architectural areas;
- when moving from experiment to architecture or implementation;
- after any governing document or Decision changes;
- before a consequential architectural, implementation, or repository-wide change;
- whenever the current state is uncertain;
- whenever the Human Gate says `ground`, `onboard`, `refresh`, or `check canon`.

Do not wait for a context limit to force a re-ground.

## Authority reading order

At minimum, inspect:

1. `STATUS.md`
2. `CHARTER.md`
3. `CONSTITUTION.md`
4. `PRINCIPLES.md`
5. `BOUNDARIES.md`
6. `EPISTEMOLOGY.md`
7. `GOVERNANCE.md`
8. `CHANGE_CONTROL.md`
9. applicable `DECISIONS/` records
10. `ARCHITECTURE.md`
11. applicable capability and project documents

The full repository tree must be considered when determining whether a more specific source of truth exists.

## Repository-state check

Before modifying anything, establish:

- repository identity;
- default branch;
- current commit;
- whether local state is clean or modified;
- whether local state differs from the remote;
- recent commits;
- files relevant to the mission;
- applicable tests and verification mechanisms.

Never assume that a remembered path, branch, commit, document, or architecture is still current.

## Reconciliation

Grounding is not merely rereading.

The agent should explicitly distinguish:

- **Established:** supported by current repository authority.
- **Proposed:** under consideration.
- **Experiment:** bounded exploration.
- **Implementation:** current machinery.
- **Unknown:** not established.
- **Stale:** remembered or previously observed, but not confirmed against current repository state.

A previous conversation is historical context, not authority.

## Generated grounding snapshot

The repository may contain a generated `GROUNDING_SNAPSHOT.md`.

This snapshot is an orientation aid only. It may summarize repository state, recent commits, document inventory, and verification metadata.

It does **not** become canon and must never override the underlying documents.

When present, inspect the snapshot first for rapid orientation, then verify consequential claims against the underlying repository sources.

## Conflict rule

If memory, a previous conversation, a generated snapshot, local state, and repository documents disagree:

**the applicable current repository authority wins, subject to the documented change-control process.**

If authority itself is ambiguous, preserve the ambiguity and ask the Human Gate when a decision is required.

## Builder behavior

A builder should begin substantial work by recording internally:

> **Grounded at:** `<commit or equivalent repository state>`

and should re-check that state before final verification.

A builder must not silently continue from stale context after detecting repository drift.

## Automation boundary

Automation can keep orientation material current, detect repository drift, and make grounding cheap.

Automation cannot grant authority or manufacture context.

The working agent remains responsible for actually reading the current repository and reconciling it before consequential work.

## Human Gate shorthand

A single `.` means proceed/continue/accepted within the already-established direction.

It does not waive grounding, authority checks, testing, or the distinction between implementation and canon.
