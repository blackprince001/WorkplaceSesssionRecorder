SHELL := /bin/bash

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
	@echo rm -rf ${find . | grep __pycache__}