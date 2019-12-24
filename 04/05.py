class A:
    count = 0
    def __init__(self):
        A.count += 1
    def __del__(self):
        A.count -= 1

a1 = A()
a2 = A()
a3 = A()
a3 = A()
a3 = A()
a34 = A()
print(A.count)
del a3
del a2
print(A.count)
print(a1)
print(a2)

