import unittest

from relationship_protocol_translation import (
    translate_relationship,
    is_faithful_translation,
)


class RelationshipProtocolTranslationTest(unittest.TestCase):
    def setUp(self):
        self.source = {
            "identity": "rel-source",
            "participants": {"subject": "urn:a", "object": "urn:b"},
            "relationship_type": "supports",
        }

    def test_faithful_mapping_retains_source_identity_and_participants(self):
        result = translate_relationship(self.source, {"supports": "supports_target"})
        self.assertTrue(is_faithful_translation(self.source, result))
        self.assertEqual(result["relationship_type"], "supports_target")

    def test_translation_records_source_and_target_meaning(self):
        result = translate_relationship(self.source, {"supports": "supports_target"})
        self.assertEqual(result["translation"]["source_relationship_type"], "supports")
        self.assertEqual(result["translation"]["target_relationship_type"], "supports_target")

    def test_unmapped_translation_fails_explicitly(self):
        with self.assertRaises(ValueError):
            translate_relationship(self.source, {"depends_on": "depends_on_target"})

    def test_changed_participants_are_not_faithful(self):
        result = translate_relationship(self.source, {"supports": "supports_target"})
        result["participants"]["object"] = "urn:other"
        self.assertFalse(is_faithful_translation(self.source, result))

    def test_changed_source_type_record_is_not_faithful(self):
        result = translate_relationship(self.source, {"supports": "supports_target"})
        result["translation"]["source_relationship_type"] = "different"
        self.assertFalse(is_faithful_translation(self.source, result))


if __name__ == "__main__":
    unittest.main()
