'''
Responsible for training the Spacy model
'''
from os import path
import spacy
import numpy as np
from .person_names import first_name_train_data, last_name_train_data
from .abstractions import ABSTRACTIONS

NLP = spacy.blank('en')


def get_trained_model():
    '''
    Returns the trained model from disk
    '''
    dirname = path.dirname(__file__)
    model_path = path.join(dirname, './model')
    return spacy.load(model_path)


def train_model(model_name='default', iters=15, save=False):
    '''
    Trains spaCy against the formatted data given by model_utils
    params:
    iters: number of training iterations
    save: if true it will save the model to disk
    '''
    print('Loading training data...')
    first_name_data = first_name_train_data()
    last_name_data = last_name_train_data()
    print('Seperate training data...')
    tmp = np.concatenate((first_name_data, last_name_data))
    np.random.shuffle(tmp)
    test_index = int(len(tmp) * 0.6)
    train_data = tmp[:test_index]
    test_data = tmp[test_index:]

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in NLP.pipe_names:
        ner = NLP.create_pipe('ner')
        NLP.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = NLP.get_pipe('ner')

    ner.add_label(ABSTRACTIONS['FIRST_NAME'])
    ner.add_label(ABSTRACTIONS['LAST_NAME'])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in NLP.pipe_names if pipe != 'ner']
    with NLP.disable_pipes(*other_pipes):  # only train NER
        print('Begin training on {:d} iterations'.format(iters))
        optimizer = NLP.begin_training()
        for itn in range(iters):
            print('Training iteration {:d} starting...'.format(itn + 1))
            np.random.shuffle(train_data)
            losses = {}
            [NLP.update([text], [annotations], sgd=optimizer, losses=losses, drop=0.35) for text, annotations in train_data]
            print(losses)
            print('Training iteration {:d} complete...'.format(itn + 1))

    if save:
        dirname = path.dirname(__file__)
        model_path = path.join(dirname, './model')
        print('Saving model to disk...')
        NLP.meta['name'] = model_name
        NLP.to_disk(model_path)

        test_model(test_data)


def test_model(test_data):
    '''
    Tests the trained model on test data
    todo: add negative cases as this data set doesn't have any yet.
    '''
    print('Testing the trained model with {0:f} test instances...'.format(len(test_data)))
    dirname = path.dirname(__file__)
    file_path = path.join(dirname, './model')
    print('Loading model from', file_path)
    nlp = spacy.load(file_path)
    errors = []
    instances_tested = 0
    for text, annotations in test_data:
        doc = nlp(text)
        print(doc.ents)
        for ent in doc.ents:
            instances_tested += 1
            if annotations.entities[1][2] != ent.label_:
                print('Error in prediction {:s} should have been {:s} but found {:s}'.format(text, annotations.entities[1][2], ent.label_))
                errors.append((text, annotations, ent.label_))
    print('{0:f} instances tested...'.format(instances_tested))
    print('Error rate {0:f}% of {0:f} test instances.'.format(int(len(errors) * 100 / instances_tested), len(test_data)))
