# Assignment: Lab3.py
# Class: CS131
# Date: 03/06/22
# Author: Mike Crawford
# Instructions: 
#
# Write a program that uses nested loops to draw this pattern:
# ===========================
#                           |
# *******                   |
# ******                    |
# *****                     |
# ****                      |
# ***                       |
# **                        |
# *                         |
#                           |
# ===========================
# 
# Use comments and good variable names.
# Save your Python script as Lab3.py

# Set num_rows to equal the total rows in the pattern. 
num_rows = 7

# Create outer loop to iterate through each row printing new line, and inner loop to iterate through each column printing "*"
for rows in range (num_rows,0,-1): # Outer loop counting from 7 to 1. Target variable rows must start at 7 and end at 1 to be used in inner loop.
    for columns in range (rows): # Uses rows variable from outer loop as argument for range. This starts at 7 and decrements by 1 on each iteration of the outer loop.
        print("*", end="") # Print asterisk with no default new-line after.
    print() # Print new line after each completion of the inner loop.

# User input to close program. Prevents program from closing immediately.
print()
input("PRESS ENTER TO EXIT")

# Alternate solutions using two variable: Rows and Columns.
#
# rows = 7
# columns = 7
#
# Solution 1: Set inside loop to decrement by outer loop.
# for r in range (rows):
#     for c in range (columns - r):
#         print ("*", end="")
#     print()
#
# Solution 2: Decrementing inside loop
# 
# for r in range (rows):
#     for c in range (columns,0,-1):
#         print("*", end="")
#     columns -= 1
#     print()