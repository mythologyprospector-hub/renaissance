# Capability Request → Episteme Real Boundary MVT

**Status:** Experiment / validation

## Question

Does the second real capability boundary—Understand/investigation—compose cleanly from Capability Request through Attention Choice into an existing Episteme investigation workflow?

## Existing implementation evidence

Episteme already has a concrete finite workflow implementation. Its Phase 12 test executes:

grounded records → structural gap → candidate completions → discriminating predictions → experiment proposal → grounded result → prediction evaluation → knowledge-state consequence → renewed discovery

The workflow preserves method/version, input/output lineage, alternatives, failures, reproducibility, and grounded/generated distinctions.

This is an actual implementation surface, not a hypothetical capability.

## Boundary fixture

A Renaissance investigation request can be represented as a Capability Request with capability=understand, intent=investigate a represented unresolved question, and mode=investigate.

When the request requires selecting a specific investigation, the established Attention Choice boundary supplies the missing selection semantics:

human expression → Capability Request (understand / investigate) → Attention Choice → authorization when required → Episteme declared workflow → Episteme execution/result history

## Boundary tests

### 1. Capability Request identifies the human-facing responsibility
PASS. understand is distinct from the Episteme workflow method.

### 2. Investigation intent remains distinct from attention selection
PASS. The request says what capability work is sought; Attention Choice records which represented target receives attention and why.

### 3. Attention Choice remains distinct from Episteme execution
PASS. Episteme's workflow definition begins with declared inputs and operations; it does not need to become the reason the investigation was selected.

### 4. Authorization remains distinct
PASS. Neither mode=investigate nor an Attention Choice manufactures permission.

### 5. Episteme retains scientific semantics
PASS. Existing workflow semantics continue to own gaps, hypotheses/candidates, predictions, experiments, results, evaluations, consequences, and renewed discovery.

### 6. Episteme evidence remains distinct from upstream interpretation
PASS. The Capability Request and Attention Choice are not epistemic evidence. Episteme results retain their existing grounded/generated rules.

### 7. No second front door is required
PASS conceptually. The existing Organs front door can remain operational routing while the Renaissance semantic layers sit behind it when Renaissance capability work is present.

## Important limitation

This is a real-boundary validation against an existing Episteme implementation, but it is not a live cross-repository runtime invocation. No new adapter, API, or persistence mechanism is justified merely by this test.

## Result

PASS.

The Learn boundary was not a special case. The same semantic separation survives a real Understand/investigation path:

Capability Request ≠ Attention Choice ≠ Episteme workflow ≠ Episteme result/evidence

The remaining question is no longer whether the semantic boundaries compose. It is whether a real user-facing runtime need now exists that requires making this composition executable across repository boundaries.