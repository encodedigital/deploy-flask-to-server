FROM python:3.8.5-alpine

WORKDIR /api

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8080 run:app
