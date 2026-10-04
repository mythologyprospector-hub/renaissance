# Attention Choice Authorization — Minimum Viable Test

**Status:** Experiment / proposal validation  
**Subject:** `PROPOSALS/ATTENTION_CHOICE_CONTRACT.md`  
**Result:** Pass

## Test method

Validate the refined distinction:

`attention choice ≠ authorization ≠ investigation`

The test asks whether an Attention Choice can preserve why a target received attention while separately preserving the provenance of authorization when execution requires it.

## Cases

### 1. Human asks a new question

**Choice:** pressure is explicit human curiosity; target is the requested question; selection basis is the human request.

**Authorization:** the applicable human direction may authorize the requested work directly.

**Result:** PASS.

The choice records attention without pretending to create authority.

### 2. Existing Episteme gap suggests a next investigation

**Choice:** pressure references the represented Episteme gap; target is the proposed investigation; selection basis is the relationship to the gap; mode is `suggest`.

**Authorization:** none is implied by the suggestion.

**Result:** PASS.

Episteme remains the scientific instrument, not the authority that decides whether the work should proceed.

### 3. Several possible investigations exist

**Choice:** one candidate is selected using an inspectable local basis; alternatives remain referable.

**Authorization:** selection does not itself authorize execution.

**Result:** PASS.

No global ranking or hidden importance score is required.

### 4. Interesting but unrelated observation appears

**Choice:** none is justified because no represented pressure or explicit human curiosity connects the observation to investigation.

**Authorization:** none.

**Result:** PASS.

The observation may remain available without manufacturing either attention or authority.

### 5. Human rejects a suggestion

**Choice:** the suggestion remains a historical attention choice.

**Authorization:** absent or explicitly not granted.

**Result:** PASS.

Rejection does not require mutating the original choice or treating the subject matter as epistemically invalid.

### 6. Human accepts a suggestion and investigation runs

**Choice:** records the original selection and its basis; mode was initially `suggest`.

**Authorization:** a separate established authorization is referenced by `authorization_ref`.

**Investigation:** Episteme receives the declared work and owns its execution/result provenance.

**Result:** PASS.

The three meanings remain distinct:

`choice → authorization reference → investigation`

The choice does not become permission merely because execution followed.

### 7. Investigation produces contradiction or new gap

**Choice:** original record remains unchanged.

**Investigation outcome:** Episteme records the contradiction/new gap.

**Next choice:** the new represented pressure may support a later Attention Choice.

**Result:** PASS.

The historical choice, authorization provenance, and scientific outcome remain distinguishable.

## Boundary checks

### Authorization reference is optional

An `authorization_ref` is required only when the applicable execution path requires separate authorization provenance.

**PASS.**

### Authorization reference does not create authority

The field points to an established source; it does not define who or what has authority.

**PASS.**

### Execute mode does not manufacture permission

`mode: execute` describes the choice's progression state. It is not itself an authorization mechanism.

**PASS.**

### Outcome does not retroactively justify selection

`outcome_ref` points to what happened after the choice. A useful result does not prove that the original selection was justified.

**PASS.**

## Conclusion

The refined contract survives the authorization test.

The smallest proposed semantic separation is now:

`represented pressure → Attention Choice → established authorization when required → declared investigation → result`

No new authority model is justified.

No runtime subsystem is justified.

No universal ranking mechanism is justified.

The remaining architectural question is whether this contract is mature enough to warrant a formal decision record, or whether another concrete boundary test is still needed.
