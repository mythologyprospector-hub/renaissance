import unittest

from protocol_design_experiment import CANDIDATES, missing_guarantees, passes_minimum_contract

class ProtocolDesignExperimentTest(unittest.TestCase):
    def test_candidates_are_distinguishable(self):
        self.assertEqual(len({candidate.name for candidate in CANDIDATES}), len(CANDIDATES))

    def test_minimal_envelope_satisfies_proposed_guarantees(self):
        candidate = next(c for c in CANDIDATES if c.name == "minimal-envelope")
        self.assertEqual(missing_guarantees(candidate), ())
        self.assertTrue(passes_minimum_contract(candidate))

    def test_opaque_payload_exposes_loss_of_source_semantics(self):
        candidate = next(c for c in CANDIDATES if c.name == "opaque-payload")
        self.assertIn("preserves_meaning", missing_guarantees(candidate))
        self.assertFalse(passes_minimum_contract(candidate))

    def test_linked_assertion_satisfies_proposed_guarantees(self):
        candidate = next(c for c in CANDIDATES if c.name == "linked-assertion")
        self.assertEqual(missing_guarantees(candidate), ())

    def test_experiment_does_not_select_a_protocol(self):
        names = {candidate.name for candidate in CANDIDATES}
        self.assertEqual(names, {"minimal-envelope", "opaque-payload", "linked-assertion"})

if __name__ == "__main__":
    unittest.main()