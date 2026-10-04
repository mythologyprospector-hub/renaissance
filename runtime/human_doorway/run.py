"""Local launcher for the Renaissance Human Doorway runtime.

This is a development/runtime harness, not a declaration of final
Renaissance service topology.
"""

from __future__ import annotations

import os

import uvicorn


def main() -> None:
    uvicorn.run(
        "main:app",
        host=os.getenv("RENAISSANCE_HOST", "127.0.0.1"),
        port=int(os.getenv("RENAISSANCE_PORT", "8010")),
        reload=False,
    )


if __name__ == "__main__":
    main()
