.PHONY: install
install: build
	pip install -Ue .[dev]

.PHONY: install-py2
install-py2: build
	python2 -m pip install -Ue .[dev]

.PHONY: force-install
force-install: force-build
	pip install -Ue .[dev]

.PHONY: force-install-py2
force-install-py2: force-build
	python2 -m pip install -Ue .[dev]

.PHONY: setup
setup:
	pip install -U setuptools pip pytest coconut-develop[watch]

.PHONY: build
build: clean
	coconut setup.coco --and bbopt-source bbopt --no-tco --strict --jobs sys
	-mkdir "./bbopt/examples"
	cp -rf "./bbopt-source/examples" "./bbopt/"

.PHONY: force-build
force-build: clean
	coconut setup.coco --and bbopt-source bbopt --force --no-tco --strict --jobs sys
	-mkdir "./bbopt/examples"
	cp -rf "./bbopt-source/examples" "./bbopt/"

.PHONY: package
package:
	python3 setup.py sdist bdist_wheel

.PHONY: upload
upload: install package
	pip3 install -U --ignore-installed twine
	twine upload dist/*

.PHONY: test
test: install
	pytest --strict-markers --full-trace -s ./bbopt/tests

.PHONY: force-test
force-test: force-install
	pytest --strict-markers --full-trace -s ./bbopt/tests

.PHONY: force-test-py2
force-test-py2: force-install-py2
	python2 -m pytest --strict-markers --full-trace -s ./bbopt/tests

.PHONY: test-keras
test-keras: install
	-rm ./bbopt/examples/keras_example.bbopt.pickle
	python ./bbopt/examples/keras_example.py

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
	coconut bbopt-source bbopt --watch --no-tco --strict --jobs sys
