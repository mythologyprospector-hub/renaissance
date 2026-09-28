"""Bounded experiment for provenance and transformation lineage."""
from __future__ import annotations

from copy import deepcopy


def record_transformation(source_id: str, transformation: dict, *, output_id: str) -> dict:
    return {
        "source_relationship_id": source_id,
        "output_relationship_id": output_id,
        "transformation": deepcopy(transformation),
    }


def preserve_lineage(envelope: dict, lineage: list[dict]) -> dict:
    result = deepcopy(envelope)
    result["lineage"] = deepcopy(lineage)
    return result


def lineage_source_ids(envelope: dict) -> tuple[str, ...]:
    return tuple(item["source_relationship_id"] for item in envelope.get("lineage", []))
