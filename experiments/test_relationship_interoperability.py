import unittest

from relationship_interoperability_prototype import (
    build_episteme_relationship,
    translate_relationship,
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

    def test_unfamiliar_type_and_unresolved_references_remain_opaque(self):
        relationship = build_episteme_relationship()
        relationship["predicate"] = "domain_specific_relationship_unknown_to_receiver"
        relationship["subject_id"] = "urn:external:object:not-present-locally"
        relationship["object_id"] = "urn:external:object:also-not-present-locally"

        envelope = wrap_episteme_relationship(relationship)
        _, imported, reexported = round_trip(envelope)
        reconstructed = unwrap_to_episteme_relationship(imported)

        self.assertEqual(imported["relationship_type"], relationship["predicate"])
        self.assertEqual(imported["participants"]["subject"], relationship["subject_id"])
        self.assertEqual(imported["participants"]["object"], relationship["object_id"])
        self.assertEqual(reexported, round_trip(envelope)[2])
        self.assertEqual(reconstructed, relationship)

    def test_status_history_survives_transport_without_rewriting_history(self):
        relationship = build_episteme_relationship()
        relationship["status_history"].append(
            {"status": "superseded", "recorded_at": "2026-09-26T00:00:03Z"}
        )

        envelope = wrap_episteme_relationship(relationship)
        _, imported, _ = round_trip(envelope)
        reconstructed = unwrap_to_episteme_relationship(imported)

        self.assertEqual(imported["status_history"], relationship["status_history"])
        self.assertEqual(reconstructed["status_history"], relationship["status_history"])

    def test_translation_preserves_source_semantics_and_records_mapping(self):
        relationship = build_episteme_relationship()
        translated = translate_relationship(relationship, {"supports": "supports_evidence"})

        self.assertEqual(translated["translation"]["source_predicate"], "supports")
        self.assertEqual(translated["translation"]["target_predicate"], "supports_evidence")
        self.assertEqual(translated["translation"]["mapping_status"], "experimentally_mapped")
        self.assertEqual(translated["id"], relationship["id"])
        self.assertEqual(translated["subject_id"], relationship["subject_id"])
        self.assertEqual(translated["object_id"], relationship["object_id"])

    def test_unfaithful_translation_fails_without_silent_reinterpretation(self):
        relationship = build_episteme_relationship()

        with self.assertRaises(ValueError):
            translate_relationship(relationship, {})

    def test_conflicting_assertions_remain_distinct(self):
        first = build_episteme_relationship()
        second = build_episteme_relationship()
        second["id"] = "55555555-5555-4555-8555-555555555555"
        second["predicate"] = "contradicts"

        first_envelope = wrap_episteme_relationship(first)
        second_envelope = wrap_episteme_relationship(second)

        _, first_imported, _ = round_trip(first_envelope)
        _, second_imported, _ = round_trip(second_envelope)

        self.assertNotEqual(first_imported["identity"], second_imported["identity"])
        self.assertNotEqual(
            first_imported["relationship_type"],
            second_imported["relationship_type"],
        )


if __name__ == "__main__":
    unittest.main()
