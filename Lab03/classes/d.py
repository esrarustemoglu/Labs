import math
class PointClass:
    def __init__ (self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self,):
        print(f"({self.x1}, {self.y1})")
    def dist(self):
        d = math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)
        print(d)
point = PointClass(2,6,4,8)
point.show()
point.move()
point.dist()