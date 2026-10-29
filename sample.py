"""
Ghost in the Machine - Sample Module
"""

from datetime import datetime


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Ghost in the Machine."


def get_status() -> dict:
    """Return a sample status payload."""
    return {
        "service": "ghost-in-the-machine",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


if __name__ == "__main__":
    print(greet("Developer"))
    print(get_status())