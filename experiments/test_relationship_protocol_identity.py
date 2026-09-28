import unittest

from relationship_protocol_identity import (
    identity_record,
    preserve_identity,
    identity_stable,
    identities_distinct,
)


class RelationshipProtocolIdentityTest(unittest.TestCase):
    def test_identity_survives_transport_without_changing_value(self):
        original = identity_record("rel-1", "source-a")
        transported = preserve_identity(original, new_container="receiver-b")
        self.assertTrue(identity_stable(original, transported))

    def test_identity_is_opaque_to_the_interoperability_layer(self):
        original = identity_record("domain-specific-token", "source-a")
        transported = preserve_identity(original)
        self.assertEqual(transported["identity"], "domain-specific-token")

    def test_same_identity_text_can_be_distinct_across_origins(self):
        first = identity_record("rel-1", "source-a")
        second = identity_record("rel-1", "source-b")
        self.assertTrue(identities_distinct(first, second))

    def test_same_origin_and_identity_remain_the_same_identity(self):
        first = identity_record("rel-1", "source-a")
        second = identity_record("rel-1", "source-a")
        self.assertFalse(identities_distinct(first, second))

    def test_changing_identity_breaks_stability(self):
        original = identity_record("rel-1", "source-a")
        changed = identity_record("rel-2", "source-a")
        self.assertFalse(identity_stable(original, changed))


if __name__ == "__main__":
    unittest.main()
