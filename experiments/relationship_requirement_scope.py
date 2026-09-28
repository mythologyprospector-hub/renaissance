"""Bounded experiment for separating Renaissance-level invariants from project-level semantics.

This experiment does not change canon or architecture. It tests a classification rule:
Renaissance-level requirements protect the interoperability boundary itself;
project-level requirements define domain meaning or implementation mechanics.
"""

RENAISSANCE_LEVEL = {
    "relationship_identity",
    "participants_and_references",
    "relationship_meaning_preservation",
    "origin_and_provenance",
    "transformation_distinction",
    "status_history_preservation",
    "epistemic_authority_neutrality",
    "failure_transparency",
}

PROJECT_LEVEL = {
    "domain_relationship_vocabulary",
    "domain_semantics",
    "internal_data_model",
    "translation_dictionary",
    "wire_format",
    "transport_protocol",
    "identifier_syntax",
    "security_mechanism",
}


def classify_requirement(name: str) -> str:
    if name in RENAISSANCE_LEVEL:
        return "renaissance_boundary_invariant"
    if name in PROJECT_LEVEL:
        return "project_contract_or_implementation"
    raise ValueError(f"unclassified requirement: {name}")


def classification_is_domain_neutral(name: str) -> bool:
    return classify_requirement(name) == "renaissance_boundary_invariant"


def project_requirement_can_remain_independent(name: str) -> bool:
    return classify_requirement(name) == "project_contract_or_implementation"


def all_classified(requirements: list[str]) -> bool:
    return all(
        classify_requirement(name)
        in {"renaissance_boundary_invariant", "project_contract_or_implementation"}
        for name in requirements
    )
