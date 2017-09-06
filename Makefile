.PHONY: install
install: build
	pip install --upgrade -e .

.PHONY: build
build:
	coconut setup.coco --no-tco --strict
	coconut bbgun-source bbgun --no-tco --strict --jobs sys
	coconut tests-source tests --no-tco --strict --jobs sys

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install --upgrade twine
	twine upload dist/*

.PHONY: setup
setup:
	pip install --upgrade setuptools pip
	pip install --upgrade "coconut-develop[watch,cPyparsing]"

.PHONY: test
test: install
	pytest --strict -s tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: wipe
wipe: clean
	find . -name '*.py' -delete
	rm -rf ./bbgun

.PHONY: watch
watch: install
	coconut bbgun-source bbgun --watch --no-tco --strict
