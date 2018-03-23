'''
Abstractor: Processes values and returns abstractions based on the input.
'''
from .train import get_trained_model


class Abstractor:
    '''
    Class responsible for replacing concrete values with abstractions.
    '''

    def __init__(self):
        self.nlp = get_trained_model()

    def get_abstraction(self, str_input):
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
            return self.get_fragment_abstraction(str_input)
        return self.get_value_abstraction(str_input)

    def get_value_abstraction(self, value):
        '''
        Given a single value, will return it's abstraction if
        known, else it will return None

        params:
        value: type string

        return:
        string abstraction
        '''

        doc = self.nlp(value)
        for entity in doc.ents:
            return entity.label_
        return None

    def get_fragment_abstraction(self, frag):
        '''
        Given a sentence fragment will return the first abstraction found
        todo: make this return an abstraction of the fragment

        params:
        frag: type string

        return:
        string abstraction
        '''

        doc = self.nlp(frag)
        for entity in doc.ents:
            if entity.label_:
                return entity.label_
        return None
