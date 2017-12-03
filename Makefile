all: lint test

test:
	pytest

lint:
	flake8
