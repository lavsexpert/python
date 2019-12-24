from random import randint

text = "Привет"
for letter in text:
    print(letter, "=", ord(letter))

a = []
for i in range(10):
    a.append(randint(1, 99))

for i in a:
    print(chr(1000+i))


