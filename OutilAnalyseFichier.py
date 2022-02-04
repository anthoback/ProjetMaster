import sys,os,string

if __name__ == '__main__':
	print("Cette outil a pour but de parcourir les différents fichier pour but de parcourir les différents fichier d'un dossier pour pouvoir découvrir des fichier malveillant PDF ou OLE")
	
	
	exit = 1
	while exit :
		print("\n 1 : Chercher des fichiers malicieux PDF \n 2 : Chercher des fichiers malicieux OLE  \n 3 : exit")

		choix = int(input("\nQuel est ton choix ? "))
		if choix == 1 :
			os.system('python "Script PDF/SearchFileMaliciousPDF.py" ')
			

		elif choix == 2 :
			os.system('python "Script MS/SearchFileMaliciousMS.py" ')


		elif choix == 3 :
			exit = 0

		else :
			print("Errueur dans le choix")

