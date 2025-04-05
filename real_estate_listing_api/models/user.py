from datetime import datetime
from enum import Enum
from typing import (
    List,
    Optional,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class RoleType(
    str,
    Enum,
):
    user = "user"
    admin = "admin"


class User(BaseModel):
    """User model

    Attributes:
        id (str): The id of the user.
        firstname (str): The first name of the user.
        lastname (str): The last name of the user.
        email (str): Email address of the user.
        roles (List[RoleType]): List of roles assigned to the user.
        disabled (bool): Flag indicating if the user account is disabled.
        revision (int): The revision number of the user.
        password_hash (str): Hashed password for user authentication.
        created (datetime): The time the project was created
        modified (datetime): The last modified time of the project
        deleted (Optional[datetime]): The deleted time
    """

    id: str = Field(..., alias="_id")
    firstname: str
    lastname: str
    email: str
    roles: List[RoleType]
    disabled: bool
    revision: int
    password_hash: Optional[str] = None
    created: datetime
    modified: datetime
    deleted: Optional[datetime] = None

    class Config:
        model_config = ConfigDict(extra="forbid")
        populate_by_name = True


class UserInput(BaseModel):
    """UserInput model

    Attributes:
        id (str): The id of the user.
        firstname (str): The first name of the user.
        lastname (str): The last name of the user.
        email (str): Email address of the user.
        roles (List[RoleType]): List of roles assigned to the user.
        disabled (bool): Flag indicating if the user account is disabled.
        password (Optional[str]): The password of the user
    """

    id: str = Field(..., alias="_id")
    firstname: str
    lastname: str
    email: str
    roles: List[RoleType]
    disabled: Optional[bool] = None
    password: Optional[str] = None

    class Config:
        model_config = ConfigDict(extra="forbid")
        populate_by_name = True


class UserModifyInput(BaseModel):
    """UserModifyInput model

    Attributes:
        firstname (Optional[str]): The firstname of the user.
        lastname (Optional[str]): The lastname of the user.
        password(Optional[str]): The password of the user.
        disabled(Optional[bool]): The Flag for user account disabled status
        modified (Optional[datatime]): The last modified time of the project
    """

    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None
    disabled: Optional[bool] = None
    modified: Optional[datetime] = None

    class Config:
        model_config = ConfigDict(extra="forbid")
        populate_by_name = True


class UserPatch(BaseModel):
    """UserPatch model

    Attributes:
        firstname (Optional[str]): The first name of the user
        lastname (Optional[str]): The last name of the user
        roles (Optional[List[RoleType]]): Assigned roles
        disabled (Optional[bool]): Flag for user account disabled status
        modified (Optional[datatime]): The last modified time of the project
        deleted (Optional[datetime]): The deleted time
    """

    firstname: Optional[str] = None
    lastname: Optional[str] = None
    roles: Optional[List[RoleType]] = []
    password_hash: Optional[str] = None
    disabled: Optional[bool] = None
    modified: Optional[datetime] = None
    deleted: Optional[datetime] = None

    class Config:
        model_config = ConfigDict(extra="forbid")
        populate_by_name = True
