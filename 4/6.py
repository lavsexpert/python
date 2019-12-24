from math import pi
class Circle:
    r = 0
    def __init__(self, r):
        self.r = r

    @staticmethod
    def sq(r):
        return pi * r**2

print(Circle.sq(10))
