import sqlite3
import random

file = open('shop.db', 'w')
file.close()

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

products = ("Арбуз", "Картошка", "Помидоры", "Яблоки", "Огурцы", "Лук", "Бананы")

cursor.execute("""
CREATE TABLE prices
(product CHAR(50), price FLOAT)
""")

for product in products:
    cursor.execute("""
    INSERT INTO prices
    VALUES(?,?)""",(product, random.randint(1,100)))

cursor.execute("""
SELECT *
FROM prices
WHERE price < 50
ORDER BY price
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], item[1])
conn.close()
