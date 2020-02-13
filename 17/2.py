import collections

abc = ("a", "b", "a", "c", "b", "a")
col = collections.Counter()
for item in abc:
    col[item] += 1
print(col)

col = collections.Counter("zzzzzzzzabrakadabra")
print(col.most_common(3))
print(list(col.elements()))

print(list(col.keys()))

first = collections.Counter("abrakadabra")
second = collections.Counter("bar")
print("first: ",first)
print("second:",second)
print("-:",first - second)
print("+:",first + second)
print("&:",first & second)
print("|:",first | second)




