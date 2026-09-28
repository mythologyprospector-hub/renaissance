"""Bounded experiment for transport semantics."""
from __future__ import annotations
from copy import deepcopy


def transport(message: dict, destination: str) -> dict:
    """Move a representation while recording movement separately from its meaning."""
    result = deepcopy(message)
    result["transport"] = {
        "destination": destination,
        "mode": "experimental",
    }
    return result


def transport_preserves_relationship(message: dict, moved: dict) -> bool:
    return (
        moved.get("identity") == message.get("identity")
        and moved.get("participants") == message.get("participants")
        and moved.get("relationship_type") == message.get("relationship_type")
    )


def transport_does_not_add_authority(message: dict, moved: dict) -> bool:
    return moved.get("authority") == message.get("authority")


def transport_does_not_claim_agreement(moved: dict) -> bool:
    return "agreement" not in moved.get("transport", {})


def transport_does_not_replace_provenance(message: dict, moved: dict) -> bool:
    return moved.get("provenance") == message.get("provenance")
