#!/usr/bin/env python3

import cgi
import db

form = cgi.FieldStorage()

phone = form.getvalue("phone")
email = form.getvalue("email")
password = form.getvalue("password")

db.reg(phone, email, password)

print("Content-type: text/html")
print("Location: http://localhost:8000/enter.html")



