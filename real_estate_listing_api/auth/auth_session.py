from core_api_lite.models.auth_session import AuthSession
from core_api_lite.models.user import (
    RoleType,
    User,
)


def _check_user_privilege_is_admin(user: User) -> bool:
    """Check the user privilege

    Args:
        user: The user object

    Returns:
        bool: Returns user is admin or not
    """

    return RoleType.admin.value in user.roles


def create_session(user: User) -> AuthSession:
    """Create a session object using current user

    Args:
        user: User object

    Returns:
        AuthSession: The AuthSession object
    """
    is_admin = _check_user_privilege_is_admin(user)

    return AuthSession(
        user=user,
        is_admin=is_admin,
    )
