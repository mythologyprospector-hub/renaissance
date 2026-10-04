import unittest

from learn_model import (
    Feedback,
    LearningEpisode,
    Performance,
    Transfer,
)


class LearnVerticalSliceTests(unittest.TestCase):
    def baseline(self):
        return Performance(
            task_id="baseline",
            response={"supported": 1, "inferred": 2},
            support_level="none",
            demonstrated=False,
            rationale="baseline attempt",
        )

    def test_complete_episode_requires_and_records_transfer(self):
        episode = LearningEpisode(
            goal="distinguish support from inference",
            capability_target="classify and justify claims",
            baseline=self.baseline(),
        )
        episode.add_activity("worked example and counterexample")
        episode.record_performance(
            Performance("practice", "correct", "guided", True, "used criteria")
        )
        episode.add_feedback(
            Feedback("task criteria", "Separate the source statement from your inference.")
        )
        episode.adapt("remove the worked-example prompt")
        episode.record_transfer(
            Transfer(
                "transfer",
                Performance("transfer", "correct", "reduced", True, "justified classification"),
                materially_different=True,
                reduced_scaffolding=True,
            )
        )

        evidence = episode.capability_evidence()

        self.assertEqual(evidence["status"], "bounded")
        self.assertEqual(evidence["transfer_task_id"], "transfer")
        self.assertEqual(evidence["support_level"], "reduced")

    def test_practice_without_transfer_is_not_capability_evidence(self):
        episode = LearningEpisode(
            goal="reason",
            capability_target="justify classifications",
            baseline=self.baseline(),
        )
        episode.record_performance(
            Performance("practice", "correct", "guided", True)
        )

        self.assertEqual(
            episode.capability_evidence(),
            {"status": "unresolved", "reason": "no valid transfer demonstration"},
        )

    def test_failed_transfer_remains_unresolved(self):
        episode = LearningEpisode(
            goal="reason",
            capability_target="justify classifications",
            baseline=self.baseline(),
        )
        episode.record_transfer(
            Transfer(
                "transfer",
                Performance("transfer", "wrong", "reduced", False),
                materially_different=True,
                reduced_scaffolding=True,
            )
        )

        self.assertEqual(episode.capability_evidence()["status"], "unresolved")

    def test_transfer_cannot_be_rehearsed_or_fully_scaffolded(self):
        episode = LearningEpisode("goal", "target", self.baseline())

        with self.assertRaises(ValueError):
            episode.record_transfer(
                Transfer(
                    "same",
                    Performance("same", "correct", "guided", True),
                    materially_different=False,
                    reduced_scaffolding=True,
                )
            )

        with self.assertRaises(ValueError):
            episode.record_transfer(
                Transfer(
                    "new",
                    Performance("new", "correct", "guided", True),
                    materially_different=True,
                    reduced_scaffolding=False,
                )
            )

    def test_feedback_and_adaptation_require_content(self):
        episode = LearningEpisode("goal", "target", self.baseline())

        with self.assertRaises(ValueError):
            episode.add_feedback(Feedback("criteria", ""))

        with self.assertRaises(ValueError):
            episode.adapt("")


if __name__ == "__main__":
    unittest.main()
