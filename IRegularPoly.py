import abc
import numpy as np
from math import sqrt
from math import tan
from math import pi

class InterfaceRegularPolygon(abc.ABC):
    @abc.abstractmethod
    def Area(self):
        return 0

    @abc.abstractmethod
    def Perimeter(self):
        return 0

    @abc.abstractmethod
    def Get_Vertices(self):
        return 0

class Triangle(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return (sqrt(3) / 4) * (self.base ** 2)

    def Perimeter(self):
        return self.base * 3

    def Get_Vertices(self):
        top_vertice = [0,0]
        top_vertice[0] = self.base / 2
        top_vertice[1] = sqrt(pow(self.base,2) - pow(top_vertice[0],2))
        vertices = np.array([
        [0,0],
        [self.base,0],
        top_vertice
        ],dtype=object)
        return vertices

class Square(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return self.base ** 2

    def Perimeter(self):
        return self.base * 4

    def Get_Vertices(self):
        raise NotImplementedError

class Rhombus(Square):
    def __init__(self, base):
        super().__init__(base)

class Rectangle(InterfaceRegularPolygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        return self.base * self.height

    def Perimeter(self):
        return (self.base * 2) + (self.height * 2)

    def Get_Vertices(self):
        raise NotImplementedError

class Parallelogram(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

class Trapezoid(InterfaceRegularPolygon):
    def __init__(self, base, base2, height):
        self.base = base
        self.base2 = base2
        self.height = height

    def Area(self):
        return ((self.base + self.base2) / 2 ) * self.height

    def Perimeter(self):
        raise NotImplementedError

    def Get_Vertices(self):
        raise NotImplementedError

class Pentagon(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        raise NotImplementedError

    def Perimeter(self):
        return self.base * 5

    def Get_Vertices(self):
        raise NotImplementedError

class Hexagon(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return (3 * sqrt(3) * pow(self.base,2) / 2)

    def Perimeter(self):
        return self.base * 6
 
    def Get_Apothem(self):
        # apothem = self.base / (2 * tan(180/6) * (pi/180))

        apothem = [0,0]
        apothem[0] = self.base / 2
        apothem[1] = sqrt(pow(self.base,2) - pow(apothem[0],2))
        return apothem

    def Get_Vertices(self):
        apothem = self.Get_Apothem()
        vertices = np.array([
        [0,0],
        [self.base,0],
        [apothem[0]+self.base,apothem[1]],
        [self.base,apothem[1]*2],
        [0,apothem[1]*2],
        [apothem[0]-self.base,apothem[1]]
        ],dtype=object)
        return vertices

# x = Hexagon(6)
# print(x.Get_Apothem())
# x = math.tan(16)
# y = math.degrees(x)

# print(y)
