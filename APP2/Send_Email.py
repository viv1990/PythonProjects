import smtplib
import ssl
import os
# OS library used to introduce the envrionment variable concept so that password is not visible to any
#other users and only store it in user local computer
#Environment variable are of two types: User & System



def Send_Email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "er.viveksoni1990@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "er.viveksoni1990@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

