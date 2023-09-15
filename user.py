"""
User class for Code Venture
"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, entered_password):
        if entered_password == self.password:
            self.logged_in = True
            print(f"Welcome, {self.username}! You are now logged in.")
        else:
            print("Incorrect password. Login failed.")

    def logout(self):
        self.logged_in = False
        print(f"Goodbye, {self.username}! You are now logged out.")

    def is_logged_in(self):
        return self.logged_in

# Example usage:
if __name__ == "__main__":
    user1 = User("user123", "password123")

    user1.login("password123")  # Successful login
    print(f"Is user1 logged in? {user1.is_logged_in()}")  # Should return True

    user1.logout()  # Logging out

    print(f"Is user1 logged in? {user1.is_logged_in()}")  # Should return False
