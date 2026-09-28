# Proposal — Minimal Relationship Interoperability Contract

**Status:** Evidence incorporated into Decision 0006  
**Authority:** Proposal / Historical evidence  
**Relationship to canon:** Decision 0006 now establishes the minimum architectural boundary described by this proposal. This document does not independently amend canon or architecture.  
**Basis:** Decision 0004 and the completed relationship-interoperability experiment chain.

## Purpose

This proposal was created to make the architectural question reviewable before authorization. Its experimentally supported minimum guarantees were subsequently authorized by Decision 0006.

## Authorized outcome

Decision 0006 establishes the minimum relationship-interoperability invariants covering identity, references, explicit meaning, origin/provenance, transformation, history, epistemic neutrality, security separation, failure transparency, and domain independence.

Decision 0006 deliberately leaves final serialization, protocol, identifiers, transport, vocabulary, ontology, translation dictionary, federation mechanism, and security mechanism unresolved.

## Evidence retained

The experiment chain remains the supporting evidence for Decision 0006, including bounded work on:

- identity;
- version negotiation and unknown-field preservation;
- transport semantics;
- provenance and transformation lineage;
- extensions and conditional-field preservation;
- translation;
- federation;
- security boundaries;
- candidate protocol shapes;
- and Renaissance-level versus project-level requirement scope.

The experiments and this proposal remain historical evidence and are not replaced by the decision record.

## Historical note

The proposal originally recommended returning the minimum-boundary question to the Human Gate. That question has now been decided by Decision 0006.

Future protocol-design work must begin from the authorized boundary and must not silently promote implementation choices into additional Renaissance architecture.
