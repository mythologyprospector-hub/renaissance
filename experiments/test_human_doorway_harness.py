"""Tests for the Human Doorway semantic harness and its corpus."""

from __future__ import annotations

import unittest

from human_doorway_harness import CASES, VARIANT_CASES, MUTATION_TEMPLATES, evaluate, mutate_case


class HumanDoorwayHarnessTests(unittest.TestCase):
    def test_corpus_is_deterministic_and_covers_boundary_cases(self) -> None:
        names = [case.name for case in CASES]

        self.assertGreaterEqual(len(CASES), 8)
        self.assertGreaterEqual(len(VARIANT_CASES), 8)
        self.assertEqual(len(names), len(set(names)))

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
        self.assertTrue(required.issubset(names))

    def test_harness_enforces_negative_authority_invariants(self) -> None:
        case = next(case for case in CASES if case.name == "learning")

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

        self.assertFalse(result["passed"])
        self.assertIn(
            "classification must not create authorization",
            result["failures"],
        )

    def test_harness_enforces_expression_preservation(self) -> None:
        case = next(case for case in CASES if case.name == "conversation")

        def bad_adapter(_case):
            return {"path": "conversation", "expression": "rewritten"}

        result = evaluate(bad_adapter, (case,))[0]

        self.assertFalse(result["passed"])
        self.assertIn("expression was not preserved exactly", result["failures"])

    def test_semantic_mutations_preserve_expected_boundary(self) -> None:
        for case in CASES[:4]:
            for mutation in MUTATION_TEMPLATES:
                mutated = mutate_case(case, mutation)
                self.assertEqual(mutated.expected_path, case.expected_path)
                self.assertEqual(mutated.expected_capability, case.expected_capability)
                self.assertEqual(mutated.expected_mode, case.expected_mode)
                self.assertNotEqual(mutated.expression, case.expression)


if __name__ == "__main__":
    unittest.main()
