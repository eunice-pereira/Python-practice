name = 'Eunice Pereira'
age = 33 
height = 64
weight = 145
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

#Curly braces {} used to embed variables in strings.
#Notice f before string double quote. Allows formatting with variables when program runs 
#This is called f string 

print(f"Let's talk about my {name}.")
print(f"She's {height} inches tall.")
print(f"She's {weight} pounds heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"My teeth are usually {teeth} depending on the coffee.")

total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}.")