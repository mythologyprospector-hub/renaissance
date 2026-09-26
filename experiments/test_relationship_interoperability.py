import unittest

from relationship_interoperability_prototype import (
    build_episteme_relationship,
    round_trip,
    unwrap_to_episteme_relationship,
    wrap_episteme_relationship,
)


class RelationshipInteroperabilityTest(unittest.TestCase):
    def test_round_trip_preserves_relationship_semantics(self):
        relationship = build_episteme_relationship()
        envelope = wrap_episteme_relationship(relationship)
        exported, imported, reexported = round_trip(envelope)
        reconstructed = unwrap_to_episteme_relationship(imported)

        self.assertEqual(exported, reexported)
        self.assertEqual(reconstructed, relationship)

    def test_transport_does_not_add_epistemic_authority(self):
        envelope = wrap_episteme_relationship(build_episteme_relationship())
        _, imported, _ = round_trip(envelope)
        forbidden = {"agreed", "verified", "truth", "confidence", "epistemic_status"}
        self.assertTrue(forbidden.isdisjoint(imported))

    def test_envelope_does_not_hide_the_source_relationship(self):
        envelope = wrap_episteme_relationship(build_episteme_relationship())
        self.assertNotIn("domain_payload", envelope)


if __name__ == "__main__":
    unittest.main()
