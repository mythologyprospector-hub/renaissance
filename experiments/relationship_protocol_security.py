"""Bounded experiment separating security properties from epistemic authority."""
from __future__ import annotations
from copy import deepcopy


def secure_envelope(message: dict, *, authenticated: bool, authorized: bool) -> dict:
    result = deepcopy(message)
    result["security"] = {
        "authenticated": authenticated,
        "authorized": authorized,
    }
    return result


def security_is_separate_from_epistemic_status(message: dict) -> bool:
    security = message.get("security", {})
    return "epistemic_status" not in security


def authentication_does_not_create_truth(message: dict) -> bool:
    return message.get("epistemic_status") != "true" or not message.get("security", {}).get("authenticated", False)


def authorization_does_not_create_agreement(message: dict) -> bool:
    return "agreement" not in message.get("security", {})


def security_properties_survive_transport(message: dict, transported: dict) -> bool:
    return transported.get("security") == message.get("security")
