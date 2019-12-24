a = "Ресторан 'Пушкин'"

print(a[0])
print(a[0:8])
print(a[:8])
print(a[9:])
print(a[-8:])

b = a + " открыт."
print(b)
c = b.split()
print(c)
d = b.split("т")
print(d)

e = "".join(c)
print(e)
f = "---".join(c)
print(f)
g = "-".join(a)
print(g)


