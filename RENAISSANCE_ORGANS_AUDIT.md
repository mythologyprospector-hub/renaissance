# Renaissance Alignment — Organs

**Status:** Established architectural relationship  
**Date:** 2026-09-23  
**Repository:** mythologyprospector-hub/organs

## Purpose

This document records the relationship between Renaissance and Organs.

The Human Gate has explicitly established that **Organs' sole purpose is to
serve Renaissance**. Organs is therefore treated as Renaissance runtime
infrastructure rather than as an independent product or competing project.

This document remains architectural documentation, not a replacement for
Renaissance constitutional canon.

---

## 1. Established role

**Organs is the runtime substrate for Renaissance.**

Its job is to provide dependable machinery for:

- service discovery and lifecycle;
- inter-component communication;
- durable runtime state;
- bounded execution;
- deterministic risk classification;
- explicit human approval paths;
- coordination;
- system introspection;
- operational telemetry;
- human-facing operation.

Renaissance domain capabilities remain separate.

Organs does not decide what Renaissance is. It implements the runtime layer
that Renaissance requires.

---

## 2. Authority relationship

The relationship is:

```
Renaissance Constitutional Canon
              ↓
Renaissance architecture and domain contracts
              ↓
Organs established runtime contracts
              ↓
Organs implementation
```

Organs implementation does not become Renaissance canon merely because it is
widely used.

Organs components have bounded responsibilities:

| Component | Role | Not its role |
|---|---|---|
| Registry | discovery | authority |
| Communications / BUS | transport | interpretation |
| Memory | runtime persistence | universal epistemology |
| Sandbox | execution containment | truth authority |
| Critic | deterministic risk classification | moral/constitutional authority |
| Executive | explicit work coordination | sovereignty |
| Orchestrator | bounded service control | arbitrary command execution |
| Introspection | operational observation | omniscience |
| Reflection | optional analysis | self-authorized action |
| Telemetry | operational history | epistemic evidence |
| I/O Interface | deterministic routing | invention of capabilities |
| TUI / Sensei | human interaction | hidden authority |

---

## 3. Current architectural boundary

Renaissance domain systems such as Episteme, Provenance, Atlas, Unknowns,
Experimentalist, Referee, and Rosetta remain independently defined.

They may consume Organs through explicit contracts.

Organs should not absorb domain semantics merely because implementing them
inside the runtime would be convenient.

In particular:

- Organs Memory is not automatically Renaissance's knowledge model.
- Operational telemetry is not automatically epistemic evidence.
- Critic rules are not constitutional law.
- Executive approval is not machine sovereignty.
- Registry identity is not institutional authority.

---

## 4. Historical cleanup

The former Digital Djinn mission is retired.

Forge is retired and must not be restored as an Organs dependency.

Historical implementation notes may remain where they explain provenance, but
they do not define current scope.

The repository's active documentation and installation paths are being
synchronized with the post-Forge architecture.

---

## 5. What this relationship permits

Organs may be changed substantially when necessary to make Renaissance
possible.

That includes:

- removing obsolete architecture;
- extracting or simplifying components;
- changing service boundaries;
- adding genuinely necessary runtime capabilities;
- improving security, reproducibility, testing, and observability;
- replacing an implementation behind a stable contract.

Such changes remain subject to Renaissance change control and Organs' own
engineering discipline.

The fact that Organs is foundational does not make it untouchable.

---

## 6. What this relationship forbids

Organs must not:

- become a separate mission;
- optimize for a different product objective;
- quietly become a general-purpose autonomous authority;
- treat its implementation as superior to Renaissance canon;
- absorb domain knowledge without an architectural decision;
- turn operational convenience into constitutional authority.

The runtime exists for the project, not the other way around.

---

## 7. Current assessment

**Classification:** Renaissance core infrastructure.

**Purpose:** Renaissance runtime substrate.

**Relationship:** Established.

**Primary architectural requirement:** keep the boundary between runtime
mechanisms and Renaissance domain/constitutional authority explicit.

**Immediate engineering requirement:** finish the post-Forge/documentation
synchronization and then perform bounded runtime hardening against the new
Renaissance role.

---

## 8. Next work

The next Organs work should be implementation-focused rather than another
identity debate:

1. complete stale-reference cleanup;
2. run the complete isolated test suite;
3. inspect failures caused by the post-Forge cleanup;
4. reconcile local /srv/organs with the repository;
5. establish the first explicit Renaissance-facing runtime contracts;
6. then return to the constellation audit and the next core repository.

No repository move or rename is required.
