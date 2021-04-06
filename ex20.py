from sys import argv

# input_file argument is test.txt 
script, input_file = argv 

# reads and prints file 
def print_all(f): 
    print(f.read())

# .seek(0) returns file to beginning (first byte). Does not return a value.  
def rewind(f): 
    f.seek(0)

def print_a_line(line_count, f): 
    print(line_count, f.readline())

# opens test.txt 
current_file = open(input_file)

print("First let's print the whole file:\n")

# first function, reads file from beginning 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# returns file to beginning 
rewind(current_file)

print("Let's print three lines:")

# current_line variable, takes lace of line_count
current_line = 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)