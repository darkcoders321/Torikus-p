#files and file writing
#open a file

myfile = open('new.txt', 'w')

# w --> write
# r --> read
# r+ --> read and write
# a --> append

print('Name ' + myfile.name)
print('Mode ' + myfile.mode)

#write a file 

myfile.write(' torikus sadik raihan \nhow are you?')
myfile.close()

#read file
myfile = open('new.txt', 'r')
print('reading....' + myfile.read())
