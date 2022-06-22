# Recursive List Sum
#
# Design a function that accepts a list of numbers as an argument. The function should recursively
# calculate the sum of all the numbers in the list and return that value.

# Define main function
def main():
    # Define list of numbers to sum
    num_list = [2, 1, 4, 3, 6, 5, 8, 7, 9]
    # Call sum_numbers function and print total
    print(f'\nThe sum of the numbers in the list is: {sum_numbers(num_list)}\n')
    # Prevent script from closing automatically
    input('PRESS ENTER TO EXIT\n\n')

# Define sum function


def sum_numbers(num_list):
    # Base Case. Exit recursive loop when list == 1.
    if len(num_list) == 1:
        return num_list[0]
    else:
        # Recursive loop adding index 0 of num_list to the sum_numebers function for the remaining numbers
        return num_list[0] + sum_numbers(num_list[1:])

# Start script
if __name__ == "__main__":
    main()