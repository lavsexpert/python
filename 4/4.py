from math import pi
class Figure:
    w = 0
    h = 0
    def sq(self):
        return self.w * self.h
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def __str__(self):
        return "Figure:"+str(self.w)+"-"+str(self.h)
    
class Rect(Figure):
    def perim(self):
        return (self.w + self.h)*2
    def __str__(self):
        return "Rect:"+str(self.w)+"-"+str(self.h)
    
class Circle(Figure):
    def perim(self):
        return (self.w * pi)*2
    def sq(self):
        return (self.w**2) * pi
    def __init__(self, w):
        self.w = w
    def __str__(self):
        return "Circle:"+str(self.w)
    
figure = Figure(1,2)
print(figure)
rect = Rect(10, 20)
print(rect.sq())
print(rect.perim())
circle = Circle(10)
print(circle.sq())
print(circle.perim())
print(rect)
print(circle)


    
