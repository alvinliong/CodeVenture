"""
File: QuizQuestion.py
Description: This file is the QuizQuestion class
Author: CodeVenture Team G13 
"""


class QuizQuestion():

    def __init__(self,
                 question_code,
                 question_type,
                 question_content, 
                 question_answer):
        """
        Constructor for the QuizQuestion class.
        """
        self.question_code = question_code
        self.question_type = question_type
        self.question_content = question_content
        self.question_answer = question_answer
        self.question_correct = False

    def get_question_code(self):
        return self.question_code

    def get_question_type(self):
        return self.question_type
    
    def get_question_content(self):
        return self.question_content
    
    def get_question_answer(self):
        return self.question_answer
    
    def get_question_correct(self):
        return self.question_correct
    
    def set_question_correct(self, bool):
        self.question_correct = bool


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week08_*.py,
    # then marks will be deducted.
    pass
