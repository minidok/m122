# Simple SMTP client Testcases
# 2021 Dominik Reuss#
#
# Test do require a local SMTP Server connect to: 
# i.e. run shell comman 'python -m smtpd -c DebuggingServer -n localhost:25'
#
# see pyhton doc for further configuration
# https://docs.python.org/3/library/email.examples.html#email-examples

#!/usr/bin/env python3


from datetime import datetime
from email.message import EmailMessage
from typing import Type
import unittest
import mailSMTP

class mailSmtpTests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_createMail(self):   
        empfaenger = "{}@mein_Firma_bzu.com".format(mailSMTP.userName) 
        absender = "python@domain.ch"
        titel = "Python sendet eine Mail"
        timestamp = datetime.time(datetime.now())
        theMail  = mailSMTP.createEmailMessage(absender, empfaenger,titel, 'Status Update '+ str(timestamp))
        self.assertIsInstance(theMail, EmailMessage, 'Email muss vom Typ Emailmessage sein')
        mailSMTP.sendEmail(theMail)  

    def test_sendAttachement(self):
        empfaenger = "{}@mein_Firma_bzu.com".format(mailSMTP.userName) 
        absender = "python@domain.ch"
        titel = "Python sendet ein Bild"
        timestamp = datetime.time(datetime.now())
        theMail  = mailSMTP.createEmailWithAttachement(absender, empfaenger,titel, 'Status Update '+ str(timestamp),"./test_image.png")
        self.assertIsInstance(theMail, EmailMessage, 'Email muss vom Typ Emailmessage sein')
        mailSMTP.sendEmail(theMail)  


    def test_Username(self):
        self.assertTrue((len(mailSMTP.userName()) > 0) , 'Username muss gueltig sein')
             
    if __name__ == '__main__':
        unittest.main()