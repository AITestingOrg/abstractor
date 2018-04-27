'''
Contains the example data for training spacy entity labels
'''
import numpy as np
from .model_utils import Importer


class TrainingData:
    '''
    Training data converted to NER format.
    '''
    def __init__(self):
        '''
        Consturctor for setting up training data.
        '''
        self.importer = Importer()

    def first_name_examples(self):
        '''
        Returns a spaCy model for training on first names
        '''
        first_names_df = self.importer.load_first_names()
        return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                         for index, row in first_names_df.iterrows()], dtype=object)


    def last_name_examples(self):
        '''
        Returns a spaCy model for training on last names
        '''
        last_names_df = self.importer.load_last_names()
        return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                         for index, row in last_names_df.iterrows()], dtype=object)

    def email_examples(self):
        '''
        Returns a spaCy model for training emails
        '''
        emails_df = self.importer.load_emails()
        return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                         for index, row in emails_df.iterrows()], dtype=object)

    def all_examples(self):
        '''
        Returns a spaCy model for all examples
        '''
        return np.concatenate((self.first_name_examples(), self.last_name_examples(), self.email_examples()))
