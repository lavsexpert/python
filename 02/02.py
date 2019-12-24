a = [12, 3.5, "яблоко", -4]
print(a[0])
print(a)
for i in a:
    if not (i == a[0] or i == a[1]):
        continue
    print(i)

b = [1, 2, 3]
c = a + b
print(c)

a.append("Привет")
print(a)
a.remove(3.5)
print(a)

print(a[0])
print(a[1])

print(c[1:4])
print(c[:4])
print(c[1:])

print(a)
a[0] = 88
print(a)

