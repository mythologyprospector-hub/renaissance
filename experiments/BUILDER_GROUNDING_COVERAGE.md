# Builder Grounding Experiment — Coverage

**Status:** Bounded experiment  
**Authority:** Experiment  
**Relationship to canon:** This experiment does not establish or amend Renaissance authority.

## Purpose

Test the operational routing rules introduced by Decision 0005 without pretending that a deterministic fixture can measure hidden model-token consumption.

## Current coverage

| Behavior | Evidence |
| --- | --- |
| Routine work avoids full authority preload | `test_routine_task_does_not_preload_full_authority` |
| Routine work loads applicable Decisions | `test_routine_task_includes_only_applicable_decisions` |
| Architectural work adds affected architecture | `test_architectural_task_adds_architecture_without_full_preload` |
| Foundational work broadens grounding | `test_foundational_task_requires_broad_grounding` |
| Uncertain classification broadens rather than guesses | `test_uncertain_task_broadens_instead_of_guessing` |
| Experiment promotion broadens grounding | `test_boundary_crossing_broadens_routine_task` |
| Repository-wide impact broadens grounding | `test_repository_wide_impact_broadens_grounding` |
| Settled decisions remain closed without a trigger | `test_settled_decision_stays_closed_without_trigger` |
| New evidence can reopen a decision | `test_new_evidence_reopens_decision` |
| Implementation failure can reopen a decision | `test_test_failure_reopens_decision` |
| Explicit reconsideration can reopen a decision | `test_explicit_reconsideration_reopens_decision` |

## Interpretation

Passing these tests establishes only that the proposed routing rules behave as encoded.

They do **not** establish:
- actual model context/token consumption;
- that a model will always classify a task correctly;
- that the routing set is complete for every future task;
- that targeted grounding is universally safer or faster;
- any new constitutional authority.

The important empirical follow-up is observation during real builder work: when targeted grounding misses something, the protocol must broaden rather than guess.

## Known limitation

The experiment cannot observe hidden model context usage. Token efficiency must therefore be evaluated through externally observable proxies such as retrieval volume, repeated document loading, turns consumed, and useful work completed.