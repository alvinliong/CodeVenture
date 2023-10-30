"""
File: UnitSelectFrame.py
Description: This file is GUI for the UnitSelectFrame
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk
from functools import partial

# Local application imports
from Database import *
from ModuleSelectFrame import ModuleSelectFrame

class UnitSelectFrame(tk.Frame):
    """
    The class definition for the UnitSelectFrame class.
    """

    def __init__(self, master, student_main_frame, current_user, current_student_progress):
        """
        The constructor for the UnitSelectFrame class
        """
        super().__init__(master)
        self.master = master
        self.student_main_frame = student_main_frame
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        units_completed = self.current_student_progress.get_units_completed()


        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        for row in range(2, len(units_database)+1):
            self.rowconfigure(row, weight=0)
        self.rowconfigure(len(units_database)+2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text="CodeVenture | Unit Select",
                               font=("Arial Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Arial Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        # print unit buttons
        unit_labels_dict = {}
        unit_buttons_dict = {}
        row_count = 2
        for unit in units_database:
            unit_title = unit.get_unit_title()
            unit_code = unit.get_unit_code()
            if (unit_code in units_completed):
                unit_buttons_dict[unit_title] = ttk.Button(self, text="\u2713 COMPLETED", state="disabled")
            else:
                unit_buttons_dict[unit_title] = ttk.Button(self, text="START", command=partial(self.select_unit, unit_code))
            unit_buttons_dict[unit_title].grid(row=row_count, column=0, padx=10, pady=10, sticky="E")
            unit_labels_dict[unit_title] = ttk.Label(master=self, text=str(unit_code) + ". " + unit_title, font=("Helvetica Bold", 16))
            unit_labels_dict[unit_title].grid(row=row_count, column=1, sticky="W", padx=10, pady=10)
            row_count += 1

        # The back button
        back_button = ttk.Button(self, text="BACK TO MAIN MENU", command=self.back)
        back_button.grid(row=row_count+1, column=0, columnspan=2, padx=10, pady=10, sticky="N")


    def select_unit(self, unit_code):
        """
        Event handler to go to selected module
        """
        self.current_student_progress.set_current_unit(unit_code)
        write_all_databases()
        self.grid_forget()
        module_select_frame = ModuleSelectFrame(self.master, self.student_main_frame, self.current_user, self.current_student_progress)
        module_select_frame.grid(column=0, row=0, sticky="nsew")

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
