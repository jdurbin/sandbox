#!/usr/bin/env python

import smtplib
from email.message import EmailMessage

me = "cmeafestivalcoordinator@gmail.com"
you = "durbin.james@gmail.com"

server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
# server.ehlo()
server.starttls()
# server.ehlo()
server.login(me,'qkqwesilxpfnwlwe')

msg = "Message_you_need_to_send"

server.sendmail(me,you,msg)
server.close()