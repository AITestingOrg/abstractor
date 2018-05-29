FROM python:3

COPY . .

RUN pip install -r requirements.txt
RUN pip install -U spacy

EXPOSE 5000

CMD ["python", "./src/app.py"]
