all:
	nbdev_export
	nbdev_docs

install:
	pip install ../NBtesting

Folder_Selector:
	jupyter nbconvert --to python Folder_Selector.ipynb
	mv Folder_Selector.py test
main:
	jupyter nbconvert --to python main.ipynb
	chmod +x main.py

testlib:
	jupyter nbconvert --to python testlib.ipynb
	mv testlib.py test

clean:
	echo "All done" 
