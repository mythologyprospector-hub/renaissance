# Decision 0004 — Establish Relationship Interoperability as a Renaissance Architectural Responsibility

**Date:** 2026-09-24  
**Status:** Accepted  
**Authority:** Human Gate  
**Scope:** Renaissance architecture and cross-project interoperability

## Decision

Renaissance establishes **relationship interoperability** as a cross-project architectural responsibility.

Renaissance should provide a common way for independent systems to preserve and exchange explicit relationships without requiring those systems to share a universal ontology.

Relationship semantics remain owned by the system or domain that defines them.

## Rationale

Renaissance already contains systems with different kinds of relationships:

- Episteme uses relationships for epistemic and provenance structures.
- Organs uses relationships within runtime infrastructure.
- specialist instruments may use relationships for their own domain semantics.

The systems need to interoperate without being collapsed into one internal model.

Testing established that a useful interoperability boundary must tolerate:

- unfamiliar relationship types;
- relationships that later change status;
- conflicting assertions;
- translation between relationship vocabularies;
- copying and federation;
- references to objects not locally present;
- relationships from unrelated domains;
- and relationships that cannot be faithfully translated.

## Principles

1. **Relationship meaning remains explicit.**  
   A receiving system must not silently reinterpret an unfamiliar relationship.

2. **Independent systems may define specialized relationships.**  
   Participation in Renaissance does not require a universal relationship vocabulary.

3. **Transport does not imply agreement.**  
   Receiving a relationship does not establish that the receiver considers it true, valid, or authoritative.

4. **Translation does not rewrite the source.**  
   A mapping between relationship vocabularies is distinguishable from the original relationship.

5. **History is preserved.**  
   Later challenge, supersession, or reinterpretation must not require destruction of the earlier relationship.

6. **References may cross boundaries.**  
   A system may preserve a relationship involving objects it does not possess or understand.

7. **Failed translation must not silently corrupt meaning.**  
   If a relationship cannot be faithfully represented, preservation of the original meaning is preferred over lossy reinterpretation.

## Interoperability Boundary

The Renaissance-level responsibility is to establish a sufficiently small contract for carrying and preserving relationships across boundaries.

The contract should preserve enough information to distinguish, as applicable:

- the relationship being represented;
- the related references;
- the origin of the assertion;
- provenance and lineage;
- transformations of the representation.

The exact serialization, protocol, identifier scheme, mapping mechanism, and optional fields remain implementation questions until separately justified.

## Consequences

1. Renaissance may define interoperability requirements for relationships without defining every relationship's meaning.
2. Participating projects retain their internal relationship models and domain semantics.
3. An interoperability layer must not silently change epistemic status, authority, ownership, or meaning.
4. Relationship mappings and translations are themselves inspectable information rather than replacements for source assertions.
5. Future protocol work should begin from this boundary rather than from a universal Renaissance ontology.

## Non-decisions

This decision does not establish:

- a universal Renaissance ontology;
- a universal relationship vocabulary;
- a universal truth score;
- a universal data model;
- a final serialization format;
- a final interoperability protocol;
- ownership of participating systems' domain semantics;
- or a requirement that every participating system understand every relationship.

## Record

This decision records the relationship-interoperability responsibility established through architectural testing in September 2026.
