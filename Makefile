all: help

help:
	@echo 'Makefile *** Doe Sangue *** Makefile'

list:
	@scrapy list

list.crawl:
	@zsh run.sh

py.crawl:
	@python run.py