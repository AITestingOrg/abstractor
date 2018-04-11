'''
Misc tools and utilities for moving, exporting, and loading the data
used in the models
'''
from os import path
import numpy as np
import pandas
from .abstractions import ABSTRACTIONS
from .labels import email_labels, first_name_labels, last_name_labels

def get_random_element(labels):
    '''
    Returns a random element from a list of labels
    '''
    return labels[np.random.randint(0, len(labels) - 1)]


def convert_and_export_names():
    '''
    Converts the Census data to a Pandas DataFrame and stores it as a pickle.
    The Census data comes in the format 'Name Percent-Frequency
    Percent-Cumlative-Frequency Rank'
    '''
    dirname = path.dirname(__file__)
    paths = [[path.join(dirname, './models/data/census-dist-all-first.txt'), ABSTRACTIONS['FIRST_NAME']],
             [path.join(dirname, './models/data/census-dist-all-last.txt'), ABSTRACTIONS['LAST_NAME']]]
    for file_path in paths:
        with open(file_path[0]) as file:
            content = file.readlines()
        content = np.array([np.array([y for y in x.split(' ') if y != '']) for x in content if x != '\n'])
        abstraction = np.empty(len(content), dtype=object)
        abstraction[:] = file_path[1]
        if file_path[1] == ABSTRACTIONS['FIRST_NAME']:
            labels = np.array([get_random_element(first_name_labels) for x in range(len(content))])
        else:
            labels = np.array([get_random_element(last_name_labels) for x in range(len(content))])
        print(content[:,0])
        df_dict = {'input': np.core.defchararray.add(labels, np.char.capitalize(content[:, 0])),
                   'word': content[:, 0],
                   'frequency': content[:, 1],
                   'label': abstraction}
        data_frame = pandas.DataFrame(df_dict)
        data_frame.to_pickle(path=path.join(dirname, './models/{:s}.pickle'.format(file_path[1])))


def convert_and_export_emails():
    '''
    Converts the random e-mail address stored in random-email-address
    to a Pandas DataFrame.
    '''
    dirname = path.dirname(__file__)
    file_path = path.join(dirname, './models/data/random-email-addresses.txt')
    with open(file_path) as file:
        content = file.readlines()
    content = np.array([x.replace('\n', '') for x in content])
    abstraction = np.empty(len(content), dtype=object)
    abstraction[:] = ABSTRACTIONS['EMAIL']
    labels = np.array([get_random_element(email_labels) for x in range(len(content))])
    df_dict = {'input': np.core.defchararray.add(labels, np.char.capitalize(content)),
               'word': content,
               'label': abstraction}
    data_frame = pandas.DataFrame(df_dict)
    data_frame.to_pickle(path=path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['EMAIL'])))


def import_all():
    '''
    Imports all data from sources.
    '''
    convert_and_export_names()
    convert_and_export_emails()


def load_first_names():
    '''
    Loads the first name DataFrame from a pickle
    '''
    dirname = path.dirname(__file__)
    return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['FIRST_NAME'])))


def load_last_names():
    '''
    Loads the last name DataFrame from a pickle
    '''
    dirname = path.dirname(__file__)
    return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['LAST_NAME'])))

def load_emails():
    '''
    Loads the email DataFrame from a pickle
    '''
    dirname = path.dirname(__file__)
    return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['EMAIL'])))
