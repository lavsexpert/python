print(type(2))
print(type(2.0))
print(type("Text"))
print(type(0 == 1))

class A:
    text = "Text"

print(A.text)
print(type(A))

class Product:
    name = "Стол"
    count = 10
    price = 100.0

    def sum(self):
        return self.count * self.price

    def string(self):
        print(self.name, self.count, self.price)

table = Product()
print(table.sum())
chair = Product()
chair.name = "Стул"
chair.count = 15
chair.price = 50.0
print(chair.sum())
print(type(chair))
chair.string()


    
