# Renaissance Work Ledger

**Purpose:** A small working bookmark for continuing human/AI work.

This file is a navigation aid, not canon, architecture, a roadmap, a changelog,
or a replacement for Git history. Canonical authority remains in the
constitutional documents and recorded Decisions.

## Current Frontier

**Status:** Attention Choice contract ratified; implementation boundary is next.

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

### Decision boundary — resolved

Decision 0009 ratified the Attention Choice contract as a Renaissance architectural boundary.

- Decision: `DECISIONS/0009-establish-attention-choice-boundary.md`
- The proposal is accepted as the contract source; implementation details remain unresolved.
- `ARCHITECTURE.md` is synchronized.
- The contract does not authorize a storage format, runtime organ, universal ranking engine, autonomous agenda subsystem, or Episteme redesign.
- Authorization remains distinct from attention choice.

### Implementation-boundary investigation

The first implementation inspection is complete across Renaissance, Episteme, and the existing Organs runtime substrate.

**Finding:** there is no existing Renaissance-side Attention Choice persistence or request/selection object to reuse directly.

- Renaissance currently defines capability contracts and architecture, but has no runtime persistence layer for this semantic object.
- Episteme has mature durable SQLite persistence, workflow definitions/executions, provenance, and lineage, but its grounded `Record` model is explicitly epistemic and its record kinds are source/observation/measurement/dataset/experiment/result. Attention Choice does not belong there without distorting Episteme's responsibility.
- Episteme workflow execution preserves what ran and how; it should not be made responsible for the prior Renaissance choice that selected the work.
- Organs Communications already provides a durable SQLite event history with topic, event type, publisher, payload, independent consumer cursors, replay/debug inspection, and no requirement that the publisher's semantic object become an Organs-owned epistemic artifact.
- Organs Memory also has durable ledgers and structured state, but its model is specifically memory/facts/scars/promises/relations and is not an appropriate owner for Attention Choice semantics.

Therefore the smallest currently justified implementation boundary appears to be **an Attention Choice event carried through the existing Communications persistence mechanism**, while Renaissance retains ownership of the semantic contract. This is an integration hypothesis, not yet an implementation decision.

### Communications transport boundary test

The existing Communications core was checked directly.

**Result: PASS as a transport/persistence mechanism; no Communications code change is justified.**

Its event contract already provides exactly the structural envelope required by the Attention Choice record:

- durable SQLite event row;
- timestamp;
- topic;
- event type;
- publisher;
- arbitrary JSON payload;
- topic-indexed inspection;
- independent consumer cursors;
- replay/reset for inspection and recovery.

The Attention Choice minimum record can therefore live unchanged inside the payload. Its semantic fields remain Renaissance-owned; Communications does not need to understand or interpret them.

The important boundary is:

`Renaissance Attention Choice record → Communications event envelope → consumer`

This preserves the distinction between **transport/storage** and **semantic ownership**. It also avoids duplicating persistence in Renaissance or turning Organs into an Attention subsystem.

One limitation remains: Communications provides durable event transport, not a domain-level Attention Choice registry or query contract. That is acceptable for the current decision because no consumer/query requirement has yet been demonstrated. A domain-specific registry should only be added if a concrete use case requires lookup, lifecycle management, or validation beyond event replay/inspection.

**Implementation conclusion:** the existing Communications mechanism is sufficient for the first durable representation. No new persistence subsystem and no Communications semantic extension are currently justified.

The next grounded step is to define the smallest Renaissance-facing event contract needed to publish an Attention Choice, then test it end-to-end without inventing a registry or autonomous consumer.\n\n### Publisher boundary inspection\n\nTargeted inspection found no existing Renaissance-side HTTP client, Communications integration wrapper, or Attention publisher. Organs' established cross-organ convention is registry discovery followed by direct HTTP calls; Communications exposes a generic publish endpoint accepting `event_type`, `payload`, and `publisher` under a caller-selected topic.\n\n**Finding:** there is currently no justified existing Renaissance publisher to reuse. Creating a generic Communications client merely for Attention Choice would be premature infrastructure. The smallest next artifact is therefore the Renaissance-facing event contract itself, not runtime code.

Do **not** turn Communications into an Attention organ, move Attention Choice semantics into Organs, or modify Episteme merely to gain storage.

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
