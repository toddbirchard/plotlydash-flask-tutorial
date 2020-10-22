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

.PHONY: run restart deploy update clean help


requirements: .requirements.txt


.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)


all help:
	@echo "$$HELP"


.PHONY: run
run:
	$(shell . .venv/bin/activate && python3 wsgi.py)


.PHONY: deploy
deploy:
	$(shell . ./deploy.sh)


.PHONY: update
update:
	poetry shell && poetry update
	pip freeze > requirements.txt
	exit


.PHONY: format
format: requirements
	$(shell . .venv/bin/activate)
	$(shell isort -rc ./)
	$(shell black ./)


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'poetry.lock' -delete
	find . -name 'Pipefile.lock' -delete