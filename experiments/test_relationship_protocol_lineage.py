import unittest

from relationship_protocol_lineage import (
    record_transformation,
    preserve_lineage,
    lineage_source_ids,
)


class RelationshipProtocolLineageTest(unittest.TestCase):
    def test_transformation_names_source_and_output(self):
        record = record_transformation(
            "rel-source",
            {"kind": "domain_mapping", "mapping": "alpha-to-beta"},
            output_id="rel-output",
        )
        self.assertEqual(record["source_relationship_id"], "rel-source")
        self.assertEqual(record["output_relationship_id"], "rel-output")
        self.assertEqual(record["transformation"]["kind"], "domain_mapping")

    def test_lineage_preserves_source_identity(self):
        envelope = {"identity": "rel-output", "relationship_type": "translated"}
        lineage = [record_transformation("rel-source", {"kind": "translation"}, output_id="rel-output")]
        result = preserve_lineage(envelope, lineage)
        self.assertEqual(lineage_source_ids(result), ("rel-source",))

    def test_lineage_does_not_replace_source_relationship(self):
        envelope = {"identity": "rel-output", "relationship_type": "translated"}
        lineage = [record_transformation("rel-source", {"kind": "translation"}, output_id="rel-output")]
        result = preserve_lineage(envelope, lineage)
        self.assertEqual(result["identity"], "rel-output")
        self.assertEqual(result["lineage"][0]["source_relationship_id"], "rel-source")

    def test_multiple_transformations_remain_ordered_and_distinct(self):
        envelope = {"identity": "rel-c", "relationship_type": "translated"}
        lineage = [
            record_transformation("rel-a", {"kind": "translation"}, output_id="rel-b"),
            record_transformation("rel-b", {"kind": "federation"}, output_id="rel-c"),
        ]
        result = preserve_lineage(envelope, lineage)
        self.assertEqual(lineage_source_ids(result), ("rel-a", "rel-b"))
        self.assertEqual(result["lineage"][0]["transformation"]["kind"], "translation")
        self.assertEqual(result["lineage"][1]["transformation"]["kind"], "federation")

    def test_no_lineage_is_valid_when_no_transformation_is_claimed(self):
        envelope = {"identity": "rel-original", "relationship_type": "native"}
        result = preserve_lineage(envelope, [])
        self.assertEqual(result["lineage"], [])


if __name__ == "__main__":
    unittest.main()
