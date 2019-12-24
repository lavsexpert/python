def maxn(a, b):
    if a>=b:
        return a
    else:
        return b

x = int(input("Введите a: "))
y = int(input("Введите b: "))
print("Большего числа: ", maxn(x,y))
