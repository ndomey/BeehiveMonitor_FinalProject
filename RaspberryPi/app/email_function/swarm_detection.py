from email.message import EmailMessage
from email_function.config import password
import ssl
import smtplib
import time

hive_num = "5"
bees = 10

def swarm_alert():

    email_sender = 'hiveguardtest@gmail.com'
    email_password = password

    email_reciever = 'domey.f@gmail.com'
    subject = f"Swarm alert from Hive {hive_num}"
    body = f"""
        Hello,

        You got a new swarm alert from Hive {hive_num} at
        {time.strftime("%d/%m/%y %H:%M:%S")}.
        
        Happy swarm hunting!

        HiveGuard Team
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
