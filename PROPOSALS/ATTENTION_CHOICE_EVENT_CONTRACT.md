# Attention Choice Event Contract

**Status:** Implementation contract derived from Decision 0009

## Purpose

Define the smallest event envelope by which Renaissance may durably publish an Attention Choice through the existing Communications bus, without transferring semantic ownership to Organs.

## Event identity

- topic: `renaissance.attention`
- event_type: `attention_choice`
- publisher: `renaissance`

These identify the integration stream only. They do not create a new authority, subsystem, ontology, or ranking mechanism.

## Payload

The payload is exactly the Renaissance Attention Choice record:

```json
{
  "id": "ac-001",
  "pressure_ref": "gap-17",
  "target_ref": "investigation-42",
  "supporting_refs": ["finding-8"],
  "selection_basis": "resolves the represented contradiction directly connected to the current question",
  "alternative_refs": ["investigation-39", "investigation-41"],
  "mode": "suggest",
  "authorization_ref": null,
  "outcome_ref": null
}
```

The payload preserves the Attention Choice fields without semantic reinterpretation.

## Field requirements

- `id` — required identifier.
- `pressure_ref` — required reference to represented pressure.
- `target_ref` — required reference to the selected target.
- `supporting_refs` — required array, possibly empty.
- `selection_basis` — required inspectable local reason or explicit selection rule.
- `alternative_refs` — required array, possibly empty.
- `mode` — required: `ask`, `suggest`, or `execute`.
- `authorization_ref` — optional reference to established authorization provenance.
- `outcome_ref` — optional reference to subsequent work/result.

## Transport boundary

Renaissance publishes through the existing Communications operation:

```text
POST /bus/topics/renaissance.attention/publish
{
  "event_type": "attention_choice",
  "payload": <AttentionChoice>,
  "publisher": "renaissance"
}
```

Communications stores and transports the event. It does not interpret the Attention Choice.

## Integrity rules

1. Required fields must be present.
2. `mode: execute` is not permission by itself.
3. `authorization_ref` remains distinct from the choice.
4. Communications metadata is not epistemic evidence.
5. Transport success is not investigation success.
6. A later outcome does not retroactively justify selection.
7. No universal importance score or ranking value belongs in this event.

## Deliberately excluded

This contract does not define an Attention registry, autonomous agenda, work queue, ranking engine, new database, new Communications capability, Episteme record type, or permission mechanism.

## First implementation boundary

The smallest implementation is a Renaissance-side publisher that constructs the validated Attention Choice payload and sends it through the existing Communications publish endpoint. Runtime integration should use the established Organs discovery convention rather than hardcoding the Communications address.

No runtime publisher is created by this document alone; implementation follows normal change control and verification.