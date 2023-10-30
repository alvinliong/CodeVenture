"""
File: ProgressFrame.py
Description: This file is the GUI for the ProgressFrame
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk
from functools import partial


# Local application imports
from Database import *
from ModuleSelectFrame import ModuleSelectFrame

class ProgressFrame(tk.Frame):
    """
    The class definition for the ProgressFrame class.
    """

    def __init__(self, master, student_main_frame, current_user, current_student_progress):
        """
        The constructor for the ProgressFrame class
        """
        super().__init__(master)
        self.master = master
        self.student_main_frame = student_main_frame
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        units_completed = self.current_student_progress.get_units_completed()
        modules_completed = self.current_student_progress.get_modules_completed()
        current_unit_code = self.current_student_progress.get_current_unit()
        current_unit = None
        for unit in units_database:
            if unit.get_unit_code() == current_unit_code:
                current_unit = unit

        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        for row in range(2, 6):
            self.rowconfigure(row, weight=0)
        self.rowconfigure(6, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text="CodeVenture | Progress Tracker",
                               font=("Arial Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Arial Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        # Current unit heading
        if current_unit != None:
            current_unit_title = ttk.Label(master=self,
                                    text=f"Current Unit Progress: " + str(current_unit.get_unit_code()) + ". " + current_unit.get_unit_title(),
                                    font=("Arial Bold", 16))
            current_unit_title.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
             # current unit percentage
            current_unit_percentage = (len(modules_completed)/(len(current_unit.get_modules())+0.1))*100

            percentage_title = ttk.Label(master=self,
                                    text=str(int(current_unit_percentage)) + "%",
                                    font=("Arial Bold", 16))
            percentage_title.grid(row=3, column=0, columnspan=1, padx=2, pady=2, sticky="E")
            progress_bar = ttk.Progressbar(self, length=100, mode="determinate", orient="horizontal")
            progress_bar.grid(row=3, column=1, columnspan=1, padx=2, pady=2, sticky="W")
            progress_bar["value"] = current_unit_percentage
        else:
            current_unit_title = ttk.Label(master=self,
                                    text=f"Current unit progress: No active unit!",
                                    font=("Arial Bold", 16))
            current_unit_title.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Current unit heading
        overall_progress_title = ttk.Label(master=self,
                                text=f"Overall CodeVenture completion",
                                font=("Arial Bold", 16))
        overall_progress_title.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
            # current unit percentage
        overall_percentage = (len(units_completed)/(len(units_database)))*100

        overall_percentage_title = ttk.Label(master=self,
                                text=str(int(overall_percentage)) + "%",
                                font=("Arial Bold", 16))
        overall_percentage_title.grid(row=5, column=0, columnspan=1, padx=2, pady=2, sticky="E")
        overall_progress_bar = ttk.Progressbar(self, length=100, mode="determinate", orient="horizontal")
        overall_progress_bar.grid(row=5, column=1, columnspan=1, padx=2, pady=2, sticky="W")
        overall_progress_bar["value"] = overall_percentage

        # The back button
        back_button = ttk.Button(self, text="BACK TO MAIN MENU", command=self.back)
        back_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="N")


    def back(self):
        """
        Event handler to back
        """
        self.grid_forget()
        self.student_main_frame.grid(column=0, row=0, sticky="nsew")
        


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
