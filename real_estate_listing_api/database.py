from pymongo.database import Database

from real_estate_listing_api.config import settings
from real_estate_listing_api.db.mongo import init_db
from real_estate_listing_api.state import get_state

mongo_db_uri = settings.mongo_db_uri


def get_db() -> Database:
    """Get the DB object

    Returns:
        Database: Database object
    """
    if not mongo_db_uri:
        raise Exception("Cannot initialize database without DB_URI!")
    state = get_state()
    if state.mongo_db is None:
        state.mongo_db = init_db(mongo_db_uri)
    return state.mongo_db
