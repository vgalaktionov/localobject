.PHONY: install
install: build
	rm -rf /Applications/localobject.app
	mv dist/localobject.app /Applications

build:
	python setup.py py2app

.PHONY: clean
clean:
	rm -rf build dist localobject.egg-info
