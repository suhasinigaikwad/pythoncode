import pandas as p
import smtplib as sm
from sys import *
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data = p.read_excel("Mail.xlsx")
email_col = data.get("MailId")
list_of_emails = list(email_col)
print(list_of_emails)

try:
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('suhasinigaikwad10@gmail.com','scijmowhpsmxjitb')
    from_ = 'suhasinigaikwad10@gmail.com'
    to_ = list_of_emails

    message = MIMEMultipart("alternative")
    message['Subject'] = "This mail is just for testing my python code"
    
    body = '''
    Hello dear,

        This mail is autogenerated by python code which is generated automatically to send the mails for multiple users at a time.
    So Kindly ignore this mail and relax.
    And just want to ask :) - "J1 zal ka?"

    Thanks & Regards,
    A new python developer in market :)
    Suh@ '''

    
    message.attach(MIMEText(body, 'plain'))
    server.sendmail(from_,to_,message.as_string())
    print("mail sent successfully")




except Exception as e:
    print(e)    