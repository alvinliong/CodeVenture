import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ForgotPassword:
    def __init__(self, users_data):
        self.users_data = users_data

    def send_password_email(self, email):
        if email not in self.users_data:
            print("Email not found in the database.")
            return False

        username = self.users_data[email]["username"]
        password = self.users_data[email]["password"]

        subject = "Password Recovery"
        message = f"Your username: {username}\nYour password: {password}"

        sender_email = "codeventure44@gmail.com"  # Change to your email
        sender_password = "SithikaM"  # Change to your email password
        receiver_email = 'sithikamm@gmail.com'

        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the message via our SMTP server
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

            print("Password recovery email sent successfully.")
            return True

        except Exception as e:
            print("An error occurred while sending the email:", str(e))
            return False

if __name__ == "__main__":
    with open("users.txt", "r") as file:
        users_data = json.load(file)
    
    forgot_password = ForgotPassword(users_data)

    while True:
        email = input("Enter your email address to recover your password (or 'exit' to quit): ")
        if email.lower() == 'exit':
            break

        forgot_password.send_password_email(email)

