# Shift Supervisor Class
#
# Create a shiftsupervisor.py file, and in it create an Employee class with 2 attributes: name, number,
# and a Shiftsupervisor subclass with 2 more attributes: bonus, salary.
# The Shiftsupervisor therefore will have the 2 inherited name, number attributes, and the 2 added new ones.
# Create the __init__ functions, as well as the setter and getter functions for each attribute.

# Define Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # Getter methods
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

# Define Shiftsupervisor subclass
class Shiftsupervisor(Employee):
    def __init__(self, name, number, bonus, salary):
        # Call superclass __init__ method
        Employee.__init__(self, name, number)
        # Initialize bonus and salary attributes
        self.__bonus = bonus
        self.__salary = salary

    # Setter methods for new methods. Employee methods inherited
    def set_bonus(self, bonus):
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    # Getter methods for new methods. Employee methods inherited
    def get_bonus(self):
        return self.__bonus

    def get_salary(self):
        return self.__salary
