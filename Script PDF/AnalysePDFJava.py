import sys,os,string
import time

#path of this file
chemin = os.path.dirname(__file__)

def intiFileCode() :
	#create the file or empty it
	with open(chemin+"/FichierTXT/CodeSuspect.txt", 'w+') as f:
	    f.truncate(0)
	f.close

def afficheFile() :
	#print the file from the word obj
	with open(chemin+"/FichierTXT/CodeSuspect.txt") as content:
		YouCanRead = False
		code = content.readlines()
		for l in code:
			if 'obj' in l:
				YouCanRead = True
			if YouCanRead :
				print(l[:-1])


def main() :
	FilePDF = 0
	with open(chemin+"/FichierTXT/FileWithOpenAction.txt") as text:
		datafile = text.readlines()
		#read all lines assumed to be paths
		for line in datafile:
			FilePDF = FilePDF + 1
			#remove last char and replace \ by / 
			li = '"'+line[:-1].replace("\\","/")+'"'
			print("-------------------------------------------------------------------------------------------\n"+li)
			#use the tool and save the results in CodeSuspect
			os.system('python "'+chemin+'/pdf-parser.py" --search openaction '+li+'  > "'+chemin+'/FichierTXT/CodeSuspect.txt"')

			print("\nPart OpenAction\n")
			afficheFile()
	return FilePDF

if __name__ == '__main__':

	intiFileCode()

	if os.path.getsize(chemin+"/FichierTXT/FileWithOpenAction.txt") != 0 :
		print("\nSTART RESEARCH\n")
		#start the timer
		start = time.time()

		FilePDF = main()

		#end the timer
		end = time.time()
		print("\nFINISH\n")

		#print some performance information
		print("Temps :" + str(int(end-start)) + " secondes")
		print("Nombre de fichier PDF: " + str(FilePDF))
	else : 
		print ("FileWithOpenAction Vide")
