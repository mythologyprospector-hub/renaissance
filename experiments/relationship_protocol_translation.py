"""Bounded experiment for faithful relationship translation."""
from __future__ import annotations

from copy import deepcopy


def translate_relationship(source: dict, mapping: dict) -> dict:
    source_type = source["relationship_type"]
    if source_type not in mapping:
        raise ValueError(f"no mapping for {source_type}")
    target_type = mapping[source_type]
    return {
        "identity": source["identity"],
        "participants": deepcopy(source["participants"]),
        "relationship_type": target_type,
        "translation": {
            "source_relationship_type": source_type,
            "target_relationship_type": target_type,
            "source_identity": source["identity"],
            "status": "experimentally_mapped",
        },
    }


def is_faithful_translation(source: dict, translated: dict) -> bool:
    record = translated.get("translation", {})
    return (
        record.get("source_identity") == source.get("identity")
        and record.get("source_relationship_type") == source.get("relationship_type")
        and translated.get("participants") == source.get("participants")
        and translated.get("translation", {}).get("status") == "experimentally_mapped"
    )
