all: lint test

test:
	pytest

lint:
	flake8 --ignore E501
