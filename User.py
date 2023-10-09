"""

"""

from email.message import EmailMessage
import ssl
import smtplib

global users_database


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
                 is_logged_in=False):
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

    @staticmethod
    def is_DOB_valid(date_of_birth):
        if not(len(date_of_birth)==10):
            return False
        if (date_of_birth[2]=='/' and date_of_birth[5] == '/'):
            DD = date_of_birth[0:2]
            MM = date_of_birth[3:5]
            YYYY = date_of_birth[6:10]
            try:
                YYYY = int(YYYY)
                if not(1800<YYYY<9999):
                    return False
            except ValueError:
                return False
            valid_days = []
            if MM in ['01','03','05','07','08','10','12']:
                # 31 day month
                for day in range(1,32):
                    valid_days.append(str(day).zfill(2))
                if not(DD in valid_days):
                    return False
            elif MM in ['04','06','09','11']:
                # 30 day month
                for day in range(1,31):
                    valid_days.append(str(day).zfill(2))
                if not(DD in valid_days):
                    return False
            elif MM == '02':
                if YYYY%4 == 0:
                    # Leap year
                    for day in range(1, 30):
                        valid_days.append(str(day).zfill(2))
                    if not(DD in valid_days):
                        return False
                else:
                    # not leap year
                    for day in range(1, 29):
                        valid_days.append(str(day).zfill(2))
                    if not(DD in valid_days):
                        return False
            else:
                return False
        else:
            return False
        return True

    @staticmethod
    def is_email_valid(email):
        if '@' in email and '.' in email:
            return True
        else:
            return False
    
    @staticmethod
    def is_phone_num_valid(phone_number):
        if phone_number is None:
            try:
                int(phone_number)
                return True
            except ValueError:
                return False
        else:
            return True
        
    

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

    @staticmethod
    def forgot_details(users_database, email):
        print('Loading...')
        username = None
        password = None

        for user in users_database:
            if email == user.get_email():
                username = user.get_username()
                password = user.get_password()
                first_name = user.get_first_name()
                last_name = user.get_last_name()

        if (username == None) or (password == None):
            print("Email is not registered in CodeVenture!")
        else:


            email_sender = 'codeventure44@gmail.com'
            password_sender = 'wqij bryl dmjm bzob'
            email_receiver = str(email)
            email_receiver = str(email_receiver)
            subject = 'CodeVenture Details'
            body = f'''
            Dear {first_name} {last_name},
            Here are your account details. 
            Username: {username}
            Password: {password}
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


