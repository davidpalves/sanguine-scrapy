FROM python:3.6-slim-stretch as requirements

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Docker creates a network layer and a dns that maps IPs to service names.
ENV MONGODB_SERVER=mongo

ENV MONGODB_PORT=27017

ENV MONGODB_DB=doe_sangue

ENV MONGODB_COLLECTION=niveis

# Creates a non root user to execute application
USER scrapy

CMD scrapy crawl hemope