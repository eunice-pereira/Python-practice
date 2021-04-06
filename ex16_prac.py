# practicing reading file 

from sys import argv

script, filename = argv 

# opening file then reading, calling txt file 
txt = open(filename)

print(txt.read())
