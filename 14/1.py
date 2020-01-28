import sqlite3

file = open('bank.db', 'w')
file.close()

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE cur
(name CHAR(50), kurs FLOAT, multy FLOAT)
""")

cursor.execute("""
    INSERT INTO cur
    VALUES(?,?,?)""",("Доллар", 62.3, 1.0))

cursor.execute("""
    INSERT INTO cur
    VALUES(?,?,?)""",("Доллар", 68.7, 1.0))

cursor.execute("""
    INSERT INTO cur
    VALUES(?,?,?)""",("Фунт", 96.3, 1.0))

cursor.execute("""
    INSERT INTO cur
    VALUES(?,?,?)""",("Юань", 10.1, 1.0))

cursor.execute("""
    INSERT INTO cur
    VALUES(?,?,?)""",("Йена", 60.5, 100.0))

print("Валюта - Курс - Кратность")
cursor.execute("SELECT * FROM cur")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1], "-", item[2])
conn.close()
