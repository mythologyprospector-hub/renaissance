"""Minimal executable Renaissance Human Doorway runtime.

This service owns Renaissance semantic interpretation only. Organs remains the
human-facing operational front door and authority path.

The interpreter is deliberately deterministic and conservative for the first
runtime slice. It must be replaced or extended only when evidence requires it.
"""

from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "shared"))
from organ_client import attach_to_registry  # noqa: E402

ORGAN_NAME = "renaissance"
ORGAN_VERSION = "0.1.0"
REGISTRY_URL = os.environ.get("ORGAN_REGISTRY_URL", "http://localhost:8000")
BASE_URL = os.environ.get("RENAISSANCE_BASE_URL", "http://localhost:8010")
CAPABILITIES = ["human_doorway"]


class DoorwayRequest(BaseModel):
    text: str = Field(min_length=1)


class DoorwayResponse(BaseModel):
    expression: str
    disposition: str
    capability: str | None = None
    mode: str | None = None


app = FastAPI(title="renaissance:human-doorway", version=ORGAN_VERSION)


def _response(text: str, disposition: str, capability: str | None = None,
              mode: str | None = None) -> DoorwayResponse:
    return DoorwayResponse(
        expression=text,
        disposition=disposition,
        capability=capability,
        mode=mode,
    )


def interpret(text: str) -> DoorwayResponse:
    """Conservative first-pass Renaissance semantic interpretation.

    This is a boundary implementation, not a general-purpose language model.
    Unknown or ambiguous expressions fail closed.
    """
    normalized = text.strip().lower()

    if not normalized:
        return _response(text, "clarify")

    # Existing Organs operational vocabulary must remain outside Renaissance.
    operational_markers = (
        "memory status",
        "current memory",
        "introspection",
        "reflect",
        "sandbox",
        "orchestrator",
    )
    if any(marker in normalized for marker in operational_markers):
        return _response(text, "operational")

    # Explicit unsupported request used by the contract corpus.
    if "teleport" in normalized:
        return _response(text, "unsupported")

    # Clear learning requests.
    learning_markers = (
        "i want to learn",
        "i'd like to learn",
        "i'd kind of like to understand how to read",
        "can you teach me",
        "teach me",
    )
    if any(marker in normalized for marker in learning_markers):
        return _response(text, "capability_request", "learn", "answer")

    # Investigative inquiry: require a recognizable question/contrast signal.
    inquiry_markers = (
        "two competing explanations",
        "two explanations",
        "which of my two explanations",
        "how could we distinguish",
        "how can we tell",
        "could these two",
        "couple ideas",
    )
    if any(marker in normalized for marker in inquiry_markers):
        return _response(text, "capability_request", "understand", "investigate")

    # Problem-solving is deliberately narrower than generic "help me".
    problem_markers = (
        "real problem",
        "constraints",
        "safe ways to test solutions",
        "safe way to tackle it",
    )
    if any(marker in normalized for marker in problem_markers):
        return _response(text, "capability_request", "praxis", "investigate")

    # Explicitly ambiguous expressions remain clarification rather than guesses.
    ambiguous_markers = (
        "something is wrong",
        "it broke again",
        "doesn't make sense",
        "keeps doing something weird",
        "help me figure out",
    )
    if any(marker in normalized for marker in ambiguous_markers):
        return _response(text, "clarify")

    # Corrections and ordinary observations remain conversation.
    conversation_markers = (
        "i need to think about it",
        "i wasn't actually asking you",
        "let me back up and explain",
        "that's interesting",
        "that's a strange result",
        "no, that's not what i meant",
    )
    if any(marker in normalized for marker in conversation_markers):
        return _response(text, "conversation")

    return _response(text, "clarify")



@app.get("/health")
def health() -> dict[str, Any]:
    return {"organ": ORGAN_NAME, "status": "ok"}


@app.get("/info")
def info() -> dict[str, Any]:
    return {
        "organ": ORGAN_NAME,
        "version": ORGAN_VERSION,
        "organ_api_version": "1.0",
        "description": "Renaissance semantic Human Doorway boundary.",
        "capabilities": CAPABILITIES,
    }


@app.post("/renaissance/doorway", response_model=DoorwayResponse)
def doorway(req: DoorwayRequest) -> DoorwayResponse:
    return interpret(req.text)


attach_to_registry(app, name=ORGAN_NAME, base_url=BASE_URL, version=ORGAN_VERSION, capabilities=CAPABILITIES)
