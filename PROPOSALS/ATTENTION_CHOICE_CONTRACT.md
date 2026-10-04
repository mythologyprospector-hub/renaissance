# Proposal — Renaissance Attention Choice Contract

**Status:** Proposed — not canon  
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
- **outcome reference** — what subsequently happened, without changing the choice itself into evidence.

## 3. What it is not

An Attention Choice is not:

- a truth claim;
- evidence;
- a confidence score;
- a universal importance score;
- a ranking of humanity's interests;
- an autonomous mandate;
- an Episteme finding, hypothesis, prediction, experiment, or result;
- permission to act merely because something was selected.

A choice records attention. It does not establish epistemic authority.

## 4. Human agency

Human curiosity may itself be sufficient represented pressure.

Renaissance may also notice represented gaps or unresolved questions and suggest that they deserve attention. A suggestion remains a suggestion unless the applicable authority permits progression.

The contract must distinguish:

- **ask** — Renaissance is requesting human direction;
- **suggest** — Renaissance proposes attention but has not received authorization to proceed;
- **execute** — the system has an already-established basis and authorization to perform the declared investigation.

Automation does not become consent merely because a target was selected.

## 5. Anti-daffodil rule

Interesting is not equivalent to relevant.

A target should not receive an investigation merely because Renaissance noticed it, can describe it, or finds it novel.

A proposed choice must point to represented pressure or explicit human curiosity. If no such basis exists, the system may record the observation or leave the matter available without spending an investigation cycle on it.

## 6. Boundary with Episteme

The intended relationship is:

`Renaissance Attention Choice → Episteme declared investigation → Episteme execution/result history`

Renaissance owns the meaning of the choice.

Episteme owns the semantics and provenance of the scientific investigation it receives.

Neither layer should manufacture the other's artifacts.

## 7. Minimum viable test

Before implementation, test the contract against at least these cases:

1. Human asks a new question.
2. Existing Episteme gap suggests a useful next investigation.
3. Several possible investigations exist with no universal ranking.
4. An interesting but unrelated observation appears.
5. Human rejects a suggested investigation.
6. A suggested investigation is accepted and executed.
7. An investigation produces a contradiction or new gap.

The contract succeeds only if each case remains inspectable without hidden importance scoring, epistemic promotion, or loss of provenance.

## 8. Open questions

This proposal intentionally does not decide:

- storage format;
- event versus record representation;
- implementation repository;
- universal selection algorithm;
- automatic generation policy;
- final authorization model;
- whether every human interaction should produce an Attention Choice.

Those questions require evidence from the minimum viable test.

## 9. Architectural consequence if accepted

If this proposal survives testing, Renaissance gains a small knowledge-growth boundary:

`curiosity / represented pressure → attention choice → investigation → result → memory → new pressure`

That boundary should remain a contract, not a new autonomous subsystem, unless later evidence demonstrates that a separate implementation is actually required.
