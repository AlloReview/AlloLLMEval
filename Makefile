.PHONY: install format lint clean build

install:
	pip install -e .[dev]

format:
	black .

lint:
	flake8 .
	black --check .

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	python setup.py sdist bdist_wheel 