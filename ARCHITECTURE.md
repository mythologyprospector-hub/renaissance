# Renaissance System Architecture

**Status:** Working architecture v0.2  
**Authority:** Architecture  
**Relationship to canon:** Constrained by `CONSTITUTION.md`, `CHARTER.md`, `PRINCIPLES.md`, and recorded decisions. This document does not override them.  
**Scope:** System-level architecture for Renaissance and its constellation of instruments.

---

## 1. Purpose

Renaissance exists to increase humanity's ability to understand, explore, create, and flourish.

This document defines the current system-level shape through which that purpose may be pursued.

The architecture is intentionally broader than any single repository or implementation. Renaissance is a constellation: different instruments may serve different purposes while remaining interoperable through explicit contracts and shared principles.

The governing architectural principle is:

> **Unity without sameness.**

Renaissance should unify principles and interfaces where useful without requiring every useful implementation to become part of one hierarchy, repository, or runtime.

---

## 2. Architectural layers

The current architecture has four primary layers:

```text
RENAISSANCE
constitutional foundation
        |
        v
SYSTEM ARCHITECTURE
        |
        +--------------------+
        |                    |
        v                    v
RUNTIME                CAPABILITIES
Organs                 Episteme and future capabilities
        |                    |
        +----------+---------+
                   |
                   v
          SPECIALIST / DOMAIN
              INSTRUMENTS
```

These layers describe responsibility, not necessarily deployment boundaries.

A capability may span multiple repositories. A repository may implement more than one capability. A specialist project may remain entirely independent while interoperating with Renaissance.

---

## 3. Constitutional layer

Renaissance's constitutional layer establishes the constraints within which the system operates.

It includes, at minimum:

- human agency;
- no inherent machine sovereignty;
- no inherent machine self-preservation mandate;
- epistemic discipline;
- recognition of the unknown;
- provenance;
- no silent constitutional drift;
- replaceability and forkability;
- capacity for revision and correction.

The constitutional layer is not an implementation component.

The constitutional layer does not itself act as a governing actor. During the founding phase, authority to establish, amend, or supersede foundational decisions is exercised through the governance process defined by Renaissance.

No runtime service, model, dataset, repository, or generated result acquires constitutional authority merely by existing, being widely used, or being technically central.

---

## 4. System architecture layer

The system architecture translates constitutional requirements into boundaries, responsibilities, contracts, and relationships.

It is responsible for answering questions such as:

- What belongs to Renaissance itself?
- What belongs to infrastructure?
- What constitutes a capability?
- What remains an independent instrument?
- Where does authority reside?
- What information may cross a boundary?
- What provenance must survive a transformation?
- Which interfaces must remain stable?
- Which decisions are intentionally unresolved?

The architecture must not prematurely prescribe implementation details that are not yet justified.

---

## 5. Runtime layer: Organs

**Organs is Renaissance runtime infrastructure.**

Its purpose is to provide bounded mechanisms such as:

- discovery and registration;
- communication;
- runtime state;
- coordination;
- bounded execution;
- approval boundaries;
- introspection;
- telemetry.

Organs is infrastructure, not epistemic authority.

In particular:

- Organs Memory is not automatically Renaissance's definition of knowledge.
- Critic is not constitutional authority.
- Executive is not sovereign.
- Registry is not institutional authority.
- telemetry is not epistemic evidence.
- sandbox containment is not evidence of truth.

Runtime mechanisms may implement Renaissance requirements, but they may not silently redefine Renaissance requirements.

---

## 6. Capability layer

Renaissance uses two related but distinct capability vocabularies.

**Human-facing capabilities** describe the human abilities Renaissance seeks to increase. The current provisional model names:

- Understand;
- Explore;
- Create;
- Learn.

**System responsibilities** describe classes of useful work that Renaissance may perform or support. Some bounded system responsibilities may be recognized as **system capabilities** when they warrant an explicit architectural contract.

The current conceptual system-responsibility set includes:

- discovery;
- provenance and lineage;
- relationship mapping;
- unknown and gap handling;
- hypothesis formation;
- prediction;
- experiment design;
- verification and contradiction analysis;
- interoperability.

These responsibilities may be implemented together where that is architecturally appropriate. They should not be split merely because they have distinct names.

### Attention Choice boundary

Decision 0009 establishes **Attention Choice** as a Renaissance knowledge-growth boundary above Episteme's scientific execution machinery.

An Attention Choice records the declared decision to give an identified matter attention. Its purpose is to preserve the transition:

`represented pressure → attention choice → established authorization when required → declared investigation`

The contract preserves the local reason for selection, supporting references, alternatives, mode, authorization provenance when applicable, and subsequent outcome reference without turning the choice into evidence, authority, permission, or a universal importance ranking.

Episteme remains responsible for the investigation it receives and its scientific provenance. Attention Choice does not make Episteme a global agenda setter.

The minimum referential record and field semantics are defined by `PROPOSALS/ATTENTION_CHOICE_CONTRACT.md` as accepted by Decision 0009. Implementation details remain intentionally unresolved until separately justified.


The two vocabularies do not imply a one-to-one mapping:

- one implementation may perform several system responsibilities;
- one system responsibility may support several human-facing capabilities;
- a human-facing capability does not automatically require a separate repository, service, or organ.

The human-facing model remains provisional, and the system-responsibility list is conceptual. Neither establishes a mandatory implementation decomposition.

---

## 7. Episteme

Episteme is currently a major Renaissance capability/instrument.

Its existing architecture already encompasses substantial work across:

- external acquisition;
- capture;
- grounded records;
- provenance;
- relationships;
- evidence assessment;
- contradictions;
- discovery;
- unknowns and gaps;
- hypotheses;
- predictions;
- experiment design;
- results;
- execution lineage;
- public inspection.

Episteme therefore should not be artificially decomposed into separate Renaissance systems merely to match an earlier conceptual list.

Renaissance remains the architectural authority.

If Episteme's existing structure conflicts with requirements established by Renaissance, the Renaissance-facing contract or architectural boundary may be revised through the normal change-control process. That does not transfer ownership or day-to-day control of Episteme's independent repository to Renaissance.

Conversely, Episteme does not acquire authority to define Renaissance's architecture merely because it is currently substantial or mature.

---

## 8. Specialist and independent instruments

Renaissance may encounter or interoperate with specialized instruments when a concrete architectural relationship is established.

An external project's similarity to a Renaissance capability does not, by itself, establish membership, implementation responsibility, or required integration.

Future specialist instruments may be considered under the same principle: establish the responsibility and contract first, then determine whether a relationship is actually needed.

---

## 9. Independent projects

A project can be useful to Renaissance without being owned, restructured, or governed as a Renaissance subsystem.

This is deliberate.

Independent specialist and domain projects may retain their own purposes, authorities, and architectures while remaining outside the Renaissance working constellation.

Renaissance may learn from, use, or interoperate with independent projects where appropriate. Their existence does not require architectural absorption into Renaissance.

## 10. Interoperability

Interoperability should be established through explicit contracts rather than repository ownership.

A project may participate in the Renaissance constellation by exposing or consuming defined interfaces while retaining its own internal architecture.

### Relationship interoperability

Renaissance establishes relationship interoperability as a cross-project architectural responsibility.

Independent systems may exchange explicit relationships without sharing a universal relationship ontology. Relationship semantics remain owned by the system or domain that defines them.

The interoperability boundary should preserve enough information to distinguish, as applicable:

- the relationship being represented;
- the related references;
- the origin of the assertion;
- provenance and lineage;
- transformations of the representation.

The interoperability boundary must not silently:

- reinterpret an unfamiliar relationship;
- turn transport into agreement;
- change epistemic status or authority;
- erase historical relationships;
- or replace an unfaithful translation with a misleading one.

Relationship mappings and translations are distinguishable from the source relationships they describe.

This does not establish a universal relationship vocabulary, universal ontology, universal data model, or final interoperability protocol. Those remain open until separately justified.

Conceptually:

```text
                    RENAISSANCE
                         |
              +----------+----------+
              |          |          |
            ORGANS    EPISTEME   OTHER TOOLS
              |          |          |
              +----------+----------+
                         |
                 explicit contracts
                         |
                  shared principles
```

Technical dependency does not create institutional or epistemic authority.

---

## 11. Authority boundaries

Authority must not emerge accidentally from implementation.

The intended relationship is:

```text
GOVERNANCE / ESTABLISHED AUTHORITY
          |
          v
SYSTEM ARCHITECTURE
          |
          v
CAPABILITY CONTRACTS
          |
          v
IMPLEMENTATIONS
```

The reverse relationship is not assumed.

In particular, the following do not automatically imply greater authority:

- more data;
- more computation;
- greater integration;
- greater autonomy;
- greater adoption;
- greater technical centrality.

Capability and authority are separate architectural concepts.

---

## 12. Data, provenance, and epistemic boundaries

Renaissance preserves distinctions between:

- external material;
- captured material and observations, where applicable and distinctly identified;
- evidence;
- interpretation;
- hypothesis;
- prediction;
- experiment;
- result;
- conclusion;
- unknown.

Captured material is not automatically an observation, and neither is automatically evidence.

Movement through a Renaissance component must not silently change the epistemic status of information.

Processing is not proof.

Containment is not truth.

Discovery output is not automatically evidence.

Infrastructure status is not epistemic authority.

Where transformations occur, provenance should remain available at the appropriate boundary.

---

## 13. Ownership boundaries

### Renaissance establishes and maintains

- the system purpose;
- constitutional constraints through its governance process;
- system-level architectural direction;
- cross-project architectural principles;
- decisions explicitly promoted to Renaissance authority.

### Individual projects own

- their internal implementation;
- project-specific domain semantics;
- project-specific workflows;
- project-specific experimental choices;
- their own internal documentation and development processes, subject to any explicit interoperability contract.

### Shared infrastructure does not own

- domain truth;
- constitutional authority;
- another project's purpose;
- the meaning of evidence outside its explicit contract.

---

## 14. Deliberately unresolved

This architecture does **not** yet decide:

- final Renaissance service topology;
- a universal data model;
- a universal event model;
- the final Organs API;
- final capability-to-repository boundaries;
- the final interoperability protocol;
- the complete autonomy model;
- final governance beyond the existing constitutional process;
- licensing strategy;
- complete security and privacy architecture.

These questions remain open until architectural evidence or requirements justify resolving them.

The relationship of Tiger Den and AI Foundry to Renaissance is no longer an open Renaissance architectural question. Decision 0008 establishes that both are outside the current Renaissance working constellation.

---

## 15. Architectural discipline

Before introducing a new component or boundary:

1. Search for an existing source of truth.
2. Determine whether the need is constitutional, architectural, infrastructural, capability-specific, or project-specific.
3. Prefer extending an existing appropriate boundary over creating a duplicate.
4. Preserve provenance and authority distinctions.
5. Record consequential architectural decisions.
6. Implement only after the architectural responsibility is clear.
7. Verify the implementation against the documented contract.
8. Do not restructure an independent project merely to make the constellation look cleaner.

---

## 16. Current architectural summary

```text
                         RENAISSANCE
                   constitutional foundation
                              |
                              v
                    SYSTEM ARCHITECTURE
                              |
              +---------------+---------------+
              |                               |
              v                               v
           ORGANS                       CAPABILITIES
      runtime substrate                      |
              |                    +---------+---------+
              |                    |                   |
              |                 EPISTEME          OTHER TOOLS
              |                    |                   |
              |              discovery, etc.     future specialist
              |                                  instruments
              |
              +----------------------------------+
                              |
                              v
                    SPECIALIST CONSTELLATION
                              |
                 independent projects may
                 interoperate without being
                 absorbed into Renaissance
```

The architecture is intentionally extensible.

Its purpose is not to predict every future component. Its purpose is to establish enough structure that future components can be added without silently changing what Renaissance is.
