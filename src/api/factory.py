'''
Flask App Factory
'''
from flask import Flask, jsonify
from api.controllers.abstraction_views import abstraction_bp
from api.utils import logger
from api.utils.exceptions import InvalidUsage

logger = logger.create_logger(__name__)


def create_app(config=None, environment=None):
    '''
    Flask App Factory method

    @config: Flask configuration dict
    @environment: Flask environment

    @returns: Flask app instance
    '''
    logger.info('Creating Flask app.')
    app = Flask(__name__)
    logger.info('Setting Flask configs.')
    app.config['ENVIRONMENT'] = environment
    app.config.update(config or {})
    logger.info('Registering Flask blueprints.')
    app.register_blueprint(abstraction_bp)

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app
