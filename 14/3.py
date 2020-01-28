import sqlite3

file = open('numbers.db', 'w')
file.close()

conn = sqlite3.connect('numbers.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE squares
(number INTEGER, square INTEGER)
""")

for i in range(11):
    cursor.execute("""
    INSERT INTO squares
    VALUES(?,?)""",(i, i*i))

cursor.execute("""
SELECT *
FROM squares
WHERE square > 50
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], item[1])
                   
cursor.execute("""
SELECT SUM(square)
FROM squares
""")
print(cursor.fetchall()[0][0])
conn.close()

                   
