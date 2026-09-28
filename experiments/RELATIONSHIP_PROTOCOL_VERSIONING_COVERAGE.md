# Relationship Protocol Versioning — Coverage

**Status:** Bounded experiment  
**Authority:** Experiment  
**Relationship to canon:** No version-negotiation requirement is established here.

## Question

Can participants establish an explicitly compatible protocol version without silently treating incompatible representations as compatible?

## Current findings

- A common supported version can be selected explicitly.
- No common version can be detected rather than silently accepted.
- Incompatible versions can fail explicitly.
- Unknown fields can remain separately preservable across a version boundary.
- Version selection does not itself alter relationship meaning.

## Deliberate non-conclusions

This experiment does not establish a final versioning scheme, compatibility policy, semantic-versioning rule, negotiation transport, downgrade policy, extension namespace, or wire format.
