# Relationship Protocol Extensions — Coverage

**Status:** Bounded experiment  
**Authority:** Experiment  
**Relationship to canon:** No protocol requirement is established here.

## Question

Can a candidate interoperability representation preserve unknown extensions and conditional information without requiring every participant to understand or supply every field?

## Current findings

- Unknown extension data can be carried without changing the source relationship meaning.
- Core identity, participants, and relationship meaning remain distinguishable from extensions.
- Provenance and status history can be conditional: absent when the source has none, preserved when present.
- Extension data must not silently override the explicit relationship meaning.

## Deliberate non-conclusions

This experiment does not establish a final extension mechanism, namespace model, versioning scheme, wire format, or mandatory/optional field list for a future protocol.
