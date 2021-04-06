# reading files 

# saved plain text file as ex15_sample.txt 
# will open file in script and print it out 

# using argv to get a filename 
from sys import argv 

script, filename = argv

# new command, open
txt = open(filename) 

# notice new function, read(). Will read command with no parameters
# can give a file a command by using the . , name of the command, and parameters 
print(f"Here's your file {filename}:")
print(txt.read()) 

