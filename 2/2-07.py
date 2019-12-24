a = {"a":"Альфа", "b":"Бета", 30:"Три", "c":100}
print(a["b"])
print(a[30])
a[30] = "Тридцать"
print(a)
del a["b"]
print(a)

for i in a:
    print(i, "=", a[i])

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

print(list(a.keys()))
print(list(a.values()))

b = a.copy()
print(b)
a.clear()
print(a)

b.setdefault(40, "Сорок")
print(b)

b.setdefault(30, "Т")
print(b)
b[30] = "TT"
print(b)

c = {30: "123", 40: "321", 50: "111"}
print(c)
b.update(c)
print(b)
