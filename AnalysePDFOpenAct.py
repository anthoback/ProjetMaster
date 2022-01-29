import warnings,sys,os,string
import re
import time

def intiFileCode() :
	
	#create the file or empty it
	with open("CodeSuspect.txt", 'w+') as f:
	    f.truncate(0)
	f.close



def main() :
	FilePDF = 0
	with open("FileWithOpenAction.txt") as text:
		datafile = text.readlines()
		#read all lines assumed to be paths
		for line in datafile:
			FilePDF = FilePDF + 1
			#remove last char and replace \ by / 
			li = '"'+line[:-1].replace("\\","/")+'"'
			print("-------------------------------------------------------------------------------------------\n"+li)
			 #use the tool and save the results in the file
			os.system('python pdf-parser_modifie.py --search openaction '+li+'  > CodeSuspect.txt')
			#open the file and write the lines that interest us
			with open("CodeSuspect.txt") as content:
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
	return FilePDF

if __name__ == '__main__':

	intiFileCode()
	print("\n\n\nSTART RESEARCH\n\n\n")
	start = time.time()

	FilePDF = main()

	end = time.time()
	print("\n\n\nFINISH\n\n\n")
	print("Temps :" + str(int(end-start)) + " secondes")
	print("Nombre de fichier PDF: " + str(FilePDF))