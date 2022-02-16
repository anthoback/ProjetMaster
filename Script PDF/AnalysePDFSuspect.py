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
	with open(chemin+"/FichierTXT/FileSuspect.txt") as text:
		datafile = text.readlines()
		#read all lines assumed to be paths
		for line in datafile:
			FilePDF = FilePDF + 1
			#remove last char and replace \ by / 
			li = '"'+line[:-1].replace("\\","/")+'"'
			print("-------------------------------------------------------------------------------------------\n"+li)
			 #use the tool and save the results in CodeSuspect
			os.system('python3 "'+chemin+'/pdf-parser.py" --search openaction '+li+'  > "'+chemin+'/FichierTXT/CodeSuspect.txt"')
			
			print("\nPartie OpenAction\n")
			afficheFile()
			
			 #use the tool and save the results in CodeSuspect
			os.system('python3 "'+chemin+'/pdf-parser.py" --search javascript '+li+'  > "'+chemin+'/FichierTXT/CodeSuspect.txt"')
			
			print("\nPartie JavaScript\n")
			afficheFile()
			
	return FilePDF
			
if __name__ == '__main__':

	intiFileCode()

	if os.path.getsize(chemin+"/FichierTXT/FileSuspect.txt") != 0 :
		print("\nDEBUT RECHERHCES\n")
		#start the timer
		start = time.time()

		FilePDF = main()

		#end the timer
		end = time.time()
		print("\nFIN\n")

		#print some performance information
		print("Temps :" + str(int(end-start)) + " secondes")
		print("Nombre de fichier PDF: " + str(FilePDF))

	else : 
		print ("FileSuspect Vide")
