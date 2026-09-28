"""Conformance checks for the authorized minimum relationship boundary.

These tests exercise Decision 0006 against the existing bounded experiment
without selecting a final protocol, serialization, or universal data model.
"""

import unittest

from relationship_interoperability_prototype import (
    build_episteme_relationship,
    copy_for_federation,
    translate_relationship,
    unwrap_to_episteme_relationship,
    wrap_episteme_relationship,
)


class RelationshipBoundaryConformanceTest(unittest.TestCase):
    def setUp(self):
        self.relationship = build_episteme_relationship()

    def test_identity_is_preserved(self):
        envelope = wrap_episteme_relationship(self.relationship)
        self.assertEqual(envelope["identity"], self.relationship["id"])

    def test_references_remain_representable(self):
        self.relationship["subject_id"] = "urn:external:subject"
        self.relationship["object_id"] = "urn:external:object"
        envelope = wrap_episteme_relationship(self.relationship)
        self.assertEqual(envelope["participants"]["subject"], "urn:external:subject")
        self.assertEqual(envelope["participants"]["object"], "urn:external:object")

    def test_meaning_remains_explicit(self):
        self.relationship["predicate"] = "domain_specific_relationship"
        envelope = wrap_episteme_relationship(self.relationship)
        self.assertEqual(envelope["relationship_type"], "domain_specific_relationship")

    def test_origin_and_provenance_remain_distinguishable(self):
        envelope = wrap_episteme_relationship(self.relationship)
        self.assertEqual(envelope["provenance"], self.relationship["provenance"])

    def test_transformation_is_distinguishable_from_source(self):
        translated = translate_relationship(self.relationship, {"supports": "supports_evidence"})
        self.assertEqual(translated["translation"]["source_predicate"], "supports")
        self.assertEqual(translated["translation"]["target_predicate"], "supports_evidence")

    def test_history_is_not_destructively_rewritten(self):
        self.relationship["status_history"].append(
            {"status": "superseded", "recorded_at": "2026-09-26T00:00:03Z"}
        )
        reconstructed = unwrap_to_episteme_relationship(
            wrap_episteme_relationship(self.relationship)
        )
        self.assertEqual(reconstructed["status_history"], self.relationship["status_history"])

    def test_transport_does_not_create_epistemic_authority(self):
        envelope = wrap_episteme_relationship(self.relationship)
        for forbidden in ("truth", "verified", "agreed", "authority", "confidence"):
            self.assertNotIn(forbidden, envelope)

    def test_federation_does_not_replace_source_identity_or_provenance(self):
        copied = copy_for_federation(self.relationship, "domain-b")
        self.assertEqual(copied["id"], self.relationship["id"])
        self.assertEqual(copied["provenance"], self.relationship["provenance"])
        self.assertNotEqual(copied["federation"]["destination"], self.relationship["id"])

    def test_unfaithful_translation_fails_explicitly(self):
        with self.assertRaises(ValueError):
            translate_relationship(self.relationship, {})

    def test_domain_specific_meaning_does_not_require_shared_ontology(self):
        self.relationship["predicate"] = "has_observed_spectrum"
        envelope = wrap_episteme_relationship(self.relationship)
        self.assertNotIn("ontology", envelope)
        self.assertEqual(envelope["relationship_type"], "has_observed_spectrum")


if __name__ == "__main__":
    unittest.main()
