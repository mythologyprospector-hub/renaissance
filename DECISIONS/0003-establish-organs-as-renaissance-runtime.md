# Decision 0003 — Establish Organs as Renaissance Runtime Substrate

**Date:** 2026-09-23  
**Status:** Accepted  
**Authority:** Human Gate  
**Scope:** Renaissance architecture and repository constellation

## Decision

The Organs repository is established as the **runtime substrate of
Renaissance**.

Its sole project purpose is to serve Renaissance.

The former Digital Djinn identity is retired as the governing mission of the
repository. Historical Digital Djinn material may remain where it provides
useful provenance, but it is no longer the project's objective.

## Rationale

Organs already contains substantial reusable runtime machinery for:

- service discovery;
- inter-component communication;
- persistent runtime state;
- bounded execution;
- risk classification;
- explicit approval;
- coordination;
- introspection;
- telemetry;
- human-facing operation.

Keeping that work available to Renaissance is preferable to treating the
runtime as an unrelated project whose architecture Renaissance must later
extract or duplicate.

## Boundary

This decision does **not** make Organs the owner of Renaissance's domain
semantics.

Renaissance remains the higher-level system.

Organs implements runtime infrastructure beneath Renaissance domain
capabilities.

In particular:

- Organs Memory is not automatically Renaissance's epistemology.
- Critic is not constitutional authority.
- Executive is not sovereign.
- Telemetry is not automatically epistemic evidence.
- Registry is not institutional authority.
- Sandbox execution does not establish truth.

## Consequences

1. Organs may be rewritten when Renaissance requires it.
2. Organs documentation must describe its Renaissance role.
3. Retired Forge/Digital-Djinn active paths must not remain hidden dependencies.
4. Renaissance domain organs remain separately defined and replaceable.
5. Organs changes remain implementation work unless explicitly promoted by
   Renaissance change control.

## Non-decisions

This decision does not yet establish:

- a complete Renaissance runtime API;
- a universal Organs data model;
- a licensing policy;
- a complete autonomy model;
- final service boundaries;
- which existing Organs components will remain unchanged.

Those questions remain open and should be resolved only when needed.

## Record

This decision supersedes the prior working audit position that Organs was only
a "shared infrastructure candidate."
