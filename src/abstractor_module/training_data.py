'''
Contains the example data for training spacy entity labels
'''
import numpy as np
from .model_utils import load_first_names, load_last_names, load_emails


def first_name_examples():
    '''
    Returns a spaCy model for training on first names
    '''
    first_names_df = load_first_names()
    return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                     for index, row in first_names_df.iterrows()], dtype=object)


def last_name_examples():
    '''
    Returns a spaCy model for training on last names
    '''
    last_names_df = load_last_names()
    return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                     for index, row in last_names_df.iterrows()], dtype=object)

def email_examples():
    '''
    Returns a spaCy model for training emails
    '''
    emails_df = load_emails()
    return np.array([(row['input'], {'entities': [(len(row['input']) - len(row['word']), len(row['input']), row['label'])]})
                     for index, row in emails_df.iterrows()], dtype=object)


def all_examples():
    '''
    Returns a spaCy model for all examples
    '''
    return np.concatenate((first_name_examples(), last_name_examples(), email_examples()))
