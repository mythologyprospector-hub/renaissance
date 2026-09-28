import unittest

from relationship_protocol_versioning import (
    negotiate_version,
    preserve_unknown_fields,
    require_explicit_compatibility,
)


class RelationshipProtocolVersioningTest(unittest.TestCase):
    def test_selects_highest_common_supported_version(self):
        self.assertEqual(negotiate_version([1, 2], [1, 2, 3]), 2)

    def test_no_common_version_is_not_silently_accepted(self):
        self.assertIsNone(negotiate_version([1], [2, 3]))

    def test_incompatible_versions_fail_explicitly(self):
        with self.assertRaises(ValueError):
            require_explicit_compatibility([1], [2])

    def test_unknown_fields_can_survive_version_boundary(self):
        message = {"identity": "rel-1", "future_extension": {"x": 1}}
        unknown = preserve_unknown_fields(message, {"identity"})
        self.assertEqual(unknown, {"future_extension": {"x": 1}})

    def test_version_selection_does_not_change_relationship_meaning(self):
        self.assertEqual(negotiate_version([1, 2], [2]), 2)


if __name__ == "__main__":
    unittest.main()
