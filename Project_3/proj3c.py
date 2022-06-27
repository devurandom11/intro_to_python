# Celsius to Fahrenheit
# Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures.
# The user should be able to enter a Celsius temperature, click a button, then see the equivalent Fahrenheit temperature.
# Use the following formula to make the conversion: F=C*9/5 + 32 where F is Fahrenheit temperature, and C is the Celsius temperature.

# Import tkinter modules
import tkinter

# Define myGUI Class
class myGUI:
    # Default init method
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        # Create a title for the window
        self.main_window.title('Temperature Converter')

        # Create three frames (top, mid, bottom)
        self.input_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create widgets for top frame, user input.
        self.label = tkinter.Label(
            self.input_frame, text='Enter a temperature in Celsius:')
        self.celsius_entry = tkinter.Entry(self.input_frame, width=5)

        # Pack input_frame widgets
        self.label.pack()
        self.celsius_entry.pack()

        # Initialize Stringvar objecvt and create widget for output frame
        self.convert_label = tkinter.Label(
            self.output_frame, text='Converted to Fahrenheit: ')
        self.converted_value = tkinter.StringVar()
        self.fahrenheit_label = tkinter.Label(
            self.output_frame, textvariable=self.converted_value)

        # Pack output frame widgets
        self.convert_label.pack(side='left')
        self.fahrenheit_label.pack(side='left')

        # Create button for conversion in button frame
        self.convert_button = tkinter.Button(
            self.button_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(
            self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons in button frame
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack all frames
        self.input_frame.pack()
        self.output_frame.pack()
        self.button_frame.pack()

        # Start main loop
        tkinter.mainloop()

    # Define the convert method for convert button
    def convert(self):
        # Get value entered in celsius_entry
        celsius = float(self.celsius_entry.get())
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius*(9/5) + 32
        # Convert temperature to a string and store in StringVar object
        self.converted_value.set(fahrenheit)


# Create my_gui object and start script
if __name__ == "__main__":
    my_gui = myGUI()