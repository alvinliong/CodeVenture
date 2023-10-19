"""
FIT1056 Problem Solving Tasks for Week 11
Student name: Sithika Mannakkara
Student ID: 33891613
Campus: Clayton
Group: CL_FRI_1000_G13
"""

import tkinter as tk

# TODO: Complete the implementation in this file

class Quizframe(tk.Frame):
    def __init__(self, master, parent_frame):
        """
        Constructor for the Quizframe class.
        :param master: Tk object; the main window that the frame is contained.
        :param parent_frame: Parent frame (e.g., PatientFrame).
        :param user: User object representing the logged-in user.
        """
        super().__init__(master=master)
        self.master = master
        self.parent_frame = parent_frame
        #self.user = user

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Label for instructions
        instructions_label = tk.Label(self, text="Please enter your weight (in kg) and height (in cm):")
        instructions_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Entry fields for weight and height
        weight_label = tk.Label(self, text="Weight (kg):")
        weight_label.grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        height_label = tk.Label(self, text="Height (cm):")
        height_label.grid(row=2, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to calculate BMI
        calculate_button = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi)
        calculate_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # Message to display BMI result
        self.bmi_result = tk.StringVar()
        bmi_result_label = tk.Label(self, textvariable=self.bmi_result)
        bmi_result_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        # Button to return to the patient's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_main_menu)
        return_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height from cm to m
            bmi = weight / (height ** 2)
            self.bmi_result.set(f"Your BMI: {bmi:.2f}")
        except ValueError:
            self.bmi_result.set(f"Invalid Input!")    
        

    def return_to_main_menu(self):
        # TODO: Implement the logic to return to the patient's main menu
        # Remove login page from display
        self.place_forget()

        # Show the PatientFrame again
        self.parent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
