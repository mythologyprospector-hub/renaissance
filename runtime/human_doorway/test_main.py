"""Executable contract tests for the Renaissance Human Doorway runtime."""

from __future__ import annotations

from fastapi.testclient import TestClient

from main import app, interpret


def test_contract_corpus_paths_and_expression_preservation() -> None:
    cases = (
        ("That's a strange result. I need to think about it.", "conversation", None, None),
        ("I want to learn how to read a Linux process map.", "capability_request", "learn", "answer"),
        ("I have two competing explanations for this observation. How could we distinguish them?",
         "capability_request", "understand", "investigate"),
        ("I have this real problem and these constraints. Help me find safe ways to test solutions.",
         "capability_request", "praxis", "investigate"),
        ("Something is wrong with this.", "clarify", None, None),
        ("Show me the current memory status.", "operational", None, None),
        ("Please make me a teleportation device.", "unsupported", None, None),
    )

    for text, disposition, capability, mode in cases:
        result = interpret(text)
        assert result.expression == text
        assert result.disposition == disposition
        assert result.capability == capability
        assert result.mode == mode


def test_http_boundary_preserves_expression() -> None:
    text = "I want to learn how to read a Linux process map."
    response = TestClient(app).post("/renaissance/doorway", json={"text": text})

    assert response.status_code == 200
    body = response.json()
    assert body["expression"] == text
    assert body["disposition"] == "capability_request"
    assert body["capability"] == "learn"
    assert body["mode"] == "answer"


def test_ambiguous_input_fails_closed() -> None:
    result = interpret("It broke again. Can you help?")
    assert result.disposition == "clarify"
    assert result.capability is None
    assert result.mode is None
