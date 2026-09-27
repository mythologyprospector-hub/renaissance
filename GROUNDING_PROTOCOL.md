# Renaissance — Grounding Protocol

**Status:** Operational guidance  
**Authority:** Implementation / operating procedure

## Purpose

The repository is the source of truth. Grounding restores the **relevant** current context; it is not a ritual of rereading the entire project.

Decision 0005 establishes targeted grounding as the normal operating procedure.

## 1. Orient

Establish enough current repository state to avoid stale work:

- repository identity and branch;
- current commit;
- recent relevant changes;
- files directly relevant to the mission;
- applicable tests/verification.

Use the generated `GROUNDING_SNAPSHOT.md` when present for rapid orientation. It is not authority and is not mandatory to reread after every turn.

## 2. Classify the mission

### Routine

Examples: implementation of an established requirement, local bug fix, test addition, or documentation synchronization that does not change established architecture.

Read the direct source of truth, affected implementation/tests, and only the authority needed to verify the task fits existing boundaries.

### Architectural

Examples: interface changes, capability boundaries, cross-project interoperability, runtime topology, or changes to established architecture.

Read the affected architecture and applicable Decisions plus the higher-level authority needed to verify compatibility.

### Foundational / constitutional

Examples: purpose, constitutional constraints, governance, change-control rules, foundational principles, or repository-wide authority.

Perform broad grounding and follow the applicable change-control process.

### Uncertain

If classification or source-of-truth ownership is unclear, broaden inspection until the uncertainty is resolved. Do not guess.

## 3. Authority routing

The repository authority map is:

- `STATUS.md` — state and authority classes
- `CHARTER.md` — purpose and scope
- `CONSTITUTION.md` — constitutional constraints
- `PRINCIPLES.md` — established principles
- `BOUNDARIES.md` — boundaries
- `EPISTEMOLOGY.md` — epistemic distinctions
- `GOVERNANCE.md` — authority and decision process
- `CHANGE_CONTROL.md` — change requirements
- `DECISIONS/` — recorded decisions
- `ARCHITECTURE.md` — current architecture
- applicable capability/project documents — task-specific requirements

These are a **routing map**, not a mandatory reading list for every task.

## 4. Repository and source-of-truth rules

The full repository tree is not a mandatory step for every mission.

Inspect broader tree structure when:
- the canonical source is unknown;
- duplicate sources may exist;
- repository-wide impact is plausible;
- a cross-project or architectural boundary is involved.

A previous conversation is historical context, not authority.

## 5. Re-grounding triggers

Broaden or refresh grounding when:

- repository state may have changed;
- another builder/contributor changed relevant files;
- the task moves into a new architectural area;
- an experiment becomes architecture or implementation;
- a governing document or applicable Decision changes;
- new evidence creates a conflict;
- current state becomes uncertain;
- the Human Gate says `ground`, `onboard`, `refresh`, or `check canon`.

A context transition alone does not require rereading unrelated authority.

## 6. Reconciliation

Distinguish:

- **Established** — supported by current authority;
- **Proposed** — under consideration;
- **Experiment** — bounded exploration;
- **Implementation** — current machinery;
- **Unknown** — not established;
- **Stale** — previously observed but not confirmed current.

If applicable current authority conflicts, stop and resolve through change control.

## 7. Settled decisions

Do not reopen established Decisions merely because a task touches their subject.

Reopen only for new evidence, contradiction, implementation/test failure, changed requirement, explicit reconsideration, or a consequence that crosses an established authority boundary.

## 8. Final verification

Before reporting completion, verify against the current repository state and applicable tests. If drift occurred, refresh the relevant grounding before final verification.

## Human Gate shorthand

A single `.` means proceed/continue/accepted within the established direction. It does not waive authority, testing, or change-control requirements.
