text = "Hello, World!"
name = "Sergey"
new = text.replace("World", name)
print(new)

text0 = "Hello, World!".replace("World", "Sergey")
print(text0)

text2 = "Hello, {0}! Мне {1} лет."
name2 = input("Введите имя: ")
age2 = int(input("Введите возраст: "))
print(text2.format(name2, age2))

text3 = "Hello, " + name2 + "! Мне " + str(age2) + " лет."
print(text3)

text4 = "Hello, {name}! Мне {age} лет."
arr = {"name":name2, "age":age2}
print(text4.format(name=arr[0], age=arr[1]))

number = 10.0/3
print(number)
print("{0:.2f}".format(number))
