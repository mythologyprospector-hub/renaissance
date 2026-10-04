"""Renaissance-side Attention Choice publisher."""

from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Mapping

TOPIC = "renaissance.attention"
EVENT_TYPE = "attention_choice"
PUBLISHER = "renaissance"
REGISTRY_URL = os.environ.get("ORGAN_REGISTRY_URL", "http://localhost:8000")


class AttentionChoiceValidationError(ValueError):
    """Raised when an Attention Choice violates its accepted contract."""


@dataclass(frozen=True)
class AttentionChoice:
    id: str
    pressure_ref: str
    target_ref: str
    supporting_refs: tuple[str, ...] = field(default_factory=tuple)
    selection_basis: str = ""
    alternative_refs: tuple[str, ...] = field(default_factory=tuple)
    mode: str = "ask"
    authorization_ref: str | None = None
    outcome_ref: str | None = None

    def to_payload(self) -> dict[str, Any]:
        if not self.id or not self.pressure_ref or not self.target_ref:
            raise AttentionChoiceValidationError("id, pressure_ref, and target_ref are required")
        if not self.selection_basis:
            raise AttentionChoiceValidationError("selection_basis is required")
        if self.mode not in {"ask", "suggest", "execute"}:
            raise AttentionChoiceValidationError("mode must be ask, suggest, or execute")
        return {
            "id": self.id,
            "pressure_ref": self.pressure_ref,
            "target_ref": self.target_ref,
            "supporting_refs": list(self.supporting_refs),
            "selection_basis": self.selection_basis,
            "alternative_refs": list(self.alternative_refs),
            "mode": self.mode,
            "authorization_ref": self.authorization_ref,
            "outcome_ref": self.outcome_ref,
        }


def _request_json(url: str, *, method: str = "GET", payload: Mapping[str, Any] | None = None) -> dict[str, Any]:
    data = None
    headers: dict[str, str] = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=5.0) as response:
        decoded = json.loads(response.read().decode("utf-8"))
    if not isinstance(decoded, dict):
        raise ValueError("expected a JSON object response")
    return decoded


def discover_communications(registry_url: str = REGISTRY_URL) -> str:
    record = _request_json(f"{registry_url.rstrip('/')}/registry/organs/communications")
    base_url = record.get("base_url")
    if not isinstance(base_url, str) or not base_url:
        raise ValueError("registry response has no usable Communications base_url")
    return base_url.rstrip("/")


def publish_attention_choice(choice: AttentionChoice, *, registry_url: str = REGISTRY_URL) -> dict[str, Any]:
    payload = choice.to_payload()
    communications_url = discover_communications(registry_url)
    return _request_json(
        f"{communications_url}/bus/topics/{urllib.parse.quote(TOPIC, safe='')}/publish",
        method="POST",
        payload={"event_type": EVENT_TYPE, "payload": payload, "publisher": PUBLISHER},
    )
