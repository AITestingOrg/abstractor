'''
Contains the first name models for training spacy entity
labels 'VALID_FIRST_NAME' and 'VALID_LAST_NAME'
'''
import numpy as np
from .model_utils import load_first_names, load_last_names


def first_name_train_data():
    '''
    Returns a spaCy model for training on first names
    '''
    first_names_df = load_first_names()
    return np.array([(row['input'].capitalize(), {'entities': [(0, len(row['input']), row['label'])]})
                     for index, row in first_names_df.iterrows()], dtype=object)


def last_name_train_data():
    '''
    Returns a spaCy model for training on last names
    '''
    last_names_df = load_last_names()
    return np.array([(row['input'].capitalize(), {'entities': [(0, len(row['input']), row['label'])]})
                     for index, row in last_names_df.iterrows()], dtype=object)
