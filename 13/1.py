import sqlite3

file = open('mydb.db', 'w')
file.close()

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE nums
(number INTEGER, square INTEGER)
""")

for i in range(11):
    cursor.execute("""
    INSERT INTO nums
    VALUES(?,?)""",(i,i*i))

cursor.execute("SELECT * FROM nums")
print(cursor.fetchall())
conn.close()
