from email.message import EmailMessage
import ssl
import smtplib

class User:
    """
    This is the class definition for the User class.
    """

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 phone_number,
                 date_of_birth,
                 username,
                 password,
                 user_type=None,
                 is_logged_in=False,):
        """
        Constructor method for the User class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password
        self.user_type = user_type
        self.is_logged_in = is_logged_in


    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_user_type(self):
        return self.user_type

    def set_user_type(self, user_type):
        self.user_type = user_type

    def set_logged_in(self):
        self.is_logged_in = True

    def set_logged_out(self):
        self.is_logged_in = False

    def forgot_details(self, email):

        for user in users_database:


        email_sender = 'codeventure44@gmail.com'
        password_sender = 'wqij bryl dmjm bzob'
        email_receiver = str(email)
        email_receiver = str(email_receiver)

        subject = 'CodeVenture Details'
        body = f'''
        Hello,
        Here are your account details. 
        Your username is {username}
        Your password is {password}
        Please delete this email once you have your details.
        Kind Regards,
        CodeVenture Team
        '''

        mail = EmailMessage()
        mail['From'] = email_sender
        mail['To'] = email_receiver
        mail['subject'] = subject
        mail.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, password_sender)
            smtp.sendmail(email_sender, email_receiver, mail.as_string())

        self.forgot_details = None

if __name__ == "__main__":
    email= input('Enter email: ')
    username = input('Enter: ')
    password = input()
    User.forgot_details(email, username, password)