"""
File: ForgotPasswordFrame.py
Description: This file will send a user their forgotten details # currently not functioning
Author: CodeVenture Team G13 
"""

from email.message import EmailMessage
import ssl
import smtplib

# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *
from User import User

class ForgotPasswordFrame(tk.Frame):
    """
    The class definition for the ForgotPasswordFrame class.
    """

    def __init__(self, master, login_frame):
        """
        Constructor for the RegisterFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.login_frame = login_frame

        # configure rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        for column_count in range(2):
            self.columnconfigure(column_count, weight=1)

        # Label containing the welcome heading
        register_title = ttk.Label(master=self,
                               text="Code Venture | Forgot Password",
                               font=("Arial Bold", 25))
        register_title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="S")

        # Label to ask user for email
        email_label = ttk.Label(master=self, text="Email:")
        email_label.grid(row=1, column=0, sticky="SE", padx=10, pady=10)

        # Variable and entry for email
        self.email = tk.StringVar()
        self.email_entry = ttk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=1, column=1, sticky="SW", padx=10, pady=10)

        # Button to send email
        send_email_button = ttk.Button(master=self, text="Send email",
                                 command=self.send_email)
        send_email_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="N")

        # Variable and label to inform user of login outcome
        self.prompt_text = tk.StringVar()
        prompt_message = ttk.Label(master=self, textvariable=self.prompt_text)
        prompt_message.grid(row=4, columnspan=2, padx=10, pady=10)

    def send_email(self):
        from LoginFrame import LoginFrame
        """
        This function runs the main logic for forgot password
        :return: None
        """
        email = self.email.get()
        current_user = None

        for user in users_database:
            if user.get_email() == email:
                current_user = user

        if (current_user == None):
            self.prompt_text.set("Email is not in the CodeVenture system!")
        else:
            email_sender = 'codeventure44@gmail.com'
            password_sender = 'wqij bryl dmjm bzob'
            email_receiver = str(email)

            subject = 'CodeVenture Details'
            body = f'''
            Hello,
            Here are your account details. 
            Your username is {current_user.get_username()}
            Your password is {current_user.get_password()}
            Please delete this email once you have your details.
            Kind Regards,
            CodeVenture Team
            '''

            mail = EmailMessage()
            mail['From'] = email_sender
            mail['To'] = email_receiver
            mail['subject'] = subject
            mail.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, password_sender)
                smtp.sendmail(email_sender, email_receiver, mail.as_string())

            self.destroy()
            LoginFrame = LoginFrame(self.master, "An account recovery email has been sent to the provided email")
            LoginFrame.grid(column=0, row=0, sticky="nsew")


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
