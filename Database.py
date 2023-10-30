"""
File: Database.py
Description: This file will read and write to the users database (file) and student
progress database (file) and creates objects
Author: CodeVenture Team G13 
"""

import json
from Student import Student
from Teacher import Teacher
from StudentProgress import StudentProgress
from Unit import Unit
from Module import Module
from QuizQuestion import QuizQuestion

def read_all_databases():
    """
    Runs all read and write functions for the databases. Essentially updates the files
    to match the database changes from the code
    :return: None
    """
    read_user_database()
    read_modules_database()
    read_units_database()
    read_student_progress_database()
    read_quiz_database()

def write_all_databases():
    """
    Runs all read and write functions for the databases. Essentially updates the files
    to match the database changes from the code
    :return: None
    """
    
    write_student_progress_database()
    write_user_database()


def read_user_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global students_database
    global teachers_database
    global users_database
    global student_progress_database

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
        print("Student data loaded.")
    except FileNotFoundError:
        print("The users data file does not exist!")


def write_user_database():
    global students_database
    global teachers_database
    global users_database
    global student_progress_database

    path = "./data/users.json"

    users_database = students_database + teachers_database
    print(users_database)
    users_dict = []

    # convert each object in users database to a dictionary, removing last item (logged in status)
    # and appending them to dictionary of users
    for user in users_database:
        users_dict.append(user.__dict__)

    # write to file
    file = open(path, "w", encoding="utf8")
    json.dump(users_dict, file, indent=4, separators=(',', ': '))


def read_student_progress_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global students_database
    global teachers_database
    global users_database
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

            student_progress = StudentProgress(username,
                                               units_completed,
                                               current_unit,
                                               modules_completed)
            student_progress_database.append(student_progress)

        file.close()
        print("Student progress data loaded.")
    except FileNotFoundError:
        print("The student progress data file does not exist!")


def write_student_progress_database():
    global students_database
    global teachers_database
    global users_database
    global student_progress_database

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

def read_units_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global units_database

    units_database = []
    path = "./data/units.json"

    try:
        file = open(path, "r", encoding="utf8")
        units = json.load(file)

        for unit in units:
            unit_title = unit["unit_title"]
            unit_code = unit["unit_code"]
            modules = unit["modules"]
            

            
            unit = Unit(unit_title,
                                unit_code,
                                modules)
            units_database.append(unit)

        file.close()
        print("Units data loaded.")
    except FileNotFoundError:
        print("The units data file does not exist!")

def read_modules_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global modules_database

    modules_database = []
    path = "./data/modules.json"

    try:
        file = open(path, "r", encoding="utf8")
        modules = json.load(file)

        for module in modules:
            module_title = module["module_title"]
            module_code = module["module_code"]
            content = module["content"]

            module = Module(module_title,
                                module_code,
                                content)
            modules_database.append(module)

        file.close()
        print("Modules data loaded.")
    except FileNotFoundError:
        print("The modules data file does not exist!")

def read_quiz_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global quiz_database

    quiz_database = []
    path = "./data/quiz_questions.json"

    try:
        file = open(path, "r", encoding="utf8")
        quiz_questions = json.load(file)

        for question in quiz_questions:
            question_code = question["question_code"]
            question_type = question["question_type"]
            question_content = question["question_content"]
            question_answer = question["question_answer"]

            question = QuizQuestion(question_code,
                                question_type,
                                question_content, 
                                question_answer)
            quiz_database.append(question)

        file.close()
        print("Quiz data loaded.")
    except FileNotFoundError:
        print("The quiz data file does not exist!")

read_all_databases()