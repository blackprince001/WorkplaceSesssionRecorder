SHELL := /bin/bash
FILES = $(find . | grep __pycache__)

vscode-extensions:
	code ext install qwtel.sqlite-viewer

install:
	python -m pip install -r requirements.txt

dev-install: install
	python -m pip install -r dev-requirements.txt

test-checkbook: 
	pytest ./tests/api/test_checkbook_table_api.py

test-worker:
	pytest ./tests/api/test_worker_table_api.py

test: test-checkbook test-worker

pytest-clean:
	rm -rf .pytest_cache

clean: pytest-clean
	FILES=${find . | grep __pycache__}
	rm -rf ${FILES}

help:
	@echo make test		- to test the api methods
	@echo make test-worker		- to test the worker Table in the database
	@echo make test-checkbook		- to test the checkbook Table in database
	@echo make pytest-clean		- to clean pytest_cache FILES
