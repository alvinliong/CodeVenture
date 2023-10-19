"""
FIT1056 Problem Solving Tasks for Week 11
Student name: Sithika Mannakkara
Student ID: 33891613
Campus: Clayton
Group: CL_FRI_1000_G13
"""
# Third party imports
import tkinter as tk

from class_quiz_GUI import Quizframe


class PatientFrame(tk.Frame):
    """
    The class definition for the PatientFrame class.
    """

    def __init__(self, master, login_frame, user_obj):
        """
        The constructor for the PatientFrame class
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user_obj = user_obj

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        # TODO: Display a welcome message.
        # Display a welcome message.
        welcome_label = tk.Label(self, text=f"Welcome back, {user_obj.get_last_name()}!")
        welcome_label.grid(row=0, column=0, padx=10, pady=10)

        # The view profile button
        view_profile_button = tk.Button(self, text="View profile")
        view_profile_button.grid(row=1, column=0, padx=10, pady=10)

        # The calculate BMI button
        # TODO: Include event handling
        calculate_bmi_button = tk.Button(self,
                                         text="Calculate body mass index "
                                              "(BMI)",
                                         command=self.show_bmi_frame)
        calculate_bmi_button.grid(row=2, column=0, padx=10, pady=10)

        # The view appointments button
        view_appointments_button = tk.Button(self, text="View appointments")
        view_appointments_button.grid(row=3, column=0, padx=10, pady=10)


        # The logout button
        # TODO: Include event handling
        logout_button = tk.Button(self, text="Log out", command=self.logout)
        logout_button.grid(row=4, column=0, padx=10, pady=10)

    def show_bmi_frame(self):
        """
        Event handler to show bmi frame
        DO NOT MODIFY THIS.
        """
        self.place_forget()
        bmi_frame = Quizframe(self.master, self)
        bmi_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
