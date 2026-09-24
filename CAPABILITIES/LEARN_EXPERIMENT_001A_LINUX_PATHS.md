# Learn Experiment 001A — Linux Paths

**Status:** Domain-specific experiment specification v0.1  
**Authority:** Experiment  
**Capability:** Learn  
**Parent experiment:** `CAPABILITIES/LEARN_EXPERIMENT_001.md`

## Purpose

Instantiate Learn Experiment 001 in a small, concrete technical domain: understanding Linux filesystem paths.

The experiment tests whether a short instructional interaction can produce transferable capability rather than merely recognition of terminology.

## Capability under test

The learner should be able to reason about filesystem paths and predict where a path refers relative to a stated working directory.

This is deliberately narrower than "learn Linux."

## Safety

The experiment is conceptual/read-only.

No file creation, deletion, modification, privilege escalation, network access, or system changes are required.

## Baseline task

Give the learner these two facts:

- current working directory: `/home/alex/projects`
- directory tree includes:
  - `/home/alex/projects/atlas`
  - `/home/alex/docs`

Ask:

1. Where does `./atlas` refer?
2. Where does `../docs` refer?
3. Is `/home/alex/docs` relative or absolute?

Record answers before teaching.

## Instruction

Provide only this compact instruction:

- An **absolute path** begins at the filesystem root, `/`.
- A **relative path** is interpreted from the current working directory.
- `.` means the current directory.
- `..` means the parent directory.

Then work through one example:

> From `/home/alex/projects`, `../docs` resolves to `/home/alex/docs`.

Do not teach the transfer tasks below.

## Immediate task

From `/home/alex/projects`, ask the learner to resolve:

1. `./atlas`
2. `../docs`
3. `../../`
4. `/home/alex/projects/atlas`

Record answers and whether hints were required.

## Transfer task

Change both the working directory and names:

Current directory:

`/srv/app/config`

Known directories:

- `/srv/app/data`
- `/srv/logs`
- `/srv/app/config/templates`

Ask:

1. What does `../data` refer to?
2. What does `../../logs` refer to?
3. What does `./templates` refer to?
4. Which of the four paths is absolute?

Do not remind the learner of the rule during the transfer task.

## Reflection

Ask the learner:

> Explain in your own words how you determine where a relative path points.

Then:

> If you were given a new relative path you had never seen before, what would you do?

Record uncertainty and corrections rather than forcing a binary pass/fail judgment.

## Evidence interpretation

### Exposure

The learner saw the definitions and example.

### Performance

The learner successfully resolved the immediate tasks.

### Transfer

The learner successfully applies the underlying rule after the directory names and working directory change.

### Reflection

The learner can describe the reasoning procedure rather than merely reproduce an answer.

### Retention

Optional later retest using a new directory tree without re-teaching the rule.

## Minimum interesting result

A useful positive result is:

- baseline shows the capability was not already demonstrated;
- learner receives the bounded instruction;
- immediate task improves;
- transfer task demonstrates the rule in a changed context;
- reflection indicates a usable procedure.

A result where immediate performance improves but transfer fails is especially valuable: it distinguishes successful short-term performance from evidence of transferable capability.

## Confounds

Record when any of these occur:

- learner already knew filesystem paths;
- task was solved through memorized pattern rather than reasoning;
- interviewer supplied hints during transfer;
- wording accidentally revealed the answer;
- learner misunderstood the task rather than the underlying concept.

## Expected architectural value

This experiment tests whether the abstract Learn distinctions can survive contact with an ordinary skill:

> **Exposure ≠ Performance ≠ Transfer.**

It also tests whether the experiment can record uncertainty without manufacturing a universal learning score.

## Result status

No result is asserted by this document.

The experiment specification precedes execution.
