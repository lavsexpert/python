import sqlite3
import random
import datetime

file = open('shop.db', 'w')
file.close()

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE goods
(id INTEGER, name CHAR(50), amount FLOAT, price FLOAT)
""")

cursor.execute("""
CREATE TABLE orders
(number INTEGER, date DATE, total FLOAT)
""")

cursor.execute("""
CREATE TABLE details
(id INTEGER, number INTEGER, goodsId INTEGER, amount FLOAT, sum FLOAT)
""")

goods = ("Арбуз", "Яблоко", "Помидор", "Огурец", "Картошка")
prices = (100.0, 10.0, 15.0, 20.0, 5.0)
i = 0
for item in goods:
    i += 1
    cursor.execute("""
        INSERT INTO goods
        VALUES(?,?,?,?)""", (i, item, random.randint(1,10), prices[i-1]))

id = 0
for order in range(10):
    total = 0
    for detail in range(random.randint(1,5)):
        id += 1
        count = random.randint(1,10)
        item = random.randint(1,5)
        total += count*prices[item-1]
        cursor.execute("""
            INSERT INTO details
            VALUES(?,?,?,?,?)""", (id, order, item, count, count*prices[item-1]))

    cursor.execute("""
        INSERT INTO orders
        VALUES(?,?,?)""", (order, datetime.datetime.today(), total))


cursor.execute("SELECT * FROM goods")
print(cursor.fetchall())
cursor.execute("SELECT * FROM orders")
print(cursor.fetchall())
cursor.execute("SELECT * FROM details")
print(cursor.fetchall())

cursor.execute("""
SELECT goods.name, details.amount, details.sum
FROM (orders
LEFT JOIN details 
ON orders.number = details.number) 
LEFT JOIN goods
ON details.goodsId = goods.id
ORDER BY details.id
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1], "-", item[2])

cursor.execute("""
SELECT *
FROM orders
LEFT JOIN details 
ON orders.number = details.number
ORDER BY details.id
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1], "-", item[2], "-", item[3], "-", item[4], "-", item[5], "-", item[6], "-", item[7])
