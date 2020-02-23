#tempfile module

import tempfile

#create a temp file

tempfile = tempfile.TemporaryFile()

#write to a temp file

tempfile.write(b'Save this special nnumber for me: 01722750669')
tempfile.seek(0)

#read the temp file
print(tempfile.read())

tempfile.close()
