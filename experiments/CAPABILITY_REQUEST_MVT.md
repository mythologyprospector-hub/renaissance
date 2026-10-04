# Capability Request Minimum Viable Test

**Status:** Experiment / proposal validation

## Purpose

Test whether a small Renaissance Capability Request boundary can represent ordinary human-facing interactions without collapsing interpretation, attention, authorization, or epistemic status into one object.

## Cases

### 1. Simple learning question

Expression: "Explain why the seasons happen."

Expected:

- capability: learn
- mode: answer
- no authorization required
- no Attention Choice required merely to answer

**Result: PASS**

### 2. Scientific curiosity

Expression: "I wonder whether this material behaves differently when heated."

Expected:

- capability: understand or explore may be represented depending on context;
- if ambiguity matters, clarify is valid;
- interpretation does not become evidence.

**Result: PASS**

### 3. Explicit investigation request

Expression: "Let's investigate whether the temperature changes the result."

Expected:

- capability: understand;
- mode: investigate;
- request may lead to Attention Choice and declared investigation;
- request itself is not authorization.

**Result: PASS**

### 4. Creative request

Expression: "Help me design a simple way to demonstrate this idea."

Expected:

- capability: create;
- mode: answer or suggest;
- no scientific evidence is manufactured by the creative interpretation.

**Result: PASS**

### 5. Human meaning without task conversion

Expression: "The stars are beautiful tonight."

Expected:

- the system need not manufacture a capability request merely because an utterance was received;
- if a response is desired, the interaction may remain conversational rather than becoming investigation work.

**Result: PASS**

### 6. Ambiguous expression

Expression: "Can you help me with this?"

Expected:

- clarify is valid;
- no invented target or capability;
- original expression remains preserved.

**Result: PASS**

### 7. Consequential request

Expression: "Change the system configuration so this service starts automatically."

Expected:

- interpretation may identify relevant capability or operational work;
- capability classification does not grant permission;
- existing authorization and safety gates remain authoritative.

**Result: PASS**

## Boundary checks

- Capability Request ≠ human expression — **PASS**
- Capability Request ≠ Attention Choice — **PASS**
- Capability Request ≠ authorization — **PASS**
- Capability Request ≠ Episteme evidence/result — **PASS**
- Clarification can stop premature classification — **PASS**
- Ordinary conversation need not become a durable task — **PASS**
- Current four-capability model remains provisional — **PASS**

## Conclusion

**PASS.**

The proposed boundary is small enough to represent distinct human-facing moments while preserving the existing separation between interpretation, attention, authorization, and epistemic execution.

This does not establish the contract as canon or justify implementation. The next question is whether it survives contact with actual Renaissance/Organs interaction paths and whether a durable record is needed at all.
