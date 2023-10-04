import smtplib
import logging

from fastapi import status, HTTPException
from email.mime.text import MIMEText
from app.config.config import RootUserEmail

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


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
                logging.info("Message sent successfully!")
            return "Message sent successfully!"
        except smtplib.SMTPException as e:
            logging.exception(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

    def __get_host_and_port(self):
        host, port = "smtp.gmail.com", 465
        if self.__sender.email.endswith("@mail.ru"):
            host = "smtp.mail.com"
        return [host, port]
