# Proposal — Renaissance Attention Choice Contract

**Status:** Accepted by Decision 0009 — implementation details remain unresolved  
**Scope:** Renaissance knowledge-growth / investigation selection boundary  
**Purpose:** Define the smallest durable semantic boundary between represented pressure and declared investigation without creating a universal ranking system.

## 1. Problem

Renaissance can already preserve knowledge, provenance, unresolved questions, hypotheses, experiments, results, and execution history through its existing constellation.

What is currently missing is the explicit transition:

`represented pressure → choice of what to attend to → declared work`

Episteme can preserve why a workflow was constructed and what it executed, but the workflow should not retroactively become the reason that investigation was selected.

## 2. Proposed semantic unit

An **Attention Choice** is a declared decision to give an identified matter attention.

It should preserve, at minimum:

- **pressure** — the represented unresolved question, gap, human curiosity, or other explicit reason that brought the matter forward;
- **target** — what is being attended to;
- **supporting references** — the knowledge, observations, questions, or other represented material that informed the choice;
- **selection basis** — the explicit reason or rule by which this target was chosen;
- **alternatives** — other represented candidates considered or intentionally left available, when applicable;
- **mode** — whether Renaissance is asking the human, suggesting an investigation, or proceeding with an already-authorized investigation;
- **outcome reference** — what subsequently happened, without changing the choice itself into evidence;
- **authorization reference** — where execution requires separate authorization, a reference to the established source that authorized progression.

## 3. Minimal record shape

If the contract is later implemented, the smallest proposed durable representation is a **referential choice record**. It records the relationship and decision; it does not duplicate the semantics of the material it references.

Conceptually:

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

### Field rules

- **id** identifies this choice record.
- **pressure_ref** points to the represented pressure that gave rise to the choice. This may be a question, gap, explicit human curiosity, or another established pressure representation.
- **target_ref** identifies what the choice attends to.
- **supporting_refs[]** points to material that materially informed the choice. Empty is permitted when the pressure itself is sufficient.
- **selection_basis** is a short, inspectable local reason or explicit selection rule. It must not be a hidden utility function, universal importance score, or opaque ranking value.
- **alternative_refs[]** identifies materially available alternatives when alternatives actually existed. It may be empty.
- **mode** is one of `ask`, `suggest`, or `execute`.
- **authorization_ref** is optional. When present, it points to the already-established source of authorization that permits progression into execution. It is provenance for authorization, not the authorization itself, and its presence must not be interpreted as a new authority mechanism.
- **outcome_ref** is optional and may be added only after subsequent work produces something referable. It does not turn the Attention Choice into evidence or retroactively justify the original selection.

### Referential boundary

The record should answer:

> **Why was this target selected for attention now?**

And, when applicable:

> **What established source authorized progression?**

It should not attempt to answer:

> **Is the target true?**

> **Is the target important to humanity in general?**

> **What scientific result did the investigation produce?**

Those questions belong to other established semantic layers.

## 4. What it is not

An Attention Choice is not:

- a truth claim;
- evidence;
- a confidence score;
- a universal importance score;
- a ranking of humanity's interests;
- an autonomous mandate;
- an authority model;
- an Episteme finding, hypothesis, prediction, experiment, or result;
- permission to act merely because something was selected.

A choice records attention. It does not establish epistemic or operational authority.

## 5. Human agency

Human curiosity may itself be sufficient represented pressure.

Renaissance may also notice represented gaps or unresolved questions and suggest that they deserve attention. A suggestion remains a suggestion unless the applicable authority permits progression.

The contract must distinguish:

- **ask** — Renaissance is requesting human direction;
- **suggest** — Renaissance proposes attention but has not received authorization to proceed;
- **execute** — the system has an already-established basis and authorization to perform the declared investigation.

Automation does not become consent merely because a target was selected.

## 6. Anti-daffodil rule

Interesting is not equivalent to relevant.

A target should not receive an investigation merely because Renaissance noticed it, can describe it, or finds it novel.

A proposed choice must point to represented pressure or explicit human curiosity. If no such basis exists, the system may record the observation or leave the matter available without spending an investigation cycle on it.

## 7. Boundary with Episteme

The intended relationship is:

`Renaissance Attention Choice → authorization (when required) → Episteme declared investigation → Episteme execution/result history`

Renaissance owns the meaning of the choice.

Episteme owns the semantics and provenance of the scientific investigation it receives.

Neither layer should manufacture the other's artifacts.

Authorization remains outside the Attention Choice's authority semantics; the choice merely preserves a reference to the established authorization when needed for provenance.

## 8. Minimum viable test

Before implementation, test the contract against at least these cases:

1. Human asks a new question.
2. Existing Episteme gap suggests a useful next investigation.
3. Several possible investigations exist with no universal ranking.
4. An interesting but unrelated observation appears.
5. Human rejects a suggested investigation.
6. A suggested investigation is accepted and executed, with separate authorization provenance where required.
7. An investigation produces a contradiction or new gap.

The contract succeeds only if each case remains inspectable without hidden importance scoring, epistemic promotion, authorization leakage, or loss of provenance.

## 9. Open questions

This proposal intentionally does not decide:

- storage format;
- event versus record representation;
- implementation repository;
- universal selection algorithm;
- automatic generation policy;
- final authorization model;
- whether every human interaction should produce an Attention Choice.

Those questions require evidence from the minimum viable test and subsequent implementation experience.

## 10. Architectural consequence if accepted

If this proposal survives testing, Renaissance gains a small knowledge-growth boundary:

`curiosity / represented pressure → attention choice → authorization when required → investigation → result → memory → new pressure`

That boundary should remain a contract, not a new autonomous subsystem, unless later evidence demonstrates that a separate implementation is actually required.
