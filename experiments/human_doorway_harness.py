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

MUTATION_TEMPLATES = {
    "hedging": ("I think maybe ", ""),
    "politeness": ("Could you help me ", "?"),
    "uncertainty": ("I'm not sure, but ", ""),
    "colloquial": ("Can you help me figure out ", "?"),
}


def mutate_case(case: Case, mutation: str) -> Case:
    """Create a semantic-preserving human-language variant of a case.

    This is intentionally a small deterministic mutator. It does not claim to
    understand language; it only supplies controlled mess for a future doorway
    adapter to face.
    """
    if mutation not in MUTATION_TEMPLATES:
        raise ValueError(f"unknown mutation: {mutation}")
    prefix, suffix = MUTATION_TEMPLATES[mutation]
    expression = f"{prefix}{case.expression[0].lower() + case.expression[1:] if prefix else case.expression}{suffix}"
    return Case(
        name=f"{case.name}__{mutation}",
        expression=expression,
        expected_path=case.expected_path,
        expected_capability=case.expected_capability,
        expected_mode=case.expected_mode,
        attention_allowed=case.attention_allowed,
    )


# Variants deliberately exercise ordinary human mess without changing the
# semantic target of the seed case. These are corpus entries, not a classifier.
VARIANT_CASES = (
    Case("learning_hedged", "I'd kind of like to understand how to read a Linux process map.", "capability_request", "learn", "answer"),
    Case("learning_colloquial", "Can you teach me what I'm looking at in this process map?", "capability_request", "learn", "answer"),
    Case("inquiry_hedged", "Could these two explanations both be causing what I'm seeing?", "capability_request", "understand", "investigate", True),
    Case("inquiry_uncertain", "I'm not sure what I'm looking at, but I have a couple ideas. How can we tell?", "capability_request", "understand", "investigate", True),
    Case("problem_constraints", "I've got a real problem, and I need a solution that doesn't risk the machine. Can we work through it?", "capability_request", "praxis", "investigate"),
    Case("problem_colloquial", "This thing keeps doing something weird. Help me figure out a safe way to tackle it.", "clarify"),
    Case("ambiguous_pronoun", "It broke again. Can you help?", "clarify"),
    Case("ambiguous_context", "That doesn't make sense to me.", "clarify"),
    Case("conversation_observation", "Huh. That's interesting. I wasn't actually asking you to do anything.", "conversation"),
    Case("correction_explicit", "Nope, you've got me wrong. Let me back up and explain.", "conversation"),
    Case("compound_learning_inquiry", "Teach me this, but I also want to know which of my two explanations fits.", "clarify"),
    Case("unsupported_uncertain", "Could you build something that lets me teleport across town?", "unsupported"),
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
