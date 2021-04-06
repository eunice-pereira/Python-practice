#Practicing escape sequences 

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat." #prints one \ in string 

# \t tab. The * serves as a bullet point for the list 
# \n makes a new line
# Notice triple single quotes; same printed result as using triple double quotes 

fat_cat = '''
I'll do a list: 
\t* Cat food 
\t* Fishies 
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)