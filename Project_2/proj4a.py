# Proj4a: Expense Pie Chart 
# The file must contain all the required data items. The pie chart should have a title and labels.

# Create a text file proj4aexpenses.txt that contains your expenses for last month in the following categories:
# Rent, Gas, Food, Clothing, Car Payment, Misc
# Write a Python program that reads the data from a file and uses matplotlib to plot a pie
# chart showing how you spend your money.

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Constant variable for expenses file
FILENAME = 'proj4aexpenses.txt'

# Define main function
def main():
    # Open file, read contents, close file
    rent, gas, food, clothing, car_pmt, misc_exp = read_file(FILENAME)
    # Plot results if no errors in read_file() function, else exit. 
    if rent == None:
        input('PRESS ENTER TO EXIT')
        return None
    elif rent != None:
        plot_expenses(rent, gas, food, clothing, car_pmt, misc_exp)


# Reads the file, stripping new lines and assigning values to categories
def read_file(file):
    try:
        infile = open(file, 'r')
        rent = infile.readline().rstrip('\n')
        gas = infile.readline().rstrip('\n')
        food = infile.readline().rstrip('\n')
        clothing = infile.readline().rstrip('\n')
        car_pmt = infile.readline().rstrip('\n')
        misc_exp = infile.readline().rstrip('\n')
        infile.close()
        return rent, gas, food, clothing, car_pmt, misc_exp
# Instructs user to run the script again from the correct directory and exits.
    except IOError:
        print(
            f'\nERROR: Please run this program from the directory containing the file {FILENAME}\n')
        return None, None, None, None, None, None


# Plots the expenses in a pie chart using index 0 as label and index 1 as amount.
def plot_expenses(rent, gas, food, clothing, car_pmt, misc_exp):
    expense_categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc'] # list of categories
    # Plot values and use expense_categories list as label
    plt.pie((rent, gas, food, clothing, car_pmt, misc_exp), labels=(
        expense_categories[0], expense_categories[1], expense_categories[2], expense_categories[3], expense_categories[4], expense_categories[5]))
    plt.title('Mike\'s Monthly Expenses') # Chart title
    plt.show()


# Start program
if __name__ == "__main__":
    main()
