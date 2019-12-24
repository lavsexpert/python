import csv

with open("table.csv", "w", newline='\n', encoding="cp1251") as file:
    writer = csv.writer(file, delimiter=';')

    #1й способ
    string = """Имя;Фамилия;Год рождения
Иван;Иванов;1980
Петр;Петров;1990
Джон;Сильвер;1970"""
    lines = string.split("\n")
    for line in lines:
        cells = line.split(";")
        print(cells)
        writer.writerow(cells)

    #2й способ
    rows = [['Имя', 'Фамилия', 'Год рождения'],
    ['Иван', 'Иванов', '1980'],
    ['Петр', 'Петров', '1990'],
    ['Джон', 'Сильвер', '1970']]
    for row in rows:
        print(row)
        writer.writerow(row)
        
    
