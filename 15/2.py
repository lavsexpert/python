import sqlite3

file = open('world.db', 'w')
file.close()

conn = sqlite3.connect('world.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE country
(id INTEGER, countryName CHAR(50))
""")

cursor.execute("""
CREATE TABLE city
(cityId INTEGER, countryId INTEGER, cityName CHAR(50), cityAmount INTEGER)
""")

country = ("Китай", "Пакистан", "Индия", "Нигерия", "Турция", "Япония")
i = 0
for item in country:
    i += 1
    cursor.execute("""
        INSERT INTO country
        VALUES(?,?)""", (i, item))

cursor.execute("""
    INSERT INTO city
    VALUES(?,?,?,?)""", (1, 1, "Шанхай", 24256800))

cursor.execute("""
    INSERT INTO city
    VALUES(?,?,?,?)""", (2, 2, "Карачи", 23500000))

cursor.execute("""
    INSERT INTO city
    VALUES(?,?,?,?)""", (3, 1, "Пекин", 21516000))

cursor.execute("""
    INSERT INTO city
    VALUES(?,?,?,?)""", (4, 3, "Дели", 16349831))

cursor.execute("""
    INSERT INTO city
    VALUES(?,?,?,?)""", (5, 4, "Лагос", 16060303))

cursor.execute("SELECT * FROM country")
print(cursor.fetchall())
cursor.execute("SELECT * FROM city")
print(cursor.fetchall())

cursor.execute("""
SELECT city.cityName, city.cityAmount, country.countryName
FROM city
LEFT JOIN country 
ON city.countryId = country.id
ORDER BY city.cityAmount
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1], "-", item[2])


cursor.execute("""
SELECT *
FROM city
LEFT JOIN country 
ON city.countryId = country.id
ORDER BY city.cityAmount DESC
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1], "-", item[2], "-", item[3], "-", item[4], "-", item[5])
