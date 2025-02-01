class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__ (self, lenght, widht):
        self.lenght = lenght
        self.widht = widht
    def area(self):
        print(self.lenght * self.widht)
a = Shape()
a.area()
a = Rectangle(5, 6)
a.area()