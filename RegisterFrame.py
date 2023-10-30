"""
File: RegisterFra,e.py
Description: This file is the GUI for the RegisterFrame
Author: CodeVenture Team G13 
"""
# Third party imports
import tkinter as tk
from tkinter import ttk

# Local application imports
from Database import *
from User import User

class RegisterFrame(tk.Frame):
    """
    The class definition for the RegisterFrame class.
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
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        
        for column_count in range(2):
            self.columnconfigure(column_count, weight=1)

        # Label containing the welcome heading
        register_title = ttk.Label(master=self,
                               text="Code Venture | Register",
                               font=("Arial Bold", 25))
        register_title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="S")

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

        # Label to ask user for first name
        first_name_label = ttk.Label(master=self, text="First name:")
        first_name_label.grid(row=3, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to first name
        self.first_name = tk.StringVar()
        self.first_name_entry = ttk.Entry(master=self, textvariable=self.first_name)
        self.first_name_entry.grid(row=3, column=1, sticky="NW", padx=10, pady=10)

        # Label to ask user for last name
        last_name_label = ttk.Label(master=self, text="Last name:")
        last_name_label.grid(row=4, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to last name
        self.last_name = tk.StringVar()
        self.last_name_entry = ttk.Entry(master=self, textvariable=self.last_name)
        self.last_name_entry.grid(row=4, column=1, sticky="NW", padx=10, pady=10)

        # Label to ask user for email
        email_label = ttk.Label(master=self, text="Email:")
        email_label.grid(row=5, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to email
        self.email = tk.StringVar()
        self.email_entry = ttk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=5, column=1, sticky="NW", padx=10, pady=10)

        # Label to ask user for phone_number
        phone_number = ttk.Label(master=self, text="Phone number:")
        phone_number.grid(row=6, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to phone_number
        self.phone_number = tk.StringVar()
        self.phone_number_entry = ttk.Entry(master=self, textvariable=self.phone_number)
        self.phone_number_entry.grid(row=6, column=1, sticky="NW", padx=10, pady=10)

        # Label to ask user for date_of_birth
        date_of_birth = ttk.Label(master=self, text="Date of birth:")
        date_of_birth.grid(row=7, column=0, sticky="NE", padx=10, pady=10)

        # Variable and entry to date_of_birth
        self.date_of_birth = tk.StringVar()
        self.date_of_birth_entry = ttk.Entry(master=self, textvariable=self.date_of_birth)
        self.date_of_birth_entry.grid(row=7, column=1, sticky="NW", padx=10, pady=10)

        # Button to login
        login_button = ttk.Button(master=self, text="Register",
                                 command=self.Register)
        login_button.grid(row=8, columnspan=2, padx=10, pady=10, sticky="N")

        # Variable and label to inform user of login outcome
        self.register_text = tk.StringVar()
        register_message = ttk.Label(master=self, textvariable=self.register_text)
        register_message.grid(row=9, columnspan=2, padx=10, pady=10)

    def is_DOB_valid(self, date_of_birth):
        if not(len(date_of_birth)==10):
            return False
        if (date_of_birth[2]=='/' and date_of_birth[5] == '/'):
            DD = date_of_birth[0:2]
            MM = date_of_birth[3:5]
            YYYY = date_of_birth[6:10]
            try:
                YYYY = int(YYYY)
                if not(1800<YYYY<9999):
                    return False
            except ValueError:
                return False
            valid_days = []
            if MM in ['01','03','05','07','08','10','12']:
                # 31 day month
                for day in range(1,32):
                    valid_days.append(str(day).zfill(2))
                if not(DD in valid_days):
                    return False
            elif MM in ['04','06','09','11']:
                # 30 day month
                for day in range(1,31):
                    valid_days.append(str(day).zfill(2))
                if not(DD in valid_days):
                    return False
            elif MM == '02':
                if YYYY%4 == 0:
                    # Leap year
                    for day in range(1, 30):
                        valid_days.append(str(day).zfill(2))
                    if not(DD in valid_days):
                        return False
                else:
                    # not leap year
                    for day in range(1, 29):
                        valid_days.append(str(day).zfill(2))
                    if not(DD in valid_days):
                        return False
            else:
                return False
        else:
            return False
        return True

    def is_email_valid(self, email):
        existing_emails = []
        for user in users_database:
            existing_emails.append(user.get_email())

        if email in existing_emails:
            return "Email already exists!"
        else:
            if '@' in email and '.' in email:
                return True
            else:
                return "Email is not valid! Must include an @ and ."

    def is_phone_num_valid(self, phone_number):
        if phone_number is None:
            return False
        else:
            try:
                int(phone_number)
                return True
            except ValueError:
                return False
        
    def is_username_valid(self, username):
        existing_usernames = []
        for user in users_database:
            existing_usernames.append(user.get_username())
    
        if username in existing_usernames:
            return False
        else:
            return True

    def Register(self):
        from LoginFrame import LoginFrame
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
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        phone_number = self.phone_number.get()
        date_of_birth = self.date_of_birth.get()

        # validate inputs
        validity = True

        if (self.is_DOB_valid(date_of_birth) != True):
            validity = "Date of birth is invalid. Must be in DD/MM/YYYY format"
        if (self.is_email_valid(email) != True):
            validity = self.is_email_valid(email)
        if (self.is_phone_num_valid(phone_number) != True):
            validity = "Phone number is invalid. Must be integers only."
        if (self.is_username_valid(username) != True):
            validity = "Username already exists!"

        if (validity == True):
            # create new user object
            new_user = User(first_name, last_name, email, phone_number, date_of_birth, username, password, user_type="student")
            students_database.append(new_user)
            users_database = students_database + teachers_database

            # create student progress object
            new_student_progress = StudentProgress(username, [], None, [])
            student_progress_database.append(new_student_progress)
            write_all_databases()

            self.destroy()
            LoginFrame = LoginFrame(self.master, "Registration successful")
            LoginFrame.grid(column=0, row=0, sticky="nsew")

        else:
            self.register_text.set(validity)


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
