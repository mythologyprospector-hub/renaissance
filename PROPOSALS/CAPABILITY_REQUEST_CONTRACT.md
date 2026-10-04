# Renaissance Capability Request Contract

**Status:** Proposed — not canon

## Purpose

Define the smallest Renaissance-owned boundary between a human-facing expression and a request for Renaissance capability work.

The contract exists so the runtime front door can remain operational routing infrastructure while Renaissance retains responsibility for interpreting what kind of human-facing capability is being requested.

## Boundary

~~~
human expression
      ↓
Renaissance Capability Request
      ↓
appropriate capability / instrument
      ↓
result or next interaction
~~~

A Capability Request is an interpretation of the human's expressed purpose for Renaissance work. It is not itself an authorization to perform consequential action.

## Minimum record

~~~
CapabilityRequest
  id
  source_ref?
  expression
  capability
  intent
  target_ref?
  constraints[]
  context_refs[]
  mode
  authorization_ref?
  outcome_ref?
~~~

### Field semantics

- **id** — unique identifier.
- **source_ref?** — originating interaction when one exists.
- **expression** — the human-facing expression as received or faithfully preserved; it must not be silently replaced by the interpretation.
- **capability** — currently understand, explore, create, or learn.
- **intent** — concise statement of what the human appears to be trying to accomplish.
- **target_ref?** — identified subject, artifact, problem, domain, or other represented target.
- **constraints[]** — explicit constraints relevant to the request.
- **context_refs[]** — represented context used in interpretation.
- **mode** — initially answer, investigate, suggest, or clarify.
- **authorization_ref?** — reference to already-established authorization when required. This does not create authority.
- **outcome_ref?** — reference to subsequent work or outcome. It does not retroactively validate the interpretation.

## Required distinctions

A Capability Request remains distinct from:

- the original human expression;
- an Attention Choice;
- authorization or permission;
- an Episteme epistemic artifact;
- an actual execution or result;
- a universal ranking of human interests.

When investigation is warranted:

~~~
human expression
      ↓
Capability Request
      ↓
Attention Choice
      ↓
authorized investigation when required
      ↓
Episteme execution / result history
~~~

Not every human interaction should become an Attention Choice. Some are answered, clarified, taught, or otherwise handled without investigation.

## Interpretation rules

1. Preserve the human expression separately from the interpretation.
2. Do not invent a capability merely to force classification.
3. Clarify is valid when information is insufficient to determine intended capability or target.
4. Capability classification does not authorize action.
5. Consequential action retains its existing authorization boundary.
6. Generated interpretation remains an interpretation, not evidence.
7. A request may be revised when the human clarifies intent; the original interpretation remains recoverable where provenance matters.
8. The current four-capability vocabulary is provisional and not permanently exhaustive.

## What this does not establish

This proposal does not establish:

- a Renaissance runtime service;
- a replacement for Organs I/O Interface;
- an LLM-based universal intent classifier;
- automatic execution;
- autonomous goals;
- universal capability ranking;
- a new persistence system;
- a new Organs capability;
- a new authority model.

## Relationship to Organs

Organs may remain the operational front door and may carry a Capability Request once a concrete integration is justified. Organs should not acquire ownership of Renaissance capability semantics merely because it transports or routes a request.

## Relationship to Attention Choice

Capability Request answers:

> What kind of human capability work is being requested, and what is the human trying to accomplish?

Attention Choice answers:

> Given represented pressure, what specifically deserves attention now, and why?

These are adjacent but distinct boundaries.

## Open questions

- Should expression preserve exact raw input or raw input plus normalization?
- Should intent have a structured vocabulary?
- Should mode remain four values or become capability-specific?
- Which interactions require durable Capability Request records?
- Where should the first real Renaissance capability interpreter live?
- Should an existing Organs interface carry this contract directly or through a Renaissance-facing adapter?

No implementation is authorized by this proposal alone.
