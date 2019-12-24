def summa(a, b):
    return a + b

number = 1
sum = 0
while number != 0:
    number = int(input("Введите 0 для выхода: "))
    sum = summa(sum, number)
print("Сумма чисел: ", sum)




