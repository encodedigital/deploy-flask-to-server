FROM python:3.8.5-alpine

WORKDIR /web

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8081 web:app
