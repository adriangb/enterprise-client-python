PYTHON:=python3

.PHONY: all
all: test pkg

.PHONY: pkg
pkg:
	@echo "==> $@"
	$(PYTHON) -m build .

.PHONY: lint
lint:
	@echo "==> $@"
	pip install pre-commit
	pre-commit run --all-files

.PHONY: test
test: lint
	@echo "==> $@"
	PYTHONPATH=src/ $(PYTHON) -m unittest discover -s src/pomerium -v
