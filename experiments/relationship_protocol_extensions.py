"""Bounded experiment for unknown extensions and conditional fields."""
from __future__ import annotations

from copy import deepcopy


def preserve_unknown_extensions(envelope: dict, extensions: dict) -> dict:
    result = deepcopy(envelope)
    result["extensions"] = deepcopy(extensions)
    return result


def preserve_conditional_fields(envelope: dict, *, provenance=None, status_history=None) -> dict:
    result = deepcopy(envelope)
    if provenance is not None:
        result["provenance"] = deepcopy(provenance)
    if status_history is not None:
        result["status_history"] = deepcopy(status_history)
    return result


def required_core_fields(envelope: dict) -> set[str]:
    """Experiment-level core: identity, participants, and relationship meaning."""
    return {"identity", "participants", "relationship_type"}.intersection(envelope)
