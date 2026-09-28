# Decision 0006 — Establish Minimum Relationship Interoperability Boundary

**Date:** 2026-09-28  
**Status:** Accepted  
**Authority:** Human Gate  
**Scope:** Renaissance architecture and cross-project relationship interoperability

## Matter

Determine whether the completed relationship-interoperability experiment chain has established a sufficiently stable minimum boundary for Renaissance to authorize as an architectural requirement, without selecting a final protocol or universal relationship model.

## Prior state

Decision 0004 established relationship interoperability as a Renaissance architectural responsibility while leaving the exact contract, serialization, protocol, identifier scheme, mapping mechanism, and optional fields as implementation questions requiring separate justification.

Subsequent bounded experiments examined identity, version negotiation, transport semantics, provenance and lineage, extensions, translation, federation, security boundaries, candidate protocol shapes, and requirement scope.

## Evidence

The completed experiment chain consistently supports the following boundary properties:

- relationship identity remains distinguishable;
- participants and unresolved references remain preservable;
- relationship meaning remains explicit;
- unfamiliar relationship types do not require reinterpretation;
- origin, provenance, and lineage remain distinguishable from destination metadata;
- transformations remain distinguishable from source assertions;
- status history can survive without destructive rewriting;
- transport does not imply truth, agreement, validity, ownership, or authority;
- authentication and authorization remain distinct from epistemic status;
- failed or unfaithful translation does not silently corrupt source meaning;
- independent domains can interoperate without a universal ontology or vocabulary;
- unknown extensions and version-incompatible information can be handled without silent semantic loss.

The candidate protocol-shape experiments further show that the accumulated guarantees can be represented without requiring a universal Renaissance data model, while also showing that opaque transport can lose required meaning.

These experiments remain evidence and do not themselves constitute authority.

## Decision

Renaissance **establishes the following minimum relationship-interoperability invariants as an architectural boundary**:

1. **Identity:** distinct relationships must remain distinguishable.
2. **References:** relevant participants and unresolved external references must remain representable.
3. **Meaning:** source relationship meaning must remain explicit; unfamiliar meaning must not be silently reinterpreted.
4. **Origin and provenance:** source origin and applicable provenance/lineage must remain distinguishable.
5. **Transformation:** translation, mapping, federation, and other transformations must remain distinguishable from the source assertion.
6. **History:** applicable relationship status and history must not require destructive rewriting of prior state.
7. **Epistemic neutrality:** transport must not manufacture truth, agreement, verification, validity, ownership, or authority.
8. **Security separation:** authentication and authorization must remain distinct from epistemic status and agreement.
9. **Failure transparency:** an unfaithful representation or translation must fail explicitly or preserve the original meaning rather than silently corrupt it.
10. **Domain independence:** interoperability must not require a universal Renaissance ontology, relationship vocabulary, or identical internal data model.

## Authorization boundary

This decision authorizes the invariants above as Renaissance architectural requirements.

It does **not** authorize or establish:

- a final serialization format;
- a final wire protocol;
- a universal identifier scheme;
- a universal relationship vocabulary or ontology;
- a universal translation dictionary;
- a mandatory federation mechanism;
- a specific transport technology;
- a universal security mechanism;
- or ownership of participating projects' domain semantics.

Those remain separate design questions.

## Implementation consequence

Future protocol and interoperability implementation may proceed only from these authorized invariants and must remain subordinate to the established change-control process.

Implementation choices must not silently become additional Renaissance architectural requirements.

Where implementation requires a new substantive boundary or resolves an explicitly open architectural question, the appropriate Decision record must precede or authorize that change.

## Historical preservation

The experiment records and the proposal that preceded this decision remain part of Renaissance history and evidence. This decision does not erase, rewrite, or collapse those records.

## Relationship to existing authority

This decision extends Decision 0004 by authorizing the minimum boundary established through subsequent bounded experimentation.

It does not supersede the Constitution, Charter, Decision 0004, or the change-control process.
