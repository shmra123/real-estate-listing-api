from typing import Optional

from pymongo.database import Database

from real_estate_listing_api.loggers.logging_interface import LoggingInterface


class AppState:
    """Represents the singleton instance of  the class

    Attributes:
        _instance: The AppState instance
        mongo_db: The mongo database
        logger: The logging interface
    """

    _instance: Optional["AppState"] = None
    mongo_db: Optional[Database] = None
    logger: Optional[LoggingInterface] = None
