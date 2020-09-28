#Superclass rectangle
class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        return self.base * self.height

    def Perimeter(self):
        return (self.base * 2) + (self.height * 2)

#Subclass of Rectangle
class Square(Rectangle):
    def __init__(self, base):
        super().__init__(base, base)

#Subclass of Rectangle
class Trapezoid(Rectangle):
    def __init__(self, base, base2, height):
        self.base2 = base2
        super().__init__(base, height)

    def Area(self):
        return ((self.base + self.base2) / 2 ) * self.height

#Subclass of Rectangle
class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def Area(self):
        return (self.base * self.height) / 2

#SubClass of Square 
class Cube(Square):
    def __init__(self, base):
        super().__init__(base)
    
    def Surface_Area(self):
        return super().Area() * 6
    
    def Volume(self):
        return self.base ** 3


