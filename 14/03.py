import sqlite3

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

#cursor.execute("""
#CREATE TABLE names
#(name CHAR(50), surname CHAR(50))
#""")

print("Введите имя и фамилию (или Enter для завершения): ")
while True:
    people = input("Имя и фамилия: ")
    if people == "":
        break
    (name, surname) = people.split(" ")
    cursor.execute("""
    INSERT INTO names
    VALUES(?,?)""",(name,surname))

cursor.execute("""
SELECT name, COUNT(surname) 
FROM names
WHERE name != 'Елена'
GROUP BY name
ORDER BY COUNT(surname) DESC
""")
print(cursor.fetchall())
conn.close()
