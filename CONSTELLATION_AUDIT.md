# Renaissance Repository Constellation Audit

**Status:** Proposed working audit — not canon  
**Original snapshot:** 2026-09-23  
**Refresh:** 2026-09-29  
**Scope:** Public/private repositories currently visible under `mythologyprospector-hub`

## Purpose

This document records the first deliberate audit of the repository constellation surrounding Renaissance.

It is an inventory and architectural assessment, not a declaration that every repository belongs inside Renaissance.

Repository visibility and project boundaries are maintained separately from this audit. This document records the observed state and preserves historical relationships; it does not itself authorize repository restructuring.

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

Its historical development material predates Renaissance in places, but the current runtime-substrate hardening and alignment checkpoint has been completed. Historical references remain where they preserve provenance rather than define current purpose.

**Relationship:** Strong architectural candidate as Renaissance's reusable runtime substrate, but not itself the definition of Renaissance.

**Action:** Keep public. Preserve the current Renaissance runtime role while retaining legitimate historical provenance.

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

**Evidence update (2026-09-28):** A dedicated Renaissance archaeology pass inspected Episteme's current contract, provenance model, capture lineage, transformation records, and artifact execution lineage. The evidence demonstrates concrete realization of Renaissance-required distinctions between material provenance, transformations, and computational execution history. No Renaissance-owned duplicate provenance/lineage subsystem is justified by that evidence.

**Action:** Keep public. Preserve Episteme's independent identity. Treat the observed relationship as established architectural evidence, not as authorization for repository absorption or a new cross-project subsystem.

---

### 4. `tiger-den`

**Current status:** Public  
**Working classification:** Specialist / independent project — outside current Renaissance working constellation

Tiger Den maps reusable computational primitives already present in the world rather than attempting to absorb them into one implementation.

Its principles — evidence before assertion, provenance, preservation of meaningful differences, valid unknowns, discovery before synthesis, and respect for external licenses/governance — closely align with Renaissance's epistemic and interoperability goals.

**Relationship:** Its discovery/mapping work is compatible with Renaissance and was examined as architectural evidence, but Tiger Den is outside the current Renaissance working constellation. Renaissance has no current dependency, capability membership, or integration requirement for it.

**Evidence update (2026-09-28):** A dedicated archaeology pass inspected Tiger Den's computational-cartography role, provenance/evidence handling, uncertainty boundaries, corpus discipline, and research protocol. Those findings remain historical evidence of compatibility with Renaissance principles; they do not establish Renaissance membership or a current integration boundary.

**Action:** Keep public and independently governed. Preserve the archaeology as historical evidence. Do not plan Renaissance integration unless a concrete future architectural relationship is independently established.

---

### 5. `ai-foundry`

**Current status:** Public  
**Working classification:** Specialist / independent project — outside current Renaissance working constellation

AI Foundry is a local-first environment for constructing, configuring, testing, evaluating, and reproducing AI systems.

Its experimental framing is particularly compatible with Renaissance's emphasis on reproducibility, provenance, controlled experimentation, and human-supervised tooling.

It is nevertheless an engineering laboratory rather than Renaissance itself.

**Relationship:** Its laboratory practices are compatible with Renaissance provenance and reproducibility principles, but AI Foundry is outside the current Renaissance working constellation. Renaissance has no current dependency, capability membership, or integration requirement for it.

**Evidence update (2026-09-28):** A dedicated archaeology pass inspected AI Foundry's foundation, terminology, artifact model, persistence rules, evaluation/comparison workflow, and explicit Run provenance. AI Foundry concretely preserves an Experiment → Run → Result → Evaluation chain and runtime/dataset/test-case provenance within its laboratory boundary. Those findings remain historical evidence of compatibility; they do not establish Renaissance membership or a current integration boundary.

**Action:** Keep public and independently governed. Preserve the archaeology as historical evidence. Do not plan Renaissance integration unless a concrete future architectural relationship is independently established.

---

### 6. `esoteric-atlas`

**Current status:** Private  
**Working classification:** Independent/private domain project

The Esoteric Atlas is a research and learning environment for esoteric and occult traditions, historical sources, structured systems, and computational research tools.

Its explicit distinction between evidence, traditional claims, scholarly interpretations, modern interpretations, and speculation is compatible with Renaissance's epistemic principles.

Its subject matter is domain-specific, however, and should not define Renaissance's general scope.

**Relationship:** Domain-specific work with compatible principles, but no demonstrated need to remain within Renaissance's public constellation.

**Action:** Keep private and independent. Preserve the historical relationship in this audit; future interoperability remains possible if a concrete relationship is established.

---

### 7. `android-dojo`

**Current status:** Private  
**Working classification:** Independent/private domain education project

Android Dojo is a beginner-oriented educational environment for understanding Android internals and experimenting safely.

Its emphasis on reproducibility, safety, evidence, recovery, and teaching rather than reckless execution fits Renaissance's broader human-capability mission.

**Relationship:** Domain-specific educational work that does not currently need to be presented as a public Renaissance component.

**Action:** Keep private and independent. Do not force its curriculum into Renaissance architecture.

---

### 8. `android-dojo-toolkit`

**Current status:** Private  
**Working classification:** Independent/private domain tooling project

Android Dojo Toolkit is the lower-level diagnostic, recovery, firmware, partition, image, and repair workbench associated with Android Dojo.

Its evidence-first workflow, safety boundaries, verification, and instructional character fit the broader Renaissance philosophy.

**Relationship:** Technical companion to Android Dojo, without a demonstrated need to remain within Renaissance's public constellation.

**Action:** Keep private and independent. Preserve its Android-specific identity and historical relationship.

---

### 9. `notation-transposer`

**Current status:** Private  
**Working classification:** Specialist/private domain project

Notation Transposer is a music-technology project centered on a canonical musical representation, format interoperability, deterministic transformation, provenance, and explicit uncertainty.

Those engineering principles are compatible with Renaissance, but the current repository does not establish a direct Renaissance dependency or architectural role.

**Relationship:** Compatible with the wider Renaissance philosophy, but not presently demonstrated as a Renaissance public component.

**Action:** Keep private and independent. Preserve the historical relationship; revisit only when a concrete integration or constellation role exists.

---

### 10. `namagiri`

**Current status:** Public (forensic work)  
**Working classification:** Specialist / independent

Namagiri is an orchestration and inspection layer for Shiva, with a tightly bounded mission around ELF inspection, capability discovery, validation, execution planning, and controlled execution.

It has its own explicit external technical authority: the Shiva source and related source-grounded evidence.

**Relationship:** Valuable engineering work, but its present identity is specific to the Shiva/Namagiri problem.

**Action:** Keep public and independent for the current forensic/reverse-engineering work. Its Issues are being used to record forensic evidence, so public visibility is operationally useful. A README notice establishes the boundary between this work and Renaissance.

---

### 11. `behemoth`

**Current status:** Public (forensic work)  
**Working classification:** Specialist / independent forensic repository

Behemoth is a read-only forensic/disassembly table supporting the Shiva/Namagiri work.

It is operationally related to Namagiri rather than Renaissance directly.

**Relationship:** Supporting repository for the independent Namagiri/Leviathan forensic constellation.

**Action:** Keep public while its Issues serve the forensic record. Preserve the explicit README boundary; do not pull it into Renaissance merely for visual uniformity.

---

### 12. `leviathan`

**Current status:** Public (forensic work)  
**Working classification:** Specialist / independent implementation repository

Leviathan is the implementation table for the AI Orchestration Workbench, explicitly constrained to accepted Behemoth findings.

Like Behemoth, its present mission is tightly coupled to the Shiva/Namagiri investigation.

**Relationship:** Supporting repository for the independent Namagiri/Behemoth forensic constellation.

**Action:** Keep public while its Issues serve the forensic record. Preserve the explicit README boundary; do not pull it into Renaissance unless future architecture establishes a concrete relationship.

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
              |               |
        CORE CAPABILITIES   SHARED
              |           INFRASTRUCTURE
          Episteme        Organs
              |
              |
       INDEPENDENT / SPECIALIST
              |
       Tiger Den / AI Foundry
       Namagiri / Behemoth / Leviathan
       (public for forensic evidence)
       Esoteric Atlas
       Notation Transposer
       Android Dojo / Toolkit

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

Episteme supplies a concrete discovery/inquiry capability and now has independently inspected evidence showing that its existing provenance, transformation, and execution-lineage mechanisms already realize several Renaissance-required distinctions.

Tiger Den and AI Foundry have been archaeologically examined and show compatibility with Renaissance principles, but Decision 0008 places both outside the current Renaissance working constellation. Their prior evidence remains useful historical context; it does not establish membership, dependency, or an integration requirement.

The exact interfaces between current Renaissance relationships remain an architecture question and should not be invented merely because conceptual fit is attractive.

## Finding 4 — Public Renaissance does not need to contain every compatible project

Tiger Den, AI Foundry, Namagiri/Behemoth/Leviathan, Notation Transposer, Esoteric Atlas, and Android Dojo/Toolkit currently have sufficiently specific or independent missions that incorporating them into Renaissance would create artificial coupling or visual symmetry.

The current evidence supports a smaller public Renaissance boundary while preserving independent projects and historical relationships. The three reverse-engineering repositories remain public for an operational reason: their Issues are being used as a forensic evidence record. Their README notices make the boundary explicit.

## Finding 5 — Akasha should remain historical/private

Akasha contains useful archaeology but should not silently become the architectural ancestor of Renaissance.

Historical lessons can be recovered deliberately.

Architecture must be earned independently.

## Finding 6 — Relationship interoperability now has an explicit minimum boundary

The relationship-interoperability experiment chain was consolidated into Decision 0006 on 2026-09-28. That decision establishes a minimum architectural boundary covering identity, references, meaning, origin/provenance, transformation, history, epistemic neutrality, security separation, failure transparency, and domain independence.

It does **not** select a final serialization, wire protocol, universal identifier scheme, ontology, vocabulary, transport, or security mechanism. The constellation therefore has a stable interoperability boundary without a prematurely frozen universal protocol.

## Finding 7 — Repository branding should follow architecture, not replace it

A shared visual language may eventually make the constellation recognizable as one world.

That should happen **after** the relationships are documented.

The social preview should therefore be regenerated after this audit is accepted and the actual constellation language is established.

---

# Open Questions

These are intentionally unresolved:

1. Which capabilities constitute the first formal Renaissance core?
2. What exact interfaces should exist between Renaissance, Organs, Episteme, and Tiger Den?
3. Is AI Foundry infrastructure, an experimental satellite, or a future core capability?
4. Should a formal Renaissance integration contract exist for any independent repository if a concrete future relationship emerges?
5. What naming/branding conventions should shared projects follow?
6. What license model should govern Renaissance and participating repositories?
7. How should independent external authorities be represented when a Renaissance project integrates specialist software?
8. What constitutes sufficient architectural evidence to promote a satellite into core?
9. How should historical repositories be referenced without implying inherited authority?

No answer is being forced by this audit.

---

# Recommended Next Work

1. Ratify or revise the constellation model only after Human Gate review.
2. Convert the completed Episteme archaeology into explicit integration documentation only if a concrete boundary is needed; do not duplicate its existing provenance/lineage mechanisms.
3. Preserve the completed Tiger Den archaeology as historical evidence; do not create integration documentation unless a concrete future boundary is needed.
4. Preserve AI Foundry's independent laboratory boundary unless a demonstrated future interoperability need emerges.
5. Use Decision 0006 as the current minimum relationship-interoperability boundary; do not infer a final protocol from it.
6. Only then finalize the Renaissance visual identity and social preview.
7. Do not move, delete, or rename repositories merely for aesthetic uniformity.
8. Keep the public Renaissance surface focused on demonstrated architectural relationships; compatible independent work may remain outside it.

**Current status:** Proposed working document. No repository classification in this document is constitutional canon.


---

## Refresh Record — 2026-09-28

This refresh preserves the 2026-09-23 audit as repository history while incorporating evidence gathered through subsequent Renaissance work. The refresh records observations and relationship status; it does not amend constitutional canon, select final integration protocols, or authorize repository restructuring.

Completed evidence work incorporated here:

- Relationship interoperability: Decision 0006 establishes the minimum architectural boundary without freezing a final protocol.
- Episteme: current provenance, transformation, capture-lineage, and artifact-execution-lineage mechanisms were inspected; no duplicate Renaissance provenance subsystem is justified.
- Tiger Den: computational-cartography/discovery relationship to Renaissance is demonstrated; integration remains deferred.
- AI Foundry: local experiment/run/result/evaluation provenance is demonstrated; formal Renaissance integration remains deferred.

These findings remain subordinate to the repository's existing authority hierarchy and change-control process.

---

## Refresh Record — 2026-09-29

This refresh records the current public-boundary clarification following Human Gate review. Android Dojo and Android Dojo Toolkit are now private. Esoteric Atlas and Notation Transposer are now private. Namagiri, Behemoth, and Leviathan remain public because their Issues are being used as a forensic evidence record for ongoing reverse-engineering work; their README notices explicitly distinguish that work from Renaissance.

The resulting distinction is deliberate: public visibility does not imply Renaissance membership, and private visibility does not imply architectural rejection. Renaissance remains responsible for its own demonstrated foundation and relationships, while independent projects retain their own identities and purposes.

---

## Refresh Record — 2026-09-29 — Decision 0008 Boundary Clarification

Decision 0008 clarifies that **Tiger Den and AI Foundry are outside the current Renaissance working constellation**. Their prior archaeology remains historical evidence of compatibility with Renaissance principles, but neither is a Renaissance implementation of Explore or Create, Renaissance does not depend on either, and no current integration is authorized or required.

This clarification preserves both projects' independent identities and does not reject the possibility of a future relationship. Any such relationship must be established independently from a concrete architectural need rather than inferred from compatibility alone.
