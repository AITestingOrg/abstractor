# Abstractor Prototype
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
Follow the instructions in the console.

## Tests
Run the tests.
```bash
pip install -r requirements.txt
python -m spacy download en
pytest
```
