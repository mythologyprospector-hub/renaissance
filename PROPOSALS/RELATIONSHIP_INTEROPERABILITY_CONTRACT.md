# Proposal — Minimal Relationship Interoperability Contract

**Status:** Proposed  
**Authority:** Proposal  
**Relationship to canon:** This document does not amend Renaissance canon, Decision 0004, or the current architecture.  
**Basis:** Decision 0004 and the completed relationship-interoperability experiment chain.

## 1. Purpose

Define a candidate minimum contract for exchanging explicit relationships between independent systems while preserving domain ownership, provenance, uncertainty, history, and the distinction between transport and agreement.

This proposal exists to make the architectural question reviewable. It is not itself an implementation specification or final protocol.

## 2. Evidence

The relationship-interoperability experiment chain has now exercised the boundary in bounded stages covering:

- relationship identity;
- version negotiation and preservation of unknown fields;
- transport semantics;
- provenance and transformation lineage;
- extension and conditional-field preservation;
- security separation from epistemic status;
- candidate protocol shapes;
- and Renaissance-level versus project-level requirement scope.

The completed experiments consistently preserve the boundary established by Decision 0004: meaning, origin, lineage, history, and epistemic neutrality are protected at the interoperability boundary, while domain vocabulary, semantics, serialization, transport, identifiers, and security mechanisms remain project-level choices.

The candidate-shape experiment distinguishes representations that satisfy the accumulated minimum guarantees from representations that lose source semantics. It does not select a final protocol or serialization.

The requirement-scope experiment likewise explicitly classifies a bounded candidate set without establishing a universal protocol, field names, identifier scheme, transport standard, security standard, or architectural amendment.

The CI workflow was extended to include the relationship requirement-scope experiment.

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

Security properties such as authentication and authorization must remain distinct from epistemic status.

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

## 9. Experimental questions now covered

The following questions were previously identified as protocol-design questions and have now received bounded experimental treatment:

1. **Smallest stable identity:** identity remains opaque to the interoperability layer and stable across transport; origin plus identity distinguishes otherwise identical identity text from different origins.
2. **Conditional envelope elements:** identity, participants, and relationship meaning form the experiment-level core; provenance and status history can remain conditional where applicable.
3. **Unknown extensions:** unfamiliar fields/extensions can survive the boundary without requiring interpretation.
4. **Version negotiation:** incompatible versions fail explicitly; a highest common supported version can be selected; unknown fields can survive the version boundary.
5. **Faithful translation:** transformations remain distinguishable from source assertions; lossy translation must not silently replace source meaning.
6. **Lineage:** transformations can retain source and output relationship identities and preserve lineage.
7. **Transport:** transport metadata remains separate from relationship meaning, provenance, authority, and agreement.
8. **Security boundary:** authentication and authorization remain security metadata rather than epistemic status or agreement.
9. **Requirement scope:** boundary invariants can be separated from project-level vocabulary, semantics, and implementation choices using an explicit classification rule.

These experiments are evidence, not automatic authorization for architecture or implementation.

## 10. Proposed next-stage decision

The experimental chain is sufficiently developed to return the minimum-boundary question to the Human Gate for an explicit architectural decision.

The proposed decision would authorize Renaissance to establish the experimentally supported minimum interoperability invariants as an architectural boundary, while explicitly preserving the unresolved implementation questions.

The decision should **not** authorize a final protocol, serialization, identifier scheme, transport standard, universal vocabulary, or security mechanism.

If accepted, implementation work should begin only from the authorized boundary and should remain subordinate to the established change-control process.

If rejected or returned for revision, the experimental record remains intact and no implementation is implied.

## 11. Relationship to existing authority

This proposal derives from and remains subordinate to:

- the Renaissance Constitution;
- Charter and Principles;
- Decision 0004;
- current Architecture;
- and the established change-control process.

It does not supersede or modify any of them.
