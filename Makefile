clean: clean-build clean-pyc clean-test

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr pybuild/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -f output.xml
	rm -f report.html

test:
	pytest

test-all:
	tox

coverage: # check code coverage quickly with the default Python
	coverage run --source cumulusci -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

