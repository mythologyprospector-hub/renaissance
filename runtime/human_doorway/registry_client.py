"""Small Registry heartbeat adapter for the Renaissance Human Doorway runtime.

Renaissance remains its own repository; this adapter speaks the existing
Organs Registry HTTP contract without importing Organs implementation code.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import urllib.error
import urllib.request

REGISTRY_URL = os.environ.get("ORGAN_REGISTRY_URL", "http://localhost:8000")
HEARTBEAT_INTERVAL = float(os.environ.get("ORGAN_HEARTBEAT_INTERVAL", "10"))

logger = logging.getLogger("renaissance.registry")


def register(name: str, base_url: str, version: str, capabilities: list[str]) -> None:
    payload = json.dumps({
        "name": name,
        "base_url": base_url,
        "version": version,
        "capabilities": capabilities,
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


def attach_to_registry(app, name: str, base_url: str, version: str,
                       capabilities: list[str]) -> None:
    heartbeat_task: asyncio.Task | None = None

    async def heartbeat_loop() -> None:
        while True:
            try:
                await asyncio.to_thread(
                    register, name, base_url, version, capabilities
                )
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
                logger.warning("registry check-in failed (will retry): %s", exc)
            await asyncio.sleep(HEARTBEAT_INTERVAL)

    @app.on_event("startup")
    async def on_startup() -> None:
        nonlocal heartbeat_task
        heartbeat_task = asyncio.create_task(heartbeat_loop())

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        if heartbeat_task is not None:
            heartbeat_task.cancel()
            try:
                await heartbeat_task
            except asyncio.CancelledError:
                pass
