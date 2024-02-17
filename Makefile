# Makefile

# List of directories and files to format and ruff
TARGETS = *.py althea/

run:
	poetry run reflex run

format:
	poetry run isort $(TARGETS)
	poetry run black $(TARGETS)

ruff:
	poetry run ruff $(TARGETS)

pylint:
	poetry run pylint -j 0 $(TARGETS)

# Test code using pytest
test:
	poetry run pytest

# Setup project for development
setup:
	poetry run pre-commit install --config .config/.pre-commit.yaml
	poetry run pre-commit autoupdate --config .config/.pre-commit.yaml

# Display help message by default
.DEFAULT_GOAL := help
help:
	@echo "Available commands:"
	@echo "  make format      - Format code using isort and black"
	@echo "  make ruff        - Lint code using ruff"
	@echo "  make pylint      - Lint code using pylint"
	@echo "  make test        - Run tests using pytest"
	@echo "  make setup       - Setup project for development"

# Declare the targets as phony
.PHONY: format ruff pylint test setup help
