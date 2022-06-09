# Date Printer (page 462)

# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
# It should print the date in the format March 12, 2018.
# Hint: You can use a list or a tuple to store the name of the months and use the month number as the index.

# List containing string Months
string_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Define main function
def main():
    intro()
    string_input = user_input()
    list_date = convert_string(string_input)
# Convert input to integers and check for decimal input
    while True:
        try:
            month = int(list_date[0])
            day = int(list_date[1])
            year = int(list_date[2])
            break
        except ValueError:
            print('ERROR: Not the correct date format.')
            string_input = user_input()
            list_date = convert_string(string_input)
    # Check input ranges and character length
    if (month <= 0 or month > 12 or len(list_date[0]) != 2): # Month 2 characters and between 1 and 12
        print('\nERROR: Month out of range or not in 2 character format.\n')
        input('PRESS ENTER TO EXIT')
    elif (day <= 0 or day > 31 or len(list_date[1]) != 2): # Day 2 characters and between 1 and 31
        print('\nERROR: Day out of range or not in 2 character format.\n')
        input('PRESS ENTER TO EXIT')
    elif (year <= 0 or len(list_date[2]) != 4): # Year 4 characters
        print('ERROR: Year out of range or not in 4 character format.\n')
        input('PRESS ENTER TO EXIT')
    else: # If the input passess the previous checks, print results.
        print('\nDate entered in correct format')
        print_results(month, day, year) 
        outro()
    
# Introduce user to script.
def intro():
    print()
    print('Welcome to the Date Printer Application.\n')
    print('This program will take in a date in the format "MM/DD/YYYY" and return the date in string format.\n')
    print('Please follow the input format specifically.\n')

# Request initial input from the user in format mm/dd/yyyy
def user_input():
    string_input = input('Please enter a date in the format "MM/DD/YYYY": ')
    return string_input

# Convert string to list format
def convert_string(string):
    list_date = string.split('/')
    return list_date

# Print results
def print_results(month, day, year):
    # Print results using months as index for string_months list.
    print(f'\n{string_months[month - 1]} {day}, {year}.\n')

# Thank user and exit
def outro():
    print('Thank you for using the Date Printer Application!\n')
    input('PRESS ENTER TO EXIT')
    
# Call main function
if __name__ == "__main__":
    main()