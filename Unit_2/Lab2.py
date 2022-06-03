# Instructions:
# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman Numeral version of that number.
# If the number is outside the range of 1 through 10, the program should display an error message.
# The following table shows the Roman numerals for the numbers 1 through 10:
#-----------------------------------------------------------------------------
#-------------------------
# Number    Roman Numeral
#-------------------------
# 1         I
# 2         II
# 3         III
# 4         IV
# 5         V
# 6         VI
# 7         VII
# 8         VIII
# 9         IX
# 10        X

# Introduce user to the program. Print new line before and after for aesthetics.
print("\nWelcome to the Roman Numeral Converter program. This program will generate the Roman Numeral for any integer between 1 and 10 entered below.\n")

# Get user_number input from user. Print blank line after for aesthetics.
user_number = int(input("Please enter a number between 1 and 10: "))
print()

# Validate that user_input is between 1 and 10 using if, elif, else statements.
if 1 <= user_number <= 10:

    # Nested if/elif statement mapping each integer in range to it's Roman Numeral counterpart
    if user_number == 1:
        print(f'The Roman numeral for {user_number} is "I"')
    elif user_number == 2:
        print(f'The Roman numeral for {user_number} is "II"')
    elif user_number == 3:
        print(f'The Roman numeral for {user_number} is "III"')
    elif user_number == 4:
        print(f'The Roman numeral for {user_number} is "IV"')
    elif user_number == 5:
        print(f'The Roman numeral for {user_number} is "V"')
    elif user_number == 6:
        print(f'The Roman numeral for {user_number} is "VI"')
    elif user_number == 7:
        print(f'The Roman numeral for {user_number} is "VII"')
    elif user_number == 8:
        print(f'The Roman numeral for {user_number} is "VIII"')
    elif user_number == 9:
        print(f'The Roman numeral for {user_number} is "IX"')
    else:
        print(f'The Roman numeral for {user_number} is "X"')

# Print error message for user_input that is out of range.
else:
    print("ERROR: Enter an integer BETWEEN 1 and 10")

# Print to prevent program from exiting immediately.
input("\nPRESS ENTER TO EXIT")
