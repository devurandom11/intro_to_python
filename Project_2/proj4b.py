# Proj4b: Sum of Digits in a String
# Input must be validated. For testing purpose you can print also the individual digits.

# Write a program that asks the user to enter a series of single-digit numbers with nothing
# separating them. The program should display the sum of all the single digit numbers in the
# string. For example, if the user enters 2514, the method should return 12, which is the sum
# of 2, 5, 1, and 4.

# Define main function
def main():
    try: # Validate input for numbers only
        total = 0
        numbers = input(
            'Please enter a string of positive whole numbers to be added together with spaces in between: ')
        for i in range(len(numbers)): # Checks length of input and sums all numbers.
            number = int(numbers[i])
            total += number
        print(f'\nThe sum of your numbers is: {total}\n')
    except: # Repeat process if all numbers not entered.
        print('\nERROR: PLEASE ENTER POSITIVE WHOLE NUMBERS WITH NO SPACES.\n')
        main()


# Introduces user to script
def intro():
    print('\nWelcome to the Sum of Digits in a String App.\nThis program will take string of positive whole numbers and return the sum.\n')


# Thank user for using the script and prevent auto exit.
def outro():
    print('Thank you for using the Sum of Digits in a String App!\n')
    input('PRESS ENTER TO EXIT')


# Start script
if __name__ == "__main__":
    intro()
    main()
    outro()
