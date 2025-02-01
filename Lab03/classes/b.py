class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__ (self, lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght **2
a = Shape()
print(a.area())
a = Square(int(input()))
print(a.area())