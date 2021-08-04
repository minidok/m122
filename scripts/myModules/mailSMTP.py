# Simple SMTP client 
# 2021 Dominik Reuss#
#
# see pyhton doc for further configuration
# https://docs.python.org/3/library/email.examples.html#email-examples

#!/usr/bin/env python3


import smtplib
import os
import platform
from email.message import EmailMessage
import mimetypes
from typing import final


def userName():
    operatingSystem = platform.system()
    if operatingSystem == "Windows":
        return os.environ.get('username')
    else:
        return os.environ.get('USER')

def createEmailMessage(sender, recipient, subject, body):
    emailMsg = EmailMessage()
    emailMsg["From"] = sender
    emailMsg["To"] = recipient
    emailMsg["Subject"] = subject
    emailMsg.set_content(body)
    return emailMsg

def createEmailWithAttachement(sender, recipient, subject, body, attachmentFilePath):
    emailWithAttachement = createEmailMessage(sender, recipient, subject, body)

    # AttachementFilePath contains FilePath and FileName
    attachement = os.path.basename(attachmentFilePath)
    mime_type, _ = mimetypes.guess_type(attachmentFilePath)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachmentFilePath, 'rb') as ap:
        emailWithAttachement.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachement)

    return emailWithAttachement  

def sendEmail(emailMsg):
    mail_server = smtplib.SMTP('localhost',25)
    #mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    try:
        #mail_server.login(sender, password)
        mail_server.send_message(emailMsg)
    except Exception: 
        print(Exception) 
    finally:
         mail_server.quit()
      


def main():
    #main empty

    if __name__ == '__main__':
     main()
