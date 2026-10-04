# Learn Experiment 001A — Delayed Retention Check

**Status:** Result recorded — delayed retention observed

## Purpose

Test whether the Linux-path capability remains available after a delay without re-teaching the rule.

## Retest conditions

- Current directory: `/opt/service/config`
- Known directories:
  - `/opt/service/data`
  - `/opt/logs`
  - `/opt/service/config/templates`

### Learner responses

1. `../data` — "to a folder named data in the parent directory"
2. `../../logs` — "to a folder named logs in the parent of the parent directory"
3. `./templates` — "to a folder named templates in my CWD"
4. Absolute path — `/opt/logs`

Reflection:

> "by the paths number of dots"

## Observation

All four path-resolution questions were answered correctly.

No hints or re-teaching were provided during the retest.

The reflection was brief, but correctly identified the dots as the relevant navigation markers for resolving a relative path from the current working directory.

## Interpretation

This retest provides bounded evidence of delayed retention and transfer of the tested Linux-path capability under these conditions.

It does not establish permanent retention or a universal learning score.

**Evidence remains bounded to the tested capability, task conditions, and learner interaction.**

## Safety

Conceptual/read-only. No filesystem changes were required.

## Relationship to 001A

This is the completed follow-up to the Linux-path experiment. The original execution record remains unchanged.
