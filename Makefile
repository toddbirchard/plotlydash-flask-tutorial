SRCPATH := $(CURDIR)
ENTRYPOINT := $(shell find $(SRCPATH) -name '*.ini')
PROJECTNAME := $(shell basename "$PWD")

define HELP
Manage $(PROJECTNAME).

Usage:

make run             - Run uWSGI server for $(PROJECTNAME).
make restart         - Purge cache & reinstall modules.
make update          - Update npm production dependencies.
make clean           - Remove cached files.
endef
export HELP

.PHONY: run restart update help

all help:
	@echo "$$HELP"

.PHONY: run
run:
	nohup uwsgi $(ENTRYPOINT) &

.PHONY: restart
restart:
	pkill -9 -f $(shell uwsgi $(ENTRYPOINT))
	nohup uwsgi $(ENTRYPOINT) &

.PHONY: update
update:
	git pull origin master
	pkill -9 -f $(shell uwsgi $(ENTRYPOINT))
	poetry shell
	poetry update
	nohup uwsgi $(ENTRYPOINT) &

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
