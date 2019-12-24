def StringRub(number):
    rub = ("рубль", "рубля", "рублей")
    if number % 100 > 10 and number % 100 < 20:
        return str(number) + " " + rub[2]
    elif number % 10 == 1:
        return str(number) + " " + rub[0]
    elif (number % 10 == 2 or number % 10 == 3 or number % 10 == 4):
        return str(number) + " " + rub[1]
    else:
        return str(number) + " " + rub[2]

text = "dszfgsdf"
dict = {}
while text != "":
    text = input("Введите:")
    if text == "":
        break
    #print(StringRub(int(text)))
    dict.setdefault(int(text), StringRub(int(text)))
    print(dict)



