"""
User class for Code Venture
"""
class User:
    def __init__(self):
        self.users_database = []
    
    def create_account(self):
        full_name = input("Enter your full name: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        email = input("Enter your email address: ")

        # Check if the email has already been registered
        if self.is_email_registered(email):
            print("Email address is already registered. Please use a different one.")
            return

        # Display terms and conditions
        print("Terms and conditions:")
        print("1. You agree to abide by all the rules and regulations of CodeVenture.")
        print("2. ... (add more terms and conditions here)")
        accept_terms = input("Do you accept the terms and conditions? (yes/no): ")

        if accept_terms.lower() == 'yes':
            # Create a new user account
            new_user = {'full_name': full_name, 'dob': dob, 'email': email}
            self.users_database.append(new_user)
            print("Account created successfully!")
        else:
            print("Account creation aborted. You must accept the terms and conditions.")

    def is_email_registered(self, email):
        for user in self.users_database:
            if user['email'] == email:
                return True
        return False

    def login(self):
        username_or_email = input("Enter your username or email: ")
        password = input("Enter your password: ")

        # Check if the credentials match an existing account
        if self.check_credentials(username_or_email, password):
            print("Login successful. Welcome back, {}!".format(username_or_email))
        else:
            print("Incorrect username/email or password. Please try again.")

    def check_credentials(self, username_or_email, password):
        for user in self.users_database:
            if (user['email'] == username_or_email or user['username'] == username_or_email) and user['password'] == password:
                return True
        return False


if __name__ == "__main__":
    pass

    






