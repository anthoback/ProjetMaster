#!user/bin/env/python
import warnings,sys,os,string
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
for root, dir, files in os.walk(str(sys.argv[1])):
	for file in files:
		if ".pdf" in file:
			
			fn = root+"\\"+file
			f= '"'+fn+'"'
			print("-------------------------------------------------------------------------------------------")
			print(fn)
			
			try:	
				print(os.system('python PDFID/pdf-parser.py --search javascript ' +f))
				#print(page)
				
			except Exception: 
				print("-------------------------------------------------------------------------------------------")
