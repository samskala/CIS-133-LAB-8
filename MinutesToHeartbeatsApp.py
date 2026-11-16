# ****************************************************************************
# Author:          Josh Meyer
# Assignment:      Lab 8
# Date:            11/14/2026
# Description:     Prompts the user to convert measurements between Minutes to
#                   Heartbeats
# Input:           Number of Minutes
# Output:          Converted measurements to Heartbeats
# Sources: Python textbook Murach 3rd ed, class material, and Lab 8 examples
# ****************************************************************************

# Import necessary packages
import os
import pygubu
import tkinter.messagebox as mb

# Initialize global variables for locating the UI file
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "minutes_to_heartbeats.ui")

# Class definition for the Minutes To Heartbeats Application
class MinutesToHeartbeatsApp:
    # Define the average heartbeats per minute as a variable
    HEARTBEATSPERMINUTE = 72

    # Function for initializating an instance of this class
    def __init__(self, root):
        # Initialize a new Pygubu Builder instance
        self.__builder = pygubu.Builder()
        # Add the resource path and UI file to the builder
        self.__builder.add_resource_path(PROJECT_PATH)
        self.__builder.add_from_file(PROJECT_UI)
        # Reference the "top_frame" and associate that to the main window
        self.__main_window = self.__builder.get_object('top_frame', root)
        # Link the callback functions in the UI to those defined by the class
        self.__builder.connect_callbacks(self)
        # Create a private attribute for retrieving the value of the "Entry"
        #  object for number of minutes from the UI.
        self.__minutes_entry = self.__builder.get_object('ent_num_minutes',
            root)
        # Create a private attribute for retrieving the text value of the
        #  "Entry" object that displays the converted value for number of
        #  heartbeats.
        self.__heartbeats_entry_variable = self.__builder.get_variable(
            'ent_num_heartbeats_txt'
        )

    # Function for calculating the number of heartbeats for the given number
    #  of minutes
    def calculate_heartbeats(self):
        try:
            # Convert the string value for number of minutes to a float
            minutes = float(self.__minutes_entry.get())
            # Multiply the number of minutes by the value of heartbeats per
            #  minute
            heartbeats = minutes * self.HEARTBEATSPERMINUTE
            # Update the "Entry" object variable that displays the number of
            #  heartbeats.
            self.__heartbeats_entry_variable.set("{:.2f} heartbeats".
                format(heartbeats))
        except ValueError:
            # Something went wrong with the calculation, most likely that the
            #  value provided to be converted to float was not a valid decimal
            mb.showerror(title="Error Calculating Heartbeats!", 
                message="Minutes must be a decimal number. Please try again."
            )

    # Function for returning the main window
    def get_top_frame(self):
        return self.__main_window

    # Function for creating the main application loop
    def run(self):
        self.__main_window.mainloop()


# If this file is run as a standalone app, build a base tkinter window with
#  the window size and title as defined and pass that to a
#  MinutesToHeartbeatsApp instance to be run as the main application loop
if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Minutes to Heartbeats Calculator")
    app = MinutesToHeartbeatsApp(root)
    app.run()
