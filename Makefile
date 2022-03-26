#!make
include .env
export $(shell sed 's/=.*//' .env)

all: help

help:
	@echo 'Makefile *** Doe Sangue *** Makefile'

list:
	@scrapy list

list.crawl:
	@zsh run.sh

py.crawl:
	@python run.py

runserver:
	@flask run

update.data:
	@cd api/ && flask data update

docker.build:
	@docker build --no-cache -t  service/sanguine:1.0.0 -f ./docker/local/sanguine/Dockerfile ./

docker.run:
	@docker-compose --profile local up

docker.shell:
	@docker exec -ti sanguine /bin/bash

docker.mongo:
	@docker exec -it mongodb mongo