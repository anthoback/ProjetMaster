import warnings,sys,os,string
import re
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import time

#Initialization var
nombrePDF = 0
nombreFichier = 0

#Initialization File
#create the file or empty it
with open("FileSuspect.txt", 'w+') as f:
    f.truncate(0)
f.close
with open("FileContent.txt", 'w+') as f:
    f.truncate(0)
f.close
with open("FileProtect.txt", 'w+') as f:
    f.truncate(0)
f.close


#Browse folders and files
print("\n\n\nSTART RESEARCH\n\n\n")
start = time.time()
try:
    for root, dir, files in os.walk(str(sys.argv[1])):
        for file in files:
            nombreFichier = nombreFichier + 1  
            #search .pdf
            if ".pdf" in file:
                
                nombrePDF = nombrePDF + 1 
                Java = False
                Action = False
                
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
                    if '/Encrypt' in line:
                        #search the number of script Java
                        NumberOfScript = re.findall(r'-?\d+\.?\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we save the path in a file
                            if int(s) > 0 :
                                fichier = open("FileProtect.txt", "a")
                                fichier.write(fn + "\n")
                                fichier.close()
                                print("\nFile crypted\n")
                    

                    if '/OpenAction' in line:
                        #search the number of script Java
                        NumberOfScript = re.findall(r'-?\d+\.?\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we save the path in a file
                            if int(s) > 0 :
                                Action = True
                                print("\n/OpenAction Found\n")

                    if '/JavaScript' in line:
                        #search the number of script Java
                        NumberOfScript = re.findall(r'-?\d+\.?\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we save the path in a file
                            if int(s) > 0 :
                                Java = True
                                print("\n/JavaScript Found\n")

                               
                if (Java and Action) :
                    fichier = open("FileSuspect.txt", "a")
                    fichier.write(fn + "\n")
                    fichier.close()
except Exception:
    print('\nError : No argument \npython3 SearchScriptPdf "folder or Path"') 

end = time.time()
print("\n\n\nFINISH\n\n\n")
print("Temps :" + str(int(end-start)) + " secondes")
print("Nombre de fichier : " + str(nombreFichier))
print("Nombre de fichier PDF: " + str(nombrePDF))
