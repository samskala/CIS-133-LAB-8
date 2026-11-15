# *******************************************************************************
# Author:          Sam M and Josh M
# Assignment:      Lab 8
# Date:            11/14/2026
# Description:     Prompts the user to convert measurements between Heartbeats
#                   and Seconds, or Minutes and Heartbeats.
# Input:           Number of Heartbeats, Number of Minutes
# Output:          Converted measurements to Seconds or to Heartbeats
# Sources: Python textbook Murach 3rd ed, class material, and Lab 8 examples
# *******************************************************************************

import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from HeartbeatToSecondsApp import HeartbeatToSecondsApp
from MinutesToHeartbeatsApp import MinutesToHeartbeatsApp

# Main Window for the team calculator project.
# To add a new tab, create an App object with a get_top_frame method.
# Then, add the app to the __main_notebook, along with a name for the tab.
# See HeartbeatToSecondsApp.py for a simple example.

class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add first calculator
        heartbeat_to_seconds_app = HeartbeatToSecondsApp(self.__mainwindow)
        self.__main_notebook.add(heartbeat_to_seconds_app.get_top_frame(), text="Heartbeat to seconds")

        minutes_to_heartbeats_app = MinutesToHeartbeatsApp(self.__mainwindow)
        self.__main_notebook.add(minutes_to_heartbeats_app.get_top_frame(), text="Minutes to Heartbeats")

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x250")
    root.title("Team Calculator Lab")
    app = MainApp(root)
    app.run()

