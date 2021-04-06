from sys import argv 

script, filename = argv 

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# 'w' flag makes Python truncate file, meanig existing file contents will be replaced (open file in write mode)
# use 'a' if you want to add content to the file (open file in append mode)
# default for open() is 'r', opens in read mode 

print("Opening the file...")
target = open(filename, 'w') 

# do not need to use .truncate() if opening with 'w' flag 
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%s \n %s \n %s \n" % (line1, line2,line3))

# target.write was previously coded using 6 lines, now condensed to one above

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()