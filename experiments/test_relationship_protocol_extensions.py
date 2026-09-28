import unittest

from relationship_protocol_extensions import (
    preserve_unknown_extensions,
    preserve_conditional_fields,
    required_core_fields,
)


class RelationshipProtocolExtensionsTest(unittest.TestCase):
    def test_unknown_extensions_survive_without_interpretation(self):
        envelope = {
            "identity": "rel-1",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "domain_specific",
        }
        extension = {"future_field": {"opaque_value": True}}
        result = preserve_unknown_extensions(envelope, extension)
        self.assertEqual(result["extensions"], extension)
        self.assertEqual(result["relationship_type"], "domain_specific")

    def test_unknown_extensions_are_not_required_for_core_representation(self):
        envelope = {
            "identity": "rel-1",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "domain_specific",
        }
        self.assertEqual(
            required_core_fields(envelope),
            {"identity", "participants", "relationship_type"},
        )

    def test_conditional_provenance_can_be_absent(self):
        envelope = {
            "identity": "rel-1",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "domain_specific",
        }
        result = preserve_conditional_fields(envelope)
        self.assertNotIn("provenance", result)
        self.assertNotIn("status_history", result)

    def test_available_conditional_fields_are_preserved(self):
        envelope = {
            "identity": "rel-1",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "domain_specific",
        }
        provenance = [{"source_id": "source-a"}]
        history = [{"status": "asserted"}]
        result = preserve_conditional_fields(
            envelope, provenance=provenance, status_history=history
        )
        self.assertEqual(result["provenance"], provenance)
        self.assertEqual(result["status_history"], history)

    def test_extension_data_is_not_promoted_to_core_meaning(self):
        envelope = {
            "identity": "rel-1",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "domain_specific",
        }
        result = preserve_unknown_extensions(envelope, {"predicate_alias": "supports"})
        self.assertEqual(result["relationship_type"], "domain_specific")
        self.assertNotEqual(result["relationship_type"], result["extensions"]["predicate_alias"])


if __name__ == "__main__":
    unittest.main()
