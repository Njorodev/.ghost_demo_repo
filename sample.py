"""
Ghost in the Machine
Advanced Sample Module

Demonstrates:
- Logging
- Environment configuration
- Dataclasses
- Type hints
- Error handling
- JSON serialization
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, asdict
from datetime import datetime, UTC
from enum import Enum
from typing import Any


# -------------------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("ghost")


# -------------------------------------------------------------------
# Models
# -------------------------------------------------------------------

class ServiceStatus(Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"


@dataclass(slots=True)
class GhostService:
    name: str
    version: str
    status: ServiceStatus
    started_at: str

    def to_json(self) -> str:
        """Serialize service data to JSON."""
        payload = asdict(self)
        payload["status"] = self.status.value
        return json.dumps(payload, indent=4)


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

class Config:
    APP_NAME = os.getenv("GHOST_APP_NAME", "Ghost In The Machine")
    APP_VERSION = os.getenv("GHOST_APP_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"


# -------------------------------------------------------------------
# Service Layer
# -------------------------------------------------------------------

class GhostManager:
    """Manages the lifecycle of the ghost service."""

    def __init__(self) -> None:
        self.service = GhostService(
            name=Config.APP_NAME,
            version=Config.APP_VERSION,
            status=ServiceStatus.STOPPED,
            started_at="",
        )

    def start(self) -> None:
        logger.info("Starting service...")

        self.service.status = ServiceStatus.RUNNING
        self.service.started_at = datetime.now(UTC).isoformat()

        logger.info(
            "Service '%s' started successfully.",
            self.service.name,
        )

    def stop(self) -> None:
        logger.info("Stopping service...")

        self.service.status = ServiceStatus.STOPPED

        logger.info(
            "Service '%s' stopped.",
            self.service.name,
        )

    def health_check(self) -> dict[str, Any]:
        return {
            "healthy": self.service.status == ServiceStatus.RUNNING,
            "service": self.service.name,
            "version": self.service.version,
            "status": self.service.status.value,
            "timestamp": datetime.now(UTC).isoformat(),
        }


# -------------------------------------------------------------------
# Utility Functions
# -------------------------------------------------------------------

def print_banner() -> None:
    print(
        """
====================================================
             GHOST IN THE MACHINE
====================================================
"""
    )


def pretty_print(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=4))


# -------------------------------------------------------------------
# Main App
# -------------------------------------------------------------------

def main() -> None:
    try:
        print_banner()

        manager = GhostManager()

        manager.start()

        print("\nSERVICE INFORMATION")
        print(manager.service.to_json())

        print("\nHEALTH CHECK")
        pretty_print(manager.health_check())

        manager.stop()

        logger.info("Application shutdown complete.")

    except Exception as exc:
        logger.exception("Fatal error occurred: %s", exc)
        raise


if __name__ == "__main__":
    main()