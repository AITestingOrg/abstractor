'''
Misc tools and utilities for moving, exporting, and loading the data
used in the models
'''
from os import path
import numpy as np
import pandas
from .abstractions import ABSTRACTIONS
from .labels import email_labels, first_name_labels, last_name_labels


class Importer:
    '''
    Importer and extractor for model data.
    '''

    def __init__(self):
        '''
        Constructor for importer
        '''
        self.shared_nouns = None
        self.shared_urls = None
        self.dirname = path.dirname(__file__)

    def __get_random_element(self, labels):
        '''
        Returns a random element from a list of labels
        '''
        return labels[np.random.randint(0, len(labels) - 1)]

    def __get_from_file(self, rel_path, delimeter=' '):
        '''
        Gets data from data file

        @rel_path: relative path of file
        @delimeter: file delimeter, defaults to ' '
        '''
        content = None
        file_path = path.join(self.dirname, rel_path)
        with open(file_path) as file:
            content = file.readlines()
        return np.array([x.split(delimeter)[0].replace('\n', '') for x in content if x != '\n'])

    def __save_to_file(self, data, name):
        '''
        Saves a dictionary object as a Pandas DataFrame

        @data: dictionary object
        @name: name of file <name>.pickle
        '''
        data_frame = pandas.DataFrame(data)
        data_frame.to_pickle(path=path.join(self.dirname, './models/{:s}.pickle'.format(name)))


    def convert_and_export_names(self):
        '''
        Converts the Census data to a Pandas DataFrame and stores it as a pickle.
        The Census data comes in the format 'Name Percent-Frequency
        Percent-Cumlative-Frequency Rank'
        '''
        paths = [['./models/data/census-dist-all-first.txt', ABSTRACTIONS['FIRST_NAME']],
                 ['./models/data/census-dist-all-last.txt', ABSTRACTIONS['LAST_NAME']]]
        for file_path in paths:
            positive_examples = self.__get_from_file(file_path[0])
            np.random.shuffle(positive_examples)
            non_proper_nouns = self.__get_from_file('./models/data/most-used-nouns.txt')
            rand_numbers = self.__get_from_file('./models/data/random-numbers.txt')
            urls = self.__get_from_file('./models/data/urls.txt')
            np.random.shuffle(non_proper_nouns)
            np.random.shuffle(rand_numbers)
            np.random.shuffle(urls)
            all_examples = np.concatenate([positive_examples[:5000], non_proper_nouns[:1000], rand_numbers[:500], urls[:500]])
            if file_path[1] == ABSTRACTIONS['FIRST_NAME']:
                labels = first_name_labels
            else:
                labels = last_name_labels
            all_examples = np.transpose([np.tile(labels, len(all_examples)), np.repeat(all_examples, len(labels))])
            abstraction = np.empty(len(all_examples), dtype=object)
            abstraction[:5000 * len(labels)] = file_path[1]
            abstraction[5000 * len(labels):] = '!{}'.format(file_path[1])
            data = {'input': np.core.defchararray.add(all_examples[:,0], all_examples[:,1]),
                       'word': all_examples[:,1],
                       'label': abstraction}
            self.__save_to_file(data, file_path[1])


    def convert_and_export_emails(self):
        '''
        Converts the random e-mail address stored in random-email-address
        to a Pandas DataFrame.
        '''
        positive_examples = self.__get_from_file('./models/data/random-email-addresses.txt')
        non_proper_nouns = self.__get_from_file('./models/data/most-used-nouns.txt')
        rand_numbers = self.__get_from_file('./models/data/random-numbers.txt')
        invalid_emails = self.__get_from_file('./models/data/invalid-email-addresses.txt')
        urls = self.__get_from_file('./models/data/urls.txt')
        np.random.shuffle(non_proper_nouns)
        np.random.shuffle(rand_numbers)
        np.random.shuffle(urls)
        np.random.shuffle(invalid_emails)
        all_examples = np.concatenate([positive_examples, non_proper_nouns[:1000], rand_numbers[:500], urls[:500], invalid_emails])
        all_examples = np.transpose([np.tile(email_labels, len(all_examples)), np.repeat(all_examples, len(email_labels))])
        abstraction = np.empty(len(all_examples), dtype=object)
        abstraction[:len(positive_examples) * len(email_labels)] = ABSTRACTIONS['EMAIL']
        abstraction[len(positive_examples) * len(email_labels):] = '!{}'.format(ABSTRACTIONS['EMAIL'])
        data = {'input': np.core.defchararray.add(all_examples[:, 0], all_examples[:, 1]),
                   'word': all_examples[:, 1],
                   'label': abstraction}
        self.__save_to_file(data, ABSTRACTIONS['EMAIL'])


    def import_all(self):
        '''
        Imports all data from sources.
        '''
        self.convert_and_export_names()
        self.convert_and_export_emails()


    def load_first_names(self, limit=None):
        '''
        Loads the first name DataFrame from a pickle
        '''
        dirname = path.dirname(__file__)
        return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['FIRST_NAME'])))


    def load_last_names(self, limit=None):
        '''
        Loads the last name DataFrame from a pickle
        '''
        dirname = path.dirname(__file__)
        return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['LAST_NAME'])))

    def load_emails(self, limit=None):
        '''
        Loads the email DataFrame from a pickle
        '''
        dirname = path.dirname(__file__)
        return pandas.read_pickle(path.join(dirname, './models/{:s}.pickle'.format(ABSTRACTIONS['EMAIL'])))
