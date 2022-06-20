# Project 3c
# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that calculates the average of all the numbers stored in
# the file. Add exception handling to the program for ValueError,

# Define main function
def main():
    # Introduce user to script
    intro()
    # Read the file
    total, count = read_file()
    
    # Print results if no errors occured in the read_file() function. 
    if total and count == None:
        return None
    elif total and count != None:
        print_results(total, count)


# Introduce user to script and pause for effect.
def intro():
    print('\nWelcome to the Average Numeber Calculator.\n\nThis app will calculate the average of all the numbers stored in the file \'numbers.txt\'\n')
    input('Press ENTER to continue...')


# Open the file, read the contents, calculate total and count, close the file. Handles various errors.
def read_file():
    try:
        count = 0
        total = 0
        num_file = open('numbers.txt', 'r')
        for line in num_file:
            amount = float(line)
            total += amount
            count += 1
        num_file.close()
        return total, count
    # Error handling to give warning and returns None to stop script execution.
    except ValueError:
        print('\nWARNING: Value Error...\nThis program can only work with numbers. Please make sure the file contains only numbers and try again.\n')
        return None, None
    except IOError:
        print('\nERROR: Can not read or locate file...\nPlease run this program from the directory containing the file \'numbers.txt\'\n')
        return None, None
    except:
        print('\nGENERAL ERROR\n')
        return None, None
    
    
# Print the results including total numbers in file, sum of numbers, and average of numbers and includes some formatting.
def print_results(total, count):
    print(f'\n\t\t\t\tResults:')
    print('-'*80 + '\n')
    print(
        f'This file contains {count:.0f} numbers totaling {total:.2f} with an average value of {total/count:.2f}')
    print('-'*80 + '\n')


# Thank user for using the script and prevent auto exit.
def outro():
    print('Thank you for using the Average Number Calculator!\n')
    input('PRESS ENTER TO EXIT')


# Start program
if __name__ == "__main__":
    main()
    outro()
