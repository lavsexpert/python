import sqlite3
import csv

file = open('site.db', 'w')
file.close()
conn = sqlite3.connect('site.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE users
(phone CHAR(50), email CHAR(50), password CHAR(50))
""")
with open("table.csv", "r") as file:
    reader = csv.reader(file, delimiter=';')
    first = True
    for row in reader:
        if first:
            print(first)
            first = False
            continue
        print(row[0], row[1], row[2])
        cursor.execute("""
            INSERT INTO users
            VALUES(?,?,?)""", (row[0], row[1], row[2]))
        conn.commit()
conn.close()