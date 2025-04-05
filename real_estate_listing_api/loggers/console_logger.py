import logging
from enum import Enum

from real_estate_listing_api.loggers.logging_interface import (
    LogLevels,
    LoggingInterface,
)


class ConsoleLogger(LoggingInterface):
    """LoggingInterface implementations to Log in the console"""

    def __init__(self) -> None:
        self.logging = logging
        self.logger = self.logging.getLogger()
        self.logger_format = "%(asctime)s - %(levelname)s - %(message)s"
        self.logging.basicConfig(
            format=self.logger_format,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def set_log_level(self, log_level: Enum) -> None:
        self.logger.setLevel(log_level.name)

    def debug(self, message: str) -> None:
        self.logger.debug(msg=message)

    def info(self, message: str) -> None:
        self.logger.info(msg=message)

    def warning(self, message: str) -> None:
        self.logger.warning(msg=message)

    def error(self, message: str) -> None:
        self.logger.error(msg=message)

    def critical(self, message: str) -> None:
        self.logger.critical(msg=message)


def init_logger(log_level: str) -> LoggingInterface:
    """Console logger initiated

    Args:
        log_level: Log level for set logger

    Returns:
        LoggingInterface: Returns LoggingInterface
    """
    LOG = ConsoleLogger()
    LOG.set_log_level(LogLevels(log_level))
    return LOG
