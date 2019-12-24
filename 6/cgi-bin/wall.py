#!/usr/bin/env python3
# -*- coding: utf-8 -*
import cgi
import html
import http.cookies
import os

from _wall import Wall
wall = Wall()

cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookies.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)

form = cgi.FieldStorage()
action = form.getfirst("action", "")

if action == "publish":
    text = form.getfirst("text", "")
    #text = html.escape(text)
    if text and user is not None:
        wall.publish(user, text)
elif action == "login":
    login = form.getfirst("login", "")
    login = html.escape(login)
    password = form.getfirst("password", "")
    password = html.escape(password)
    if wall.find(login, password):
        cookie = wall.set_cookie(login)
        print("Set-cookie: session={}".format(cookie))
    elif wall.find(login):
        pass
    else:
        wall.register(login, password)
        cookie = wall.set_cookie(login)
        print("Set-cookie: session={}".format(cookie))

pattern = """
<!DOCTYPE HTML>
<html lang=ru>
<head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
    <title>Стена</title>
</head>
<body>
    {auth}
    {login}
    {posts}
    {publish}
</body>
</html>
"""

auth = """
<p>Введите логин и пароль для входа или регистрации</p>
<form action="/cgi-bin/wall.py">
    Логин: <input type="text" name="login">
    Пароль: <input type="password" name="password">
    <input type="hidden" name="action" value="login">
    <input type="submit">
</form>
"""

if user is not None:
    name = user + "<br>"
    pub = """
    <p>Отправьте сообщение</p>
    <form action="/cgi-bin/wall.py">
        <textarea name="text"></textarea>
        <input type="hidden" name="action" value="publish">
        <input type="submit">
    </form>
    """
else:
    name = ""
    pub = ""

print("Content-type: text/html;charset=utf-8\n")
print(pattern.format(auth=auth, login=name, posts=wall.html_list(), publish=pub))
