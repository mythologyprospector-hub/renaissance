# Renaissance Work Ledger

**Purpose:** A small working bookmark for continuing human/AI work.

This file is a navigation aid, not canon, architecture, a roadmap, a changelog,
or a replacement for Git history. Canonical authority remains in the
constitutional documents and recorded Decisions.

## Current Frontier

**Status:** Attention Choice contract validated; formal decision gate pending.

### Last verified stopping point

The Learn 001A experiment and delayed-retention follow-up are complete:

- Initial execution recorded baseline, instruction, immediate performance, transfer, and reflection.
- Delayed retest used a new directory layout with no hints or re-teaching.
- All four path-resolution questions were answered correctly, providing bounded evidence of delayed retention and transfer.
- **Commit:** `e1926b106e8c07b80b9a9baf67fa2dd24fe5f24b9`
- No implementation of Learn was introduced.

### Cross-repository catch-up finding

A world-level review found that Praxis and Episteme completed their first explicit evidence handoff boundary on 2026-10-03.

- Praxis records the problem/intervention/test/result domain semantics.
- Praxis explicitly admits evidence through a human decision boundary.
- Episteme has a canonical Praxis handoff adapter that preserves the supplied Praxis evidence and admission objects, assigns an Episteme-owned identity, and preserves provenance without making Praxis a runtime dependency.
- Praxis commits: `7baa1db6`, `1aca6554`, `873c54e8`, `740ff5bf`, `e3bb5b8b`
- Episteme commits: `ce3d5464`, `a0c3a347`, `72cd2555`, `0ea499c1`, `8f88274f`

The Renaissance-facing relationship was checked against `ARCHITECTURE.md` and `CONSTELLATION_AUDIT.md`.

**Result:** this is documentation synchronization, not a missing Renaissance architecture boundary.

The smallest justified change was made in `CONSTELLATION_AUDIT.md`:

- Praxis is recorded as a supporting/satellite project.
- The concrete Praxis→Episteme handoff is recorded as an existing constellation relationship.
- No Renaissance runtime interface, dependency, or ownership was introduced.
- The audit now explicitly records that the existing Renaissance interoperability and authority rules are sufficient for this relationship.

**Commit:** `c3ff5d0b1fb32788b36094c853f8b55e00cc91bf`

### Human-facing interaction discovery

Recent role-play established that Renaissance should not require the human to classify a request into a capability or workflow before receiving useful help.

Examples tested:

- curiosity that could become a small self-run experiment (color and mood);
- a request for a way into an unfamiliar subject (systems);
- conceptual exploration with boundary-checking ("anti-magnets");
- observations and meaning-bearing thoughts ("the stars are beautiful", a poetic thought about God);
- causal curiosity about a person and history (Van Gogh).

The important finding is broader than question answering: a human-facing Renaissance must be able to recognize the kind of moment it is in and respond proportionately. Sometimes that means investigation, sometimes learning, sometimes conceptual exploration, and sometimes simply participating in a human moment without turning it into a task.

### Knowledge-growth hypothesis

The latest discussion points toward a stronger hypothesis:

> Renaissance may be most useful as a system for reasoning over, accumulating, connecting, testing, and expanding knowledge, with the human participating rather than manually driving every step.

A possible long-running cycle is:

`curiosity → exploration → reasoning → evidence/experiment → knowledge → memory → connections → new questions`

A further possibility is that the system can generate some of its own next questions and investigations rather than waiting for the human to supply every step.

This is **not yet an architecture decision** and does not justify a new repository or subsystem by itself.

The investigation that followed established that the missing pressure is **attention**, not another epistemic-memory object.

### Attention Choice investigation

The grounded investigation established:

- Episteme already preserves findings, hypotheses, predictions, experiments, results, evaluations, workflow lineage, acquisition lineage, and provenance.
- The missing seam is the transition:
  `represented pressure → choice of what to attend to → declared work`
- Renaissance has no existing request/intent/selection contract that owns this seam.
- A universal importance score or global ranking mechanism is neither present nor justified.
- The smallest useful semantic unit is an **Attention Choice**: a declared decision to give an identified matter attention.
- The choice belongs above Episteme's scientific execution machinery.
- Episteme remains responsible for the investigation it receives and its scientific provenance.

The proposed contract was created at:

`PROPOSALS/ATTENTION_CHOICE_CONTRACT.md`

It remains explicitly **Proposed — not canon**.

### Attention Choice record validation

The proposed referential record was tested against seven knowledge-growth cases.

The record shape is:

```
AttentionChoice
  id
  pressure_ref
  target_ref
  supporting_refs[]
  selection_basis
  alternative_refs[]
  mode
  authorization_ref?
  outcome_ref?
```

The tests established:

- human curiosity can supply pressure directly;
- an Episteme gap can motivate a suggestion without making Episteme the agenda setter;
- multiple candidates can be handled without universal ranking;
- unrelated novelty does not justify investigation;
- rejection remains a valid outcome;
- investigation results remain separate from the original choice;
- a choice does not become permission merely because execution follows.

The authorization test exposed and resolved one real provenance seam: when execution requires separate authorization, the choice must preserve a reference to that established authorization without becoming an authority object itself.

Validation records:

- `experiments/ATTENTION_CHOICE_MVT.md`
- `experiments/ATTENTION_CHOICE_RECORD_MVT.md`
- `experiments/ATTENTION_CHOICE_AUTHORIZATION_MVT.md`

Latest validation commit:

**`3b040d21150e24ca864034983b26bdd6c72409d2`**

### Current decision boundary

The Attention Choice concept and its minimum record shape have now survived the concrete validation cases examined so far.

The next step is **not implementation**.

Because adopting this as an established Renaissance architectural contract would be a substantive change, the project's `CHANGE_CONTROL.md` requires a decision record and `GOVERNANCE.md` places final authority with the Human Gate during the founding phase.

Therefore the next grounded task is to prepare the formal decision record for human review, preserving the current proposal and experiments as evidence.

Do **not**:

- implement storage;
- create a runtime Attention organ;
- create a universal ranking or importance engine;
- make Attention Choice an authorization mechanism;
- make Episteme responsible for global agenda selection;
- silently promote the proposal to canon.

If the Human Gate does not adopt the contract, the proposal and experiments remain useful historical evidence and no implementation follows.

## Last Known Organs Boundary

Organs has a real Communications BUS carrying Memory events, but current
Renaissance requirements do not establish a consumer for those topics.

Archaeology confirmed that this is an available integration seam, not a missing
component or current architectural defect. No subscriber, organ, protocol, or
Decision is required at this time.

If a concrete capability later requires one of these events, establish the
responsible contract at that time before implementing the consumer.

## Ledger Rule

Keep this document small.

Move the pointer rather than turning this into a diary. The useful question is:

> **Where were we, and what was the next grounded place to look?**

Git is the long-term record. The ledger is the bookmark. Conversation is the
scratchpad.
