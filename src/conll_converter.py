'''

'''
import spacy
from spacy.gold import biluo_tags_from_offsets
import numpy as np
from abstractor_module.training_data import all_examples


def convert():
    '''
    '''
    print('Loading spaCy...')
    nlp = spacy.load('en')
    print('Converting Examples...')
    data = []
    for example in all_examples():
        doc = nlp(example[0])
        data.append([[t.text for t in doc],
                     biluo_tags_from_offsets(doc, example[1]['entities'])])
    print(data)
    return
    DATA = [
      [
        [['Who', 'is', 'Shaka', 'Khan', '?'], ['O', 'O', 'I-PER', 'I-PER', 'O']]
      ],
      [
        [['I', 'like', 'London', 'and', 'Berlin', '.'], ['O', 'O', 'I-LOC', 'O', 'I-LOC', 'O']]
      ]
    ]
    print('Saving Examples...')
    with open('train_data.conll', 'w') as f:
      for doc in DATA:
        f.write('-DOCSTART- -X- O O\n')
        for sentence, sent_entities in doc:
          for token, BIO_tag in zip(sentence, sent_entities):
            f.write('{} -X- _ {}\n'.format(token, BIO_tag))
    f.write('\n')


if __name__ == '__main__':
    convert()