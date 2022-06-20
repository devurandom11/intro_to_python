# Project 3B
# Write a program that displays all the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function.

# Define main function

def main():
    # Introduce user to script
    intro()
    # Prints all prime numbers between 1 and 100
    print_prime()
    # Thank user and exit
    outro()


# Introduce user to script
def intro():
    print('\nWelcome to the Prime Number App.\nThis app will print all the prime numbers from 1 to 100.\n')


# Loops from 1 to 100 to check if a number is prime or not. Print's the number if it is prime.
def print_prime():
    for i in range(1, 101):
        # Print i is_prime returns true.
        if is_prime(i) and i != 1:  # Based on assumption 1 is not a prime number.
            print(f'{i} is a prime number')
    print()


# Check whether a number is prime or not by dividing every number by all integers < number starting at 2. Return True if prime (no remainder)
def is_prime(number):
    for i in range(2, number):
        if (number % i == 0) and (number != i):
            return False
    return True


# Thank user for using the script and prevent auto exit.
def outro():
    print('Thank you for using the Prime Number App!\n')
    input('PRESS ENTER TO EXIT.')


# Start script
if __name__ == "__main__":
    main()
