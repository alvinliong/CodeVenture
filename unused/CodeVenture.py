
#C:\Users\sithi\OneDrive\Documents\GitHub\CodeVenture
# Enter "pip install art" in terminal first
import json
from art import *
from email.message import EmailMessage
import ssl
import smtplib
class User:
    def __init__(self):
        self.users_db = "users.txt"
        self.logged_in_user = None
        self.users_data = self.load_users_data()

    def load_users_data(self):
        try:
            with open(self.users_db, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users_data(self):
        with open(self.users_db, "w") as file:
            json.dump(self.users_data, file)

    def create_account(self, full_name, date_of_birth, email, username, password):
        if username in self.users_data or email in self.users_data:
            print("Username or email already registered. Please choose a different one.")
            return False

        terms_accepted = input("Do you accept the terms and conditions? (yes/no): ").lower()
        if terms_accepted != "yes":
            print("You must accept the terms and conditions to register.")
            return False

        user_info = {
            "full_name": full_name,
            "date_of_birth": date_of_birth,
            "email": email,
            "username": username,
            "password": password
        }

        self.users_data[username] = user_info
        self.save_users_data()
        print("Account successfully created.")
        return True

    def login(self, username_or_email, password):
        if (username_or_email=='q') or (password=='q'):
            print('Redirecting to main menu.')
            return False
        
        user_info = self.users_data.get(username_or_email)

        if user_info and user_info["password"] == password:
            self.logged_in_user = username_or_email
            print("Login successful.")
            return True
        else:
            print("Incorrect username/email or password.")
            return False

    def logout(self):
        self.logged_in_user = None

    def forgotPassword(self):
        email_sender = 'codeventure44@gmail.com'
        password_sender = 'wqij bryl dmjm bzob'
        email_receiver = input('Please enter email: ')
        email_receiver = str(email_receiver)

        subject = 'CodeVenture!'
        body = f'''
        Your username is ___
        Your password is ___ 
        '''

        mail = EmailMessage()
        mail['From'] = email_sender
        mail['To'] = email_receiver
        mail['subject'] = subject
        mail.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, password_sender)
            smtp.sendmail(email_sender, email_receiver, mail.as_string())        

class Homepage(User):
    def __init__(self, user):
        self.user = user

    def display_homepage(self):
        while True:
            Art = text2art("Code Venture",font="bulbhead") # correct --> Art=text2art("test",font="block")
            print(Art)
            print("1. Create Account")
            print("2. Login")
            print("3. Forgot details")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.forgotPassword()
            elif choice == "4":
                quit(0)
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        full_name = input("Enter your full name: ")
        date_of_birth = input("Enter your date of birth: ")
        email = input("Enter your email address: ")
        username = input("Choose a username: ")
        password = input("Choose a password: ")

        if self.user.create_account(full_name, date_of_birth, email, username, password):
            self.login()

    def login(self):
        username_or_email = input("Enter your username or email: ")
        password = input("Enter your password: ")

        if self.user.login(username_or_email, password):
            quiz_and_test = QuizAndTest(self.user)
            quiz_and_test.display_quiz_menu()

class QuizAndTest(User):
    def __init__(self, user):
        self.user = user
        self.questions = [
            {
                "question": "What is an integer?",
                "options": ["a. integers store words", "b. integers are whole numbers", "c. integers contain decimal places","a. integers are not in python"],
                "answer": "b"
            },
            {
                "question": "Which of the following is a data type in Python?",
                "options": ["a. Car", "b. List", "c. House", "d. Tree"],
                "answer": "b"
            },
            {
                "question": "What is the result of 3 + 5?",
                "options": ["a. 7", "b. 8", "c. 9", "d. 10"],
                "answer": "b"
            },
            {
                "question": "What does the 'print' function do in Python?",
                "options": ["a. Add two numbers", "b. Open a file", "c. Create a folder","d. Display text on the screen"],
                "answer": "d"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["a. def", "b. function", "c. define", "d. func"],
                "answer": "a"
            }
        ]
    def display_quiz_menu(self):       
        if not self.user.logged_in_user:
            print("You must log in to access this class.")
            return

        while True:
            print("\nQuiz and Test Menu:")
            print("1. Take a Quiz")
            print("2. Take a Test")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.take_quiz()
            elif choice == "2":
                self.take_test()
            elif choice == "3":
                self.user.logout()
                break
            else:
                print("Invalid choice. Please try again.")

    def take_quiz(self):
        score = 0
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            print("Options:")
            for option in question['options']:
                print(f" {option}")

            try:
                user_answer = input("Your answer: ").strip()
                user_answer = user_answer.lower()
            except ValueError:
                user_answer = 'fail'

            if user_answer == question['answer']:
                score += 1

        grade = (score / total_questions) * 100
        print(f"\nQuiz Completed!\nYou got {score} out of {total_questions} questions correct.")
        print(f"Your grade: {grade}%")

    def take_test(self):
        print("Taking a test...")  # Add test logic here

    def ads_for_u(self):
        pass




if __name__ == "__main__":
    user_manager = User()
    homepage = Homepage(user_manager)
    homepage.display_homepage()

