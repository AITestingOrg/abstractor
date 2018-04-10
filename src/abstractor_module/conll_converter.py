'''

'''
import spacy
from spacy.gold import biluo_tags_from_offsets
import numpy as np
from .training_data import all_examples
import time


def convert():
    '''
    '''
    start = time.time()
    print('Loading spaCy...')
    nlp = spacy.load('en')
    end = time.time()
    print(end - start)
    print('Loading examples...')
    start = time.time()
    data = []
    examples = all_examples()
    i = 0
    last = 0
    count = len(examples)
    end = time.time()
    print(end - start)
    start = time.time()
    print('Converting', count, 'examples...')
    print('0% converted...')
    for example in examples:
        doc = nlp(example[0])
        data.append([[t.text for t in doc],
                     biluo_tags_from_offsets(doc, example[1]['entities'])])
        i += 1
        percent = int(i / count * 100)
        if percent != last:
          last = percent
          print(str(percent) + '% converted...')
    end = time.time()
    print(end - start)

    i = 0
    last = 0
    count = len(data)
    print('Saving Examples to CONLL...')
    print('0% written...')
    with open('models/train_data.conll', 'w') as f:
      for doc in [data]:
        for sentence, sent_entities in doc:
          f.write('-DOCSTART- -X- O O\n')
          i += 1
          percent = int(i / count * 100)
          if percent != last:
            last = percent
            print(percent, '% written...')
          for token, BIO_tag in zip(sentence, sent_entities):
            f.write('{} -X- _ {}\n'.format(token, BIO_tag))
          f.write('\n')
    print('Export to CONLL Format Completed.')


if __name__ == '__main__':
    convert()