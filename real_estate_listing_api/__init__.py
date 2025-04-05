from flask import Flask, jsonify

from real_estate_listing_api.errors import (
    AuthenticationError,
    ResourceNotFound,
    DuplicateKeyError,
    PermissionError,
    ValidationError,
)
from real_estate_listing_api.database import get_db
from real_estate_listing_api.logger import get_logger
from real_estate_listing_api.router import (
    login
)


LOG = get_logger()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    get_db()

    app.register_blueprint(login.bp)
    @app.errorhandler(AuthenticationError)
    def handle_authentication_error(error: AuthenticationError):
        """Error handler for AuthenticationError

        Args:
            error: The AuthenticationError raised
        """
        LOG.debug("Authentication Failure (exception)")
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(ResourceNotFound)
    def handle_resource_not_found(error: ResourceNotFound):
        """Error handler for ResourceNotFound

        Args:
            error: The ResourceNotFound error raised
        """
        LOG.debug("A ResourceNotFound error occurred")
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(DuplicateKeyError)
    def handle_duplicate_error(error: DuplicateKeyError):
        """Error handler for DuplicateKeyError

        Args:
            error: The DuplicateKeyError error raised
        """
        LOG.debug("A DuplicateKeyError error occurred")
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(PermissionError)
    def handle_permission_error(error: PermissionError):
        """Error handler for PermissionError

        Args:
            error: The PermissionError error raised
        """
        LOG.debug("A PermissionError error occurred")
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        """Error handler for ValidationError

        Args:
            error: The ValidationError error raised
        """
        LOG.debug("A ValidationError error occurred")
        return jsonify(error.to_dict()), error.status_code

    return app
