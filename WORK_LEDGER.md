# Renaissance Work Ledger

**Purpose:** A small working bookmark for continuing human/AI work.

This file is a navigation aid, not canon, architecture, a roadmap, a changelog,
or a replacement for Git history. Canonical authority remains in the
constitutional documents and recorded Decisions.

## Current Frontier

**Status:** Organs runtime-substrate hardening checkpoint complete; no next
implementation task is currently established.

### Last verified stopping point

The work stopped in **Organs** after the Orchestrator live subprocess
regression was merged:

- **PR:** #1 — `test: add live Orchestrator subprocess regression`
- **Merge:** `e4f71f256dd8ccb309123bf04b6d44dd476303cb`
- **Repository:** `mythologyprospector-hub/organs`
- **Verification:** `uv run pytest -q orchestrator/tests` → **32 passed, 33 warnings**

The PR added a bounded live regression for the existing Orchestrator
subprocess path. No runtime behavior or architecture changed.

Before merge, the PR branch was synchronized with current Organs `main`,
including the current hardening history. GitHub then merged the PR into
`main`.

### Why the work was in Organs

Organs is Renaissance runtime infrastructure. Work may temporarily cross into
Organs when Renaissance architectural requirements require runtime
investigation, integration, or hardening.

The move between repositories is therefore part of the working trail, not an
architectural claim that the projects are the same thing.

## Resume From Here

When continuing this work:

1. Inspect the current Organs state from its repository.
2. Identify whether any remaining concrete hardening pressure exists.
3. If a task belongs to Organs implementation/hardening, establish it from
   current repository evidence before changing anything.
4. If the next task requires a Renaissance architectural decision, return to
   the applicable Renaissance authority and Decision process.
5. Do not manufacture work merely to maintain momentum.
6. Preserve the authority boundary between Renaissance and Organs.
7. Update this ledger when the next meaningful stopping point is established.

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
