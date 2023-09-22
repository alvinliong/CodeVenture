"""
Run this file to start CodeVenture
"""

import json

from User import User
from Student import Student
from Teacher import Teacher
from StudentProgress import StudentProgress


def read_user_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global students_database
    global teachers_database
    global users_database

    students_database = []
    teachers_database = []
    path = "./data/users.json"

    try:
        file = open(path, "r", encoding="utf8")
        users = json.load(file)

        for user in users:
            user_type = user["user_type"]
            first_name = user["first_name"]
            last_name = user["last_name"]
            email = user["email"]
            phone_number = user["phone_number"]
            date_of_birth = user["date_of_birth"]
            username = user["username"]
            password = user["password"]

            if (user_type == "student"):
                student = Student(first_name,
                                  last_name,
                                  email,
                                  phone_number,
                                  date_of_birth,
                                  username,
                                  password)
                students_database.append(student)
            elif (user_type == "teacher"):
                teacher = Teacher(first_name,
                                  last_name,
                                  email,
                                  phone_number,
                                  date_of_birth,
                                  username,
                                  password)
                teachers_database.append(teacher)
            else:
                "User type undefined."

            users_database = teachers_database + students_database

        file.close()
    except FileNotFoundError:
        print("The users data file does not exist!")


def write_user_database():
    path = "./data/users.json"

    users_database = students_database + teachers_database
    users_dict = []

    # convert each object in users database to a dictionary, removing last item (logged in status)
    # and appending them to dictionary of users
    for user in users_database:
        user_dict = user.__dict__
        user_dict.popitem()
        users_dict.append(user_dict)

    # write to file
    file = open(path, "w", encoding="utf8")
    json.dump(users_dict, file, indent=4, separators=(',', ': '))


def read_student_progress_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global student_progress_database

    student_progress_database = []
    path = "./data/student_progress.json"

    try:
        file = open(path, "r", encoding="utf8")
        student_progress = json.load(file)

        for student in student_progress:
            username = student["username"]
            units_completed = student["units_completed"]
            current_unit = student["current_unit"]
            modules_completed = student["modules_completed"]
            current_module = student["current_module"]
            quizzes_completed = student["quizzes_completed"]

            student_progress = StudentProgress(username,
                                               units_completed,
                                               current_unit,
                                               modules_completed,
                                               current_module,
                                               quizzes_completed)
            student_progress_database.append(student_progress)

        file.close()
    except FileNotFoundError:
        print("The student progress data file does not exist!")


def write_student_progress_database():
    path = "./data/student_progress.json"

    student_progress_dict = []

    # convert each object in users database to a dictionary
    # and appending them to dictionary of users
    for student in student_progress_database:
        student_dict = student.__dict__
        student_progress_dict.append(student_dict)

    # write to file
    file = open(path, "w", encoding="utf8")
    json.dump(student_progress_dict, file, indent=4, separators=(',', ': '))


def clear_console():
    """
    Prints empty lines to clear the console
    :return: None
    """
    print("\n" * 5)


def main_menu():
    """
    This function prints all the menu options available to select in the main menu
    :return: None
    """
    clear_console()
    print("CodeVenture")
    print("=" * 50)
    print("\n")
    print("\t1. Register")
    print("\t2. Login")
    print("\t3. Exit")
    print("\n")


def register_menu():
    """
    This function prints the menu for register page
    :return: None
    """
    clear_console()
    print("Register")
    print("=" * 50)
    print("\n")
    print("Register a new account with CodeVenture. CTRL+C to return to main menu at anytime.")
    print("\n")


def register_main():
    """
    This function runs the main logic for the register page
    :return: None
    """
    clear_console()
    register_menu()
    while True:
        valid_details = True
        try:
            print("What account would you like to register as?")
            print("\n")
            print("\t1. Student")
            print("\t2. Teacher")
            print("\n")
            user_input = input("Enter your option: ")
            if user_input == "1":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                phone_number = input(
                    "Enter your phone number (optional, press enter to skip): ")
                date_of_birth = input(
                    "Enter your date of birth (DD/MM/YYYY): ")
                username = input("Enter your chosen username: ")
                password = input("Enter your chosen password: ")
                terms_and_conditions = input(
                    "Do you accept the terms and conditions (Y or N): ")

                if (terms_and_conditions.upper() != "Y"):
                    valid_details = "You must accept the terms and conditions to register!"

                for student in students_database:
                    if (student.get_username() == username or student.get_email() == email):
                        valid_details = "Username or email already exists"
                if (valid_details == True):
                    new_user = Student(
                        first_name, last_name, email, phone_number, date_of_birth, username, password)
                    students_database.append(new_user)

                    write_user_database()
                    read_user_database()

                    new_student_progress = StudentProgress(
                        username, [], None, [], None, [])
                    student_progress_database.append(new_student_progress)

                    write_student_progress_database()
                    read_student_progress_database()

                    print("User registered!")
                    break
                else:
                    print(valid_details)

            elif user_input == "2":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                phone_number = input(
                    "Enter your phone number (optional, press enter to skip): ")
                date_of_birth = input(
                    "Enter your date of birth (DD/MM/YYYY): ")
                username = input("Enter your chosen username: ")
                password = input("Enter your chosen password: ")
                terms_and_conditions = input(
                    "Do you accept the terms and conditions (Y or N): ")

                if (terms_and_conditions.upper() != "Y"):
                    valid_details = "You must accept the terms and conditions to register!"

                for student in students_database:
                    if (student.get_username() == username or student.get_email() == email):
                        valid_details = "Username or email already exists"
                if (valid_details == True):
                    new_user = Teacher(
                        first_name, last_name, email, phone_number, date_of_birth, username, password)
                    students_database.append(new_user)
                    write_user_database()
                    read_user_database()
                    print("User registered!")
                    break
                else:
                    print("\n")
                    print(valid_details)
                    print("\n")
            else:
                "Please enter a valid option."
        except KeyboardInterrupt:
            clear_console()
            print("Registration cancelled.")
            break


def login_menu():
    """
    This function prints the menu for login page
    :return: None
    """
    clear_console()
    print("Login")
    print("=" * 50)
    print("\n")
    print("Login to your CodeVenture account. CTRL+C to return to main menu at anytime.")
    print("\n")


def login_main():
    """
    This function runs the main logic for the login page
    :return: None
    """
    global current_user
    global current_student_progress

    current_user = None
    current_student_progress = None

    clear_console()
    login_menu()
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for student in students_database:
                if (student.get_username() == username and student.get_password() == password):
                    student.set_logged_in()
                    current_user = student
                    for progress in student_progress_database:
                        if progress.get_username() == username:
                            current_student_progress = progress
                    if current_student_progress == None:
                        print("Student progress data was not found! Uh oh!")

            for teacher in teachers_database:
                if (teacher.get_username() == username and teacher.get_password() == password):
                    teacher.set_logged_in()
                    current_user = teacher

            current_user.set_logged_in()

            if (current_user != None):
                clear_console()
                print("Logged in!")
                if (current_user.get_user_type() == "student"):
                    student_main()
                elif (current_user.get_user_type() == "teacher"):
                    teacher_main()
                break

            else:
                print("Username or password is incorrect!")

        except KeyboardInterrupt:
            clear_console()
            print("Login cancelled.")
            break


def student_main_menu():
    """
    This function prints the menu for student main menu page
    :return: None
    """
    clear_console()
    print("CodeVenture - Student")
    print("=" * 50)
    print("\n")
    print("Welcome, " + current_user.get_first_name() +
          " " + current_user.get_last_name())
    print("User type: " + current_user.get_user_type())
    print("Username: " + current_user.get_username())
    print("\n")
    print("\t1. Start module")
    print("\t2. Unit selection page")
    print("\t3. Attempt quiz")
    print("\t4. View my progress")
    print("\t5. Settings")
    print("\t6. Q&A Forum")
    print("\t7. Logout")
    print("\n")


def student_main():
    """
    This function runs the main logic for the student main menu
    :return: None
    """

    clear_console()
    while True:
        # Print the menu options
        student_main_menu()
        menu_input = input("Please enter a menu option: ")

        if menu_input == "1":
            pass
        elif menu_input == "2":
            pass
        elif menu_input == "3":
            pass
        elif menu_input == "4":
            pass
        elif menu_input == "5":
            pass
        elif menu_input == "6":
            pass
        elif menu_input == "7":
            current_user.set_logged_out()
            print("Logging out!")
            break
        else:
            # Invalid input option
            print("You have not selected a valid menu option!",
                  "Please try again.")


def teacher_main_menu():
    """
    This function prints the menu for teacher main menu page
    :return: None
    """
    clear_console()
    print("CodeVenture - Teacher")
    print("=" * 50)
    print("\n")
    print("Welcome, " + current_user.get_first_name() +
          " " + current_user.get_last_name())
    print("User type: " + current_user.get_user_type())
    print("Username: " + current_user.get_username())
    print("\n")
    print("\t1. View my students")
    print("\t2. Settings")
    print("\t3. Q&A Forum")
    print("\t4. Logout")
    print("\n")


def teacher_main():
    """
    This function runs the main logic for the teacher main menu
    :return: None
    """

    clear_console()
    while True:
        # Print the menu options
        teacher_main_menu()
        menu_input = input("Please enter a menu option: ")

        if menu_input == "1":
            pass
        elif menu_input == "2":
            pass
        elif menu_input == "3":
            pass
        elif menu_input == "4":
            current_user.set_logged_out()
            print("Logging out!")
            break
        else:
            # Invalid input option
            print("You have not selected a valid menu option!",
                  "Please try again.")


def main():
    """
    This function handles all program logic related to the main menu.
    :return: None
    """

    # populate databases
    read_user_database()
    read_student_progress_database()

    while True:
        main_menu()
        menu_input = input("Please enter a menu option: ")

        if menu_input == "1":
            register_main()
        elif menu_input == "2":
            login_main()
        elif menu_input == "3":
            print("Exiting CodeVenture")
            break
        else:
            # Invalid input option
            print("You have not selected a valid menu option!",
                  "Please try again.")


if __name__ == "__main__":
    main()      # Execute the main() function if this file is run
