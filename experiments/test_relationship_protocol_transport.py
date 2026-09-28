import unittest

from relationship_protocol_transport import (
    transport,
    transport_preserves_relationship,
    transport_does_not_add_authority,
    transport_does_not_claim_agreement,
    transport_does_not_replace_provenance,
)


class RelationshipProtocolTransportTest(unittest.TestCase):
    def setUp(self):
        self.source = {
            "identity": "rel-transport-1",
            "participants": {"subject": "a", "object": "b"},
            "relationship_type": "supports",
            "provenance": {"source": "system-a"},
            "authority": None,
        }

    def test_transport_preserves_relationship(self):
        moved = transport(self.source, "system-b")
        self.assertTrue(transport_preserves_relationship(self.source, moved))

    def test_transport_does_not_add_authority(self):
        moved = transport(self.source, "system-b")
        self.assertTrue(transport_does_not_add_authority(self.source, moved))

    def test_transport_does_not_claim_agreement(self):
        moved = transport(self.source, "system-b")
        self.assertTrue(transport_does_not_claim_agreement(moved))

    def test_transport_does_not_replace_provenance(self):
        moved = transport(self.source, "system-b")
        self.assertTrue(transport_does_not_replace_provenance(self.source, moved))

    def test_destination_is_transport_metadata_not_relationship_meaning(self):
        moved = transport(self.source, "system-b")
        self.assertEqual(moved["transport"]["destination"], "system-b")
        self.assertEqual(moved["relationship_type"], "supports")


if __name__ == "__main__":
    unittest.main()
