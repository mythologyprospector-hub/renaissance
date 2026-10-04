# Attention Choice Record — Minimum Viable Test

**Status:** Experiment / proposal validation  
**Subject:** `PROPOSALS/ATTENTION_CHOICE_CONTRACT.md`  
**Result:** Pass with one provenance refinement

## Test method

Test the proposed record shape against the seven previously validated cases, this time asking a narrower question:

> Can the record preserve why attention was selected and the transition into later work without duplicating epistemic artifacts or silently becoming authorization?

The proposed shape is:

```
AttentionChoice
  id
  pressure_ref
  target_ref
  supporting_refs[]
  selection_basis
  alternative_refs[]
  mode
  outcome_ref?
```

A case passes when the record remains referential, inspectable, and distinct from evidence, scientific results, and permission.

## Cases

### 1. Human asks a new question

The human request can be represented as the pressure, the requested question as the target, and the request as the selection basis.

**Result:** PASS.

The record preserves why this target received attention.

### 2. Existing Episteme gap suggests a next investigation

The Episteme gap becomes `pressure_ref`; the proposed investigation becomes `target_ref`; the relationship to the gap becomes `selection_basis`; mode is `suggest`.

**Result:** PASS.

No Episteme artifact needs to be copied.

### 3. Several possible investigations exist

One candidate becomes `target_ref`; the materially considered alternatives become `alternative_refs[]`; the local selection rule is preserved in `selection_basis`.

**Result:** PASS.

The record does not require a universal ranking.

### 4. Interesting but unrelated observation appears

There is no represented pressure connecting the observation to investigation.

**Result:** PASS.

The observation can remain available without creating an unjustified investigation choice.

### 5. Human rejects a suggestion

The original choice remains intact with mode `suggest`; the rejection can be referenced as the subsequent outcome.

**Result:** PASS.

The choice does not become false or epistemically invalid because the human declined it.

### 6. Human accepts a suggestion and investigation runs

The original choice records the suggestion and its basis; the resulting Episteme work can be referenced through `outcome_ref`.

**Result:** PARTIAL.

The record preserves the attention decision and resulting work, but it does not yet preserve **what authorized the transition from suggestion to execution**. The choice must not itself become permission merely because its mode is `execute`.

### 7. Investigation produces contradiction or new gap

The resulting Episteme artifact can be referenced by `outcome_ref`; the new gap becomes a new pressure for a later Attention Choice.

**Result:** PASS.

The original choice remains historically stable.

## Refinement discovered

For provenance, an executed choice may need an **authorization reference** distinct from the choice itself.

Conceptually:

```
authorization_ref?
```

This should point to the already-established source of authorization when execution requires one. It must not encode permission merely by existing, and it must not become a general authority model.

This is especially important for the distinction:

`suggest → human/system authorization → execute`

The Attention Choice should record the decision to attend; the authorization reference, where required, records the separate basis for being allowed to proceed.

## Conclusion

The minimal record shape is sufficient for the attention/provenance relationship in six of seven cases and exposes one real boundary condition in the seventh.

No runtime implementation is justified yet.

No universal ranking mechanism is justified.

No Episteme change is justified.

The proposal should be refined to make authorization provenance explicit without making Attention Choice itself an authorization object.
