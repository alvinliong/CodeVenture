"""
FIT1056 Problem Solving Tasks for Week 11
Student name: Sithika Mannakkara
Student ID: 33891613
Campus: Clayton
Group: CL_FRI_1000_G13
"""


# Third party imports
import tkinter as tk

# Local application imports
from authenticator_GUI import Authenticator
from patientframe_GUI import PatientFrame
from user_GUI import User


class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master

        # Logo image for the login page
        login_canvas = tk.Canvas(master=self, width=256, height=256)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Image obtained from:
        # https://miro.medium.com/v2/resize:fit:1200/1*m0H6-tUbW6grMlezlb52yw.png
        image_path = "GUI\images\python-icon.png"
        self.login_logo = tk.PhotoImage(file=image_path)
        login_canvas.create_image(0,0, 
                                  anchor=tk.NW,
                                  image=self.login_logo)

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Welcome to\n"
                                    "Code Venture",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry for username
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to password
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                  show="●")
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        # Button to login
        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Variable and label to inform user of login outcome
        self.login_text = tk.StringVar()
        login_message = tk.Label(master=self, textvariable=self.login_text)
        # Alternatively, you may use Message widget,
        # but width must be wide enough
        # login_message = tk.Message(master=self,
        #                            textvariable=self.login_text,
        #                            width=150)
        login_message.grid(row=5, columnspan=2, padx=10, pady=10)

    def authenticate_login(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the login button is clicked.
        :return: None
        """
        authenticator = Authenticator()
        auth_res = authenticator.authenticate(self.username.get(),
                                              self.password.get())

        if isinstance(auth_res, User):

            # TODO: Clear entries upon successful login
            self.username.set("")  # Clear the username entry
            self.password.set("")  # Clear the password entry

            if auth_res.get_role() == "PA":  # patient login

                # Remove login page from display
                self.place_forget()

                # Create and display the Patient login frame
                patient_frame = PatientFrame(self.master, self, auth_res)
                patient_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif auth_res.get_role() in ["AD", "RE"]:
                self.login_text.set("Login successfully!")
        else:
            self.login_text.set("Failed to login")


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
