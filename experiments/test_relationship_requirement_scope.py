import unittest

from relationship_requirement_scope import (
    RENAISSANCE_LEVEL,
    PROJECT_LEVEL,
    all_classified,
    classify_requirement,
    classification_is_domain_neutral,
    project_requirement_can_remain_independent,
)


class RelationshipRequirementScopeTest(unittest.TestCase):
    def test_established_boundary_guarantees_are_renaissance_level(self):
        for name in RENAISSANCE_LEVEL:
            self.assertEqual(
                classify_requirement(name),
                "renaissance_boundary_invariant",
            )

    def test_domain_and_implementation_choices_remain_project_level(self):
        for name in PROJECT_LEVEL:
            self.assertEqual(
                classify_requirement(name),
                "project_contract_or_implementation",
            )

    def test_boundary_requirements_are_domain_neutral(self):
        self.assertTrue(
            classification_is_domain_neutral("relationship_meaning_preservation")
        )
        self.assertTrue(
            classification_is_domain_neutral("failure_transparency")
        )

    def test_project_requirements_can_remain_independent(self):
        self.assertTrue(project_requirement_can_remain_independent("wire_format"))
        self.assertTrue(
            project_requirement_can_remain_independent("domain_relationship_vocabulary")
        )

    def test_unclassified_requirement_fails_explicitly(self):
        with self.assertRaises(ValueError):
            classify_requirement("invented_requirement")

    def test_candidate_set_is_fully_classified(self):
        candidates = sorted(RENAISSANCE_LEVEL | PROJECT_LEVEL)
        self.assertTrue(all_classified(candidates))


if __name__ == "__main__":
    unittest.main()
