from real_estate_listing_api.config import settings
from real_estate_listing_api.loggers.console_logger import init_logger
from real_estate_listing_api.loggers.logging_interface import LoggingInterface
from real_estate_listing_api.state import get_state

LOG_LEVEL = settings.log_level


def get_logger() -> LoggingInterface:
    """Initialize the logger instance.

    Returns:
       LoggingInterface: An instance of the logging interface.
    """
    if not LOG_LEVEL:
        raise Exception("Cannot initialize logger without LOG_LEVEL!")
    state = get_state()
    if state.logger is None:
        state.logger = init_logger(LOG_LEVEL)
    return state.logger
