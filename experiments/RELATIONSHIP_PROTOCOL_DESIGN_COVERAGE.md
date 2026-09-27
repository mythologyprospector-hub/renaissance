# Relationship Protocol Design Experiment — Coverage

**Status:** Bounded experiment  
**Authority:** Experiment  
**Relationship to canon:** No candidate is selected or promoted to the final Renaissance protocol.

## Question

Can candidate representation shapes be compared against the minimum guarantees proposed after Decision 0004 without prematurely choosing a serialization or protocol?

## Candidates

1. **Minimal envelope** — explicit relationship plus references, origin/provenance, transformations, and history.
2. **Opaque payload** — explicit relationship identity with important semantics hidden in an opaque payload.
3. **Linked assertion** — explicit relationship with separately linked lineage/transformation records.

## Current findings

- The minimal-envelope and linked-assertion shapes satisfy the encoded minimum guarantees.
- The opaque-payload shape fails because source meaning and transformation information are not sufficiently explicit.
- These results compare conceptual shapes only.

## Deliberate non-conclusions

This experiment does not select a final protocol, wire format, identifier scheme, transport, mandatory field set, versioning model, or security mechanism.

## Next evidence

Further work should test conditional/optional fields, unknown extensions, faithful translation representation, versioning, provenance lineage, and security/authentication boundaries before any final protocol decision.