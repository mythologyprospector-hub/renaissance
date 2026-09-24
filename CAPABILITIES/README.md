# Renaissance Capabilities

**Status:** Working architectural framework v0.1  
**Authority:** Architecture  
**Constrained by:** Renaissance Constitution, Charter, Decisions, and Canon

## Purpose

A Renaissance **capability** is a bounded responsibility that Renaissance recognizes as useful work, with an explicit contract, without requiring a particular implementation.

Renaissance defines capabilities by **responsibility, not implementation**.

The purpose of this layer is to let Renaissance describe *what useful work exists* without prematurely deciding which repository, service, organ, algorithm, model, or project must perform it.

## 1. Capability Is Not Implementation

The governing relationship is:

```
Capability
    ↓
Contract
    ↓
Implementation(s)
```

A capability may be implemented by:

- one repository;
- several repositories;
- an Organs runtime mechanism;
- a specialist instrument;
- a combination of existing systems;
- multiple replaceable implementations;
- or, initially, no software at all.

Therefore:

- **Capability ≠ repository**
- **Capability ≠ service**
- **Capability ≠ organ**
- **Capability ≠ algorithm**
- **Capability ≠ authority**
- **Capability ≠ ownership**

A capability remains conceptually stable even if its implementation changes.

## 2. Capability vs. Infrastructure

**Infrastructure** provides mechanisms that other work can use.

**Capability** performs or defines a bounded class of useful work.

For Renaissance:

```
Renaissance
    │
    ├── Runtime infrastructure
    │      └── Organs
    │
    └── Domain / functional capabilities
           └── Episteme and future instruments
```

Infrastructure may enable a capability without becoming the capability.

In particular, technical centrality does not grant epistemic, constitutional, or institutional authority.

Organs therefore remain runtime substrate. Episteme remains an inquiry capability/instrument. Episteme is not required to become an Organs service merely because Organs provides infrastructure it can consume.

## 3. Capability vs. Authority

A capability is a responsibility, not a source of sovereignty.

Performing a task does not grant the performer authority over:

- Renaissance purpose;
- constitutional constraints;
- human judgment;
- other capabilities;
- domain truth outside its contract;
- or the future architecture.

A highly capable implementation remains subordinate to its explicit contract and the authority structure governing that contract.

## 4. Capability Contracts

Each recognized capability should have a contract defining, at minimum:

1. **Purpose** — what useful responsibility it exists to perform.
2. **Scope** — what it covers.
3. **Boundaries** — what it does not own.
4. **Inputs** — what it may consume.
5. **Outputs** — what it may produce.
6. **Epistemic status** — how generated, captured, observed, inferred, or unknown material is distinguished.
7. **Provenance** — how relevant lineage survives across transformations and boundaries.
8. **Authority** — what decisions remain outside the capability.
9. **Interoperability** — what must be explicit when interacting with other capabilities.
10. **Acceptance conditions** — what must remain true for the capability to satisfy its contract.

A contract should describe responsibility without unnecessarily prescribing implementation.

## 5. Composition

Capabilities may compose.

Composition does not imply ownership.

For example:

```
Runtime infrastructure
        │
        ▼
   Inquiry capability
        │
   ┌────┼─────┐
   ▼    ▼     ▼
Discovery  Unknowns  Experiments
```

These may be separate conceptual responsibilities while being implemented together when that is the most coherent design.

Conversely, a responsibility may later be extracted into another implementation without requiring Renaissance itself to be redesigned.

**Conceptual separation does not require physical separation.**

## 6. Provenance Across Capability Boundaries

Capability boundaries must not erase epistemic distinctions or provenance.

When material crosses a boundary, the receiving capability must not silently upgrade its status.

In particular:

- processing is not proof;
- capture is not automatically observation;
- generation is not observation;
- discovery output is not automatically evidence;
- provenance does not certify source truth;
- infrastructure status is not epistemic authority;
- unknowns and contradictions must remain representable.

Where transformations occur, the relationship between source material and derived material should remain inspectable to the extent required by the participating contracts.

## 7. Recognition

A capability becomes recognized by an explicit architectural decision, not merely because:

- a repository exists;
- a service has been deployed;
- a component has a useful name;
- an implementation has become technically central;
- or a project claims a broader purpose.

Recognition should establish the responsibility and boundary first.

The normal sequence is:

```
Need / demonstrated responsibility
        ↓
Architectural discussion
        ↓
Capability boundary
        ↓
Capability contract
        ↓
Implementation
        ↓
Verification
```

Implementation may precede formal recognition during experimentation, but experimental existence does not by itself establish architectural status.

## 8. Independent Instruments

A specialist or independent project may participate in Renaissance without becoming a Renaissance subsystem.

Participation should be established through an explicit contract.

This preserves the distinction between:

- Renaissance architecture;
- a project's own purpose;
- interoperability;
- and ownership.

The Shiva-related constellation is an established example of this boundary. Behemoth, Leviathan, and Namagiri remain independent projects; compatibility or future interoperability does not require their internal architecture to become Renaissance architecture.

## 9. Replaceability and Retirement

A capability should not depend on one irreplaceable implementation unless an explicit architectural decision says otherwise.

An implementation may be:

- replaced;
- rewritten;
- split;
- recombined;
- retired;
- or superseded.

The responsibility and contract should remain the architectural reference point unless Renaissance explicitly revises the capability itself.

Retirement of a capability is therefore different from retirement of an implementation.

A capability may be retired when its responsibility is no longer useful, is intentionally absorbed into another recognized capability, or is otherwise superseded by an explicit architectural decision.

Such changes should preserve provenance and record the relevant decision.

## 10. First Concrete Example: Episteme

**Episteme** is currently the first concrete Renaissance capability/instrument governed by an explicit capability contract:

`CAPABILITIES/EPISTEME_CONTRACT.md`

Its contracted responsibility includes disciplined inquiry: representing grounded knowledge, preserving provenance and lineage, exposing unknowns and gaps, developing and comparing explanatory possibilities, designing discriminating investigations, preserving results, making knowledge change explicit, and supporting reproducibility and inspection.

The Episteme contract also explicitly limits what Episteme does not own, including Renaissance constitutional purpose, human judgment, universal truth definition, universal data models, Organs runtime architecture, other projects' purposes, and Renaissance canon.

This makes Episteme a useful reference case for the capability model without requiring every future capability to resemble its implementation.

## 11. Current Conceptual Capability Set

The current Renaissance architecture identifies several responsibilities that may be expressed as capabilities:

- discovery;
- provenance and lineage;
- relationship mapping;
- unknown and gap handling;
- hypothesis formation;
- prediction;
- experiment design;
- verification and contradiction analysis;
- interoperability.

This list is **conceptual, not a mandate for separate repositories or services**.

Existing implementations may cover several responsibilities. Episteme is one such case.

### Provisional human-facing model

A separate provisional architectural model is now recorded in:

`CAPABILITIES/HUMAN_CAPABILITY_MODEL.md`

It proposes four broad human-facing responsibilities for further architectural testing:

- **Understand**
- **Explore**
- **Create**
- **Learn**

This is **provisional** and does not yet replace the conceptual responsibility list above or establish four formally recognized capabilities. It is being treated as a hypothesis to test against real workflows and implementation evidence.

The current working evidence maps:

- Episteme primarily toward **Understand**;
- Tiger Den toward **Explore**;
- AI Foundry toward **Create**;
- no mature Renaissance implementation currently identified as primary for **Learn**.

These mappings do not transfer ownership of those broader responsibilities to the named projects.

## 12. Architectural Rules

1. Define responsibilities before implementations.
2. Do not infer authority from technical centrality.
3. Do not force conceptual boundaries into artificial service boundaries.
4. Do not duplicate an existing source of truth merely to make the architecture look cleaner.
5. Preserve provenance and epistemic distinctions across boundaries.
6. Keep independent projects independent unless an explicit decision changes that status.
7. Prefer replaceable implementations behind stable contracts.
8. Record significant capability recognition, revision, composition, and retirement.
9. Do not silently expand a capability's authority or scope.
10. When uncertain, resolve the boundary explicitly rather than assuming.

## 13. Status

This document establishes the working Renaissance capability framework.

It does **not** establish:

- a final capability registry;
- a universal data model;
- a universal event model;
- a final interoperability protocol;
- a mandatory repository/service decomposition;
- a complete autonomy policy;
- a final governance model;
- or a requirement that every named capability become a separate system.

Those remain open architectural questions until explicitly decided.
