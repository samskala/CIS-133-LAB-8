# ****************************************************************************
# Author:          Sam M and Josh M
# Assignment:      Lab 8
# Date:            11/14/2026
# Description:     Prompts the user to convert measurements between Heartbeats
#                   and Seconds, or Minutes and Heartbeats.
# Input:           Number of Heartbeats, Number of Minutes
# Output:          Converted measurements to Seconds or to Heartbeats
# Sources: Python textbook Murach 3rd ed, class material, and Lab 8 examples
# ****************************************************************************

# Import necessary packages
import tkinter as tk
import tkinter.ttk as ttk
# Import App classes for the Notebook tabs
from AboutApp import AboutApp
from HeartbeatToSecondsApp import HeartbeatToSecondsApp
from MinutesToHeartbeatsApp import MinutesToHeartbeatsApp

# Main Window for the team calculator project.
# To add a new tab, create an App object with a get_top_frame method.
# Then, add the app to the __main_notebook, along with a name for the tab.
# See HeartbeatToSecondsApp.py for a simple example.

class MainApp:
    def __init__(self, root):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(root, 0, weight=1)
        tk.Grid.rowconfigure(root, 0, weight=1)

        # Build the base Notebook, set the grid to sticky, and configure the
        #  rows and columns with the same default weight
        self.__main_notebook = ttk.Notebook(root)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__main_window = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__main_window)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add Heartbeat to seconds tab
        heartbeat_to_seconds_app = HeartbeatToSecondsApp(self.__main_window)
        self.__main_notebook.add(heartbeat_to_seconds_app.get_top_frame(), text="Heartbeat to seconds")

        # Add Minutes to Heartbeats tab
        minutes_to_heartbeats_app = MinutesToHeartbeatsApp(self.__main_window)
        self.__main_notebook.add(minutes_to_heartbeats_app.get_top_frame(), text="Minutes to Heartbeats")

    # Function for creating the main application loop
    def run(self):
        self.__main_window.mainloop()

# Build a base tkinter window with the window size and title as defined and
#  pass that to a MainApp instance to be run as the main application loop
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x250")
    root.title("Team Calculator Lab")
    app = MainApp(root)
    app.run()

