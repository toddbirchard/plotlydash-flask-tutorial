SRCPATH := $(CURDIR)
PROJECTNAME := $(shell basename $(CURDIR))

define HELP
Manage $(PROJECTNAME). Usage:

make run        - Run $(PROJECTNAME).
make deploy     - Install requirements and run app for the first time.
make update     - Update pip dependencies via Python Poetry.
make format     - Format code with Python's `Black` library.
make clean      - Remove cached files and lock files.
endef
export HELP

.PHONY: run deploy update format clean help


requirements: .requirements.txt
env: .venv/bin/activate


.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)


all help:
	@echo "$$HELP"


.PHONY: run
run: env
	$(shell . .venv/bin/activate && flask run)


.PHONY: deploy
deploy:
	$(shell . ./deploy.sh)


.PHONY: update
update: env
	.venv/bin/python3 -m pip install -U pip
	poetry update
	poetry export -f requirements.txt --output requirements.txt --without-hashes


.PHONY: format
format: env
	$(shell . .venv/bin/activate && isort -rc ./)
	$(shell . .venv/bin/activate && black ./)


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'poetry.lock' -delete
	find . -name 'Pipefile.lock' -delete