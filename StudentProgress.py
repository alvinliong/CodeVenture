"""
File: StudentProgress.py
Description: This file is StudentProgress Class
Author: CodeVenture Team G13 
"""

class StudentProgress:
    """
    This is the class definition for the Student Progress class.
    """

    def __init__(self, username, units_completed, current_unit, modules_completed):
        """
        Constructor method for the Student Progress class
        """
        self.username = username
        self.units_completed = units_completed
        self.current_unit = current_unit
        self.modules_completed = modules_completed

    def get_username(self):
        return self.username

    def update_units_completed(self, unit):
        self.units_completed.append(unit)

    def get_units_completed(self):
        return self.units_completed

    def set_current_unit(self, unit):
        self.current_unit = unit

    def get_current_unit(self):
        return self.current_unit

    def update_modules_completed(self, module):
        self.modules_completed.append(module)

    def get_modules_completed(self):
        return self.modules_completed
    
    def add_modules_completed(self, module_code):
        if(module_code not in self.modules_completed):
            self.modules_completed.append(module_code)

    def reset_modules_completed(self):
        self.modules_completed = []

    def set_current_module(self, module):
        self.current_module = module

    def get_current_module(self):
        return self.current_module


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week08_receptionist.py,
    # then marks will be deducted.
    pass
