import unittest

from builder_grounding_experiment import (
    AUTHORITY_MAP, Mission, TaskClass, required_grounding, should_reopen_decision,
)

class BuilderGroundingExperimentTest(unittest.TestCase):
    def test_routine_task_does_not_preload_full_authority(self):
        grounded = required_grounding(Mission(TaskClass.ROUTINE, "CAPABILITIES/example.md"))
        self.assertEqual(grounded, {"CAPABILITIES/example.md"})
        self.assertTrue(len(grounded) < len(AUTHORITY_MAP))

    def test_routine_task_includes_only_applicable_decisions(self):
        grounded = required_grounding(Mission(
            TaskClass.ROUTINE, "experiments/example.py",
            applicable_decisions=("DECISIONS/0004-relationship-interoperability.md",),
        ))
        self.assertIn("DECISIONS/0004-relationship-interoperability.md", grounded)
        self.assertNotIn("CONSTITUTION.md", grounded)
        self.assertNotIn("ARCHITECTURE.md", grounded)

    def test_architectural_task_adds_architecture_without_full_preload(self):
        grounded = required_grounding(Mission(
            TaskClass.ARCHITECTURAL, "CAPABILITIES/EPISTEME_CONTRACT.md",
            applicable_decisions=("DECISIONS/0004-relationship-interoperability.md",),
        ))
        self.assertIn("ARCHITECTURE.md", grounded)
        self.assertIn("DECISIONS/0004-relationship-interoperability.md", grounded)
        self.assertNotEqual(grounded, AUTHORITY_MAP)

    def test_foundational_task_requires_broad_grounding(self):
        grounded = required_grounding(Mission(TaskClass.FOUNDATIONAL, "CONSTITUTION.md"))
        self.assertTrue(AUTHORITY_MAP.issubset(grounded))

    def test_uncertain_task_broadens_instead_of_guessing(self):
        grounded = required_grounding(Mission(TaskClass.UNCERTAIN, "unknown-source"))
        self.assertTrue(AUTHORITY_MAP.issubset(grounded))
        self.assertIn("unknown-source", grounded)

    def test_boundary_crossing_broadens_routine_task(self):
        grounded = required_grounding(Mission(TaskClass.ROUTINE, "experiments/example.py", experiment_promotion=True))
        self.assertTrue(AUTHORITY_MAP.issubset(grounded))
        self.assertIn("experiments/example.py", grounded)

    def test_repository_wide_impact_broadens_grounding(self):
        grounded = required_grounding(Mission(TaskClass.ROUTINE, "AGENTS.md", repository_wide=True))
        self.assertTrue(AUTHORITY_MAP.issubset(grounded))
        self.assertIn("AGENTS.md", grounded)

    def test_settled_decision_stays_closed_without_trigger(self):
        self.assertFalse(should_reopen_decision())

    def test_new_evidence_reopens_decision(self):
        self.assertTrue(should_reopen_decision(new_evidence=True))

    def test_test_failure_reopens_decision(self):
        self.assertTrue(should_reopen_decision(implementation_failure=True))

    def test_explicit_reconsideration_reopens_decision(self):
        self.assertTrue(should_reopen_decision(explicit_reconsideration=True))

if __name__ == "__main__":
    unittest.main()