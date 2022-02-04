import sys,os,string
import time

def intiFileCode() :
		#create the file or empty it
	with open("FichierTXT/CodeSuspect.txt", 'w+') as f:
	    f.truncate(0)
	f.close

def afficheFile() :
	#open the file and write the lines that interest us
	with open("FichierTXT/CodeSuspect.txt") as content:
		YouCanRead = 0
		code = content.readlines()
		for l in code:
			print(l[:-1])		

def main() :
	FileMS = 0
	with open("FichierTXT/FileSuspect.txt") as text:
		datafile = text.readlines()
		#read all lines assumed to be paths
		for line in datafile:
			ListeM = []
			FileMS = FileMS + 1
			#replace \ by / 
			l = line.split()
			f = '"'+l[0].replace("\\","/")+'"'
			print("-------------------------------------------------------------------------------------------\n"+f)
			 #use the tool and save the results in CodeSuspect
			for m in range (1,len(l)) :
				print("-------------------------------------------------------------------------------------------\n"+ 'Fichier concerné :' + f + '\nFlux concerné :' + l[m] + "\n\n")
				os.system('python3 oledump.py -s '+l[m] +' -v ' + f + ' > FichierTXT/CodeSuspect.txt' )
				afficheFile()	

	return FileMS


if __name__ == '__main__':

   
    print("\nSTART RESEARCH\n")
    #start the timer
    start = time.time()
    
    intiFileCode()
    MS = main()
    
    #end the timer
    end = time.time()
    print("\nFINISH\n")
    
    #print some performance information
    print("Temps :" + str(int(end-start)) + " secondes")
    print("Nombre de fichier MS: " + str(MS))
   
