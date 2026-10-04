"""Tests for the Human Doorway semantic harness and its corpus."""

from __future__ import annotations

from experiments.human_doorway_harness import CASES, evaluate


def test_corpus_is_deterministic_and_covers_boundary_cases() -> None:
    names = [case.name for case in CASES]

    assert len(CASES) >= 8
    assert len(names) == len(set(names))

    required = {
        "conversation",
        "learning",
        "inquiry",
        "problem_solving",
        "ambiguous",
        "operational",
        "unsupported",
        "correction",
        "compound",
    }
    assert required.issubset(names)


def test_harness_enforces_negative_authority_invariants() -> None:
    case = CASES[1]

    def bad_adapter(_case):
        return {
            "path": "capability_request",
            "capability": "learn",
            "mode": "answer",
            "expression": case.expression,
            "authorized": True,
            "evidence": False,
            "attention_choice": False,
            "executed": False,
        }

    result = evaluate(bad_adapter, (case,))[0]

    assert not result["passed"]
    assert "classification must not create authorization" in result["failures"]


def test_harness_enforces_expression_preservation() -> None:
    case = CASES[0]

    def bad_adapter(_case):
        return {"path": "conversation", "expression": "rewritten"}

    result = evaluate(bad_adapter, (case,))[0]

    assert not result["passed"]
    assert "expression was not preserved exactly" in result["failures"]
