import datetime
import locale

locale.setlocale(locale.LC_ALL, "ru")

now = datetime.datetime.today()
print(now)

olddate = datetime.datetime(2010, 1, 25, 10, 15, 30)
print(olddate)

testdate = datetime.date(2011, 3, 15)
print(testdate)

testtime = datetime.time(10,20,15,123456)
print(testtime)

test = datetime.datetime.combine(testdate, testtime)
print(test)

print("Год:    ",olddate.year)
print("Месяц:  ",olddate.month)
print("День:   ",olddate.day)
print("Час:    ",olddate.hour)
print("Минута: ",olddate.minute)
print("Секунда:",olddate.second)

delta = now - olddate
print(delta)
print(delta.days)
seconds = delta.total_seconds()
print(seconds)
hours = seconds // 3600 - delta.days * 24
print(hours)
minutes = seconds // 60 - delta.days * 24 * 60 - hours * 60
print(minutes)

print(now.strftime("%Y.%m.%d %H.%M.%S"))
print(now.strftime("Год:%Y,Месяц:%m,День:%d"))
print(now.strftime("%y"))
print(now.strftime("%A, %d, %B %Y %I:%M%p"))

print("0..6:",now.weekday())
print("1..7:",now.isoweekday())
print(now.isocalendar())
print(now.isoformat("T"))

add = 11
addmonth = int(now.month + add) % 12
addyear = int(now.year) + int(now.month + add) // 12
#new = now.replace(month = addmonth)
#new = new.replace(year = addyear)
print(now.replace(month = addmonth, year = addyear))
print(now.replace(1,2,3,4,5,6))

