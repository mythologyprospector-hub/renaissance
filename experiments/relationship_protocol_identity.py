"""Bounded experiment for the smallest stable relationship identity requirement."""
from __future__ import annotations

from copy import deepcopy


def identity_record(identity: str, origin: str) -> dict:
    """Represent identity without prescribing a syntax or global identifier system."""
    return {"identity": identity, "origin": origin}


def preserve_identity(envelope: dict, *, new_container: str | None = None) -> dict:
    result = deepcopy(envelope)
    if new_container is not None:
        result["container"] = new_container
    return result


def identity_stable(original: dict, transported: dict) -> bool:
    return (
        original.get("identity") == transported.get("identity")
        and original.get("origin") == transported.get("origin")
    )


def identities_distinct(first: dict, second: dict) -> bool:
    return (first.get("origin"), first.get("identity")) != (
        second.get("origin"), second.get("identity")
    )
