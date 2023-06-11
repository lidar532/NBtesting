all:
	echo "Building all"
	jupyter nbconvert --to python *.ipynb 
	mv *.py test

File_Selector:
	jupyter nbconvert --to python File_Selector.ipynb
	mv File_Selector.py test
main:
	jupyter nbconvert --to python main.ipynb
	chmod +x main.py

testlib:
	jupyter nbconvert --to python testlib.ipynb
	mv testlib.py test

clean:
	echo "All done" 
