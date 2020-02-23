# zipfile module

import zipfile

#open and list

zip = zipfile.ZipFile('archive.zip', 'r')
print(zip.namelist())

#metadata in the zip folder

for meta in zip.infolist():
    print(meta)
info = zip.getinfo('zipfile1.txt')
print(info)

#access to files in zip folder

print(zip.read('zipfile1.txt'))
with zip.open('zipfile1.txt') as f:
    print(f.read())

# Extracting files

#zip.extract('zipfile1.txt')
zip.extractall()

#closing the zip

