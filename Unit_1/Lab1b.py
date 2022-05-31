'''
Assignment: Lab1a.py
Class: CS131
Date: 5/14/22
Author: Mike Crawford

Instructions:
A cookie recipe calls for the following ingredients:
    1.5 cups of Sugar
    1 Cup of Butter
    2.75 cups of Flour
The recpie produces 48 cookies with this amount of ingredients. Write a program that asks the user how many cookies he or she want to make, then display the number ofcups of each ingredient needed for the specified number of cookies.
'''

# Introduce program to user
print("Welcome to the Ingredient Adjuster. This program calculate the amount of ingredients you need to make \"N\" number of cookies\n")
cookies = float(input("Please enter the number of cookies you would like to make: "))

# Create a new line before printing results.
#print()

# Calculate ingredients and assign to variables
sugar = (cookies / 48 * 1.5)
butter = (cookies / 48 * 1)
flour = (cookies / 48 * 2.75)

# Print results
if cookies < 0:
    print("\nYou can't make a negative amount of cookies. That's too sad!\n")
else:
    print("\nThe amount of ingredients required to make", f'{cookies:.0f}', "cookies is:\n")
    print(f'{sugar:.2f}', "cups of sugar")
    print(f'{butter:.2f}', "cups of butter")
    print(f'{flour:.2f}', "cups of flour\n")

### Debugging DO NOT USE IN PRODUCTION
'''
debug_sugar = 1.5625
debug_butter = 1.041666666667
debug_flour = 2.86458333333335

print("debug_sugar [ ", f'{debug_sugar:.2f}', " ] --> sugar [ ", f'{sugar:.2f}', " ]")
print("debug_butter [ ", f'{debug_butter:.2f}', " ] --> butter [ ", f'{butter:.2f}', " ]")
print("debug_flour [ ", f'{debug_flour:.2f}', " ] --> flour [ ", f'{flour:.2f}', " ]")
'''

# Prevent program from closing immediately
input("Press ENTER to close")
