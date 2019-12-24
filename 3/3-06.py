from random import randint
a = []
for i in range(10):
    a.append(randint(1, 99))
print(a)

#Сортировка выбором
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

#Сортировка пузырьком
def bubble_sort(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

b = a.copy()
sel_sort(b)
print(b)

c = a.copy()
bubble_sort(c)
print(c)
