#!/usr/bin/env python3

import cgi
import db

form = cgi.FieldStorage()

login = form.getvalue("login")
password = form.getvalue("password")

is_reg = db.is_reg(login, password)

if (is_reg):
    print("Content-type: text/html")
    print("Location: http://localhost:8000/index.html")
else:
    print("Content-type: text/html")
    print("Location: http://localhost:8000/enter.html")