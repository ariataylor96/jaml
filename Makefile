dist: clean
	python setup.py sdist bdist_wheel

upload: dist
	twine upload dist/*

clean:
	rm -f dist/*
