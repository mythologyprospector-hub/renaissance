# Capability Request — Real Workflow Boundary MVT

**Status:** Experiment / validation  
**Capability:** Learn  
**Evidence workflow:** `CAPABILITIES/LEARN_EXPERIMENT_001A_LINUX_PATHS_RESULT.md`

## Question

Can the Capability Request boundary represent a real Renaissance capability interaction without inventing a new front door, changing the capability's semantics, or turning the interaction into an authorization or epistemic artifact?

## Real workflow

Learn Experiment 001A was actually executed conversationally on 2026-09-30.

The workflow had a concrete learner goal, baseline, bounded instruction, immediate task, transfer task, reflection, and recorded evidence. The execution record explicitly distinguishes exposure, performance, transfer, and reflection and does not manufacture a universal learning score.

This is sufficient to test the boundary against an actual Renaissance capability interaction rather than a hypothetical request.

## Candidate Capability Request

The interaction can be represented minimally as:

```
CapabilityRequest
  id: <new interaction identifier>
  source_ref: <conversation/interaction reference when available>
  expression: <preserved human request/expression>
  capability: learn
  intent: increase ability to reason about Linux filesystem paths
  target_ref: linux-filesystem-paths
  constraints:
    - conceptual/read-only
    - no system changes
  context_refs:
    - Learn Experiment 001
    - Learn Experiment 001A
  mode: answer
  authorization_ref: omitted
  outcome_ref: <execution record>
```

The exact identifiers and storage location are intentionally not established by this experiment.

## Boundary tests

### 1. Human expression remains recoverable
**PASS.** The Capability Request can preserve the originating expression separately from the interpreted learning goal.

### 2. Capability classification remains distinct from execution
**PASS.** The request identifies Learn without becoming the execution record.

### 3. Capability classification does not authorize action
**PASS.** The workflow is conceptual/read-only and requires no consequential authorization.

### 4. Learn semantics remain owned by Learn
**PASS.** The experiment's actual distinctions and acceptance conditions remain in the Learn contract and execution record.

### 5. Execution evidence remains distinct
**PASS.** The execution record remains evidence about the learning interaction; the Capability Request does not become evidence merely by pointing to it.

### 6. Attention Choice is not manufactured unnecessarily
**PASS.** This interaction can be answered/taught without creating an Attention Choice. No separate investigation was required.

### 7. Existing front door remains sufficient
**PASS conceptually.** The real interaction demonstrates that a Capability Request is a semantic interpretation of an existing human interaction, not a replacement front door.

## Finding

A real Renaissance capability interaction now exists that exercises the proposed boundary.

The smallest useful relationship is:

```
human expression
    ↓
Capability Request
    ↓
Learn capability workflow
    ↓
execution/result record
```

For an investigative request, the previously established Attention Choice path remains available:

```
Capability Request
    ↓
Attention Choice
    ↓
authorization when required
    ↓
Episteme investigation
```

This evidence does **not** justify a new runtime service, API, persistence layer, or universal interpreter.

## Result

**PASS.**

The Capability Request contract is now grounded by a real Renaissance capability workflow, not only conceptual tests.

The remaining implementation question is narrower: where should a Renaissance-owned semantic boundary live when this kind of capability interaction is made operational beyond conversational execution?
