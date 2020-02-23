#Rename unlimited ha ha 

import os as neel

def rename(path,name,number,extension):
    list= neel.listdir(path)
    neel.chdir(path)
    count =number
    for i in list:
        neel.rename(i,name+str(count)+'.'+extension)
        count+=1

        
path = "C:\\Users\\RAIHAN\\Desktop\\rename"
rename(path,'fahim',1,'png')
