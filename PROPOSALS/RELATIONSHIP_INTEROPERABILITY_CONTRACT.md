# Proposal — Minimal Relationship Interoperability Contract

**Status:** Proposed  
**Authority:** Proposal  
**Relationship to canon:** This document does not amend Renaissance canon, Decision 0004, or the current architecture.  
**Basis:** Decision 0004 and the completed relationship-interoperability experiment.

## 1. Purpose

Define a candidate minimum contract for exchanging explicit relationships between independent systems while preserving domain ownership, provenance, uncertainty, history, and the distinction between transport and agreement.

This proposal exists to make the architectural question reviewable. It is not itself an implementation specification or final protocol.

## 2. Evidence

The bounded experiment exercised all eleven behaviors identified by Decision 0004:

1. relationship semantics survive transport;
2. transport does not add epistemic authority;
3. the source relationship is not hidden inside an opaque payload;
4. unfamiliar relationship types remain opaque;
5. references to objects not locally present remain preservable;
6. conflicting assertions remain distinct;
7. status history survives transport without rewriting history;
8. translation can be represented without replacing the source semantics;
9. federation preserves source identity and provenance;
10. relationships from unrelated domains can cross the boundary without a shared ontology;
11. an unfaithful translation fails rather than silently changing meaning.

The final experiment-test run and final grounding snapshot both passed in CI for the completed experiment state.

## 3. Proposed minimum guarantees

A Renaissance relationship interoperability contract should require that an interoperable representation be able, as applicable, to preserve or explicitly represent:

### 3.1 Relationship identity

The represented relationship must remain distinguishable from other relationships.

An interoperability layer must not silently merge distinct assertions merely because their participants or predicates appear similar.

### 3.2 Participants and references

The representation should identify the relevant participants or references.

References may identify objects that the receiving system does not possess, resolve, or understand.

Unresolved references must remain representable rather than being silently discarded or replaced.

### 3.3 Relationship meaning

The source relationship's semantic expression must remain explicit.

An unfamiliar relationship type must be carried as unfamiliar rather than silently mapped into a receiver-defined meaning.

### 3.4 Origin and provenance

The representation should preserve the source/origin and applicable provenance or lineage.

Copying or federation must not erase the relationship's origin.

### 3.5 Transformations

Translations, mappings, federation metadata, or other transformations should be distinguishable from the source relationship.

A transformation must not masquerade as the original assertion.

### 3.6 Status and history

Where the source system records relationship status or status changes, that history should remain available without destructive rewriting.

A later status must not require erasing the earlier record.

### 3.7 Epistemic and authority neutrality

Transport alone must not imply truth, agreement, verification, validity, ownership, or authority.

The interoperability layer must not manufacture epistemic status that was absent from the source representation.

### 3.8 Failure transparency

If a relationship cannot be faithfully represented or translated, the interoperability mechanism must fail explicitly or preserve the original representation rather than silently corrupting its meaning.

## 4. Domain independence

The contract should be intentionally domain-neutral.

Participation must not require:

- a universal Renaissance ontology;
- a universal relationship vocabulary;
- identical internal data models;
- identical domain semantics;
- or the ability to understand every relationship received.

A receiving system may carry a relationship without being capable of interpreting it.

## 5. Translation boundary

Translation should be treated as a transformation between representations, not as replacement of the source assertion.

A faithful mapping may produce a target-domain representation while retaining enough information to identify:

- the source relationship;
- the source relationship type;
- the target representation;
- the mapping or transformation;
- and, where applicable, whether the mapping is known to be faithful.

The contract should not require a universal translation service.

## 6. Federation boundary

Federation or copying should preserve lineage to the originating relationship.

A federated copy may acquire destination-specific metadata, but destination metadata must not silently become source provenance or source authority.

Federation is transport/copy semantics, not agreement semantics.

## 7. Candidate contract shape

A future protocol could therefore be organized conceptually around a small envelope containing, as applicable:

```
relationship
participants / references
origin
provenance / lineage
status history
transformations
```

This is a conceptual decomposition, not a proposed final serialization.

The exact field names, wire format, identifier scheme, versioning model, transport protocol, required/optional status, and extensibility mechanism remain open.

## 8. Explicit non-goals

This proposal does not establish:

- a universal ontology;
- a universal predicate vocabulary;
- a universal relationship schema;
- a universal truth or confidence score;
- a final wire format;
- a final identifier system;
- a universal translation dictionary;
- a mandatory federation mechanism;
- ownership of participating projects' domain semantics;
- or a requirement that every project implement every part of the candidate envelope.

## 9. Architectural questions still open

Before a final protocol is authorized, the following questions should be considered separately:

1. What is the smallest stable identity requirement?
2. Which envelope elements are mandatory versus conditional?
3. How should unknown extensions be preserved?
4. How should version negotiation work, if needed?
5. What constitutes a faithful translation?
6. How should provenance and transformation lineage be represented?
7. What transport mechanisms, if any, should Renaissance standardize?
8. How should security, authenticity, and authorization relate to—but remain distinct from—epistemic authority?
9. Which requirements belong at Renaissance level versus individual project contracts?

These are protocol-design questions, not assumptions to be resolved by implementation.

## 10. Recommendation for next stage

Treat this document as a **proposal for review**, not as an accepted architectural requirement.

If the Human Gate accepts the direction, the next bounded work should be a protocol-design experiment comparing candidate representations against the established guarantees.

Any resulting substantive architectural requirement should receive its own Decision record before implementation becomes authoritative.

## 11. Relationship to existing authority

This proposal derives from and remains subordinate to:

- the Renaissance Constitution;
- Charter and Principles;
- Decision 0004;
- current Architecture;
- and the established change-control process.

It does not supersede or modify any of them.
