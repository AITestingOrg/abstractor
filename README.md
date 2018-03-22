# Abstractor Prototype
[![Build Status](https://travis-ci.org/AITestingOrg/abstractor.svg?branch=master)](https://travis-ci.org/AITestingOrg/abstractor)

Small prototype, currently only scaffolding for converting values to abstractions.

## Features
* Convert values like 'Jack' to VALID_NAME

## Running Demo
Run the prototype.
```bash
pip install -r requirements.txt
pip install -U spacy
python -m spacy download en
python src/app.py
``` 
Follow the instructions in the console. You must train the model first. To do this choose `2` at the prompt to import the examples then `3` to train on them. Once done, you can start testing out concrete values using the `1` prompt

## Tests
Run the tests.
```bash
pip install -r requirements.txt
python -m spacy download en
pytest
```
