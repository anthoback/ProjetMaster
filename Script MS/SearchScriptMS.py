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

def main() :
	#Initialization var
    numberFile = 0
    numberMS = 0
    #listWord = ['.doc','.dot','.wbk','.docx','.docm','.dotx','.dotm','.docb']
    #listExcel = ['.xls','.xlt','.xlm','.xll_','.xla_','.xla5_','.xla8_','.xlsx','.xlsm','.xltx','.xltm','.xlsb','.xla','.xla','.xll','.xlw']
    #listPowerPoint = ['.ppt','.pot','.pps','.ppa','.ppam','.pptx','.pptm','.potx','.potm','.ppam','.ppsx','.ppsm','.sldx','.sldm','.pa']
    
    #List of MS extensions
    list_ = ['.zip','.doc','.dot','.wbk','.docx','.docm','.dotx','.dotm','.docb','.xls','.xlt','.xlm','.xll_','.xla_','.xla5_','.xla8_','.xlsx','.xlsm','.xltx','.xltm','.xlsb','.xla','.xla','.xll','.xlw','.ppt','.pot','.pps','.ppa','.ppam','.pptx','.pptm','.potx','.potm','.ppam','.ppsx','.ppsm','.sldx','.sldm','.pa']
    for root, dir, files in os.walk(str(sys.argv[1])):
        for file in files:
            numberFile = numberFile + 1
            if any(word in file for word in list_):         
                numberMS = numberMS + 1 

                ListeMacro = []
                StrMacro =""

                #save the path
                fn = root+"\\"+file
                f= '"'+fn+'"'
                print("-------------------------------------------------------------------------------------------\n"+fn)
                #use the tool and save the results in FileContent
                os.system('python3 oledump.py ' +f +' > FichierTXT/FileContent.txt')
                
                #open the file and save all the lines
                with open('FichierTXT/FileContent.txt') as text:
                    datafile = text.readlines()

                #search the line with m or M which indicates if there are macros
                for line in datafile:
                    if (r' m ' in line) or (r' M ' in line):
                        ListeMacro.append(re.findall(r'A\d+\d*', line)[0])
                
                #transform the list into a sequence of strings                       
                for m in ListeMacro :
                    StrMacro = StrMacro +" "+ m

                # if there is a macro so we save the path in File Suspect with streams that have macros   
                if ListeMacro != [] :
                    fichier = open("FichierTXT/FileSuspect.txt", "a")
                    fichier.write(fn + "    "+ StrMacro +"\n")
                    fichier.close()
                    print('Liste des macros :' + StrMacro)
            
    return ( numberFile,numberMS )

if __name__ == '__main__':

   
    print("\nSTART RESEARCH\n")
    #start the timer
    start = time.time()
    
    initFile()
    File,MS = main()
    
    #end the timer 
    end = time.time()
    print("\nFINISH\n")
    
    #print some performance information
    print("Temps :" + str(int(end-start)) + " secondes")
    print("Nombre de fichier : " + str(File))
    print("Nombre de fichier MS: " + str(MS))
   