'''
Responsible for training the Spacy model
'''
from os import path
import spacy
import numpy as np
from .training_data import TrainingData
from .abstractions import ABSTRACTIONS

NLP = spacy.blank('en')


def get_trained_model():
    '''
    Returns the trained model from disk
    '''
    dirname = path.dirname(__file__)
    model_path = path.join(dirname, './model')
    return spacy.load(model_path)


def train_model(model_name='default', iters=15, drop_rate=0.35, save=False):
    '''
    Trains spaCy against the formatted data given by model_utils
    params:
    iters: number of training iterations
    save: if true it will save the model to disk
    '''
    print('Loading training data...')
    tmp = TrainingData().all_examples()
    print('Seperate training data...')
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
    ner.add_label(ABSTRACTIONS['EMAIL'])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in NLP.pipe_names if pipe != 'ner']
    with NLP.disable_pipes(*other_pipes):  # only train NER
        print('Begin training on {:d} iterations'.format(iters))
        optimizer = NLP.begin_training()
        for itn in range(iters):
            print('Training iteration {:d} starting...'.format(itn + 1))
            np.random.shuffle(train_data)
            losses = {}
            [NLP.update([text], [annotations], sgd=optimizer, losses=losses, drop=drop_rate) for text, annotations in train_data]
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
    Todo: Create cases with more context (labels from inputs, etc...) also, resolve ambiguity in the model
    with popular first names that are also last names.
    Some things to try
    * Use the frequency to inject a higher number of similar cases
    * Get more context on the input
    * Trim the last name data to be about the size of first name
    '''
    print('Testing the trained model with {:d} test instances...'.format(len(test_data)))
    dirname = path.dirname(__file__)
    file_path = path.join(dirname, './model')
    print('Loading model from', file_path)
    nlp = spacy.load(file_path)
    errors = []
    instances_tested = 0
    for text, annotations in test_data:
        doc = nlp(text)
        has_entity = False
        for ent in doc.ents:
            has_entity = True
            instances_tested += 1
            if '!' not in annotations['entities'][0][2] and annotations['entities'][0][2] != ent.label_ or '!' in annotations['entities'][0][2] and ent.label_ is None:
                print('Error in prediction {:s} should have been {:s} but found {:s}'.format(text, annotations['entities'][0][2], ent.label_))
                errors.append((text, annotations, ent.label_))
        if not has_entity and '!' not in annotations['entities'][0][2]:
            print('Error in prediction {:s} should have been {:s} but found {:s}'.format(text, annotations['entities'][0][2], 'None'))
            errors.append((text, annotations, None))

    print('{0:f} instances contained entities...'.format(instances_tested))
    print('Error rate of {}% for {} test instances.'.format((len(errors) * 100) / len(test_data), len(test_data)))
