"""
Home Screen class for Code Venture
"""
from user import User
class HomePage:
    def __init__(self, user):
        self.user = user

    def display_menu(self):
        while True:
            print("CodeVenture")
            print("1. Create an account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.user.create_account()
            elif choice == '2':
                self.user.login()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    user_manager = User()
    homepage = HomePage(user_manager)
    homepage.display_menu()
