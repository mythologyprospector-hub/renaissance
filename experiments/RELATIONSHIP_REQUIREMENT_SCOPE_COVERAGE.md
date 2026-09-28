# Relationship Requirement Scope Experiment Coverage

**Status:** Experiment  
**Authority:** Experiment  
**Scope:** Protocol-design question 9 from `PROPOSALS/RELATIONSHIP_INTEROPERABILITY_CONTRACT.md)

This experiment does not amend canon, Decision 0004, or architecture.

## Question

Which requirements belong at Renaissance level versus individual project contracts?

## Experimental classification rule

A requirement is treated as **Renaissance-level** when it protects the cross-project interoperability boundary itself without prescribing a project's domain semantics or implementation.

A requirement is treated as **project-level** when it chooses domain vocabulary, internal semantics, serialization, transport, identifier syntax, security mechanism, or other implementation-specific behavior.

## Covered Renaissance-level boundary invariants

- relationship identity;
- participants and references;
- relationship meaning preservation;
- origin and provenance;
- transformation distinction;
- status/history preservation;
- epistemic/authority neutrality;
- failure transparency.

## Covered project-level choices

- domain relationship vocabulary;
- domain semantics;
- internal data model;
- translation dictionary;
- wire format;
- transport protocol;
- identifier syntax;
- security mechanism.

## Result

The candidate set is fully classified by the experimental rule.

This is evidence for a layered boundary: Renaissance can specify preservation/integrity invariants while projects retain ownership of domain semantics and implementation choices.

## Non-conclusions

This experiment does **not** establish:

- a final Renaissance protocol;
- mandatory field names or serialization;
- a universal domain vocabulary;
- a universal identifier scheme;
- a transport or security standard;
- that every project must implement every candidate guarantee;
- or an architectural amendment.

A requirement that does not fit the classification rule remains unresolved rather than being forced into either layer.

## Evidence boundary

The experiment tests the classification rule against a bounded candidate set derived from Decision 0004 and the existing proposal. It does not prove that every future interoperability requirement will fit the same categories.
