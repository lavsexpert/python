#Первый вариант
file = open("text.txt")
words = []
for line in file:
    linewords = line.split()
    for word in linewords:
        words.append(word)
sortedwords = sorted(words, key = len)
for word in sortedwords:
    print(word)
file.close()

#Второй вариант
file = open("text.txt")
text = file.read()
a = text.split()
words = []
for word in a:
    words.append(word)
print(sorted(words, key = len))
file.close()
