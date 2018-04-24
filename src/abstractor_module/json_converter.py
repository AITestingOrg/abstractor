'''
Converts from NER format to spaCy JSON format, could be used in the future for training via CLI with mini-batches.
'''
import json
import spacy
from spacy.gold import biluo_tags_from_offsets
import numpy as np
from training_data import TrainingData
import time


def convert():
    '''
    Gathers the data and formats it using BILUO, then wrhites it in spaCy JSON format to a file.
    '''
    start = time.time()
    print('Loading spaCy...')
    nlp = spacy.load('en')
    end = time.time()
    print(end - start)
    print('Loading examples...')
    start = time.time()
    data = []
    trainingData = TrainingData()
    examples = trainingData.all_examples()
    counter = 0
    last = 0
    count = len(examples)
    end = time.time()
    print(end - start)
    start = time.time()
    print('Converting', count, 'examples...')
    print('0% converted...')
    sentences = []
    for t in examples:
        doc = nlp(t[0])
        tags = biluo_tags_from_offsets(doc, t[1]['entities'])
        ner_info = list(zip(doc, tags))
        tokens = []
        for n, i in enumerate(ner_info):
            token = {"head" : 0,
            "dep" : "",
            "tag" : "",
            "orth" : i[0].string,
            "ner" : i[1],
            "id" : n}
            tokens.append(token)
        sentences.append(tokens)
        counter += 1
        percent = int(counter / count * 100)
        if percent != last:
          last = percent
          print(str(percent) + '% converted...')
    end = time.time()
    print(end - start)

    print('Saving Examples to spaCy JSON...')
    print('0% written...')
    with open('train_data.json', 'w+') as f:
        json.dump(sentences, f)
    print('Export to spaCy JSON Format Completed.')


if __name__ == '__main__':
    convert()