# Renaissance Work Ledger

**Purpose:** A small working bookmark for continuing human/AI work.

This file is a navigation aid, not canon, architecture, a roadmap, a changelog,
or a replacement for Git history. Canonical authority remains in the
constitutional documents and recorded Decisions.

## Current Frontier

**Status:** Active work temporarily crossed from Renaissance into the Organs
runtime-substrate project.

### Last verified stopping point

The work stopped in **Organs** after PR #12 was merged:

- **PR:** #12 — `docs: clarify install overlay cleanup boundary`
- **Merge:** `a147501a1b08de4c0cb474c87e4f9f88f2084483`
- **Repository:** `mythologyprospector-hub/organs`

That change clarified the existing installer overlay contract: existing runtime
data and component directories are preserved, and retirement cleanup must be
explicit and authorized. No runtime behavior or deletion policy was introduced.

### Why the work was in Organs

Organs is Renaissance runtime infrastructure. Work may temporarily cross into
Organs when Renaissance architectural requirements require runtime
investigation, integration, or hardening.

The move between repositories is therefore part of the working trail, not an
architectural claim that the projects are the same thing.

## Resume From Here

When continuing this work:

1. Inspect the current Organs state from its repository.
2. Identify whether the next task belongs to Organs implementation/hardening or
   requires a Renaissance architectural decision.
3. Do not treat conceptual alignment as an architectural decision.
4. Preserve the authority boundary between Renaissance and Organs.
5. Return the working frontier here when the next meaningful stopping point is
   established.
6. Update this ledger before stopping again.

## Last Known Organs Boundary

Organs has a real Communications BUS carrying Memory events, but current
Renaissance requirements do not establish a consumer for those topics.

Archaeology confirmed that this is an available integration seam, not a missing
component or current architectural defect. No subscriber, organ, protocol, or
Decision is required at this time.

If a concrete capability later requires one of these events, establish the
responsible contract at that time before implementing the consumer.

## Ledger Rule

Keep this document small.

Move the pointer rather than turning this into a diary. The useful question is:

> **Where were we, and what was the next grounded place to look?**

Git is the long-term record. The ledger is the bookmark. Conversation is the
scratchpad.
