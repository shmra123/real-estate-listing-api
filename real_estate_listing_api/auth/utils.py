from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)


def generated_password_hash(password: str) -> str:
    """Generate a password hash using Werkzeug's security module.

    Args:
        password: The password string to be hashed

    Returns:
        str: Hashed password string
    """
    return generate_password_hash(password)


def verify_password(password_hash: str, password: str) -> bool:
    """Verify if a password matches its hash value

    Args:
        password_hash: Hashed password value to compare against
        password: The password to compare

    Returns:
         bool: True if the provided plain text password matches the
         hashed password;False otherwise
    """
    return check_password_hash(password_hash, password)
