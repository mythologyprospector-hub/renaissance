# Proposal — Runtime Event Consumer Ownership

**Status:** Proposed / unresolved  
**Authority:** Proposal only; no architectural or implementation authorization  
**Scope:** Renaissance runtime responsibility and Organs integration

## Question

Does Renaissance need to establish ownership or responsibility for consuming events
published by Organs Memory, and if so, which existing capability, project, or
domain responsibility should own that work?

## Current evidence

Current Organs implementation provides a persistent pull-based Communications
BUS with per-consumer cursors.

Current Organs Memory publishes runtime events including:

- fact-added events;
- scar-added and scar-superseded events;
- promise-resolved events;
- unknowable-resolved events;
- relation-resolved events.

Current Organs documentation and implementation establish publication and
consumption mechanisms, but do not establish which organ or higher-level
capability is responsible for consuming these topics.

Current Renaissance architecture establishes Organs as runtime substrate, not
domain authority. Decision 0004 and Decision 0006 establish requirements for
relationship interoperability, but do not assign ownership of runtime event
consumption.

## Boundary

This proposal does **not**:

- create a subscriber;
- assign an existing organ as subscriber;
- define a new organ or capability;
- define a universal event model;
- define a protocol or transport;
- change Organs canon;
- change Renaissance architecture;
- promote runtime behavior into architectural authority.

## Decision needed

Human Gate should determine whether the unresolved subscriber boundary requires
an architectural decision now.

If yes, the decision should identify the responsible existing capability,
project, or ownership boundary without prematurely specifying implementation.

If no, the boundary should remain explicitly unresolved until a concrete
requirement makes ownership necessary.

## Evidence to preserve

The current Organs BUS and Memory implementation should remain unchanged while
this question is unresolved. No consumer should be invented merely to make the
existing transport appear complete.

## Relationship to existing authority

This proposal follows:

- Decision 0003 — Organs as Renaissance runtime substrate;
- Decision 0004 — relationship interoperability as a Renaissance architectural
  responsibility;
- Decision 0005 — targeted builder grounding;
- Decision 0006 — minimum relationship interoperability boundary;
- Renaissance change control, which requires unresolved matters to remain
  unresolved rather than being forced prematurely.
