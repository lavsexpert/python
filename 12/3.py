import datetime
from dates import getdays

now = datetime.datetime.today()
nowdate = str(now.day) + "." + str(now.month) + "." + str(now.year)
date = input("Введите дату открытия вклада: ")
summa = float(input("Сумма вклада: "))
percent = float(input("Процент годовых: "))

days = getdays(date, nowdate)
newsumma = summa + summa*days*percent/36500

print(newsumma)
