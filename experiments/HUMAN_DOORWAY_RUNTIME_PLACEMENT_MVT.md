# Human Doorway Runtime Placement MVT

**Status:** PASS — placement candidate identified, implementation still gated

## Question

Where can the Renaissance-owned semantic doorway execute without creating a second human front door or making Organs the owner of Renaissance meaning?

## Candidates

### A. Put Renaissance semantics inside Organs I/O

**FAIL.**

This makes the operational front door the semantic owner of Renaissance capability interpretation. It also couples Renaissance capability vocabulary to the Organs operational catalog.

### B. Put the doorway in Communications

**FAIL.**

Communications is transport. It stores and routes events but has no semantic ownership of human expressions.

### C. Create a separate Renaissance application/front door

**FAIL as a first implementation.**

This duplicates the human-facing entry topology and creates a second front door without evidence that a second transport is required.

### D. Implement a Renaissance semantic service using the existing Organs runtime convention

**PASS as the current placement candidate.**

The existing Organs convention already provides:

- service lifecycle through FastAPI;
- registry registration/discovery;
- health/info conventions;
- stable inter-organ HTTP transport;
- bounded capability declaration.

The service would be Renaissance-owned in meaning while participating in Organs only as runtime infrastructure.

Its public semantic surface would accept preserved human expression and return the bounded Human Doorway result. It would not expose operational execution authority.

## Result

The smallest currently justified executable topology is:

```
human
  |
  v
Organs I/O
  |
  +--> operational intent -> existing operational path
  |
  +--> non-operational expression
          |
          v
   Renaissance semantic service
          |
          v
   Capability Request / conversation / clarification
```

The Renaissance service may subsequently use Communications or other organs, but those are downstream infrastructure, not the semantic owner.

## Boundary invariants

- Renaissance service does not replace Organs I/O.
- Renaissance service cannot directly execute operational Organs calls.
- Interpretation does not authorize.
- Interpretation does not create evidence.
- Original expression is preserved.
- Existing Human Doorway harness can test the semantic response.
- Service failure must fail closed rather than silently execute or reinterpret the request.
- No autonomous agenda or universal ranking is introduced.

## Important limitation

This MVT establishes **runtime placement**, not authorization to create the service.

Creating the service would be an implementation of the proposed Human Doorway Runtime Boundary and therefore remains subject to the Human Gate under normal change control.
