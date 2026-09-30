# Learn Experiment 001A — Linux Paths — Execution Record

**Experiment:** `CAPABILITIES/LEARN_EXPERIMENT_001A_LINUX_PATHS.md`
**Execution:** 2026-09-30
**Mode:** Human learner / conversational execution
**Safety:** Conceptual/read-only; no system changes

## Baseline

Conditions:

- Current working directory: `/home/alex/projects`
- Known directory: `/home/alex/projects/atlas`
- Known directory: `/home/alex/docs`

Learner responses, recorded before instruction:

1. `./atlas` — "CWD in the folder atlas"
2. `../docs` — "parent directrory in the folder docs"
3. `/home/alex/docs` — "absolute"

No hints or correction were provided before the instruction phase.

## Instruction

The specified compact instruction was provided:

- An absolute path begins at the filesystem root, `/`.
- A relative path is interpreted from the current working directory.
- `.` means the current directory.
- `..` means the parent directory.

The specified example was provided:

From `/home/alex/projects`, `../docs` resolves to `/home/alex/docs`.

No transfer-task answers were supplied during instruction.

## Immediate Task

Conditions:

- Current working directory: `/home/alex/projects`

Learner responses:

1. `./atlas` — "CWD inside the folder atlas"
2. `../docs` — "parent directory inside the folder docs"
3. `../../` — "parent directory of the parent directory"
4. `/home/alex/projects/atlas` — "CWD"

No hints were supplied during the immediate task.

## Transfer Task

Conditions:

- Current working directory: `/srv/app/config`
- Known directory: `/srv/app/data`
- Known directory: `/srv/logs`
- Known directory: `/srv/app/config/templates`

Learner responses:

1. `../data` — "parent directory inside the data folder"
2. `../../logs` — "parent directory, parent directory inside the folder logs"
3. `./templates` — "CWD inside the folder templates"
4. Absolute path — "none"

No hints were supplied during the transfer task.

## Reflection

Learner responses:

1. How to determine where a relative path points:
   "by a . or .."

2. Approach to an unfamiliar relative path:
   "check for dots a move accordingly from my current working directory"

3. Uncertainty/corrections:
   "i dont think so"

## Observed Evidence

The execution provides recorded evidence for the experiment's defined categories:

- **Exposure:** The learner received the specified definitions and example.
- **Performance:** Immediate-task responses were recorded after instruction.
- **Transfer:** Responses were recorded after changing both the working directory and directory names, without reminders of the rule.
- **Reflection:** The learner described a procedure for resolving relative paths.

This record does not assign a universal learning score or declare a binary pass/fail result.

## Notes

The immediate and transfer responses contain observable misunderstandings of path resolution. The reflection nevertheless describes a general procedure involving `.`, `..`, and the current working directory.

No delayed-retention retest was performed in this execution.

