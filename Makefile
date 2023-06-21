all:
	nbdev_export
	nbdev_docs

install:
	pip install ../NBtesting
    
bump:
	nbdev_bump_version

widgets:
	nbdev_export
	jupyter nbconvert --to python 20_widgets.ipynb

testlib:
	jupyter nbconvert --to python testlib.ipynb
	mv testlib.py test

clean:
	echo "Not setup yet.  All done" 
