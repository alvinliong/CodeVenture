"""

"""


class Unit():

    def __init__(self,
                 unit_title,
                 unit_code,
                 modules):
        """
        Constructor for the Unit class.
        """
        self.unit_title = unit_title
        self.unit_code = unit_code
        self.modules = modules

    
    def get_unit_title(self):
        return self.unit_title

    def set_unit_title(self, unit_title):
        self.unit_title = unit_title

    def get_unit_code(self):
        return self.unit_code

    def set_unit_code(self, unit_code):
        self.unit_code = unit_code

    def get_modules(self):
        return self.modules

    def set_modules(self, modules):
        self.modules = modules


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week08_*.py,
    # then marks will be deducted.
    pass
