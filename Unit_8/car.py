# Write a class named Car that has the following data attributes:
    # __year_model (for the car's year and model)
    # __make(for the make of the car)
    # __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments. 
# These valuse should be assigned to the object's __year_model and __make data attributes. 
# It should also assign 0 to the __speed data attribute.
# The class should have the following methods:
    # accelerate
        # The accelerate method should add 5 to the speed data attribute each time it is called.
    # brake
        # The break method should subtract 5 to the speed data attribute each time it is called.
    # get_speed
        # The get_speed method should return the current speed.

# Create Car class
class Car:
    
# Init method for Car(__year_model,__make)
    def __init__(self, __year_model, __make):
        self.year_model = __year_model
        self.make = __make
        # Set speed to 0
        __speed = 0
        self.speed = __speed

# Define accelerate method. Car increases speed by 5.
    def accelerate(self):
        print('Accelerating...')
        self.speed += 5

# Define brake method. Car decreases speed by 5. Prevents negative speed.
    def brake(self):
        print('Braking...')
        if self.speed > 0:
            self.speed -= 5
        elif self.speed == 0:
            self.speed = 0
        else:
            print('MALFUNCTION!')

# Define get_speed method. Print current speed.
    def get_speed(self):
        print(f'Speed: {self.speed}mph')
