number = 1
while(number != 0):
    number = int(input("Введите число или 0 для выхода: "))
    if(number == 0):
        break
    elif (number % 2 == 0):
        print("Четное")
    else:
        print("Нечетное")
