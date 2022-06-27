# Largest List Item
# Design a function that accepts a list as an argument and returns the largest value in the list.
# The function should use recursion to find the largest item.

# Define main function
def main():
    # Define list of numbers
    num_list = [14, 2, 6, 15.01, .001, -2, 3, 1, 14.99]
    # Call largest_number function and print results
    print(
        f'\nThe largest number in the list {num_list} is: {largest_number(num_list)}\n')
    # Prevent script from closing automatically
    input('PRESS ENTER TO EXIT')

# Define largest_number function that recursively finds the largest number in a list.
def largest_number(list):
    # BASE CASE
    # If there is only 1 number in num_list, return that number as the largest
    if len(list) == 1:
        maximum = list[0]
        return maximum
    # RECURSION
    # If more than 1 number in the num_list, recurse through the rest of the list comparing num_list[1:] to num_list[0] and return largest.
    else:
        maximum = largest_number(list[1:])
        if maximum > list[0]:
            return maximum
        else:
            return list[0]


# Start script
if __name__ == "__main__":
    main()
