"""
File: QuizQuestionFrame.py
Description: This file is the GUI for the QuizQuestionFrame
Author: CodeVenture Team G13 
"""
# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *
from QuizResultFrame import QuizResultFrame

class QuizQuestionFrame(tk.Frame):
    """
    The class definition for the QuizQuestionFrame class.
    """

    def __init__(self, master, quiz_questions, quiz_index_counter, student_main_frame, current_unit, current_user, current_student_progress):
        """
        The constructor for the QuizQuestionFrame class
        """
        super().__init__(master)
        self.master = master
        self.quiz_questions = quiz_questions
        self.quiz_index_counter = quiz_index_counter
        self.student_main_frame = student_main_frame
        self.current_unit = current_unit
        self.current_user = current_user
        self.current_student_progress = current_student_progress
        self.user_answer = None
        self.wrong_questions = []

        self.question_no = self.quiz_index_counter + 1
        self.current_question = self.quiz_questions[self.quiz_index_counter]

        # configure rows and columns
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)
        self.rowconfigure(7, weight=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Label containing the CodeVenture heading
        main_title = ttk.Label(master=self,
                               text="Quiz" + " | " + str(self.current_unit.get_unit_code()) + ". " + self.current_unit.get_unit_title(),
                               font=("Helvetica Bold", 25))
        main_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        # Username heading
        username_title = ttk.Label(master=self,
                               text=f"{current_user.get_first_name()} {current_user.get_last_name()}",
                               font=("Helvetica Bold", 18))
        username_title.grid(row=0, column=3, columnspan=1, padx=10, pady=10, sticky="E")

        # Question title
        question_title=tk.Label(self, font=("Helvetica Bold", 16), text="Question " + str(self.question_no))
        question_title.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="W")

        # Answer title
        answer_title=tk.Label(self, font=("Helvetica Bold", 16), text="Answer")
        answer_title.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="W")

        # question content
        question_content=tk.Text(self, font=("Helvetica", 14), height="15")
        question_content.insert("insert", self.current_question.get_question_content())
        question_content.config(state="disabled")
        question_content.grid(row=2, column=0, columnspan=1, rowspan=4, padx=10, pady=10, sticky="W")

        # answers section
        if (self.current_question.get_question_type() == "multiple_choice"):
            self.user_answer = tk.StringVar()
            rA = tk.Radiobutton(self, text = "A", variable=self.user_answer, value="A")
            rA.grid(row=2, column=1, padx=10, pady=10)
            rB = tk.Radiobutton(self, text = "B", variable=self.user_answer, value="B")
            rB.grid(row=3, column=1, padx=10, pady=10)
            rC = tk.Radiobutton(self, text = "C", variable=self.user_answer, value="C")
            rC.grid(row=4, column=1, padx=10, pady=10)
            rD = tk.Radiobutton(self, text = "D", variable=self.user_answer, value="D")
            rD.grid(row=5, column=1, padx=10, pady=10)

        if (self.current_question.get_question_type() == "free_form"):
            self.user_answer = tk.StringVar()
            self.free_form_text=tk.Text(self, font=("Helvetica", 14), wrap="word", height="15",)
            self.free_form_text.grid(row=2, column=1, columnspan=1, rowspan=4, padx=10, pady=10, sticky="W")
           

        if (self.question_no < len(quiz_questions)):
            # Next question quiz button
            next_question_button = ttk.Button(self, text="NEXT QUESTION", command=self.submit_question)
            next_question_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        
        elif(self.question_no == len(quiz_questions)):
            # complete quiz button
            finish_question_button = ttk.Button(self, text="FINISH QUIZ", command=self.submit_quiz)
            finish_question_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        
        # Prompt title
        self.prompt_text = tk.StringVar()
        prompt_title=tk.Label(self, font=("Helvetica Bold", 16), textvariable=self.prompt_text)
        prompt_title.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

    def submit_question(self):
        """
        Event handler to submit question
        """
        
        question_answered = False
        if (self.current_question.get_question_type() == "multiple_choice"):
            if(self.user_answer.get() == ""):
                self.prompt_text.set("You must answer the question!")
            else:
                question_answered = True
        elif (self.current_question.get_question_type() == "free_form"):
            if self.free_form_text.get("1.0",'end-1c') == "":
                self.prompt_text.set("You must answer the question!")
            else:
               question_answered = True 
        if question_answered:
            self.user_answer = self.user_answer.get()
            # lowercase for free form questions
            if (self.current_question.get_question_type() == "free_form"):
                self.user_answer = self.free_form_text.get("1.0",'end-1c').lower()
                
            # check if answer is correct
            print("Given answer: " + self.user_answer)
            print("Correct answer: " + self.current_question.get_question_answer())
            if (self.user_answer == self.current_question.get_question_answer()):
                self.current_question.set_question_correct(True)
            else:
                self.current_question.set_question_correct(False)

            self.quiz_index_counter += 1
            self.grid_forget()
            self.next_quiz_question_frame = QuizQuestionFrame(self.master, self.quiz_questions, self.quiz_index_counter, self.student_main_frame, self.current_unit, self.current_user, self.current_student_progress)
            self.next_quiz_question_frame.grid(column=0, row=0, sticky="nsew")

            for question in self.quiz_questions:
                print(str(question.get_question_code()) + ": " + str(question.get_question_correct()))


    def submit_quiz(self):
        """
        Event handler to submit quiz
        """

        question_answered = False
        if (self.current_question.get_question_type() == "multiple_choice"):
            if(self.user_answer.get() == ""):
                self.prompt_text.set("You must answer the question!")
            else:
                question_answered = True
        elif (self.current_question.get_question_type() == "free_form"):
            if self.free_form_text.get("1.0",'end-1c') == "":
                self.prompt_text.set("You must answer the question!")
            else:
               question_answered = True 
        if question_answered:
            self.user_answer = self.user_answer.get()
            # lowercase for free form questions
            if (self.current_question.get_question_type() == "free_form"):
                self.user_answer = self.free_form_text.get("1.0",'end-1c').lower()
                
            # check if answer is correct
            print("Given answer: " + self.user_answer)
            print("Correct answer: " + self.current_question.get_question_answer())
            if (self.user_answer == self.current_question.get_question_answer()):
                self.current_question.set_question_correct(True)
            else:
                self.current_question.set_question_correct(False)

        for question in self.quiz_questions:
                print(str(question.get_question_code()) + ": " + str(question.get_question_correct()))

        for question in self.quiz_questions:
            if question.get_question_correct() == False:
                self.wrong_questions.append(question)
    
        if len(self.wrong_questions) != 0:
            # take user to results page
            self.grid_forget()
            quiz_result_frame = QuizResultFrame(self.master, "fail", self.wrong_questions, self.student_main_frame, self.current_unit, self.current_user, self.current_student_progress)
            quiz_result_frame.grid(column=0, row=0, sticky="nsew")

        if len(self.wrong_questions) == 0:
            # update student progress
            self.current_student_progress.set_current_unit(None)
            self.current_student_progress.reset_modules_completed()
            self.current_student_progress.update_units_completed(self.current_unit.get_unit_code())
            write_all_databases()

            # take user to results page
            self.grid_forget()
            quiz_result_frame = QuizResultFrame(self.master, "pass", self.wrong_questions, self.student_main_frame, self.current_unit, self.current_user, self.current_student_progress)
            quiz_result_frame.grid(column=0, row=0, sticky="nsew")

        
    
        


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
