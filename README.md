# spaCy Service
[![Build Status](https://travis-ci.org/AITestingOrg/abstractor.svg?branch=master)](https://travis-ci.org/AITestingOrg/abstractor)

Small prototype, currently only scaffolding for converting values to abstractions.

## Features
* Convert values like 'Jack' to VALID_NAME
* Return random, concrete examples of abstractions
** Supports First Name, Last Name,
** Coming soon Full Name, Currency

## Running the API
```bash
pip install -r requirements.txt
pip install -U spacy
python -m spacy download en
python src/app.py
```

### Endpoints

#### Get Abstraction
```bash
POST /abstraction { label: 'First name', value: 'John' }
REPONSE { abstraction: 'VALID_FIRST_NAME', target: 'John' }
```

#### Get Concrete Example
```bash
GET /abstraction/concrete/example/:abstraction
REPONSE { abstraction: 'VALID_FIRST_NAME', example: 'John' }
```


#### Get Supported Abstractions
```bash
GET /abstraction/supported
RESPONSE ['VALID_FIRST_NAME', 'VALID_LAST_NAME']
```


## Running Demo
Run the prototype.
```bash
pip install -r requirements.txt
pip install -U spacy
python -m spacy download en
python src/console_app.py
``` 
Follow the instructions in the console. You don't need to train or import the model, there is a default one provided. Note, that the default model is very poor as it was trained on a tiny fraction of the data to avoid growing too large. To train a better model: choose `3` to train on the data, if you want to change the data then update the text files in models/data then choose `2` at the prompt to import the new data, finally choosing `3` to train on that data. Once done, you can start testing out concrete values using the `1` prompt.

## Tests
Run the tests.
```bash
pip install -r requirements.txt
python -m spacy download en
pytest
```
