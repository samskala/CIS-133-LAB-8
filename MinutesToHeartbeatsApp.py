# *******************************************************************************
# Author:          Josh Meyer
# Assignment:      Lab 8
# Date:            11/14/2026
# Description:     Prompts the user to convert measurements between Minutes to
#                   Heartbeats
# Input:           Number of Minutes
# Output:          Converted measurements to Heartbeats
# Sources: Python textbook Murach 3rd ed, class material, and Lab 8 examples
# *******************************************************************************

# Import necessary packages
import os
import pygubu
import tkinter.messagebox as mb

#
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "minutes_to_heartbeats.ui")


class MinutesToHeartbeatsApp:
    HEARTBEATSPERMINUTE = 42

    def __init__(self, root):
        self.__builder = pygubu.Builder()
        self.__builder.add_resource_path(PROJECT_PATH)
        self.__builder.add_from_file(PROJECT_UI)
        self.__main_window = self.__builder.get_object('top_frame', root)
        self.__builder.connect_callbacks(self)


        self.__minutes_entry = self.__builder.get_object('ent_num_minutes', root)
        self.__heartbeats_entry_variable = self.__builder.get_variable('ent_num_heartbeats_txt')

    def calculate_heartbeats(self):
        try:
            minutes = float(self.__minutes_entry.get())
            heartbeats = minutes * self.HEARTBEATSPERMINUTE
            self.__heartbeats_entry_variable.set("{:.2f} heartbeats".format(heartbeats))
        except ValueError:
            mb.showerror(title="Error Calculating Heartbeats!", message="Minutes must be a decimal number. Please try again.")

    def get_top_frame(self):
        return self.__main_window

    def run(self):
        self.__main_window.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Minutes to Heartbeats Calculator")
    app = MinutesToHeartbeatsApp(root)
    app.run()
