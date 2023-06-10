all:
	echo "Building all"
	jupyter nbconvert --to python *.ipynb 
	mv *.py test

main:
	jupyter nbconvert --to python main.ipynb
	chmod +x main.py

testlib:
	jupyter nbconvert --to python testlib.ipynb

clean:
	echo "All done" 
