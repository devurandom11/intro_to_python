# Design a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelrate method, get the current speed of the car and display it.
# Then call the brake method five times.
# After each call to the brake method, get the current speed of the car and display it.
# Sample Output:
# Accelerate
# Speed: 5 mph
# Accelerate
# Speed: 10 mph
# Accelerate
# Speed: 15 mph
# Accelerate
# Speed: 20 mph
# Brake
# Speed: 15 mph
# Brake
# Speed: 10 mph
# Brake
# Speed: 5 mph
# Brake
# Speed: 0 mph

# import car.py module
import car

# Define main function
def main():

    # Present user with list of 5 cars to choose from.
    intro()

    # Get user input
    year_model = user_input()

    # Create car object based on user selection.
    user_car = assign_car(year_model)

    # Show user car selection and press Enter to start driving
    show_car(user_car)

    # Call accelerate and print results five times
    accelerate(user_car)

    # Call brake and print results five times
    brake(user_car)

    # Thank user
    outro()

# Define intro function. Introduce script and give user car selection.
def intro():
    print('\nWhich car would you like to drive today?')
    print('\n----------------------------------------')
    print('1: 2020 Tesla Model S')
    print('2: 2022 Lexus RX350')
    print('3: 1999 Toyota Camry')
    print('4: 2016 Mercedes C300')
    print('5: 2021 Lamborghini Huracán')
    print()

# Define user input function
def user_input():
    # Get user selection.
    year_model = input('Select car number (1 through 5): ')

    # Validate correct input range
    while True:
        try:
            if 1 <= int(year_model) <= 5:
                break
            else:
                print('\nERROR: PLEASE ENTER THE VEHICLE NUMBER (1-5)\n')
                year_model = input('Select car number (1 through 5): ')
        except:
            print('\nERROR: PLEASE ENTER THE VEHICLE NUMBER (1-5)\n')
            year_model = input('Select car number (1 through 5): ')
    return year_model

# Define assign_car function. Creates user_car object and assigns user selection.
def assign_car(year_model):
    if int(year_model) == 1:
        user_car = car.Car('2020 Tesla', 'Model S')
    elif int(year_model) == 2:
        user_car = car.Car('2022 Lexus', 'RX350')
    elif int(year_model) == 3:
        user_car = car.Car('1999 Toyota', 'Camry')
    elif int(year_model) == 4:
        user_car = car.Car('2016 Mercedes', 'C300')
    elif int(year_model) == 5:
        user_car = car.Car('2021 Lamborghini', 'Huracán')
    else:
        print('ASSIGNMENT ERROR')
    return user_car

# Define show_car function. Prints user selection and prompts for ENTER to continue.
def show_car(user_car):
    print(f'\nYou selected the {user_car.year_model} {user_car.make}')
    input('\nPress ENTER to start driving...')
    print()

# Define accelerate function which calls accerate method 5 times and prints state each time.
def accelerate(user_car):
    user_car.get_speed()
    user_car.accelerate()
    user_car.get_speed()
    user_car.accelerate()
    user_car.get_speed()
    user_car.accelerate()
    user_car.get_speed()
    user_car.accelerate()
    user_car.get_speed()
    user_car.accelerate()
    user_car.get_speed()

# Define brake function which calls brake method 5 times and prints state each time.
def brake(user_car):
    user_car.brake()
    user_car.get_speed()
    user_car.brake()
    user_car.get_speed()
    user_car.brake()
    user_car.get_speed()
    user_car.brake()
    user_car.get_speed()
    user_car.brake()
    user_car.get_speed()

# Define outro function. Thanks user and prevent auto exit.
def outro():
    print('\nThank you for driving with us today!')
    input('\nPRESS ENTER TO EXIT')


# Start script
if __name__ == "__main__":
    main()
