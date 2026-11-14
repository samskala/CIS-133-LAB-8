import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "heartbeat_to_seconds.ui")


class HeartbeatToSecondsApp:
    heartbeats_per_second = .7

    # This class implements a simple calculator to convert heartbeats to seconds.
    # It can either be run as a stand-alone app (run HeartbeatToSecondsApp.py directly)
    # or within a tabbed notebook (run main.py and select the Grams to Ounces tab).

    def __init__(self, master):

        # Boilerplate to build the tkinter interface based on heartbeat_to_seconds.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        # Save these two UI elements as properties so that we can access them when
        # the user clicks on the calculate button.
        self.__heartbeats_entry = builder.get_object('heartbeats_entry', master)
        self.__seconds_entry_variable = builder.get_variable('seconds_entry_variable')

    def calculate(self):
        # Convert heartbeats to seconds. If there's an error, display an error message.
        try:
            heartbeats = int(self.__heartbeats_entry.get())
            seconds = heartbeats / self.heartbeats_per_second
            self.__seconds_entry_variable.set("{:.2f} seconds".format(seconds))
        except ValueError:
            mb.showerror(title="Error Calculating Seconds!", message="Heartbeats must be a whole number. Please try again.")

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = HeartbeatToSecondsApp(root)
    app.run()

