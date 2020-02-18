import sqlite3
import csv

conn = sqlite3.connect('site.db')
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM users
""")
table = cursor.fetchall()
conn.close()
table.insert(0,("Телефон","E-mail","Пароль"))
with open("table.csv", "w", newline='\n', encoding="cp1251") as file:
    writer = csv.writer(file, delimiter=';')
    for line in table:
        writer.writerow(line)

#text = "Телефон;Е-mail;Пароль\n"
#for line in table:
#    text += line[0]+";"+line[1]+";"+line[2]+"\n"
#
#with open("table.csv", "w", newline='\n', encoding="cp1251") as file:
#    writer = csv.writer(file, delimiter=';')
#    lines = text.split("\n")
#    for line in lines:
#        cells = line.split(";")
#        print(cells)
#        writer.writerow(cells)

