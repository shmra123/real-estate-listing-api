from pydantic import BaseModel, Extra

from real_estate_listing_api.models.user import User


class AuthSession(BaseModel):
    """AuthSession model for session

    Attributes:
        user (User): The user object
        is_admin (bool): A boolean field for check admin
    """

    user: User
    is_admin: bool = False

    class Config:
        extra = Extra.forbid
