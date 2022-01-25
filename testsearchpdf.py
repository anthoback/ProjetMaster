import warnings,sys,os,string
import re
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
with open("data.txt", 'r+') as f:
    f.truncate(0)
f.close
with open("text.txt", 'r+') as f:
    f.truncate(0)
f.close
for root, dir, files in os.walk(str(sys.argv[1])):
	for file in files:
		if ".pdf" in file:
			
			fn = root+"\\"+file
			f= '"'+fn+'"'
			os.system('python pdfid_modifie.py ' +f + ' > text.txt')

			#try:	
			#	document = PdfFileReader(open(fn, 'rb'))
			#	metadata = document.getDocumentInfo()
			#	author = metadata.author if metadata.author else u'Unknown'
			#	title = metadata.title if metadata.title else fn
			#	subject = metadata.subject if metadata.subject else "No Subject"
			with open('text.txt') as text:
				datafile = text.readlines()
			for line in datafile:
				if 'PDFiD' in line:
					chemin = line
				elif '/JavaScript' in line:
					NumberOfJava = re.findall(r'-?\d+\.?\d*', line)
					for s in NumberOfJava:
						if int(s) > 0 :
							print(fn)
							print(line)
							fichier = open("data.txt", "a")
							fichier.write(fn + "\n")
							fichier.close()
							
			#except Exception: 
			#	print()