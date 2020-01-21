curs = int(input("Введите курс доллара: "))

for i in range(11):
    print('{} $ - {} рублей'.format(i, i*curs))
