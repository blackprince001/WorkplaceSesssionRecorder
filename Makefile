vscode-extensions:
	code ext install qwtel.sqlite-viewer

install:
	python -m pip install -r requirements.txt

dev-install: install
	python -m pip install -r dev-requirements.txt

