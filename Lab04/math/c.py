import math
n = int(input())
l = int(input())
area = round((n * l *(l / (2 * math.tan(math.pi / n)))) / 2)
print(f"The area of polygon is: {area}")