"""
FIT1056 Problem Solving Tasks for Week 11
"""


class User:
    """
    Class definition for the User class
    """

    def __init__(self, username, password, role=None, is_active=True):
        """
        Constructor for the User class
        :param username: str
        :param password: str
        :param role: str
        :param is_active: bool
        """
        self.__username = username
        self.__password = password
        self.__role = role
        self.__is_active = is_active

    def get_username(self):
        """
        Getter for the username attribute.
        :return: str
        """
        return self.__username

    def get_password(self):
        """
        Getter for the password attribute.
        :return: str
        """
        return self.__password

    def get_role(self):
        """
        Getter for the role attribute.
        :return: str
        """
        return self.__role

    def get_is_active(self):
        """
        Getter for the is_active attribute.
        :return: bool
        """
        return self.__is_active


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
