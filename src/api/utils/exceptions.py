'''
Exceptions for API
'''
from flask import jsonify
from api.utils import logger

logger = logger.create_logger(__name__)

class InvalidUsage(Exception):
    '''
    Exception for Flask errors
    '''
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        '''
        '''
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        logger.error(message)

    def to_dict(self):
        '''
        '''
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
