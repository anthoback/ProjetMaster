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
		print("\nChercher des fichiers malicieux PDF \n 1 : Chercher des fichiers malicieux \n 2 : Analyser les fichier Suspect (Javascript + OpenAction) \n 3 : Analyser les fichier avec uniquement du Javascript \n 4 : Analyser les fichier avec uniquement des action à l'ouverture \n 5 : Recherche complete pour les PDF \n 6 : Afficher les fichiers malicieux trouvé\n 7 : exit")

		choix = int(input("\nQuel est ton choix ? "))

		print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")

		if choix == 1 :
				
			Dossier = str(input("Quel est le chemin du dossier complet ? "))
			os.system('python "Script PDF/SearchScriptPdf.py" ' + Dossier)	

		elif choix == 2 :

			os.system('python "Script PDF/AnalysePDFSuspect.py"')

		elif choix == 3 :

			os.system('python "Script PDF/AnalysePDFJava.py"')

		elif choix == 4 :

			os.system('python "Script PDF/AnalysePDFOpenAct.py"')	
					
		elif choix == 5 :

			Dossier = str(input("Quel est le chemin du dossier complet ? "))
			os.system('python "Script PDF/SearchScriptPdf.py" ' + Dossier)
			print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
			os.system('python "Script PDF/AnalysePDFSuspect.py"')
			print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
			os.system('python "Script PDF/AnalysePDFJava.py"')
			print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
			os.system('python "Script PDF/AnalysePDFOpenAct.py"')	
		
		elif choix == 6 :
			
			exit2 = 1
			while exit2 :
				print("\nAfficher les fichiers malicieux trouvé \n 1 : Afficher les fichier Suspect (Javascript + OpenAction) \n 2 : Afficher les fichier avec uniquement du Javascript \n 3 : Afficher les fichier avec uniquement des action à l'ouverture \n 4 : exit")
				
				choix2 = int(input("\nQuel est ton choix ? "))

				print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
				
				if choix2 == 1 :

					affiche(chemin+"/FichierTXT/FileSuspect.txt")

				elif choix2 == 2 :

					affiche(chemin+"/FichierTXT/FileWithJava.txt")

				elif choix2 == 3 :

					affiche(chemin+"/FichierTXT/FileWithOpenAction.txt")
		
				elif choix2 == 4 :
					exit2 = 0

				else : 
					print("Errueur dans le choix")
				print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")
				

		elif choix == 7 :		
			exit = 0

		else : 
			print("Errueur dans le choix")

		print ("\n\n///////////////////////////////////////////////////////////////////////////////////////////////////\n\n")