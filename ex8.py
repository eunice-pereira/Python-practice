formatter = "{} {} {} {}" #definig variable 

#Using format function below, syntax is string.format() 
#This allows for multiple substitution and value formatting
#Places one or more replacement fields and placeholders defined by {}
#value inside string.format() can be integer, string, character, variable, floating point numeric constant 

print(formatter.format(1, 2, 3, 4)) 
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "What a beautiful day", 
        "To be alive", 
        "And to express gratiude", 
        "For God's grace"
))

#When called, values assigned in () replace four {} assigned in iniital formatter variable 