"""
File: ModuleFrame.py
Description: This file is the GUI for the ModuleFrame
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *

class ModuleFrame(tk.Frame):
    """
    The class definition for the ModuleFrame class.
    """

    def __init__(self, master, module_select_frame, module, student_main_frame, current_user, current_student_progress):
        """
        The constructor for the ModuleFrame class
        """
        super().__init__(master)
        self.master = master
        self.module = module
        self.student_main_frame = student_main_frame
        self.module_select_frame = module_select_frame
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        module_title = module.get_module_title()
        module_code = module.get_module_code()
        content = module.get_content()
        
        # configure rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text=str(module_code) + " | " + module_title,
                               font=("Helvetica Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Helvetica Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        # Module content
        content_text=tk.Text(self, font=("Helvetica", 14), wrap="word", width="100")
        content_text.insert("insert", content)
        content_text.config(state="disabled")
        content_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        # The complete button
        complete_button = ttk.Button(self, text="FINISH MODULE", command=self.complete)
        complete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="N")


    def complete(self):
        from ModuleSelectFrame import ModuleSelectFrame
        """
        Event handler to complete module
        """
        module_code = self.module.get_module_code()
        self.current_student_progress.add_modules_completed(module_code)
        write_all_databases()
        self.grid_forget()
        self.module_select_frame.destroy()
        self.module_select_frame = ModuleSelectFrame(self.master, self.student_main_frame, self.current_user, self.current_student_progress)
        self.module_select_frame.grid(column=0, row=0, sticky="nsew")
        
        


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
