from sys import argv
from os.path import exists # exists command returns True if a file exists, based on name in string as argument

script, from_file, to_file = argv 

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

#len () function gets length of string and returns as a number 
print(f"The input file is {len(indata)} bytes long")

# will return as true or false (in this case false, to_file is created in terminal)
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# good practice to use close() method to close all files 
out_file.close()
in_file.close() 