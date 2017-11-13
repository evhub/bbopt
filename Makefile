.PHONY: install
install: build
	pip install -e .[all]

.PHONY: install-2
install-2: build
	python2 -m pip install -e .[all]

.PHONY: setup
setup:
	pip install --upgrade setuptools pip pytest
	pip install --upgrade "coconut-develop[watch,cPyparsing]"

.PHONY: build
build:
	coconut setup.coco --no-tco --strict
	coconut "bbopt-source" bbopt --no-tco --strict --jobs sys
	-mkdir "./bbopt/examples/data"
	cp -rf "./bbopt-source/examples/data" "./bbopt/examples/"

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install --upgrade twine
	twine upload ./dist/*

.PHONY: test
test: install
	pytest --strict -s ./bbopt/tests

.PHONY: test-2
test-2: install-2
	python2 -m pytest --strict -s ./bbopt/tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.bbopt.json' -delete
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: wipe
wipe: clean
	rm -rf ./bbopt
	find . -name '*.py' -delete

.PHONY: watch
watch: install
	coconut "bbopt-source" bbopt --watch --no-tco --strict
