"""

"""

from User import User


class Teacher(User):

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 phone_number,
                 username,
                 password,
                 date_of_birth):
        """
        Constructor for the Student class.
        """
        super().__init__(first_name, last_name, email, phone_number, username, password, date_of_birth,
                         user_type="teacher")

    def __str__(self):
        return self.username


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week08_*.py,
    # then marks will be deducted.
    pass
