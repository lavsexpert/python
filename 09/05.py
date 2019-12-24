import csv

with open("table.csv", "r") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(" ".join(row))
