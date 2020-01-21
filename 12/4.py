import datetime
import dates

now = datetime.datetime.today()
nowdate = str(now.day) + "." + str(now.month) + "." + str(now.year)
date = input("Введите взятия кредита: ")
summa = float(input("Сумма кредита: "))
percent = float(input("Процент годовых: "))
month = float(input("На сколько месяцев кредит: "))

restmonth = month - dates.getmonth(date, nowdate)
full = summa + summa*(month/12)*(percent/100)
rest = full/month*restmonth 
print(rest)
for i in range(int(restmonth)):
    print(dates.plusmonth(nowdate, i)," - ",full/month)




