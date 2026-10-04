"""Contract tests for the Renaissance Attention Choice publisher."""

from __future__ import annotations

from unittest.mock import patch

import attention_choice_publisher as publisher


def test_attention_choice_payload_matches_contract() -> None:
    choice = publisher.AttentionChoice(
        id="ac-001",
        pressure_ref="gap-17",
        target_ref="investigation-42",
        supporting_refs=("finding-8",),
        selection_basis="resolves the represented contradiction directly connected to the current question",
        alternative_refs=("investigation-39", "investigation-41"),
        mode="suggest",
    )

    assert choice.to_payload() == {
        "id": "ac-001",
        "pressure_ref": "gap-17",
        "target_ref": "investigation-42",
        "supporting_refs": ["finding-8"],
        "selection_basis": "resolves the represented contradiction directly connected to the current question",
        "alternative_refs": ["investigation-39", "investigation-41"],
        "mode": "suggest",
        "authorization_ref": None,
        "outcome_ref": None,
    }


def test_execute_mode_does_not_create_authorization() -> None:
    choice = publisher.AttentionChoice(
        id="ac-002",
        pressure_ref="question-1",
        target_ref="investigation-2",
        selection_basis="human selected the investigation",
        mode="execute",
    )

    assert choice.to_payload()["mode"] == "execute"
    assert choice.to_payload()["authorization_ref"] is None


def test_invalid_choice_fails_before_transport() -> None:
    choice = publisher.AttentionChoice(
        id="ac-003",
        pressure_ref="question-1",
        target_ref="investigation-2",
        selection_basis="reason",
        mode="not-a-mode",
    )

    with patch.object(publisher, "_request_json") as request:
        try:
            publisher.publish_attention_choice(
                choice, registry_url="http://localhost:8000"
            )
        except publisher.AttentionChoiceValidationError:
            pass
        else:
            raise AssertionError("invalid mode was accepted")
        request.assert_not_called()


def test_publisher_discovers_communications_and_preserves_payload() -> None:
    choice = publisher.AttentionChoice(
        id="ac-004",
        pressure_ref="gap-4",
        target_ref="investigation-9",
        selection_basis="directly addresses the represented gap",
        mode="suggest",
    )
    calls = []

    def fake_request(url, *, method="GET", payload=None):
        calls.append((url, method, payload))
        if method == "GET":
            return {"name": "communications", "base_url": "http://localhost:8002"}
        return {"accepted": True, "id": 17}

    with patch.object(publisher, "_request_json", side_effect=fake_request):
        result = publisher.publish_attention_choice(
            choice, registry_url="http://localhost:8000"
        )

    assert result == {"accepted": True, "id": 17}
    assert calls[0] == (
        "http://localhost:8000/registry/organs/communications",
        "GET",
        None,
    )
    assert calls[1][0] == "http://localhost:8002/bus/topics/renaissance.attention/publish"
    assert calls[1][1] == "POST"
    assert calls[1][2] == {
        "event_type": "attention_choice",
        "payload": choice.to_payload(),
        "publisher": "renaissance",
    }
