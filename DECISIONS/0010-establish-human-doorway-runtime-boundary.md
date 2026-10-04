# Decision 0010 — Establish the Human Doorway Runtime Boundary

**Status:** Ratified  
**Authority:** Human Gate  
**Date:** 2026-10-04

## Matter

Renaissance has a validated semantic Human Doorway contract, but no executable runtime boundary through which the existing human-facing Organs front door can hand non-operational human expressions to Renaissance without making Organs the owner of Renaissance meaning.

The question is whether Renaissance should establish a runtime boundary using the existing Organs runtime convention while preserving the existing separation of transport, semantics, authorization, and execution.

## Prior state

The Human Doorway semantic MVT established that:

- ordinary conversation may remain conversation;
- learning requests can become CapabilityRequest(capability=learn);
- inquiry can become CapabilityRequest(capability=understand, mode=investigate) and may proceed to Attention Choice;
- problem-solving requests remain within Praxis semantics;
- ambiguous expressions require clarification;
- recognized operational requests remain owned by Organs I/O;
- unsupported requests fail closed.

The Human Doorway runtime proposal then identified the missing executable seam:

Organs I/O → Renaissance semantic boundary → Capability Request / conversation / clarification

The runtime placement MVT tested the available infrastructure and found that an independent Renaissance-owned semantic service using the existing Organs runtime convention is the smallest justified placement candidate.

Communications was inspected as a possible transport and rejected as semantic owner: it provides event transport/storage/routing, not human-expression interpretation.

## Evidence and reasoning

The following validations establish the boundary:

- experiments/HUMAN_DOORWAY_MVT.md — semantic boundary cases pass.
- experiments/HUMAN_DOORWAY_MVT_RESULT.md — semantic distinctions and failure behavior pass.
- experiments/human_doorway_harness.py — executable boundary corpus and invariant checks.
- experiments/test_human_doorway_harness.py — deterministic corpus, negative authorization, expression preservation, and semantic mutation checks.
- experiments/CAPABILITY_REQUEST_REAL_BOUNDARY_MVT.md — real Learn boundary passes.
- experiments/CAPABILITY_REQUEST_EPISTEME_REAL_BOUNDARY_MVT.md — real Episteme boundary passes.
- experiments/HUMAN_DOORWAY_RUNTIME_PLACEMENT_MVT.md — runtime placement candidate passes.
- Organs io_interface/main.py — confirms the existing operational front door and its authority path.
- Organs shared/organ_client.py — confirms registry/discovery and inter-organ runtime convention.
- Organs communications/main.py — confirms Communications is transport infrastructure rather than semantic ownership.

The evidence supports a narrow runtime boundary without requiring a second human-facing front door, a new transport system, or semantic expansion of Organs I/O.

## Decision

Renaissance hereby establishes an **executable Human Doorway runtime boundary** with the following ownership:

- **Organs I/O** remains the existing human-facing transport/front door and retains ownership of recognized operational requests.
- **Renaissance** owns semantic interpretation of non-operational human expressions for Renaissance capabilities.
- **The Renaissance semantic runtime** may use the existing Organs runtime convention for lifecycle, registry/discovery, health, and transport infrastructure.
- **Communications** remains transport infrastructure and does not become the semantic owner.
- **Attention Choice** remains the established Renaissance knowledge-growth boundary and is invoked only when investigation is actually warranted.
- **Authorization** remains distinct from interpretation and Attention Choice.
- **Episteme, Praxis, Learn, and other instruments** retain their existing domain ownership.

The minimum runtime result is:

```text
original expression
disposition:
  conversation | clarify | capability_request | unsupported
CapabilityRequest?
```

The original expression must remain exactly recoverable.

## Required invariants

1. Recognized Organs operational requests remain on the existing operational path.
2. Renaissance interpretation cannot directly execute an Organs action.
3. Capability classification does not authorize work.
4. Interpretation does not create evidence.
5. Ambiguous expressions produce clarification rather than invented capability.
6. Ordinary conversation remains possible.
7. Unsupported requests fail closed.
8. No second human-facing front door is introduced.
9. No universal ranking engine or autonomous agenda is introduced.
10. No new persistence layer is required by this decision.
11. The Human Doorway harness remains the executable contract test.
12. Runtime failure must not silently execute, authorize, or reinterpret an expression.

## Runtime placement

The initial implementation boundary is:

```text
human
  |
  v
Organs I/O
  |
  +--> recognized operational intent --> existing Organs path
  |
  +--> non-operational expression
          |
          v
   Renaissance semantic runtime
          |
          v
   conversation / clarification / Capability Request
```

The Renaissance runtime may subsequently invoke established capability instruments or transports, but this decision does not grant it execution authority over those systems.

## Explicit non-goals

This decision does not establish:

- a universal LLM classifier;
- a new user interface;
- autonomous agenda generation;
- automatic cross-repository execution;
- replacement of Organs I/O;
- a new Communications capability;
- an Episteme redesign;
- a universal capability-ranking algorithm;
- a new authorization mechanism;
- autonomous machine authority.

## Implementation constraint

This decision authorizes implementation of the narrow runtime boundary only.

The first implementation must be the smallest service and adapter surface capable of passing the existing Human Doorway harness against the real Organs transport.

Implementation must not silently add capability routing, autonomous work selection, persistence, authorization, or execution.

Any later expansion that changes an established boundary requires its own evidence and change-control decision.

## Effective status

**Effective immediately.**

The Human Doorway runtime boundary is now established as Renaissance architecture. Implementation may proceed against this contract.