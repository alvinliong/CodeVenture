"""

"""
# Third party imports
import tkinter as tk

# Local application imports
from Database import *
from PyInfoFrame import PyInfoFrame

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

        # Label containing the welcome heading
        main_title = tk.Label(master=self,
                               text=f"Welcome back, {current_user.get_first_name()}!",
                               font=("Arial Bold", 25))
        main_title.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # The view profile button
        view_profile_button = tk.Button(self, text="View profile")
        view_profile_button.grid(row=1, column=0, padx=10, pady=10)

        # The calculate BMI button
        # TODO: Include event handling
        calculate_bmi_button = tk.Button(self,
                                         text="Python Information",
                                         command=self.show_py_info)
        calculate_bmi_button.grid(row=2, column=0, padx=10, pady=10)

        # The view appointments button
        view_appointments_button = tk.Button(self, text="View appointments")
        view_appointments_button.grid(row=3, column=0, padx=10, pady=10)


        # The logout button
        # TODO: Include event handling
        logout_button = tk.Button(self, text="Log out", command=self.logout)
        logout_button.grid(row=4, column=0, padx=10, pady=10)

    def show_py_info(self):
        """
        Event handler to show py info frame
        """
        self.place_forget()
        py_info_frame = PyInfoFrame(self.master)
        py_info_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def logout(self):
        """
        Event handler to logout
        DO NOT MODIFY THIS.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
