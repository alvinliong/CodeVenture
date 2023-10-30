"""
File: QuizResultFrame.py
Description: This file is the GUI for the QuizResultFrame
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *

class QuizResultFrame(tk.Frame):
    """
    The class definition for the QuizResultFrame class.
    """

    def __init__(self, master, result, wrong_questions, student_main_frame, current_unit, current_user, current_student_progress):
        """
        The constructor for the QuizResultFrame class
        """
        super().__init__(master)
        self.master = master
        self.result = result
        self.wrong_questions = wrong_questions
        self.student_main_frame = student_main_frame
        self.current_unit = current_unit
        self.current_user = current_user
        self.current_student_progress = current_student_progress
        
        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

       
        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                            text="Quiz" + " | " + str(self.current_unit.get_unit_code()) + " " + self.current_unit.get_unit_title(),
                            font=("Helvetica Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Helvetica Bold", 18))
        username_title.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="E")

        if self.result == "pass":
            # result title
            result_title=tk.Label(self, font=("Helvetica Bold", 16), text="You passed!")
            result_title.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            # details title
            details_title=tk.Label(self, font=("Helvetica", 14), text="You got 100%! You have now completed this unit!")
            details_title.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        if self.result == "fail":
            # result title
            result_title=tk.Label(self, font=("Helvetica Bold", 16), text="You failed!")
            result_title.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            wrong_questions_numbers = []
            for question in wrong_questions:
                wrong_questions_numbers.append(str(question.get_question_code()).split(".")[1])

            # details title
            details_title=tk.Label(self, font=("Helvetica", 14), text="You got question(s): " + str(wrong_questions_numbers) + " wrong. Try again.")
            details_title.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # The back button
        back_button = ttk.Button(self, text="BACK", command=self.back)
        back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="N")

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
