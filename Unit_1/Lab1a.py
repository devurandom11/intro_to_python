'''
Assignment: Lab1a.py
Class: CS131
Date: 5/14/22
Author: Mike Crawford

Instructions:
Write a program that converts Celsius temperature to Fahrenheit temperature. The formula is as follows:
F = 9/5C + 32
The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.
'''
# Introduce program to user.
print("Hello and welcome to the temperature converter, where I'll help you convert a temperature from Celsius to Fahrenheit!\n")

# Get user input of celsius temperature.
temp_celsius = float(input("Please enter a temperature in Celsius: "))

# Calculate temperature in fahrenheit and report to the user.
temp_fahrenheit = (temp_celsius * (9 / 5) + 32)
print("")
print(temp_celsius, "degrees celsius converts to", f'{temp_fahrenheit:.2f}', "degrees fahrenheit!\n")

## Debugging DO NOT USE IN PRODUCTION
'''
debug_temp = -89.6
print("debug_temp [ ", debug_temp, " ] --> temp_farenheit [", temp_fahrenheit, " ]\n" )
'''

# Prevents program from closing immediately.
input("Press ENTER to close")
