'''
'''
import spacy
import numpy as np
from .person_names import load_first_names, load_last_names

NLP = spacy.blank('en')


def train_models(iters=100, save=False):
    '''
    '''
    print('Loading training data...')
    first_name_data = load_first_names()
    last_name_data = load_last_names()
    print('Seperate training data...')


    optimizer = NLP.begin_training()
    for itn in range(iters):
        np.random.shuffle(train_data)
        [nlp.update([text], [annotations], sgd=optimizer) for text, annotations in train_data]
            
    if save:
        NLP.to_disk('./model')