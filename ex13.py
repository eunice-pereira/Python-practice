# Input methods; parameters, unpacking, variables 

# import is used to add modules (or libraries) to script from Python feature set
# argv is argument variable, holds arguments passed to Python script when ran 
# line 8 unpacks argv, rather than holding arguments, it gets assigned to four variables 
# i.e. Tells Python to take whatever is in argv, unpack it, and assing it to these variables in order 

from sys import argv 
script, first, second, third = argv 

print("The script is called:", script)
print("Your frist variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

response = input("Do you know what's going on? ")
print(f"In conclusion, {response}")

# Difference between argv and input() 
# argv requires script inputes on command line 
# input() requires incupt while script is running 