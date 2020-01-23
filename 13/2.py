import sqlite3

file = open('people.db', 'w')
file.close()

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE names
(name CHAR(50), surname CHAR(50))
""")

print("Введите имя и фамилию (или Enter для завершения): ")
while True:
    people = input("Имя и фамилия: ")
    if people == "":
        break
    (name, surname) = people.split(" ")
    cursor.execute("""
    INSERT INTO names
    VALUES(?,?)""",(name,surname))

cursor.execute("SELECT * FROM names")
print(cursor.fetchall())
conn.close()
