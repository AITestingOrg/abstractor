'''
Contains the first name models for training spacy entity
labels 'VALID_FIRST_NAME' and 'VALID_LAST_NAME'
'''
from .model_utils import load_first_names, load_last_names


def first_name_train_data():
    '''
    Returns a spaCy model for training on first names
    '''
    first_names_df = load_first_names()
    return [(row[0], [(0, len(row[0]), 'VALID_FIRST_NAME')])
            for index, row in first_names_df.iterrows()]


def last_name_train_data():
    '''
    Returns a spaCy model for training on last names
    '''
    last_names_df = load_last_names()
    return [(row[0], [(0, len(row[0]), 'VALID_LAST_NAME')])
            for index, row in last_names_df.iterrows()]
