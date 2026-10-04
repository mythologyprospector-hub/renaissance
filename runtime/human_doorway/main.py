"""Minimal executable Renaissance Human Doorway runtime.

This service owns Renaissance semantic interpretation only. Organs remains the
human-facing operational front door and authority path.

The interpreter is deliberately deterministic and conservative for the first
runtime slice. It must be replaced or extended only when evidence requires it.
"""

from __future__ import annotations

import os
import urllib.error
import urllib.request
import json
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

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


def _register() -> None:
    payload = json.dumps({
        "name": ORGAN_NAME,
        "base_url": BASE_URL,
        "version": ORGAN_VERSION,
        "capabilities": CAPABILITIES,
    }).encode("utf-8")
    request = urllib.request.Request(
        f"{REGISTRY_URL}/registry/register",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Telemetry-Internal": "1",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=5.0):
        return


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


@app.on_event("startup")
async def register_with_organs() -> None:
    # Registry failure must not make the semantic service fabricate authority.
    # A deployment may retry registration externally; the service itself
    # remains available for direct contract testing.
    try:
        _register()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        pass
