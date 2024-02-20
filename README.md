Folder Structure should be in below format:


1. Create input folder and add all pdf files in input folder
input/pdf1.pdf
input/pdf2.pdf
input/pdf3.pdf
input/pdf4.pdf
input/pdf5.pdf


2. Create output folder
output/


3. Create src folder and add below files
main.py
test_main.py (contains test cases)


Installation Steps:


1. Install dependencies

a. pip install camelot-py

b. pip install camelot-py[cv]

c. pip install PyPDF2

d. pip install --upgrade PyPDF2==2.12.1

e. Download and install: https://ghostscript.com/releases/gsdnld.html

f. pip install PyCryptodome

g. pip install coverage

h. pip install reportlab

f. Create virtual environment: py -m venv vnev

g. Activate virtual environment: cd venv/Scripts -> ./activate -> cd ../..


Run Program:

py main.py

User Input 1. Provide the file name in format: pdf1.pdf

User Input 2. Provide password of the encrypted pdf file or else hit enter


Run Unit Test:

python -m coverage run -m unittest test_main.py

coverage report 
