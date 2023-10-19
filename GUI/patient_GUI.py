"""
FIT1056 Problem Solving Tasks for Week 11
"""

from user_GUI import User


class Patient(User):
    """
    Class definition for the Patient class,
    which inherits from the User class.
    """

    def __init__(self, username, password, first_name, last_name,
                 is_active=True):
        super().__init__(username=username,
                         password=password,
                         role="PA",
                         is_active=is_active)
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        """
        Getter for the first_name attribute.
        :return: str
        """
        return self.__first_name

    def get_last_name(self):
        """
        Getter for the last_name attribute.
        :return: str
        """
        return self.__last_name


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass