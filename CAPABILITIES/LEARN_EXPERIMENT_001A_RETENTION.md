# Learn Experiment 001A — Delayed Retention Check

**Status:** Protocol only — no result asserted

## Purpose

Test whether the Linux-path capability remains available after a delay without re-teaching the rule.

## Rule

Do not repeat or hint at the original instruction before the retest.

## Retest conditions

Use a new directory layout:

- Current directory: `/opt/service/config`
- Known directories:
  - `/opt/service/data`
  - `/opt/logs`
  - `/opt/service/config/templates`

Ask:

1. What does `../data` refer to?
2. What does `../../logs` refer to?
3. What does `./templates` refer to?
4. Which path is absolute: `logs/archive`, `/opt/logs`, or `../logs`?

Then ask:

> Without looking back at the earlier lesson, explain how you determine where a relative path points.

## Record

Record the learner's answers verbatim, whether any hint was given, and any uncertainty or correction.

Do not convert the result into a universal learning score.

## Interpretation

- Correct delayed transfer supports retention.
- Incorrect delayed transfer does not erase earlier evidence; it shows that the capability was not retained under this test condition.
- Hints or re-teaching invalidate the retest as a clean delayed-retention observation.

## Safety

Conceptual/read-only. No filesystem changes are required.

## Relationship to 001A

This is a follow-up to the existing Linux-path experiment. It deliberately does not change the existing execution record or invent a result.
