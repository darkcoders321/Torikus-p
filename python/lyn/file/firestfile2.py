# Iterative files

myfile = open('new.txt', 'r')

#read one line at a time

print('my one line is: ' + myfile.readline())
myfile.seek(0)

#iterate through each line of a file

for line in myfile:
    newtext = line.replace('hey', 'hlw')
    print(newtext)
myfile.close()
