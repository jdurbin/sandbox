#!/usr/bin/env python

import smtplib
from email.message import EmailMessage

sender = "cmeafestivalcoordinator@gmail.com"
recipient = "durbin.james@gmail.com"

server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
# server.ehlo()
server.starttls()
# server.ehlo()
server.login(sender,'qkqwesilxpfnwlwe')


msg = EmailMessage()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = 'Learning to send email from medium.com'

body = """Hello
I am learning to send emails using Python!!!"""
msg.set_content(body)

# You should use msg.as_string() if you call smtplib.SMTP.sendmail()
server.sendmail(sender,recipient,msg.as_string())
server.close()