#!/usr/bin/env python3

import sys,re
from beautifier import Email, Url
import ftfy

name1="Tschöp"

email1=" bob@gmail.com"
email2=" mary@gmail.com.     "
email3=" jim at gmail.com"


#cleanre = r"[^a-zA-Z0-9@]"
#cleanmail = re.sub(cleanre,"",email2)
clean = email2.strip(' ').strip(".")
print(f">{clean}<")

clean=email1.strip('.com')
print(f"{clean}")

em1 = Email(email2)
#print(em1.domain)
#print(em1.username)
#print(f"{em1.username}@{em1.domain}")

#print(ftfy.fix_text(name1))