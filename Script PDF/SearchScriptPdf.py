import sys,os,string
import re
import time


def initFile() :
    #Initialization File
    #create the file or empty it
    with open("FichierTXT/FileContent.txt", 'w+') as f:
        f.truncate(0)
    f.close
    with open("FichierTXT/FileSuspect.txt", 'w+') as f:
        f.truncate(0)
    f.close
    with open("FichierTXT/FileProtect.txt", 'w+') as f:
        f.truncate(0)
    f.close
    with open("FichierTXT/FileWithJava.txt", 'w+') as f:
        f.truncate(0)
    f.close
    with open("FichierTXT/FileWithOpenAction.txt", 'w+') as f:
        f.truncate(0)
    f.close


def main() :
    #Initialization var
    numberPDF = 0
    numberFile = 0
    #Folder or disk path
    for root, dir, files in os.walk(str(sys.argv[1])):
        for file in files:
            numberFile = numberFile + 1  
            #search .pdf
            if ".pdf" in file:
                
                numberPDF = numberPDF + 1 
                Java = False
                Action = False
                
                #save the path
                fn = root+"\\"+file
                print("-------------------------------------------------------------------------------------------\n"+fn)
                f= '"'+fn+'"'                
                #use the tool and save the results in FileContent
                os.system('python pdfid_modifie.py ' +f + ' > FichierTXT/FileContent.txt')
                

                #open the file and save all the lines
                with open('FichierTXT/FileContent.txt') as text:
                    datafile = text.readlines()
                

                #search the line with JavaScript or Encrypt or OpenAction
                for line in datafile:
                    if '/Encrypt' in line:
                        #find the number of crypted object
                        NumberOfScript = re.findall(r'-?\d+\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we save the path in FileProtect
                            if int(s) > 0 :
                                fichier = open("FichierTXT/FileProtect.txt", "a")
                                fichier.write(fn + "\n")
                                fichier.close()
                                print("\nFile crypted\n")
                    

                    if '/OpenAction' in line:
                        #find the number of openAction
                        NumberOfScript = re.findall(r'-?\d+\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we set action at true
                            if int(s) > 0 :
                                Action = True
                                print("\n/OpenAction Found\n")

                    if '/JavaScript' in line:
                        #find the number of script Java
                        NumberOfScript = re.findall(r'-?\d+\d*', line)
                        for s in NumberOfScript:
                            #if more than 0 so we set java at true
                            if int(s) > 0 :
                                Java = True
                                print("\n/JavaScript Found\n")

                #if we hava action and java, this file is particularly suspect              
                if (Java and Action) :
                    fichier = open("FichierTXT/FileSuspect.txt", "a")
                    fichier.write(fn + "\n")
                    fichier.close()

                elif (Java) :
                    fichier = open("FichierTXT/FileWithJava.txt", "a")
                    fichier.write(fn + "\n")
                    fichier.close()

                elif (Action) :
                    fichier = open("FichierTXT/FileWithOpenAction.txt", "a")
                    fichier.write(fn + "\n")
                    fichier.close()
    
    return (numberFile,numberPDF)
    

if __name__ == '__main__':

   
    print("\nSTART RESEARCH\n")
    #start the timer
    start = time.time()
    
    initFile()
    File,FilePDF = main()
    
    #end the timer
    end = time.time()
    print("\nFINISH\n")
    
    #print some performance information
    print("Temps :" + str(int(end-start)) + " secondes")
    print("Nombre de fichier : " + str(File))
    print("Nombre de fichier PDF: " + str(FilePDF))
