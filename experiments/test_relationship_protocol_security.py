import unittest

from relationship_protocol_security import (
    secure_envelope,
    security_is_separate_from_epistemic_status,
    authentication_does_not_create_truth,
    authorization_does_not_create_agreement,
    security_properties_survive_transport,
)


class RelationshipProtocolSecurityTest(unittest.TestCase):
    def setUp(self):
        self.source = {
            "identity": "rel-security-1",
            "relationship_type": "supports",
            "epistemic_status": "asserted",
        }

    def test_authentication_is_security_metadata_not_epistemic_status(self):
        secured = secure_envelope(self.source, authenticated=True, authorized=True)
        self.assertTrue(security_is_separate_from_epistemic_status(secured))
        self.assertEqual(secured["epistemic_status"], "asserted")

    def test_authentication_does_not_create_truth(self):
        secured = secure_envelope(self.source, authenticated=True, authorized=True)
        self.assertTrue(authentication_does_not_create_truth(secured))

    def test_authorization_does_not_create_agreement(self):
        secured = secure_envelope(self.source, authenticated=True, authorized=True)
        self.assertTrue(authorization_does_not_create_agreement(secured))

    def test_security_properties_can_survive_transport_without_changing_meaning(self):
        secured = secure_envelope(self.source, authenticated=True, authorized=False)
        transported = dict(secured)
        self.assertTrue(security_properties_survive_transport(secured, transported))
        self.assertEqual(transported["epistemic_status"], "asserted")

    def test_unauthenticated_representation_can_remain_epistemically_separate(self):
        secured = secure_envelope(self.source, authenticated=False, authorized=False)
        self.assertEqual(secured["epistemic_status"], "asserted")
        self.assertFalse(secured["security"]["authenticated"])


if __name__ == "__main__":
    unittest.main()
