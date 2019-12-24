class Figure:
    w = 0
    h = 0

    def squire(self):
        return self.w * self.h

    def __init__(self, w, h):
        if h == 0:
            self.h = w
            self.w = w
        else:
            self.w = w
            self.h = h

#rect = Figure()
#rect.w = 10
#rect.h = 5
#print(rect.squire())

rect2 = Figure(3,9)
print(rect2.squire())

rect3 = Figure(3,0)
print(rect3.squire())
