# Decision 0009 — Establish the Attention Choice Boundary

**Status:** Ratified  
**Authority:** Human Gate  
**Date:** 2026-10-04

## Matter

Renaissance needs a durable semantic boundary between represented pressure or human curiosity and the decision to give a particular matter attention.

The question is whether that boundary should be established as an explicit Renaissance architectural contract without creating a universal ranking system, duplicating Episteme's epistemic records, or granting the system autonomous authority to determine what humanity should pursue.

## Prior state

No established Renaissance request, intent, attention, selection, or investigation-choice contract owned this transition.

Episteme already preserves scientific work after selection, including findings, hypotheses, predictions, experiments, results, workflow lineage, and provenance. Those structures explain what was investigated and how it was conducted, but they do not own the prior decision that a particular matter was selected for attention.

The working proposal therefore identified the missing transition as:

`represented pressure → choice of what to attend to → declared investigation`

## Evidence and reasoning

The proposed Attention Choice contract was validated through three focused experiments:

- `experiments/ATTENTION_CHOICE_MVT.md`
- `experiments/ATTENTION_CHOICE_RECORD_MVT.md`
- `experiments/ATTENTION_CHOICE_AUTHORIZATION_MVT.md`

The latest validation established that the distinction remains coherent across human questions, Episteme-derived gaps, competing possible investigations, unrelated novelty, rejection, accepted execution, and contradictory results.

The authorization test established a further necessary distinction:

`Attention Choice ≠ Authorization ≠ Investigation`

In particular:

- selecting something for attention does not grant permission to act;
- `mode: execute` does not manufacture permission;
- an existing authorization may be referenced without becoming part of the Attention Choice authority model;
- a later outcome does not retroactively justify the original selection.

The contract also preserves the anti-daffodil boundary: novelty or notice alone is not sufficient reason to spend an investigation cycle. A choice must have a traceable relationship to represented pressure or explicit human curiosity.

## Decision

Renaissance hereby establishes **Attention Choice** as a system-level architectural contract at the Renaissance knowledge-growth boundary.

An Attention Choice is a declared decision to give an identified matter attention.

The minimum referential record is:

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

### Semantics

- `pressure_ref` identifies the represented pressure, unresolved question, gap, or equivalent originating reason.
- `target_ref` identifies the matter selected for attention.
- `supporting_refs[]` preserves represented material supporting consideration of the target.
- `selection_basis` records an inspectable local reason or explicit selection rule. It must not conceal a universal utility, importance, or ranking calculation.
- `alternative_refs[]` records alternatives considered or left available.
- `mode` distinguishes whether the system is asking, suggesting, or executing.
- `authorization_ref` is optional and refers to an already-established source of authorization when separate authorization is required. It is provenance for authorization, not authorization itself.
- `outcome_ref` is optional and points to subsequent work or result. It does not become evidence and does not retroactively justify the choice.

## Architectural boundary

The established relationship is:

```
represented pressure
        ↓
Attention Choice
        ↓
established authorization, when required
        ↓
declared investigation
        ↓
Episteme execution and result history
```

Attention Choice belongs above Episteme's scientific execution machinery.

Episteme remains responsible for the investigation it receives, its scientific semantics, and its execution provenance.

Attention Choice does **not** become:

- a truth claim;
- evidence;
- a confidence score;
- a universal importance score;
- a ranking of humanity's interests;
- an autonomous mandate;
- an authority mechanism;
- an Episteme finding, hypothesis, prediction, experiment, or result;
- permission merely because a target was selected.

## Human agency

The contract preserves the existing Renaissance authority model.

Human curiosity may originate an Attention Choice.

The system may formulate a suggestion when supported by represented pressure.

A system choice does not override an existing authorization boundary.

The contract does not establish a new machine authority or self-directed mandate.

## Affected documents

- `PROPOSALS/ATTENTION_CHOICE_CONTRACT.md` — source proposal is now marked accepted by this decision; its historical development remains preserved.
- `ARCHITECTURE.md` — synchronized to recognize Attention Choice as a Renaissance knowledge-growth boundary.
- `WORK_LEDGER.md` — advanced to the post-decision implementation boundary.

The validation experiments remain historical evidence and are not themselves architectural authority.

## Effective status

**Effective immediately as a Renaissance architectural contract.**

This decision authorizes future implementation work against the contract.

It does **not** authorize a particular storage mechanism, runtime organ, universal ranking engine, autonomous agenda subsystem, or Episteme redesign.

Those remain unresolved until separately justified.

## Superseded material

No prior decision is superseded.

The prior Attention Choice proposal was exploratory material below the authority of this decision. It is now accepted as the basis for the established contract, with this decision controlling where the proposal and this record differ.

## Implementation constraint

Implementation must follow the established contract and existing change-control process.

Before implementation, the responsible boundary must determine the smallest appropriate durable representation and integration point. No implementation may silently expand Attention Choice into a ranking system, authority mechanism, or autonomous agenda setter.
