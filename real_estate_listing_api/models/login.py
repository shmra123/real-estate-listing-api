from pydantic import BaseModel


class LoginInput(BaseModel):
    """LoginInput model for credential

    Attributes:
        user_name (str): The user name/id
        password (str): The password
    """

    user_name: str
    password: str


class Token(BaseModel):
    """Token model for auth token

    Attributes:
        access_token (str): The access token
        token_type (str): The type of the token
    """

    access_token: str
    token_type: str
