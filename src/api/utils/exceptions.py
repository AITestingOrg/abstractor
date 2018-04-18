'''
Exceptions for API
'''
from api.utils import logger

LOGGER = logger.create_logger(__name__)

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
        LOGGER.error(message)

    def to_dict(self):
        '''
        Returns the exception as a dictionary object.
        '''
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
