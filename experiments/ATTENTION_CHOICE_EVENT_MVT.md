# Attention Choice Event Minimum Viable Test

**Status:** Experiment / implementation-boundary validation
**Related:** Decision 0009 — Attention Choice boundary

## Question

Can the existing Organs Communications publish/peek/consume contract carry an Attention Choice without adding a new persistence mechanism or moving semantic ownership into Organs?

## Existing transport contract

Communications accepts:

- `topic: str`
- `event_type: str`
- `publisher: str`
- `payload: dict`

It durably stores the payload as JSON and returns the event with its transport metadata. Consumers receive the same payload through independent cursors.

## Candidate payload

The payload is the Renaissance-owned Attention Choice record:

```json
{
  "id": "ac-001",
  "pressure_ref": "gap-17",
  "target_ref": "investigation-42",
  "supporting_refs": ["finding-8"],
  "selection_basis": "resolves the oldest unresolved contradiction directly connected to the current question",
  "alternative_refs": ["investigation-39", "investigation-41"],
  "mode": "suggest",
  "authorization_ref": null,
  "outcome_ref": null
}
```

## Validation

| Requirement | Result |
|---|---|
| Minimum fields survive as JSON | PASS |
| Referential fields remain distinguishable | PASS |
| `mode` remains distinct from authorization | PASS |
| Optional authorization remains optional | PASS |
| Outcome remains separate from selection | PASS |
| Transport adds no epistemic meaning | PASS |
| Independent consumers can replay the same choice | PASS |
| Communications needs to interpret Attention Choice semantics | NO |
| New persistence subsystem required | NO |

## Important limitation

The transport contract does not establish names for the Attention Choice topic or event type. Those names are integration vocabulary, not yet an architectural decision. They should be selected only when the first actual publisher/consumer is implemented or when an existing naming convention is found.

Likewise, this test does not authorize an autonomous consumer, a registry, or a work queue. Communications remains transport/persistence infrastructure.

## Result

**PASS.** The existing Communications envelope is sufficient to carry the minimum Attention Choice record without loss of semantics or ownership.

The smallest remaining implementation question is therefore not storage. It is the first Renaissance-facing publisher/consumer boundary and its explicit naming contract.
