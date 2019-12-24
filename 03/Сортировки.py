import random
import timeit

count = 1000 # количество элементов - чем больше, тем больше разница во времени

#Заполняем массив случайными числами
a = []
for i in range(count):
    a.append(random.randint(1, count))
print("Перемешанный список:")
#print(a)

#Сортировка пузырьком
def bubble_sort(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

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
    return array

#Быстрая сортировка
def quicksort(array):
   if len(array) <= 1:
       return array
   else:
       q = random.choice(array)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in array:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

print("\nСортировка пузырьком:")
time = timeit.default_timer()
b = bubble_sort(a.copy())
#print(b)
print("{0:.4f}".format(timeit.default_timer()-time))

print("\nСортировка выбором:")
time = timeit.default_timer()
c = sel_sort(a.copy())
#print(c)
print("{0:.4f}".format(timeit.default_timer()-time))

print("\nБыстрая сортировка:")
time = timeit.default_timer()
d = quicksort(a.copy())
#print(d)
print("{0:.4f}".format(timeit.default_timer()-time))

