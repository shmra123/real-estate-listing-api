"""Standard error classes for error handling and exceptions"""


class BaseError(Exception):
    """Base Error class for handling custom exceptions"""

    status_code = 400
    message = "An error occurred"

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        self.message = message or self.message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        error_resp = dict(self.payload or ())
        error_resp["message"] = self.message
        return error_resp


class AuthenticationError(BaseError):
    """Error class for authentication failure"""

    status_code = 401
    message = "You are not authenticated"


class ResourceNotFound(BaseError):
    """Error class for resource not found"""

    status_code = 404
    message = "Could not find resource"


class PermissionError(BaseError):
    """Error class for permission error"""

    status_code = 403
    message = "Insufficient permissions for user"


class ValidationError(BaseError):
    """Error class for validation errors"""

    status_code = 422
    message = "Validation failed for the provided input"


class DuplicateKeyError(BaseError):
    """Error class for conflict errors"""

    status_code = 409
    message = "Conflict occurred, resource already exists"
