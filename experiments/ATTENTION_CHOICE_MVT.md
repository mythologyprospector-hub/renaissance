# Attention Choice Contract — Minimum Viable Test

**Status:** Experiment / proposal validation  
**Subject:** `PROPOSALS/ATTENTION_CHOICE_CONTRACT.md`  
**Result:** Pass with one refinement

## Test method

Run the proposed semantic unit against representative knowledge-growth situations without implementing storage, scoring, automation, or a new runtime component.

A case passes when the choice can be represented without:
- hidden importance scoring;
- converting attention into epistemic authority;
- duplicating an Episteme artifact;
- treating selection as consent;
- losing the reason the target was selected.

## Cases

### 1. Human asks a new question

**Example:** “How does color affect mood?”

**Pressure:** explicit human curiosity.  
**Target:** the question.  
**Selection basis:** human request.  
**Mode:** execute or ask, depending on what the human has authorized.

**Result:** PASS.

The contract handles direct human curiosity naturally. No ranking mechanism is required.

### 2. Existing Episteme gap suggests a next investigation

**Pressure:** an existing represented unresolved question/gap.  
**Target:** a proposed investigation addressing that pressure.  
**Selection basis:** explicit relationship to the represented gap.  
**Mode:** suggest.

**Result:** PASS.

Episteme can provide the scientific gap and investigation machinery without becoming Renaissance's global agenda setter.

### 3. Several possible investigations exist

**Pressure:** multiple represented unresolved questions.  
**Target:** one declared candidate.  
**Selection basis:** an explicit local rule or human choice.  
**Alternatives:** preserve the other candidates.

**Result:** PASS.

The contract does not require a universal score. A selection rule may be contextual and inspectable.

### 4. Interesting but unrelated observation appears

**Example:** Renaissance notices a daffodil while investigating an unrelated question.

**Pressure:** none connecting the observation to current represented work or explicit human curiosity.  
**Target:** observation may be recorded, but no investigation is justified merely by novelty.

**Result:** PASS.

This is the anti-daffodil boundary.

### 5. Human rejects a suggestion

**Pressure:** represented gap.  
**Target:** suggested investigation.  
**Mode:** suggest.  
**Outcome:** human rejection.

**Result:** PASS.

Rejection is a legitimate outcome and does not need to be treated as failure, contradiction, or epistemic evidence about the subject matter.

### 6. Human accepts a suggestion and investigation runs

**Pressure:** represented gap or explicit curiosity.  
**Selection basis:** accepted suggestion.  
**Mode:** transition from suggest to authorized execution.  
**Outcome:** reference the resulting Episteme work/history.

**Result:** PASS.

The choice remains a choice; Episteme owns the investigation and its scientific provenance.

### 7. Investigation produces contradiction or new gap

**Pressure:** prior attention choice.  
**Outcome:** Episteme produces contradiction/new gap.  
**Next pressure:** newly represented epistemic state.

**Result:** PASS.

The cycle can continue without mutating the original choice into evidence.

## Refinement discovered

The phrase **“selection basis”** is potentially too broad. It must mean an inspectable reason for this particular choice, not a hidden utility function or generalized importance calculation.

The contract should therefore distinguish:

- **selection basis:** the explicit local reason/rule used for this choice;
- **importance:** deliberately unspecified and not required.

This refinement does not require a new object or implementation.

## Conclusion

The proposed Attention Choice contract survives the minimum test.

No new runtime subsystem is justified.

No universal ranking mechanism is justified.

No Episteme change is justified.

The next architectural question is narrower:

> What is the smallest Renaissance-owned representation of an Attention Choice, if any, that must persist for provenance across the knowledge-growth cycle?

That question should be answered before implementation.
