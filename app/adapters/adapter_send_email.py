import smtplib
import logging

from email.mime.text import MIMEText
from config.config import RootUserEmail


class SendEmail:
    def __init__(self, to, subject, message):
        self.to = to
        self.subject = subject
        self.message = message
        self.__msg = MIMEText(self.message)
        self.__sender = RootUserEmail()

    def send_email(self):
        self.__msg['Subject'] = self.subject
        self.__msg['From'] = self.__sender.email
        self.__msg['To'] = self.to
        host, port = self.__get_host_and_port()
        try:
            with smtplib.SMTP_SSL(host, port) as smtp_server:
                smtp_server.login(self.__sender.email, self.__sender.password, initial_response_ok=True)
                smtp_server.sendmail(self.__sender.email, self.to, self.__msg.as_string())
            return "Message sent!"
        except smtplib.SMTPException as e:
            logging.exception(e)
            raise e

    def __get_host_and_port(self):
        host, port = "smtp.gmail.com", 465
        if self.__sender.email.endswith("@mail.ru"):
            host = "smtp.mail.com"
        return [host, port]
