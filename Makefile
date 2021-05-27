.PHONY: install
install: build
	pip install -Ue .[dev]

.PHONY: install-2
install-2: build
	python2 -m pip install -Ue .[dev]

.PHONY: force-install
force-install: force-build
	pip install -Ue .[dev]

.PHONY: setup
setup:
	pip install -U setuptools pip pytest coconut-develop[watch]

.PHONY: build
build:
	coconut setup.coco --no-tco --strict
	coconut "bbopt-source" bbopt --no-tco --strict --jobs sys
	-mkdir "./bbopt/examples"
	cp -rf "./bbopt-source/examples" "./bbopt/"

.PHONY: force-build
force-build:
	coconut setup.coco --no-tco --strict --force
	coconut "bbopt-source" bbopt --no-tco --strict --jobs sys --force
	-mkdir "./bbopt/examples"
	cp -rf "./bbopt-source/examples" "./bbopt/"

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install -U --ignore-installed twine
	twine upload dist/*

.PHONY: test
test: clean install
	pytest --strict --fulltrace -s ./bbopt/tests

.PHONY: test-keras
test-keras: clean install
	-rm ./bbopt/examples/keras_example.bbopt.pickle
	python ./bbopt/examples/keras_example.py

.PHONY: test-2
test-2: clean install-2
	python2 -m pytest --strict --fulltrace -s ./bbopt/tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	-find . -name '*.pyc' -delete
	-C:/GnuWin32/bin/find.exe . -name '*.pyc' -delete
	-find . -name '__pycache__' -delete
	-C:/GnuWin32/bin/find.exe . -name '__pycache__' -delete
	-find . -name '*.bbopt.pickle' -delete
	-C:/GnuWin32/bin/find.exe . -name '*.bbopt.pickle' -delete
	-find . -name '*.bbopt.json' -delete
	-C:/GnuWin32/bin/find.exe . -name '*.bbopt.json' -delete

.PHONY: wipe
wipe: clean
	rm -rf ./bbopt ./setup.py

.PHONY: watch
watch: install
	coconut "bbopt-source" bbopt --watch --no-tco --strict
