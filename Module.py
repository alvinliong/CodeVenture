"""
File: Module.py
Description: This file is the Module class
Author: CodeVenture Team G13 
"""

class Module():

    def __init__(self,
                 module_title,
                 module_code,
                 content):
        """
        Constructor for the Module class.
        """
        self.module_title = module_title
        self.module_code = module_code
        self.content = content

    def get_module_title(self):
        return self.module_title

    def set_module_title(self, module_title):
        self.module_title = module_title

    def get_module_code(self):
        return self.module_code

    def set_module_code(self, module_code):
        self.module_code = module_code

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week08_*.py,
    # then marks will be deducted.
    pass
