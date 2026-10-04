"""Live Renaissance -> Organs Registry -> Communications integration test.

The workflow starts real Registry, Critic, and Communications processes.
This test deliberately uses Renaissance's production publisher code and
then reads the event back from the real Communications bus.
"""

from __future__ import annotations

import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))

import attention_choice_publisher as publisher


def _get_json(url: str):
    with urllib.request.urlopen(url, timeout=5) as response:
        import json
        return json.loads(response.read().decode("utf-8"))


def test_attention_choice_reaches_real_bus() -> None:
    choice = publisher.AttentionChoice(
        id="live-ac-001",
        pressure_ref="live-gap-1",
        target_ref="live-investigation-1",
        supporting_refs=("live-finding-1",),
        selection_basis="live integration test selected the represented investigation",
        alternative_refs=("live-investigation-0",),
        mode="suggest",
    )

    result = publisher.publish_attention_choice(
        choice,
        registry_url=os.environ.get("ORGAN_REGISTRY_URL", "http://localhost:8000"),
    )

    assert result["topic"] == "renaissance.attention"
    assert result["event_type"] == "attention_choice"
    assert result["publisher"] == "renaissance"
    assert result["payload"] == choice.to_payload()

    topic = urllib.parse.quote("renaissance.attention", safe="")
    events = _get_json(
        f"http://localhost:8002/bus/topics/{topic}/events?since_id=0&limit=50"
    )

    matches = [
        event for event in events
        if event["event_type"] == "attention_choice"
        and event["publisher"] == "renaissance"
        and event["payload"]["id"] == choice.id
    ]
    assert len(matches) == 1
    assert matches[0]["payload"] == choice.to_payload()
