def calc(a, oper, b):
    if oper == "+":
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b
    elif oper == "/":
        return a / b
    else:
        return "Неизвестный оператор"

a = int(input("Введите a: "))
oper = input("Введите операцию :")
b = int(input("Введите b: "))
print(calc(a,oper,b))
