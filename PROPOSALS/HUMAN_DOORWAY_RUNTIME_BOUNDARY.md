# Proposal — Renaissance Human Doorway Runtime Boundary

**Status:** Proposed — not ratified
**Purpose:** Define the smallest executable boundary that lets the existing Organs human front door hand a non-operational human expression to Renaissance without making Organs the semantic owner.

## Finding

The semantic Human Doorway MVT passes, but no executable Renaissance handoff currently exists.

Organs I/O already owns the operational front door and must retain that responsibility. Its deterministic catalog, Critic gate, and Executive approval path must remain unchanged for operational requests.

Renaissance owns the semantic interpretation of Renaissance capability requests.

## Proposed boundary

For a human expression arriving at Organs I/O:

```
human expression
      |
      v
Organs I/O front door
      |
      +--> recognized operational intent --> existing Organs path
      |
      +--> not an operational intent
                    |
                    v
          Renaissance doorway boundary
                    |
                    v
             Capability Request
                    |
          +---------+---------+
          |                   |
       ordinary          capability work
      conversation             |
                           Attention Choice
                           when warranted
                                |
                         authorization
                         when required
                                |
                             instrument
```

Organs remains the transport/front-door host. Renaissance owns the meaning of the Renaissance semantic handoff.

## Smallest executable shape

A Renaissance-facing adapter should accept a preserved human expression and return a bounded semantic result containing, at minimum:

- original expression;
- disposition: `conversation`, `clarify`, `capability_request`, or `unsupported`;
- Capability Request when applicable;
- no authorization merely because interpretation occurred;
- no evidence merely because interpretation occurred;
- no execution of cross-repository work.

The boundary should be callable synchronously from the existing Organs I/O request path.

## Required invariants

1. Existing recognized Organs operational requests remain on the existing operational path.
2. Renaissance interpretation cannot directly execute an Organs action.
3. Capability classification does not authorize work.
4. Interpretation does not create evidence.
5. Ambiguous expressions produce clarification rather than invented capability.
6. Ordinary conversation remains possible.
7. The original human expression remains recoverable exactly.
8. The boundary is testable by the existing Human Doorway harness.
9. No universal ranking engine, autonomous agenda, new persistence layer, or second human-facing front door is introduced.

## Explicit non-goals

This proposal does not establish:

- a universal LLM classifier;
- a new user interface;
- autonomous agenda generation;
- automatic cross-repository execution;
- a replacement for Organs I/O;
- a new Communications capability;
- an Episteme redesign;
- a universal capability-ranking algorithm.

## Open implementation questions

- Which existing Organs transport mechanism should carry the synchronous handoff?
- Where should the Renaissance semantic runtime live?
- What model/rules, if any, perform the initial semantic interpretation?
- How should Renaissance return ordinary conversational responses versus structured capability requests?
- What minimum operational observability is required?
- What failure behavior is required when the Renaissance boundary is unavailable?

## Gate

This proposal should not be implemented as architecture until the Human Gate establishes the boundary and its runtime placement through the normal change-control process.

Until then, the Human Doorway harness remains the executable contract test without pretending an implementation exists.
