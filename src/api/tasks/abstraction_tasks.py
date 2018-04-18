'''
API tasks
'''
import numpy as np
from abstractor_module import abstractions, model_utils, abstractor
from api.utils import logger

LOGGER = logger.create_logger(__name__)


def get_concrete_example(abstraction):
    '''
    Returns an example given a valid abstraction

    @abstraction: string abstraction
    @returns: random concrete example of abstraction
    '''
    LOGGER.info('Get Concrete Example: %s', abstraction)
    data_frame = None
    if abstractions.ABSTRACTIONS['FIRST_NAME'].lower() == abstraction.lower():
        data_frame = model_utils.load_first_names()
    elif abstractions.ABSTRACTIONS['LAST_NAME'].lower() == abstraction.lower():
        data_frame = model_utils.load_last_names()
    elif abstractions.ABSTRACTIONS['EMAIL'].lower() == abstraction.lower():
        data_frame = model_utils.load_emails()

    if data_frame is None:
        LOGGER.info('No examples found for: %s', abstraction)
        return None
    word = data_frame.ix[np.random.randint(0, data_frame.shape[0]), 'word']
    LOGGER.info('Found example: %s', word)
    return word


def get_abstraction(concrete_example):
    '''
    Gets an abstraction for the given example

    @concrete_example: dict containing a value and label for the example
    @returns: String abstraction name
    '''
    LOGGER.info('Get Abstraction: %s', concrete_example)
    example_str = '{} {}'.format(concrete_example['label'], concrete_example['value'])
    LOGGER.info('Formatted example: %s', example_str)
    abstract = abstractor.Abstractor()
    return abstract.get_abstraction(example_str)


def get_abstractions():
    '''
    Returns all the supported abstractions for the system

    @returns: Supported abstractions
    '''
    LOGGER.info('Get Supported Abstractions.')
    return [value for _, value in abstractions.ABSTRACTIONS.items()]
