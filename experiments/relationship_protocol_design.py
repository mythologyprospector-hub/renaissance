"""Bounded protocol-design experiment for relationship interoperability.

This compares three conceptual representation shapes against Decision 0004
and the minimal guarantees proposed in RELATIONSHIP_INTEROPERABILITY_CONTRACT.
It does not select a final protocol or serialization.
"""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    name: str
    shape: str
    preserves_identity: bool
    preserves_references: bool
    preserves_meaning: bool
    preserves_origin: bool
    preserves_transformations: bool
    preserves_history: bool
    neutral_transport: bool
    explicit_failure: bool

CANDIDATES = (
    Candidate("minimal-envelope", "explicit envelope", True, True, True, True, True, True, True, True),
    Candidate("opaque-payload", "relationship + opaque payload", True, True, False, True, False, False, True, False),
    Candidate("linked-assertion", "relationship plus linked lineage records", True, True, True, True, True, True, True, True),
)

GUARANTEES = (
    "preserves_identity",
    "preserves_references",
    "preserves_meaning",
    "preserves_origin",
    "preserves_transformations",
    "preserves_history",
    "neutral_transport",
    "explicit_failure",
)

def missing_guarantees(candidate: Candidate) -> tuple[str, ...]:
    return tuple(name for name in GUARANTEES if not getattr(candidate, name))

def passes_minimum_contract(candidate: Candidate) -> bool:
    return not missing_guarantees(candidate)