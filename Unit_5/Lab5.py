# Plot the functions x, x**2, and x**3
# 
# 1. Install the "matplotlib" module from the command line using: pip install matplotlib.
# 2. Check the newly installed module. In case of errors you should not continue.
# 
# 3. In your program, create a list of 51 float values [0.0,0.25.0.50,0.75,...]. Start the list with the value [0.0] and then use a loop to append values in increments of 0.25.
# [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75,
#  8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5]
# 
# 4. Use the previous list to create 2 other lists with corresponding values for the other functions (x**2, and x**3). You can call these lists, y_line, y_square, and y_cube. All these lists should start
# with [0.0]. You can use one single "for" loop in range (1,50) to append computed values using the list values from point 3.
# 
# 5. Use 3 different "plot" methods (label the graph, the X and Y axis, change colors etc). Plot all three graphs, straight line, the square, and the cube.  Finally, call only once the show method to
# display the graph.

# Import matplot library
import matplotlib.pyplot as plt

# Define main function
def main():
    y_line = make_y_line()
    y_squared = make_y_squared(y_line)
    y_cubed = make_y_cubed(y_line)
    plot_base(y_line)
    plot_squared(y_line, y_squared)
    plot_cubed(y_line, y_cubed)

    # Plot Title
    plt.title('Average impact of studying on test scores \ngiven days awake before exam')
    # Plot axes labels
    plt.xlabel('Hours Studied')
    plt.ylabel('Test Scores')
    # Scaling
    plt.xlim(xmin=1)
    plt.ylim(ymin=1)
    # Display gridlines
    plt.grid(True)
    # Add legend for days awake
    plt.legend('210')
    # Display plot
    plt.show()

# Populate y_line list.
def make_y_line():
    y_line = [0.0]
    for i in range(50):
        append_value = (y_line[i] + .25)
        y_line.append(append_value)
    return y_line

# Create y_squared list
def make_y_squared(base_list):
    y_squared = []
    for i in range(len(base_list)):
        append_value = (base_list[i]**2)
        y_squared.append(append_value)
    return y_squared

# Create y_cubed list
def make_y_cubed(base_list):
    y_cubed = []
    for i in range(len(base_list)):
        append_value = (base_list[i]**3)
        y_cubed.append(append_value)
    return y_cubed

# y_value plotted against y_value
def plot_base(base_value):
    plt.plot(base_value, base_value, marker="*", color='r')
    return

# y_value plotted against squared_value
def plot_squared(base_value, squared_value):
    plt.plot(base_value, squared_value, marker="*", color='y')
    return

# y_value plotted against cubed_value
def plot_cubed(base_value, cubed_value):
    plt.plot(base_value, cubed_value, marker="D", color='g')
    return


# Start script
if __name__ == "__main__":
    main()