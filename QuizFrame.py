"""
File: QuizFrame.py
Description: This file is the QuizFrame class
Author: CodeVenture Team G13 
"""

# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *

class QuizFrame(tk.Frame):
    """
    The class definition for the QuizFrame class.
    """

    def __init__(self, master, module_select_frame, student_main_frame, current_unit, current_user, current_student_progress):
        """
        The constructor for the QuizFrame class
        """
        super().__init__(master)
        self.master = master
        self.module_select_frame = module_select_frame
        self.student_main_frame = student_main_frame
        self.current_unit = current_unit
        self.current_user = current_user
        self.current_student_progress = current_student_progress

        # get the questions for the quiz
        self.quiz_questions = []
        current_unit_code = self.current_unit.get_unit_code()
        for question in quiz_database:
            question_unit_code = int(str(question.get_question_code()).split(".")[0])
            if question_unit_code == current_unit_code:
                question.set_question_correct(False)
                self.quiz_questions.append(question)
        
        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

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

        # Quiz title
        quiz_title=tk.Label(self, font=("Helvetica Bold", 16), text="Unit Quiz\n" + str(current_unit_code) + ". " + self.current_unit.get_unit_title())
        quiz_title.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # No of questions and time limit title
        details_title=tk.Label(self, font=("Helvetica", 14), text="No. of questions: " + str(len(self.quiz_questions)) + "\nTime limit: None")
        details_title.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # instructions title
        instructions_title=tk.Label(self, font=("Helvetica Bold", 14), text="You must get all questions correct to pass the quiz\n and to complete the unit.")
        instructions_title.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Start quiz button
        quiz_start_button = ttk.Button(self, text="START QUIZ", command=self.begin_quiz)
        quiz_start_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="N")

        # The back button
        back_button = ttk.Button(self, text="BACK", command=self.back)
        back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="N")


    def begin_quiz(self):
        from QuizQuestionFrame import QuizQuestionFrame
        """
        Event handler to start quiz 
        """
        quiz_index_counter = 0
        self.grid_forget()
        quiz_question_frame = QuizQuestionFrame(self.master, self.quiz_questions, quiz_index_counter, self.student_main_frame, self.current_unit, self.current_user, self.current_student_progress)
        quiz_question_frame.grid(column=0, row=0, sticky="nsew")

    def back(self):
        """
        Event handler to back
        """
        self.grid_forget()
        self.module_select_frame.grid(column=0, row=0, sticky="nsew")
        
        


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
