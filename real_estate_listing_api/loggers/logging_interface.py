from abc import ABC, abstractmethod
from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


LOG_LEVELS = {
    "DEBUG": LogLevel.DEBUG,
    "INFO": LogLevel.INFO,
    "WARNING": LogLevel.WARNING,
    "ERROR": LogLevel.ERROR,
    "CRITICAL": LogLevel.CRITICAL,
}


class LogLevels(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __init__(self, value: str) -> None:
        self.log_levels = LOG_LEVELS.get(value, 0)


class LoggingInterface(ABC):
    """Logging Interface"""

    @abstractmethod
    def set_log_level(self, log_level: LogLevel) -> None:
        """Set the log level for logging

        Args:
            log_level: Log level enum
        """
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        """Debug log level definition

        Args:
            message: Log message
        """
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        """Info log level definition

        Args:
            message: Log message
        """
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        """Warning log level definition

        Args:
            message: Log message
        """

    @abstractmethod
    def error(self, message: str) -> None:
        """Error log level definition

        Args:
            message: Log message
        """
        pass

    @abstractmethod
    def critical(self, message: str) -> None:
        """Critical log level definition

        Args:
            message: Log message
        """
        pass
