project_name = mcm-bot

install: install-python install-hooks

install-python:
	poetry install

install-hooks: install-python
	poetry run pre-commit install --install-hooks --overwrite

lint-black:
	poetry run black .

lint-pyright:
	export PYRIGHT_PYTHON_GLOBAL_NODE=on; poetry run pyright .

lint-flake8:
	poetry run flake8 .

lint: lint-black lint-pyright lint-flake8

deep-clean-install:
	rm -f -d -r .venv/
	asdf uninstall poetry
	asdf uninstall python
	asdf plugin remove poetry
	asdf plugin remove python
	asdf plugin add python
	asdf install python
	asdf plugin add poetry
	asdf install poetry
	poetry install

pre-commit:
	poetry run pre-commit run --all-files
