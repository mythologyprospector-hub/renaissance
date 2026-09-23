# Renaissance Alignment Audit — Organs

**Status:** Proposed working audit — not canon  
**Date:** 2026-09-23  
**Repository:** `mythologyprospector-hub/organs`

## Purpose

This document records the first Renaissance-oriented architectural review of Organs.

It does **not** change Organs' own canon, rename the project, or establish that Organs is a Renaissance component.

The question is narrower:

> Can the existing Organs system serve Renaissance as reusable infrastructure, and if so, what must be true before that relationship is treated as established?

---

## 1. What Organs actually is today

The repository's own current documentation describes Organs as a service-oriented runtime built from independent HTTP services ("organs") using shared conventions, Registry-based discovery, and bounded execution.

Its stated project goal is currently **Digital Djinn**: a local coding agent intended eventually to take suitable programming work from specification through a working, reviewable deliverable.

The current goal explicitly describes:

```text
customer specification
        ↓
      goal
        ↓
       plan
        ↓
      generate
        ↓
    workspace
        ↓
       build
        ↓
       test
        ↓
     telemetry
        ↓
   current state
        ↓
   diagnose / revise
        └──────────────→ test again
```

The repository is therefore **not currently a generic Renaissance runtime by its own declared identity**.

That distinction matters.

---

## 2. What appears reusable by Renaissance

Several Organs mechanisms are naturally reusable as infrastructure beneath Renaissance capabilities:

### Registry / discovery

A central registry gives independent services a discoverable identity without hardcoding one another's ports.

Potential Renaissance value:

- modular deployment;
- replaceable components;
- explicit service identity;
- bounded discovery.

### Shared organ boundary

`organ_base.py` provides a common HTTP contract for health, information, errors, telemetry, and risk gating.

Potential Renaissance value:

- common operational interface;
- consistent failure reporting;
- inspectable service boundaries;
- shared instrumentation.

### Communications BUS

The Communications service provides persistent, pull-based, broadcast event history with independent consumer cursors.

Potential Renaissance value:

- decoupled event communication;
- replayable event history;
- independent consumers;
- avoidance of direct coupling between domain organs.

The current repository explicitly leaves the question of which organs should consume which Memory topics unresolved. That restraint is useful: Renaissance should not invent subscribers merely because the bus exists.

### Memory

Memory provides persistent records, provenance-related fields, confidence/salience distinctions, proposals and decisions, relations, promises, and an "unknowable" state.

Potential Renaissance value:

- durable state;
- explicit uncertainty;
- provenance-bearing records;
- human-controlled permanence;
- relation structures.

However, Renaissance should not automatically adopt Memory's exact schema as its universal knowledge model. That would be an architectural decision requiring its own justification.

### Sandbox

Sandbox provides bounded execution in isolated containers with no network by default and resource limits.

Potential Renaissance value:

- controlled experimental execution;
- reproducible bounded computation;
- separation between an experiment and the host.

### Critic / Executive

Critic provides deterministic risk classification and Executive provides explicit goal/plan/step tracking with approval gates.

Potential Renaissance value:

- explicit authorization boundaries;
- inspectable risk classification;
- human approval for risky actions.

Renaissance's constitutional principle that automation is not consent makes these mechanisms architecturally interesting.

### Telemetry

Telemetry provides persistent operational observation and correlation support.

Potential Renaissance value:

- operational traceability;
- debugging;
- reproducibility support;
- cross-component observation.

Telemetry must remain operational telemetry unless Renaissance explicitly defines a separate epistemic meaning for an event. Operational observation is not automatically evidence about the external world.

---

## 3. What is NOT established

The following must **not** currently be inferred:

### Organs is not Renaissance

The Organs repository has its own project goal, canon, glossary, and development history.

It should not be relabeled as Renaissance infrastructure merely because its components look useful.

### Digital Djinn is not Renaissance's purpose

The coding-agent objective belongs to Organs' current project identity.

It may remain a valuable application or laboratory use of the substrate.

It is not automatically the mission of Renaissance.

### Organs' Memory is not Renaissance's epistemology

Memory contains useful mechanisms for persistence, uncertainty, proposals, decisions, and relations.

That does not make its record model the constitutional knowledge model of Renaissance.

Episteme already has an independent epistemic architecture. Any eventual relationship between Episteme and Memory must be designed rather than assumed.

### Critic is not the Renaissance constitution

Critic's deterministic risk rules are an implementation mechanism.

Renaissance's constitutional authority hierarchy is a higher-level concern.

No current Critic rule acquires constitutional authority merely because Organs implements it.

### Executive is not a sovereign

Executive's ability to track goals, plans, steps, and approvals does not make it an authority over Renaissance.

This follows directly from Renaissance's existing boundary:

> Capability is not authority.

---

## 4. Important historical residue

The current Organs README and installer documentation still contain references to **Forge**, including:

- Forge in the documented organ layout;
- Forge in installation copy lists;
- Forge in installation/startup instructions;
- Forge-specific health and runtime instructions.

The live Forge organ was previously removed from the installed system and its Registry registration was removed.

A repository-level documentation cleanup therefore appears warranted.

This is a **documentation/reality synchronization issue**, not evidence that Forge should be restored.

The correct direction is to make the repository describe the current post-Forge system, while preserving legitimate historical information where it belongs.

The cleanup should be done as a bounded maintenance pass, not as a redesign.

---

## 5. Important identity mismatch

There is a deeper issue than stale Forge documentation.

Organs' `GOAL.md` explicitly identifies its project as:

> **Digital Djinn**

and defines the project's future success in terms of a local coding agent completing programming work.

That is a legitimate project identity, but it is narrower than Renaissance.

Therefore there are presently three distinct possibilities:

### A. Organs remains an independent coding-agent project

Renaissance may use selected Organs capabilities through explicit interfaces.

### B. Organs becomes a general-purpose Renaissance substrate

That would require an explicit architectural and governance decision, followed by changing Organs' own project identity and contracts.

### C. Organs remains Digital Djinn while a future extracted substrate becomes Renaissance infrastructure

This would preserve Digital Djinn's existing mission while allowing genuinely general mechanisms to graduate into a separately governed infrastructure project.

**No choice is made by this audit.**

The current evidence supports saying only that **Organs contains reusable substrate candidates**.

---

## 6. Relationship to the Renaissance constitutional hierarchy

If Organs eventually participates in Renaissance, the relationship should follow this direction:

```text
Renaissance Constitutional Canon
              ↓
Renaissance architecture / integration contracts
              ↓
Organs' own established contracts
              ↓
Organs implementation
```

This does **not** mean Renaissance should rewrite Organs' internal canon.

It means a Renaissance integration contract would specify only the interface and obligations relevant to Renaissance.

Organs should retain authority over implementation details that do not conflict with the higher-level integration contract.

Conversely, Organs implementation must not silently become Renaissance canon.

---

## 7. Candidate Renaissance-facing role

The most defensible current description is:

> **Organs is a candidate shared runtime substrate containing reusable mechanisms for service discovery, communication, memory, bounded execution, risk gating, coordination, and telemetry. Its present project identity remains independent.**

That wording deliberately avoids claiming more than the evidence establishes.

---

## 8. Required work before formal integration

No code integration is required yet.

Before Renaissance declares a formal dependency on Organs, the following should be answered:

1. Which Organs capabilities does Renaissance actually need?
2. Which of those capabilities are sufficiently generic to justify reuse?
3. Which interfaces are stable enough to become integration contracts?
4. Does Renaissance need Organs as a whole, or only selected substrate components?
5. What happens if Renaissance needs to replace an Organs component?
6. Which Organs persistence models, if any, should Renaissance adopt?
7. How are operational telemetry and epistemic evidence kept distinct?
8. How are Renaissance's constitutional authority rules represented at the implementation boundary?
9. Does Digital Djinn remain the primary application of Organs?
10. If Organs changes its mission, what decision formally authorizes that change?

These are architecture questions, not implementation tasks.

---

## 9. Current assessment

**Working classification:** Shared infrastructure candidate.

**Confidence:** High that useful reusable substrate exists.

**Confidence:** Not yet sufficient to declare Organs itself a Renaissance core repository.

**Primary reason:** Organs currently has an independent, explicitly stated Digital Djinn mission and its own canon.

**Secondary reason:** Some of its mechanisms are general-purpose, but the boundary between generic substrate and coding-agent-specific machinery has not yet been formally defined.

**Immediate maintenance issue:** Repository documentation still describes Forge even though Forge has been removed from the live system.

---

## 10. Recommended next step

Do **not** move or rename Organs yet.

First perform a bounded **Organs substrate extraction analysis**:

- identify which organs/components are genuinely domain-neutral;
- identify which are Digital Djinn-specific;
- identify historical residue;
- identify current contracts and dependencies;
- identify what Renaissance would actually consume;
- produce a proposed boundary without implementing it.

Only after that analysis should we decide whether:

- Renaissance consumes Organs as-is;
- a subset becomes a formal shared substrate;
- Organs remains an independent application platform;
- or some other arrangement is warranted.

This preserves both projects while giving Renaissance the architectural clarity it needs.

---

## Relationship status

**Renaissance → Organs:** Proposed infrastructure relationship  
**Organs → Renaissance:** Not yet established  
**Current Organs identity:** Digital Djinn / local coding-agent infrastructure  
**Repository changes made by this audit:** None
