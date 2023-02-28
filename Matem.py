class Rectangle:# #############Фаил Probnuy.py
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_sqare(self):
        return self.a **2
#Возведение в степень **2 (в квадрат)
class Circle:
    def __init__(self, p, r):
        self.p = p
        self.r = r
    def S_cricle(self):
        return self.p * self.r**2
#######################----------------Фаил Matem.py------
from Probnuy import Rectangle, Square, Circle

#Создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#Вывод площадей
print(rect_1.get_area())
print(rect_2.get_area())

sqare_1 = Square(5)
sqare_2 = Square(10)

print(sqare_1.get_area_sqare(), sqare_2.get_area_sqare())

figures = [rect_1, rect_2, sqare_1, sqare_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_sqare())
    else:
        print(figure.get_area())

S_1 = Circle(3.14, 10)
S_2 = Circle(3.14, 25)

print(S_1.S_cricle(), S_2.S_cricle())