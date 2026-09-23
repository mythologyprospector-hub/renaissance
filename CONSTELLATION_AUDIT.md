# Renaissance Repository Constellation Audit

**Status:** Proposed working audit — not canon  
**Date:** 2026-09-23  
**Scope:** Public/private repositories currently visible under `mythologyprospector-hub`

## Purpose

This document records the first deliberate audit of the repository constellation surrounding Renaissance.

It is an inventory and architectural assessment, not a declaration that every repository belongs inside Renaissance.

No repository is being moved, deleted, renamed, made private, or otherwise altered by this document.

The governing question is:

> Does this repository have a coherent relationship to Renaissance's purpose, and if so, what kind of relationship?

Renaissance's purpose is:

> **Renaissance exists to increase humanity's ability to understand, explore, create, and flourish.**

The audit therefore distinguishes between:

- **Foundation** — defines Renaissance itself.
- **Core capability** — directly implements a major Renaissance capability.
- **Shared infrastructure** — provides reusable technical substrate.
- **Supporting/satellite project** — advances a domain or capability that may belong in the wider constellation without being part of the core.
- **Specialist/independent project** — useful work whose present mission is sufficiently specific or externally bounded that it should remain independent unless a later decision establishes a stronger relationship.
- **Historical/private** — preserved for archaeology, provenance, or future reconsideration rather than treated as current architecture.

These are working classifications, not rankings.

---

## Current Repository Inventory

### 1. `renaissance`

**Current status:** Public  
**Working classification:** Foundation

The constitutional and foundational home of Renaissance.

It establishes purpose, principles, boundaries, epistemic distinctions, authority hierarchy, governance during the founding phase, and change control.

**Relationship:** Direct and definitive.

**Action:** Keep as the umbrella/foundation repository.

---

### 2. `organs`

**Current status:** Public  
**Working classification:** Shared infrastructure / probable core substrate

Organs is a general-purpose service substrate built around independently deployable organs, Registry-based discovery, HTTP communication, Memory, Telemetry, Sandbox, Critic, Executive, I/O, and related infrastructure.

Its architecture maps naturally onto Renaissance's need for reusable infrastructure beneath domain-specific capabilities.

However, it currently contains historical architectural material that predates Renaissance, including references to Forge and Akasha-era development. Forge has already been removed from the live system, but the repository still requires a deliberate source/documentation cleanup pass.

**Relationship:** Strong architectural candidate as Renaissance's reusable runtime substrate, but not itself the definition of Renaissance.

**Action:** Keep public. Later perform a Renaissance-alignment audit and remove stale historical assumptions from active documentation without erasing legitimate history.

---

### 3. `episteme`

**Current status:** Public  
**Working classification:** Core capability

Episteme directly addresses scientific discovery, evidence, provenance, unknowns, hypotheses, predictions, experiments, results, acquisition, execution history, and reproducibility.

Its canonical invariant:

> **No information may gain epistemic authority merely by passing through Episteme.**

is strongly compatible with Renaissance's epistemic foundation.

Episteme's own README explicitly states that it is an independent project and that historical experiments are archaeology rather than inherited architecture. That independence should be respected unless a later Renaissance decision establishes an explicit integration relationship.

**Relationship:** Strong candidate for a Renaissance core capability while remaining independently governed as software.

**Action:** Keep public. Do not rewrite Episteme's identity prematurely. Establish the relationship through architecture/integration documentation first.

---

### 4. `tiger-den`

**Current status:** Public  
**Working classification:** Core-adjacent discovery infrastructure / likely Renaissance capability

Tiger Den maps reusable computational primitives already present in the world rather than attempting to absorb them into one implementation.

Its principles — evidence before assertion, provenance, preservation of meaningful differences, valid unknowns, discovery before synthesis, and respect for external licenses/governance — closely align with Renaissance's epistemic and interoperability goals.

**Relationship:** Strong candidate for a Renaissance capability concerned with discovering and mapping existing computational knowledge.

**Action:** Keep public. Treat as a candidate core/satellite capability pending explicit architecture work.

---

### 5. `ai-foundry`

**Current status:** Public  
**Working classification:** Supporting infrastructure / experimental laboratory

AI Foundry is a local-first environment for constructing, configuring, testing, evaluating, and reproducing AI systems.

Its experimental framing is particularly compatible with Renaissance's emphasis on reproducibility, provenance, controlled experimentation, and human-supervised tooling.

It is nevertheless an engineering laboratory rather than Renaissance itself.

**Relationship:** Potential Renaissance experimental/engineering infrastructure.

**Action:** Keep public. Do not force it into the core until the architecture demonstrates an actual dependency or integration need.

---

### 6. `esoteric-atlas`

**Current status:** Public  
**Working classification:** Domain satellite

The Esoteric Atlas is a research and learning environment for esoteric and occult traditions, historical sources, structured systems, and computational research tools.

Its explicit distinction between evidence, traditional claims, scholarly interpretations, modern interpretations, and speculation is compatible with Renaissance's epistemic principles.

Its subject matter is domain-specific, however, and should not define Renaissance's general scope.

**Relationship:** Good example of a domain-specific Renaissance satellite.

**Action:** Keep public. Preserve its independent domain identity while allowing future Renaissance interoperability.

---

### 7. `android-dojo`

**Current status:** Public  
**Working classification:** Domain satellite / education

Android Dojo is a beginner-oriented educational environment for understanding Android internals and experimenting safely.

Its emphasis on reproducibility, safety, evidence, recovery, and teaching rather than reckless execution fits Renaissance's broader human-capability mission.

**Relationship:** Domain-specific educational satellite.

**Action:** Keep public. Do not force its curriculum into Renaissance core architecture.

---

### 8. `android-dojo-toolkit`

**Current status:** Public  
**Working classification:** Domain tooling satellite

Android Dojo Toolkit is the lower-level diagnostic, recovery, firmware, partition, image, and repair workbench associated with Android Dojo.

Its evidence-first workflow, safety boundaries, verification, and instructional character fit the broader Renaissance philosophy.

**Relationship:** Technical satellite of Android Dojo and potentially an example of Renaissance tooling in practice.

**Action:** Keep public. Preserve the Android-specific identity.

---

### 9. `notation-transposer`

**Current status:** Public  
**Working classification:** Specialist domain satellite / presently independent

Notation Transposer is a music-technology project centered on a canonical musical representation, format interoperability, deterministic transformation, provenance, and explicit uncertainty.

Those engineering principles are compatible with Renaissance, but the current repository does not establish a direct Renaissance dependency or architectural role.

**Relationship:** Compatible with the wider Renaissance philosophy, but not presently demonstrated as core.

**Action:** Keep public and independent for now. Revisit only when a concrete integration or constellation role exists.

---

### 10. `namagiri`

**Current status:** Public  
**Working classification:** Specialist / independent

Namagiri is an orchestration and inspection layer for Shiva, with a tightly bounded mission around ELF inspection, capability discovery, validation, execution planning, and controlled execution.

It has its own explicit external technical authority: the Shiva source and related source-grounded evidence.

**Relationship:** Valuable engineering work, but its present identity is specific to the Shiva/Namagiri problem.

**Action:** Keep public and independent unless a later decision identifies a concrete Renaissance capability it implements.

---

### 11. `behemoth`

**Current status:** Public  
**Working classification:** Specialist research/support repository

Behemoth is a read-only forensic/disassembly table supporting the Shiva/Namagiri work.

It is operationally related to Namagiri rather than Renaissance directly.

**Relationship:** Supporting repository for the Namagiri specialist constellation.

**Action:** Keep with that constellation. Do not pull it into Renaissance merely for visual uniformity.

---

### 12. `leviathan`

**Current status:** Public  
**Working classification:** Specialist implementation/support repository

Leviathan is the implementation table for the AI Orchestration Workbench, explicitly constrained to accepted Behemoth findings.

Like Behemoth, its present mission is tightly coupled to the Shiva/Namagiri investigation.

**Relationship:** Supporting repository for the Namagiri/Behemoth specialist constellation.

**Action:** Keep with that constellation unless future architecture establishes otherwise.

---

### 13. `akasha`

**Current status:** Private  
**Working classification:** Historical/private archaeology

Akasha contains substantial prior experimentation, including analogy engines, domain packs, truth-kernel work, orchestration experiments, and older organ concepts.

The current Renaissance architecture explicitly does **not** inherit Akasha as its architectural ancestor.

Its historical value is real: it records experiments and lessons that may inform future work.

**Relationship:** Historical predecessor/archaeological record, not current Renaissance architecture.

**Action:** Keep private. Do not expose it as a current Renaissance component. Reuse individual lessons only when independently justified and explicitly documented.

---

## Deleted Repository

### `first-dollar`

This repository is no longer present in the account.

No restoration is proposed.

Its deletion does not create an architectural gap in the current Renaissance constellation.

---

# Preliminary Constellation Shape

The current evidence suggests a layered world rather than a single monolithic software repository:

```text
                         RENAISSANCE
                   constitutional foundation
                              |
              +---------------+---------------+
              |               |               |
        CORE CAPABILITIES   SHARED         SATELLITES
              |           INFRASTRUCTURE        |
          Episteme        Organs           Esoteric Atlas
          Tiger Den       AI Foundry        Android Dojo
                                           Android Dojo Toolkit
                                           Notation Transposer
              |
       SPECIALIST CONSTELLATIONS
              |
       Namagiri
       Behemoth
       Leviathan

       HISTORICAL / PRIVATE
              |
            Akasha
```

This diagram is a **working model**, not canon.

The important architectural conclusion is that **unity does not require sameness**.

A coherent Renaissance constellation can contain:

- one constitutional foundation;
- multiple independently useful capability repositories;
- shared infrastructure;
- domain-specific applications;
- specialist projects with their own external authorities;
- historical/private archaeology.

The relationship between repositories should be explicit rather than implied by branding alone.

---

# Findings

## Finding 1 — The account already contains a recognizable intellectual pattern

Across multiple repositories, recurring principles appear independently:

- evidence before assertion;
- provenance;
- reproducibility;
- explicit uncertainty;
- separation of representation from reality;
- controlled experimentation;
- safety boundaries;
- modularity;
- interoperability;
- human review;
- refusal to treat generated output as automatically authoritative.

This is evidence of architectural compatibility, not proof that every repository belongs to Renaissance.

## Finding 2 — Renaissance should be the constitutional layer, not a replacement for every existing project

The current Renaissance repository already says it does not contain the whole system.

That is useful.

Trying to collapse every project into one repository would erase useful domain boundaries and would make the foundation responsible for details it should not own.

## Finding 3 — Organs and Episteme currently have the clearest technical relationship to Renaissance

Organs supplies reusable runtime infrastructure.

Episteme supplies a concrete discovery/inquiry capability.

Tiger Den appears to occupy another potentially important discovery/mapping layer.

The exact interfaces between these projects remain an architecture question and should not be invented merely because the conceptual fit is attractive.

## Finding 4 — Several projects should remain independent unless a concrete relationship is demonstrated

Namagiri/Behemoth/Leviathan and Notation Transposer currently have sufficiently specific missions that forcing them into Renaissance would create artificial coupling.

Their independence is compatible with a coherent larger constellation.

## Finding 5 — Akasha should remain historical/private

Akasha contains useful archaeology but should not silently become the architectural ancestor of Renaissance.

Historical lessons can be recovered deliberately.

Architecture must be earned independently.

## Finding 6 — Repository branding should follow architecture, not replace it

A shared visual language may eventually make the constellation recognizable as one world.

That should happen **after** the relationships are documented.

The social preview should therefore be regenerated after this audit is accepted and the actual constellation language is established.

---

# Open Questions

These are intentionally unresolved:

1. Which capabilities constitute the first formal Renaissance core?
2. What exact interfaces should exist between Renaissance, Organs, Episteme, and Tiger Den?
3. Is AI Foundry infrastructure, an experimental satellite, or a future core capability?
4. Should a formal Renaissance integration contract exist for satellite repositories?
5. What naming/branding conventions should shared projects follow?
6. What license model should govern Renaissance and participating repositories?
7. How should independent external authorities be represented when a Renaissance project integrates specialist software?
8. What constitutes sufficient architectural evidence to promote a satellite into core?
9. How should historical repositories be referenced without implying inherited authority?

No answer is being forced by this audit.

---

# Recommended Next Work

1. Ratify the constellation model only after Human Gate review.
2. Perform a dedicated `organs` cleanup/alignment audit, especially stale Forge/Akasha-era references.
3. Perform a dedicated Episteme integration audit against Renaissance's epistemology and authority hierarchy.
4. Perform a Tiger Den integration audit.
5. Define the minimum Renaissance-to-project relationship contract.
6. Only then finalize the Renaissance visual identity and social preview.
7. Do not move, delete, or rename repositories merely for aesthetic uniformity.

**Current status:** Proposed working document. No repository classification in this document is constitutional canon.
