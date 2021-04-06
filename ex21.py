# Functions for math 

# add is name of function, return is performing the actual function. 
# a and b are arguments 
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b): 
    print(f"SUBTRACTING {a} - {b}")
    return a - b 

def multipy(a, b): 
    print(f"MULTIPLYING {a} * {b}")
    return a * b 

def divide(a, b): 
    print(f"DIVIDING {a} / {b}")
    return a / b 

print("Let's do some math with just functions.")

# Using fucntions above
age = add(30, 5) 
height = subtract (78, 4)
weight = multipy(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

# functions are ran using PEMDAS so it will print as each func is calculated 
what = add(age, subtract(height, multipy(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")