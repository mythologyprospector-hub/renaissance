"""Bounded experiment for protocol version negotiation."""
from __future__ import annotations


def negotiate_version(offered: list[int], supported: list[int]) -> int | None:
    common = sorted(set(offered) & set(supported), reverse=True)
    return common[0] if common else None


def preserve_unknown_fields(message: dict, known_fields: set[str]) -> dict:
    return {key: value for key, value in message.items() if key not in known_fields}


def require_explicit_compatibility(offered: list[int], supported: list[int]) -> int:
    selected = negotiate_version(offered, supported)
    if selected is None:
        raise ValueError("no mutually supported protocol version")
    return selected
