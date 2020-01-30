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
    for detail in range(random.randint(1,5)):
        id += 1
        count = random.randint(1,10)
        item = random.randint(1,5)
        cursor.execute("""
            INSERT INTO details
            VALUES(?,?,?,?,?)""", (id, order, item, count, count*prices[item-1]))

    total = 0;
    cursor.execute("""
        INSERT INTO orders
        VALUES(?,?,?)""", (order, datetime.datetime.today(), total))


cursor.execute("SELECT * FROM goods")
print(cursor.fetchall())
cursor.execute("SELECT * FROM orders")
print(cursor.fetchall())
cursor.execute("SELECT * FROM details")
print(cursor.fetchall())


