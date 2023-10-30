"""
File: StudentMainFrame.py
Description: This file is the GUI for the StudentMainFrame
Author: CodeVenture Team G13 
"""
# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *
from ModuleSelectFrame import ModuleSelectFrame
from UnitSelectFrame import UnitSelectFrame
from ProgressFrame import ProgressFrame


class StudentMainFrame(tk.Frame):
    """
    The class definition for the StudentMainFrame class.
    """

    def __init__(self, master, login_frame, current_user, current_student_progress):
        """
        The constructor for the StudentMainFrame class
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text="CodeVenture | Student",
                               font=("Helvetica Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Helvetica Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        # The play button
        play_button = ttk.Button(self, text="PLAY", command=self.play)
        play_button.grid(row=1, column=0, padx=10, pady=10, sticky="SE")

        # The view progress button
        progress_button = ttk.Button(self, text="PROGRESS", command=self.progress)
        progress_button.grid(row=1, column=1, padx=10, pady=10, sticky="SW")

        # The forum button
        forum_button = ttk.Button(self, text="FORUM")
        forum_button.grid(row=2, column=0, padx=10, pady=10, sticky="NE")

        # The settings button
        settings_button = ttk.Button(self, text="SETTINGS")
        settings_button.grid(row=2, column=1, padx=10, pady=10, sticky="NW")

        # The logout button
        logout_button = ttk.Button(self, text="LOG OUT", command=self.logout)
        logout_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="N")

    def progress(self):
        """
        Event handler to view progress
        """
        self.grid_forget()
        progress_frame = ProgressFrame(self.master, self, self.current_user, self.current_student_progress)
        progress_frame.grid(column=0, row=0, sticky="nsew")
        
    def play(self):
        """
        Event handler if student to play
        """
        if(self.current_student_progress.get_current_unit() == None):
            unit_select_frame = UnitSelectFrame(self.master, self, self.current_user, self.current_student_progress)
            unit_select_frame.grid(column=0, row=0, sticky="nsew")
        else:
            module_select_frame = ModuleSelectFrame(self.master, self, self.current_user, self.current_student_progress)
            module_select_frame.grid(column=0, row=0, sticky="nsew")
    def logout(self):
        from LoginFrame import LoginFrame
        """
        Event handler to logout
        """
        self.grid_forget()
        LoginFrame = LoginFrame(self.master, "")
        LoginFrame.grid(column=0, row=0, sticky="nsew")
        print(self.current_user.get_first_name() + " logged out")
        self.current_user = None


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
