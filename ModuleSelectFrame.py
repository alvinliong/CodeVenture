"""
File: ModuleFrame.py
Description: This file is the GUI for the ModuleFrame
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk
from functools import partial

# Local application imports
from Database import *
from ModuleFrame import ModuleFrame
from QuizFrame import QuizFrame

class ModuleSelectFrame(tk.Frame):
    """
    The class definition for the ModuleSelectFrame class.
    """

    def __init__(self, master, student_main_frame, current_user, current_student_progress):
        """
        The constructor for the ModuleSelectFrame class
        """
        super().__init__(master)
        self.master = master
        self.student_main_frame = student_main_frame
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        # get current unit data
        current_unit_code = self.current_student_progress.get_current_unit()
        for unit in units_database:
            if (unit.get_unit_code() == current_unit_code):
                self.current_unit = unit

        # get the unit modules as objects
        module_codes = self.current_unit.get_modules()
        modules = []
        for code in module_codes:
            for module in modules_database:
                if code == module.get_module_code():
                    modules.append(module)

        # get the modules completed from the student progress
        modules_completed = self.current_student_progress.get_modules_completed()

        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        for row in range(2, len(modules)+1):
            self.rowconfigure(row, weight=0)
        self.rowconfigure(len(modules)+2, weight=0)
        self.rowconfigure(len(modules)+3, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text="CodeVenture | Module Select",
                               font=("Helvetica Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Helvetica Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        # print current unit
        current_unit_title = ttk.Label(master=self,
                               text="Current Unit: " + str(self.current_unit.get_unit_code()) + ". " + self.current_unit.get_unit_title(),
                               font=("Helvetica Bold", 18))
        current_unit_title.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # print module buttons
        module_labels_dict = {}
        module_buttons_dict = {}
        row_count = 2
        for module in modules:
            module_title = module.get_module_title()
            module_code = module.get_module_code()
            if (module_code in modules_completed):
                module_buttons_dict[module_title] = ttk.Button(self, text="\u2713 COMPLETED", command=partial(self.module, module))
            else:
                module_buttons_dict[module_title] = ttk.Button(self, text="START", command=partial(self.module, module))
            module_buttons_dict[module_title].grid(row=row_count, column=0, padx=10, pady=10, sticky="E")
            module_labels_dict[module_title] = ttk.Label(master=self, text=str(module_code) + " " + module_title, font=("Helvetica Bold", 16))
            module_labels_dict[module_title].grid(row=row_count, column=1, sticky="W", padx=10, pady=10)
            row_count += 1

        # if user has completed all modules in the unit
        if (sorted(modules_completed) == sorted(self.current_unit.get_modules())):
            quiz_button = ttk.Button(self, text="ATTEMPT QUIZ", command=self.quiz)
            quiz_button.grid(row=row_count+1, column=0, columnspan=2, padx=10, pady=10, sticky="N")
        # The back button
        back_button = ttk.Button(self, text="BACK TO MAIN MENU", command=self.back)
        back_button.grid(row=row_count+2, column=0, columnspan=2, padx=10, pady=10, sticky="N")

    def module(self, module):
        """
        Event handler to go to selected module
        """
        self.grid_forget()
        module_frame = ModuleFrame(self.master, self, module, self.student_main_frame, self.current_user, self.current_student_progress)
        module_frame.grid(column=0, row=0, sticky="nsew")

    def quiz(self):
        """
        Event handler to begin quiz
        """
        self.grid_forget()
        quiz_frame = QuizFrame(self.master, self, self.student_main_frame, self.current_unit, self.current_user, self.current_student_progress)
        quiz_frame.grid(column=0, row=0, sticky="nsew")

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
