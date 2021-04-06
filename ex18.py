# names, variables, code, functions 

# *args is like script using argv but for functions 
# use : to start indenting. Indented lines are part of function 
def print_two(*args):
    arg1, arg2 = args # unpacks argument, same as with previous scripts 
    print(f"arg1: {arg1}, arg2: {arg2}")

# replaces *args above, easier way to recode first function 
# skip unpacking arguments and insert directly into fucntion () 
def print_two_again(arg1, arg2): 
    print(arg1, arg2)

# takes one argument 
def print_one(arg1):
    print(f"arg1: {arg1}")

# takes no arguments 
def print_none(): 
    print("I got nothing.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

