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
	nbdev_export --path testlib.ipynb

clean:
	echo "Not setup yet.  All done" 
