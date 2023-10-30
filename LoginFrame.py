"""
File: LoginFrame.py
Description: This file is the login frame
Author: CodeVenture Team G13 
"""
# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *
from StudentMainFrame import StudentMainFrame
from RegisterFrame import RegisterFrame
from ForgotPasswordFrame import ForgotPasswordFrame

class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master, login_text):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master

        # configure rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
            

        for column_count in range(2):
            self.columnconfigure(column_count, weight=1)

        # Label containing the welcome heading
        login_title = ttk.Label(master=self,
                               text="Code Venture",
                               font=("Arial Bold", 25))
        login_title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="S")

        # Label to ask user for Username
        username_label = ttk.Label(master=self, text="Username:")
        username_label.grid(row=1, column=0, sticky="SE", padx=10, pady=10)

        # Variable and entry for username
        self.username = tk.StringVar()
        self.username_entry = ttk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=1, column=1, sticky="SW", padx=10, pady=10)

        # Label to ask user for Password
        password_label = ttk.Label(master=self, text="Password:")
        password_label.grid(row=2, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to password
        self.password = tk.StringVar()
        self.password_entry = ttk.Entry(master=self, textvariable=self.password,
                                  show="●")
        self.password_entry.grid(row=2, column=1, sticky="NW", padx=10, pady=10)

        # Button to login
        login_button = ttk.Button(master=self, text="Login",
                                 command=self.Login)
        login_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="S")

        # Button to register
        register_button = ttk.Button(master=self, text="Register a new account",
                                 command=self.Register)
        register_button.grid(row=4, columnspan=2, padx=10, pady=10, sticky="N")

        # Button to forgot password
        forgot_password_button = ttk.Button(master=self, text="Forgot password?",
                                 command=self.ForgotPassword, state="disabled")
        forgot_password_button.grid(row=5, columnspan=2, padx=10, pady=10, sticky="N")

        # Variable and label to inform user of login outcome
        self.login_text = tk.StringVar()
        self.login_text.set(login_text)
        login_message = ttk.Label(master=self, textvariable=self.login_text)
        login_message.grid(row=6, columnspan=2, padx=10, pady=10)

    def Login(self):
        """
        This function runs the main logic for login
        :return: None
        """
        global current_user
        global current_student_progress

        current_user = None
        current_student_progress = None

        username = self.username.get()
        password = self.password.get()

        for student in students_database:
            if (student.get_username() == username and student.get_password() == password):
                current_user = student
                for progress in student_progress_database:
                    if progress.get_username() == username:
                        current_student_progress = progress
                if current_student_progress == None:
                    print("Student progress data was not found! Uh oh!")

        for teacher in teachers_database:
            if (teacher.get_username() == username and teacher.get_password() == password):
                current_user = teacher

        if (current_user != None):
            # Hide the login frame
            self.username.set("")
            self.password.set("")
            self.destroy()
            if(current_user.get_user_type() == "student"):
                # Create and display the Student login frame
                student_main_frame = StudentMainFrame(self.master, self, current_user, current_student_progress)
                student_main_frame.grid(column=0, row=0, sticky="nsew")
            elif (current_user.get_user_type() == "teacher"):
                print("teacher logged in")
        else:
            self.login_text.set("Account details are incorrect!")

    def Register(self):
        """
        This function runs the main logic for register page
        :return: None
        """
        self.grid_forget()
        register_frame = RegisterFrame(self.master, self)
        register_frame.grid(column=0, row=0, sticky="nsew")

    def ForgotPassword(self):
        """
        This function runs the main logic for forgot password page
        :return: None
        """
        self.grid_forget()
        forgot_password_frame = ForgotPasswordFrame(self.master, self)
        forgot_password_frame.grid(column=0, row=0, sticky="nsew")

if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
