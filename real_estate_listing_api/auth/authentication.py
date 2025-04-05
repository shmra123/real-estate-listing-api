import jwt
from datetime import timedelta
from functools import wraps
from flask import request
from pymongo.database import Database

from core_api_lite.auth.auth_session import create_session
from core_api_lite.auth.utils import verify_password
from core_api_lite.config import settings
from core_api_lite.errors import (
    ResourceNotFound,
    AuthenticationError,
    PermissionError,
)
from core_api_lite.mapper.user import get_by_id
from core_api_lite.models.auth_session import AuthSession
from core_api_lite.models.user import User
from core_api_lite.services.utils import utcnow

ALGORITHM = "HS256"


def _get_session(current_user: User) -> AuthSession:
    """Get the current auth session

    Args:
        current_user: The User object

    Returns:
        AuthSession: The AuthSession object

    Raises:
        UserDisabledError: Raises if user is disabled
    """
    return create_session(current_user)


def _validate_secret_key(secret_key: str) -> str:
    """Validates the secret key used for token authentication.

    Args:
        secret_key: The secret key to be validated.

    Returns:
        str: The validated secret key

    """
    if secret_key == "":
        raise ResourceNotFound(
            "Secret key required for token authentication",
            status_code=404,
        )
    return secret_key


def authenticate_user(
    db: Database,
    user_id: str,
    password: str,
) -> User:
    """Authenticate user using credential

    Args:
        db: Database object
        user_id: The given user_id
        password: The given password

    Returns:
        User: The user object
    """

    user = get_by_id(user_id)
    if not user:
        raise ResourceNotFound(
            "User not found in the given user_id",
            status_code=404,
        )
    if not verify_password(str(user.password_hash), password):
        raise AuthenticationError(
            "Password is incorrect",
            status_code=401,
        )
    return user


def token_generator(payload: dict) -> str:
    """Generate a JWT token using the provided payload

    Args:
        payload: A dictionary containing token payload data

    Returns:
        str: The generated JWT token.
    """
    expire = utcnow() + timedelta(
        minutes=settings.auth_token_expire_minutes,
    )
    payload.update({"exp": expire})
    secret_key = _validate_secret_key(settings.secret_key)
    token = jwt.encode(
        payload,
        secret_key,
        algorithm=ALGORITHM,
    )
    return token


def token_required(func):
    """A decorator created for token validation"""

    @wraps(func)
    def token_required_decorator(*args, **kwargs):
        secret_key = _validate_secret_key(settings.secret_key)
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            raise AuthenticationError(
                "Authentication Token is missing!",
                status_code=401,
            )

        try:
            data = jwt.decode(
                token,
                secret_key,
                algorithms=[ALGORITHM],
            )
            current_user = get_by_id(data.get("user_id"))

            if current_user is None:
                raise AuthenticationError(
                    "Invalid Authentication token!",
                    status_code=401,
                )
            if current_user.disabled:
                raise PermissionError(
                    "Disabled user",
                    status_code=403,
                )
            auth_session = _get_session(current_user)
        except PermissionError:
            raise PermissionError("This user account is disabled")
        except Exception:
            raise AuthenticationError(
                "Invalid Authentication token",
                status_code=401,
            )
        return func(auth_session, *args, **kwargs)

    return token_required_decorator
