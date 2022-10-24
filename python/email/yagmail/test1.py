#!/usr/bin/env python3

import yagmail
yag = yagmail.SMTP('durbin.james@gmail.com')
yag.send('durbin.james@gmail.com', subject = 'Hello test', contents = 'This is a test, Jack')