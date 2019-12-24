#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("text_1", "не задано")
text2 = form.getfirst("text_2", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
         <html>
         <head>
             <title>Всё что угодно</title>
         </head>
         <body>""")
print("<h1>УРА!!!</h1>")
print("<p>text_1: {}</p>".format(text1))
print("<p>text_2: {}</p>".format(text2))
print("""</body>
         </html>""")
