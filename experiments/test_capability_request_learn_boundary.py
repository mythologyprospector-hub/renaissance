import unittest

from learn_model import (
    CapabilityEvidence,
    Feedback,
    LearningEpisode,
    LearningMaterial,
    Performance,
    Transfer,
)


class CapabilityRequestLearnBoundaryTests(unittest.TestCase):
    def make_learning_result(self):
        baseline = Performance(
            task_id="baseline",
            response="unfamiliar classification",
            support_level="none",
            demonstrated=False,
            rationale="baseline attempt",
        )
        episode = LearningEpisode(
            goal="learn to distinguish source support from inference",
            capability_target="classify and justify claims",
            baseline=baseline,
        )
        episode.add_activity(
            LearningMaterial(
                "bounded instruction",
                "instruction",
                "learn-vertical-fixture",
            )
        )
        episode.record_performance(
            Performance(
                "practice",
                "supported / inferred / unresolved",
                "guided",
                True,
                "applied stated criteria",
            )
        )
        episode.add_feedback(
            Feedback("criteria", "Separate source support from inference.")
        )
        episode.adapt("remove the worked-example prompt")
        episode.record_transfer(
            Transfer(
                "transfer",
                Performance(
                    "transfer",
                    "supported / inferred / unresolved",
                    "reduced",
                    True,
                    "justified each classification",
                ),
                materially_different=True,
                reduced_scaffolding=True,
            )
        )
        return episode.capability_evidence()

    def test_request_and_learning_evidence_remain_distinct(self):
        expression = "Help me learn how to distinguish source support from inference."

        request = {
            "id": "capreq-learn-fixture",
            "source_ref": "conversation-fixture",
            "expression": expression,
            "capability": "learn",
            "intent": "increase ability to classify and justify claims",
            "target_ref": "claim-classification",
            "constraints": ["domain-light", "bounded"],
            "context_refs": ["LEARN_CONTRACT", "LEARN_INSTRUMENT_MODEL"],
            "mode": "answer",
            "authorization_ref": None,
            "outcome_ref": "learn-episode-fixture",
        }

        evidence = self.make_learning_result()

        self.assertEqual(request["expression"], expression)
        self.assertEqual(request["capability"], "learn")
        self.assertIsNone(request["authorization_ref"])
        self.assertEqual(request["outcome_ref"], "learn-episode-fixture")

        self.assertIsInstance(evidence, CapabilityEvidence)
        self.assertEqual(evidence.status, "bounded")

        # The request is interpretation; the episode is execution; the
        # evidence is the bounded result. None of these may silently collapse.
        self.assertNotEqual(request, evidence)
        self.assertEqual(evidence.transfer_task_id, "transfer")

    def test_request_does_not_create_authorization_or_epistemic_status(self):
        request = {
            "expression": "Teach me this reasoning skill.",
            "capability": "learn",
            "mode": "answer",
            "authorization_ref": None,
        }

        self.assertNotIn("evidence", request)
        self.assertNotIn("truth", request)
        self.assertNotIn("permission", request)
        self.assertIsNone(request["authorization_ref"])


if __name__ == "__main__":
    unittest.main()
