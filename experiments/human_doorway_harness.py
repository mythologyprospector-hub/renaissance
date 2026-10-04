"""Human Doorway semantic test harness.

This module deliberately does not implement a doorway. It defines the contract
between a future doorway implementation and a deterministic corpus of human
expressions.

A doorway adapter is expected to accept one Case and return a mapping describing
what it would do. The harness checks boundary invariants, not answer quality.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping


@dataclass(frozen=True)
class Case:
    name: str
    expression: str
    expected_path: str
    expected_capability: str | None = None
    expected_mode: str | None = None
    attention_allowed: bool = False


CASES = (
    Case("conversation", "That's a strange result. I need to think about it.", "conversation"),
    Case(
        "learning",
        "I want to learn how to read a Linux process map.",
        "capability_request",
        "learn",
        "answer",
    ),
    Case(
        "inquiry",
        "I have two competing explanations for this observation. How could we distinguish them?",
        "capability_request",
        "understand",
        "investigate",
        True,
    ),
    Case(
        "problem_solving",
        "I have this real problem and these constraints. Help me find safe ways to test solutions.",
        "capability_request",
        "praxis",
        "investigate",
    ),
    Case("ambiguous", "Something is wrong with this.", "clarify"),
    Case("operational", "Show me the current memory status.", "operational"),
    Case("unsupported", "Please make me a teleportation device.", "unsupported"),
    Case("correction", "No, that's not what I meant. Let me explain it another way.", "conversation"),
    Case(
        "compound",
        "I want to learn this, but first help me figure out why my current approach fails.",
        "clarify",
    ),
)


def evaluate(
    adapter: Callable[[Case], Mapping[str, Any]],
    cases: tuple[Case, ...] = CASES,
) -> list[dict[str, Any]]:
    """Run the corpus against an adapter and return inspectable case results.

    The adapter is intentionally injected. This prevents the harness from
    inventing a Renaissance runtime or pretending that the harness itself is
    the doorway.
    """

    results: list[dict[str, Any]] = []

    for case in cases:
        actual = dict(adapter(case))
        failures: list[str] = []

        if actual.get("path") != case.expected_path:
            failures.append(f"path: expected {case.expected_path!r}, got {actual.get('path')!r}")

        if case.expected_capability is not None and actual.get("capability") != case.expected_capability:
            failures.append(
                f"capability: expected {case.expected_capability!r}, got {actual.get('capability')!r}"
            )

        if case.expected_mode is not None and actual.get("mode") != case.expected_mode:
            failures.append(f"mode: expected {case.expected_mode!r}, got {actual.get('mode')!r}")

        if actual.get("expression") != case.expression:
            failures.append("expression was not preserved exactly")

        if actual.get("authorized", False):
            failures.append("classification must not create authorization")

        if actual.get("evidence", False):
            failures.append("interpretation must not create evidence")

        if actual.get("attention_choice", False) and not case.attention_allowed:
            failures.append("Attention Choice was created where the corpus does not warrant investigation")

        if actual.get("executed", False):
            failures.append("doorway classification must not silently execute cross-boundary work")

        results.append(
            {
                "name": case.name,
                "passed": not failures,
                "failures": failures,
            }
        )

    return results
