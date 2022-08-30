from os import listdir
from PyPDF2 import PdfFileMerger
print(""" 
		Put all the files you want to merge in one folder
 """)
path = input("Enter the path to the file with the PDFs: ")
PDFs = []
merger = PdfFileMerger()
for file in listdir(path):
	if file.endswith(".pdf"):
		PDFs.append(file)
print("Merging files....")
for pdf in PDFs:
	merger.append(path + '\\' + pdf)
merger.write(f"{path}\merged.pdf")
merger.close()
