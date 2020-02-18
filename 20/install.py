import sqlite3

file = open('site.db', 'w')
file.close()

conn = sqlite3.connect('site.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users
(phone CHAR(50), email CHAR(50), password CHAR(50))
""")

conn.close()