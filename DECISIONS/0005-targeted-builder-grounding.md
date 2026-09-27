# Decision 0005 — Targeted Builder Grounding

**Date:** 2026-09-27  
**Status:** Accepted  
**Authority:** Human Gate  
**Scope:** Builder operating procedure and context management

## Matter

Determine whether Renaissance builders should perform broad authority reconstruction before ordinary work, or load only the authority and evidence relevant to the current mission while preserving broad grounding for work that actually crosses foundational boundaries.

## Prior state

The grounding protocol required consequential work to reconcile current repository state, current authority documents, current Decisions, relevant architecture/capability documents, recent history, and the generated snapshot. Its authority reading order named the full foundational authority set, and the full repository tree was to be considered when determining whether a more specific source existed.

This preserved rigor but could impose the same context cost on routine implementation as on architectural or foundational work.

## Evidence

The Episteme build retrospective, the Renaissance-specific operating analysis supplied by the Human Gate, and independent review of Codex operating practices converge on the same operational distinction:

- the repository is durable memory;
- active model context is working memory;
- authority should be consulted by relevance;
- settled decisions should not be repeatedly reopened without a trigger;
- routine implementation should not be treated as foundational work;
- investigation should converge into action when sufficient evidence exists.

The current Renaissance documents were inspected directly before this decision. Current Codex guidance also emphasizes keeping persistent project guidance concise and avoiding bloated context.

## Decision

Renaissance adopts **targeted grounding** as its normal builder operating procedure.

A builder MUST establish enough current repository state and applicable authority to safely perform the mission, but MUST NOT automatically reread the entire authority set for routine work.

Broad grounding remains mandatory when the mission:

- changes constitutional or foundational material;
- changes governance or change-control rules;
- changes established architecture or cross-project boundaries;
- changes repository-wide conventions;
- moves an experiment into architecture or implementation;
- presents unresolved authority conflict;
- crosses a boundary whose applicability cannot be determined locally.

For routine implementation, the builder should:

1. orient to current repository state;
2. classify the task;
3. identify the direct source of truth;
4. inspect applicable authority and Decisions;
5. implement the smallest coherent change;
6. test and verify;
7. document when required;
8. commit and continue.

The generated grounding snapshot is an orientation aid, not a mandatory reread target.

The full repository tree is not a mandatory step for every task; it is required when source-of-truth discovery or repository-wide impact makes it relevant.

A settled Decision is not reopened merely because a task touches its subject. Reopening requires new evidence, contradiction, failure, changed requirement, explicit reconsideration, or a consequence that crosses an established authority boundary.

## Safeguards retained

This decision does not remove or weaken:

- Constitutional Canon;
- Charter or ratified Decisions;
- Human Gate authority;
- epistemic distinctions;
- provenance/history requirements;
- change control;
- testing and final verification;
- conflict escalation;
- prohibition on silent architecture or canon changes.

It changes the **context-loading strategy**, not the authority hierarchy.

## Consequences

Builder context should become smaller and more task-specific.

Some tasks will still require broad grounding. The builder is responsible for recognizing when the boundary has been crossed and broadening grounding rather than guessing.

The desired optimization is:

> smallest sufficient context that safely completes the mission.

It is not:

> minimum possible context regardless of risk.

## Follow-up

Update the operational guidance and onboarding material to implement this decision. Subsequent work should observe whether targeted grounding reduces unnecessary context consumption without increasing missed dependencies, authority conflicts, or verification failures.
