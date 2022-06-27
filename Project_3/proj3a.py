# shiftsupsupervisor
#
# Create a separate proj5a file, and create 2 objects, one an Employee, the other a shiftsupsupervisor
# initialize both objects
# print Employee name and number
# print shiftsupsupervisor name, number, salary, bonus
# you may also use an if/then/else and "isinstance" function to determine and print which object belongs to which class

# Import shiftsupsupervisor
import shiftsupervisor

def main():
    # Define arguments for Classes
    # Employee Superclass
    employee_name = 'Mike'
    employee_number = 1001
    # Supervisor Subclass
    supervisor_name = 'Marry'
    supervisor_number = 1000
    supervisor_salary = 75000
    supervisor_bonus = .1 * supervisor_salary

    # Create Employee
    employee = shiftsupervisor.Employee(employee_name, employee_number)

    # Create Supervisor
    supervisor = shiftsupervisor.Shiftsupervisor(supervisor_name, supervisor_number, supervisor_bonus, supervisor_salary)

    # Print Employee name and number
    print()
    print(f'The employee\'s name is {employee.get_name()} and his ID number is {employee.get_number()}')

    # Print Supervisor name, number, salary, and bonus
    print(f'The supervisor\'s name is {supervisor.get_name()} and her ID number is {supervisor.get_number()}')
    print(f'The supervisor also makes ${supervisor.get_salary():,.2f} annually with a bonus of ${supervisor.get_bonus():,.2f}')

    # Prevent script from closing
    input('\nPRESS ENTER TO EXIT')


# Start script
if __name__ == "__main__":
    main()