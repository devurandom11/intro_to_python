# Solve the following problem:
#
# 7. Stadium Seating (page 295)
# A stadium has 3 types of seats:
# Seat A = $20 per ticket
# Seat B = $15 per ticket
# Seat C = $10 per ticket
# Write a program that asks the user how many of each type of ticket was sold, and return the total revenue for all seat types.
# 
# Use the following functions:
#
# get_seats ( seat_type ) # this function asks the user and returns number of seats for the string seat_type. Do not accept negative numbers.
# total_sales ( seat_A, seat_B, seat_C ) # parameters are number of seats for each type; function computes and returns the total sales.
# main() # calls the above functions and displays the total sales
#
# Seat costs should be declared as global constants
#
# Use comments and good variable names. Save your Python script as Lab4.py
# The program must be tested and then uploaded onto Canvas.


# Define seat costs as constants
SEAT_A_COST = 20
SEAT_B_COST = 15
SEAT_C_COST = 10

# Define main() function
def main():
    # Introduce program and print seat costs.
    print()
    print('Hello user, this program computes the total revenue from seat sales by seat type.')
    print('Please follow the instructions carefully:\n')

    # Report seat costs to user. 
    print(f'The cost for each seat type is:\n')
    print("-" * 23)
    print(f'Seat A\t\t${SEAT_A_COST:,.2f}\nSeat B\t\t${SEAT_B_COST:,.2f}\nSeat C\t\t${SEAT_C_COST:,.2f}')
    print("-" * 23+"\n")
    # Call get_seats function and assign to argument for total_sales function
    seat_a_sold = get_seats('Seat A')
    seat_b_sold = get_seats('Seat B')
    seat_c_sold = get_seats('Seat C')

    # Call total_sales function to calculate total revenue from all seat sales and return results as total_revenue
    total_revenue = total_sales(seat_a_sold, seat_b_sold, seat_c_sold)

    # Print results
    print()
    print(f'The total revenue for the reported seat sales is ${total_revenue:,.2f}\n')

# Define get_seats function
def get_seats(seat_type):
    seats_sold = int(input(f'Please enter the total number of \"{seat_type}\" seats sold: '))
    while seats_sold < 0:
        print('ERROR: YOU CANNOT ENTER A NEGATIVE NUMBER')
        seats_sold = int(input(f'Please enter the total number of \"{seat_type}\" seats sold: '))
    return seats_sold

# Define total_sales function
def total_sales(seat_A, seat_B, seat_C):
    total_revenue_test = ((seat_A * SEAT_A_COST) + (seat_B * SEAT_B_COST) + (seat_C * SEAT_C_COST))
    return total_revenue_test

# Call main function
main()

# Input to prevent program from closing
input("PRESS ENTER TO CLOSE")
