# Capability Request Real-Boundary MVT

**Status:** Experiment / proposal validation

## Purpose
Test the proposed Renaissance Capability Request contract against the actual human-facing Organs I/O Interface and the established Praxis/Episteme boundaries.

## Findings
- Existing operational requests remain correctly owned by Organs I/O, with deterministic catalog matching, Critic evaluation, and Executive approval where required.
- Ordinary human conversation does not need to become a Capability Request.
- Renaissance learning and investigation requests can be represented by the proposed contract without becoming authorization or evidence.
- Praxis retains its problem-solving domain semantics downstream.
- Episteme retains scientific execution and provenance downstream.
- Unrecognized Renaissance requests fail closed at the current Organs front door rather than being guessed into API calls.

## Case results

1. Existing operational request: **PASS**
2. Ordinary conversation: **PASS**
3. Renaissance learning request: **PASS at semantic boundary; integration not implemented**
4. Renaissance investigation request: **PASS at semantic boundary; integration not implemented**
5. Praxis-oriented problem solving: **PASS**
6. Consequential operational request: **PASS**
7. Unrecognized Renaissance request: **PASS as safety boundary; OPEN as integration boundary**

## Boundary checks
- Organs I/O remains operational routing infrastructure — **PASS**
- Renaissance Capability Request remains semantic ownership — **PASS**
- Capability Request does not replace the I/O catalog — **PASS**
- Capability Request does not become authorization — **PASS**
- Capability Request does not become Attention Choice — **PASS**
- Praxis retains its domain semantics — **PASS**
- Episteme retains scientific execution/provenance — **PASS**
- Unrecognized requests fail closed — **PASS**
- A Renaissance runtime/adapter is required by current evidence — **NOT ESTABLISHED**

## Conclusion
**PASS with one integration finding.**

The Capability Request boundary survives contact with the real front door and the established Praxis/Episteme boundaries.

The existing Organs I/O Interface is already doing the correct safety-critical job: deterministic operational routing with Critic/Executive gates and explicit refusal to guess.

A Renaissance Capability Request therefore belongs above or alongside that operational catalog, not inside it.

The current world has a semantic contract but no justified runtime host for it. No runtime, adapter, I/O catalog expansion, or persistence mechanism should be invented yet.

Next grounded question:

> What existing Renaissance-facing interaction surface, if any, can host Capability Request interpretation without creating a second front door?

If none exists, establish that absence before implementation rather than solving it by architectural guesswork.