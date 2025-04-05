from pymongo import MongoClient
from pymongo.database import Database

from typing import Any, Dict

from real_estate_listing_api.auth.utils import generated_password_hash
from real_estate_listing_api.logger import get_logger
from real_estate_listing_api.services.utils import utcnow

LOG = get_logger()


def _get_default_user() -> Dict[str, Any]:
    """Generates default user data

    Returns:
        Dict[str, Any]: A dictionary representing default user data
    """
    now = utcnow()
    user_data = {
        "_id": "admin@miniproject.com",
        "firstname": "Admin",
        "lastname": "Mini_project",
        "email": "admin@miniproject.com",
        "roles": ["admin"],
        "disabled": False,
        "password_hash": generated_password_hash("admin"),
        "revision": 1,
        "created": now,
        "modified": now,
    }
    return user_data


def _insert_default_user_data(db: Database):
    """Insert default user data in the users collection

    Args:
        db:Database object
    """
    user_data = _get_default_user()
    db.users.insert_one(user_data)


def init_db(
    db_url: str,
    connect_timeout: int = 5000,
    select_timeout: int = 5000,
    connect: bool = False,
) -> Database:
    """Database initialization

    Args:
        db_url: MongoDB connection URL
        connect_timeout: Connection timeout duration
        select_timeout: Server selection timeout duration
        connect: Connect on the first operation
    """
    LOG.info(f"Database URL:  {db_url}")
    db: Database = MongoClient(
        db_url,
        True,
        connectTimeoutMS=connect_timeout,
        serverSelectionTimeoutMS=select_timeout,
        tz_aware=True,
        connect=connect,
    ).get_default_database()
    if not db.users.find_one({"_id": "admin@miniproject.com"}):
        _insert_default_user_data(db)
        LOG.info("Inserted default user data")
    return db
