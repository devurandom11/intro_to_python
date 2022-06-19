# Long-Distance Calls
# A long-distance provider charges the following rates for telephone calls:
#
# Rate Category                             Rate per Minute
# Daytime (6:00 a.m. through 5:59 p.m.)         $0.07
# Evening (6:00 p.m. through 11:59 p.m.)        $0.12
# Off-Peak (midnight through 5:59 a.m.)         $0.05
#
# Write a GUI application that allows the user to select a rate category (from a set of radio
# buttons), and enter the number of minutes of the call into an Entry widget. An info dialog
# box should display the charge for the call.

# Import tkinter modules
import tkinter
import tkinter.messagebox

# Define Constant Rates
DAYTIME = .07
EVENTING = .12
OFF_PEAK = .05

# Define myGUI Class
class myGUI:
    # Default init method
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        # Create a title for the window
        self.main_window.title('Long Distance Calling')

        # Create three frames (call selection, minute input, buttons)
        self.selection_frame = tkinter.Frame(self.main_window)
        self.input_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create Label for title in top frame
        self.title = tkinter.Label(self.selection_frame, text='Long Distance Calling Rates:')
        
        # Create IntVar object for Radio Buttons and set to 1 as default.
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Create radio button widgets in top frame
        self.rb1 = tkinter.Radiobutton(self.selection_frame, text='Daytime(6:00am-5:59pm)', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.selection_frame, text='Evening(6:00pm-11:59pm)', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.selection_frame, text='Off-Peak(midnight-5:59am)', variable=self.radio_var, value=3)
        
        # Pack title and radio buttons for top frame
        self.title.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # Create widgets for mid frame, user input.
        self.label = tkinter.Label(self.input_frame, text='Enter the number of minutes for the call:')
        self.call_length = tkinter.Entry(self.input_frame, width=5)

        # Pack input_frame widgets
        self.label.pack(side='left')
        self.call_length.pack(side='left')

        # Create buttons for conversion in button frame
        self.cost_button = tkinter.Button(self.button_frame, text='OK', command=self.cost)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons in button frame
        self.cost_button.pack(side='left', padx=5, pady=20)
        self.quit_button.pack(side='left', padx=5, pady=20)

        # Pack all frames
        self.selection_frame.pack()
        self.input_frame.pack(padx=25) # add vertical padding for user input area
        self.button_frame.pack()

        # Start main loop
        tkinter.mainloop()

    # Define the cost method for cost button
    def cost(self):
        # Get the radio button option selected and call length
        radio_option = self.radio_var.get()
        call_length = float(self.call_length.get())
        # Calculate Cost based on selection
        if radio_option == 1:
            total_cost = call_length * DAYTIME
        elif radio_option == 2:
            total_cost = call_length * EVENTING
        else:
            total_cost = call_length * OFF_PEAK
        # Print results to message box
        tkinter.messagebox.showinfo('Total Cost', f'The total cost of your call is ${total_cost:,.2f}')

# Create my_gui object to start program 
if __name__ == "__main__":
    my_gui = myGUI()