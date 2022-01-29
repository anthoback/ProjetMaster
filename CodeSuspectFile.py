import warnings,sys,os,string
import re
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
#create the file or empty it
with open("CodeJava.txt", 'w+') as f:
    f.truncate(0)
f.close

#Browse folders and files
print("\n\n\nSTART RESEARCH\n\n\n")
with open(str(sys.argv[1])) as text:
	datafile = text.readlines()
	#read all lines assumed to be paths
	for line in datafile:
		#remove last char and replace \ by / 
		li = '"'+line[:-1].replace("\\","/")+'"'
		print("-------------------------------------------------------------------------------------------\n"+li)
		 #use the tool and save the results in the file
		os.system('python pdf-parser_modifie.py --search openaction '+li+'  > CodeJava.txt')
		#open the file and write the lines that interest us
		with open("codeJava.txt") as content:
			YouCanRead = 0
			code = content.readlines()
			print("\nPart OpenAction")
			for l in code:
				if '<' in l:
					YouCanRead = YouCanRead + 1
				if YouCanRead > 0:
					print(l[:-1])
				if '>' in l:
					YouCanRead = YouCanRead - 1

		os.system('python pdf-parser_modifie.py --search javascript '+li+'  > CodeJava.txt')
		#open the file and write the lines that interest us
		with open("codeJava.txt") as content:
			YouCanRead = 0
			code = content.readlines()
			print("\nPart JavaScript")
			for l in code:
				if '<' in l:
					YouCanRead = YouCanRead + 1
				if YouCanRead > 0:
					print(l[:-1])
				if '>' in l:
					YouCanRead = YouCanRead - 1
print("\n\n\nFINISH\n\n\n")
