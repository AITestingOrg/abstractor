'''
Abstractor: Processes values and returns abstractions based on the input.
'''
import spacy
from .abstractions import ABSTRACTIONS


NLP = spacy.load('en')


def get_abstraction(str_input):
    '''
    Given a string will return an abstraction of it

    params:
    str_input: type string

    return:
    string abstraction
    '''

    if not isinstance(str_input, str):
        raise Exception('Only strings but found: {:s}'.format(str_input))

    if len(str_input.split(' ')) > 1:
        return get_fragment_abstraction(str_input)
    return get_value_abstraction(str_input)


def get_value_abstraction(value):
    '''
    Given a single value, will return it's abstraction if
    known, else it will return None

    params:
    value: type string

    return:
    string abstraction
    '''

    doc = NLP(value)
    for entity in doc.ents:
        return ABSTRACTIONS[entity.label_]
    return None


def get_fragment_abstraction(frag):
    '''
    Given a sentence fragment will return the first abstraction found
    todo: make this return an abstraction of the fragment

    params:
    frag: type string

    return:
    string abstraction
    '''

    doc = NLP(frag)
    for entity in doc.ents:
        if entity.label_:
            return ABSTRACTIONS[entity.label_]
    return None
