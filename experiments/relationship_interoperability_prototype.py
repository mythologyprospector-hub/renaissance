"""Small, non-canonical Renaissance relationship interoperability experiment."""
from __future__ import annotations

import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def build_episteme_relationship() -> dict[str, Any]:
    """Representative instance matching Episteme's current Relationship shape."""
    return {
        "id": "11111111-1111-4111-8111-111111111111",
        "subject_id": "22222222-2222-4222-8222-222222222222",
        "predicate": "supports",
        "object_id": "33333333-3333-4333-8333-333333333333",
        "provenance": [{
            "source_id": "episteme-prototype-source",
            "captured_at": "2026-09-26T00:00:00Z",
            "source_location": "https://example.invalid/episteme-prototype",
            "source_version": "prototype-1",
            "capture_id": "44444444-4444-4444-8444-444444444444",
            "note": "Representative relationship for interoperability testing.",
        }],
        "created_at": "2026-09-26T00:00:01Z",
        "schema_version": 1,
    }


def wrap_episteme_relationship(relationship: dict[str, Any]) -> dict[str, Any]:
    """Map into a bounded experiment envelope; this is not a final protocol."""
    return {
        "identity": relationship["id"],
        "participants": {
            "subject": relationship["subject_id"],
            "object": relationship["object_id"],
        },
        "relationship_type": relationship["predicate"],
        "provenance": relationship["provenance"],
        "created_at": relationship["created_at"],
        "schema_version": relationship["schema_version"],
    }


def unwrap_to_episteme_relationship(envelope: dict[str, Any]) -> dict[str, Any]:
    """Reconstruct the Episteme-shaped relationship without retaining the source object."""
    return {
        "id": envelope["identity"],
        "subject_id": envelope["participants"]["subject"],
        "predicate": envelope["relationship_type"],
        "object_id": envelope["participants"]["object"],
        "provenance": envelope["provenance"],
        "created_at": envelope["created_at"],
        "schema_version": envelope["schema_version"],
    }


def round_trip(envelope: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    exported = canonical_json(envelope)
    imported = json.loads(exported)
    reexported = canonical_json(imported)
    return exported, imported, reexported
