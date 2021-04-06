# practicing input
# When input() function executes program flow will be stopped until user have given an input
# end= ' ' tells print to not end the line with a newline character and go to next line

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print("What is your diet preference?", end=' ')
diet = input()

print(f"So, you're {age} old, {height} tall, {weight} heavy and eat a {diet} diet.")
