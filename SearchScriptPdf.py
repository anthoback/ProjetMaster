import warnings,sys,os,string
import re
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
#create the file or empty it
with open("FileWithJava.txt", 'w+') as f:
    f.truncate(0)
f.close
with open("FileContent.txt", 'w+') as f:
    f.truncate(0)
f.close
#Browse folders and files
print("\n\n\nSTART RESEARCH\n\n\n")
for root, dir, files in os.walk(str(sys.argv[1])):
	for file in files:  
        #search .pdf
		if ".pdf" in file:
			#save the path
			fn = root+"\\"+file
			print("-------------------------------------------------------------------------------------------\n"+fn)
			f= '"'+fn+'"'
			#use the tool and save the results in the file
			os.system('python pdfid_modifie.py ' +f + ' > FileContent.txt')
			#open the file and save all the lines
			with open('FileContent.txt') as text:
				datafile = text.readlines()
			#search the lien with"JavaScript
			for line in datafile:
				if '/JavaScript' in line:
                    #search the number of script Java
					NumberOfScript = re.findall(r'-?\d+\.?\d*', line)
					for s in NumberOfScript:
						#if more than 0 so we save the path in a file
						if int(s) > 0 :
							print("\nJavaScript Found\n")
							fichier = open("FileWithJava.txt", "a")
							fichier.write(fn + "\n")
							fichier.close()
print("\n\n\nFINISH\n\n\n")
