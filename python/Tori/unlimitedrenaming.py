#Rename unlimited ha ha 
""" [*] coded by: Mr Nobody """
import os

def rename(path,name,number,extension):
    list= os.listdir(path)
    os.chdir(path)
    count =number
    for i in list:
        os.rename(i,name+str(count)+'.'+extension)
        count+=1

        
path = "C:\\Users\\RAIHAN\\Desktop\\rename"
rename(path,'fahim',1,'png')
