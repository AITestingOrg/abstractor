'''
Custom logger
'''
import logging
from os import environ

def create_logger(name):
    '''
    Custom logger factory, creates a logger that supports time and date stamps

    @name: Name of Logger to build or get
    @returns: Logger
    '''
    logger = logging.getLogger(name)
    ch = logging.StreamHandler()
    ch.setLevel(environ.get('LOG_LEVEL', logging.INFO))
    ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(ch)
    return logger