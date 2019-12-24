file = open("text.txt")
#print(len(file.read()))
lines = 0
words = 0
letters = 0
for line in file:
    lines += 1
    words += len(line.split())
    letters += len(line.replace("\n",""))
print("Строк:", lines)
print("Слов: ", words)
print("Букв: ", letters)
file.close()



