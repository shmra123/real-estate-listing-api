from flask import Blueprint

from flask_pydantic import validate  # type: ignore

#from core_api_lite.handler import login as login_handler
from real_estate_listing_api.models.login import LoginInput, Token


bp = Blueprint("login", __name__)


@bp.route("/login", methods=["POST"])
@validate()
def login(body: LoginInput) -> Token:
    """Router to return auth token

    Args:
        body:The login input

    Returns:
        Token: Returns the token object
    """
    return "success"
