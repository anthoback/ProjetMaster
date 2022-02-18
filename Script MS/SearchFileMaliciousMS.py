import sys,os,string

#path of this file
chemin = os.path.dirname(__file__)

def affiche(path) :
	with open(path) as text:
		datafile = text.readlines()
		#read all lines assumed to be paths
		for line in datafile:
			#remove last char and replace \ by / 
			li = '"'+line[:-1].replace("\\","/")+'"'
			print(li)

if __name__ == '__main__':

	exit = 1
	while exit :
		print("\nChercher des fichiers malicieux OLE \n 1 : Chercher des fichiers malicieux \n 2 : Analyser les fichiers Suspects \n 3 : Recherche complete pour les OLE \n 4 : Afficher les fichiers Suspects\n 5 : exit")

		choix = int(input("\nQuel est le choix ? "))

		print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")

		if choix == 1 :

			Dossier = str(input("\nQuel est le chemin du dossier complet à parcourir ? "))
			os.system('python3 "Script MS/SearchScriptMS.py" "' + Dossier+'"')

		elif choix == 2 :

			os.system('python3 "Script MS/AnalyseMSSuspect.py"')

		elif choix == 3 :

			Dossier = str(input("\nQuel est le chemin du dossier complet à parcourir ? "))
			os.system('python3 "Script MS/SearchScriptMS.py" "' + Dossier+ '"')
			print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
			os.system('python3 "Script MS/AnalyseMSSuspect.py"')

		elif choix == 4 :

			affiche(chemin+"/FichierTXT/FileSuspect.txt")

		elif choix == 5 :		
			exit = 0

		else :
			print("Erreur dans le choix")

		print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
