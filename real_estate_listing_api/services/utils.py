from datetime import datetime, timezone


def utcnow() -> datetime:
    """Get the current datetime in UTC timezone.

    Returns:
        datetime: The current datetime in UTC timezone.
    """
    return datetime.now(timezone.utc)
