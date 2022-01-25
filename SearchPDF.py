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
			os.system('python pdfid_modifie.py ' +f + ' > text3.txt')
			try:	
				document = PdfFileReader(open(fn, 'rb'))
				metadata = document.getDocumentInfo()
				author = metadata.author if metadata.author else u'Unknown'
				title = metadata.title if metadata.title else fn
				subject = metadata.subject if metadata.subject else "No Subject"
				print (author + "|" + title + "|" + subject)
				os.system('type text3.txt'  )
				#print(page)
					
			except Exception: 
				print("-------------------------------------------------------------------------------------------")