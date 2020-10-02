import abc
import numpy as np
from math import sqrt
from math import tan
from math import pi

#Interface Class for making other Regular Polygon Classes
#Area is an abstract method for finding Area of an object
#Perimeter is an abstract method for finding the perimeter of an object
#Get_Vertices is an abstract method for finding the vertices given base 
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

#Regular Triangle Class using the InterfaceRegularPolygon interface
class Triangle(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return (sqrt(3) / 4) * (self.base ** 2)

    def Perimeter(self):
        return self.base * 3

    #Returns a numpy 2 dimensional array containing the vertices for ploting the object
    #utilizes the pythagorean theorem to find the top vertice
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

#Regular Square Class using the InterfaceRegularPolygon interface
class Square(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return self.base ** 2

    def Perimeter(self):
        return self.base * 4

    def Get_Vertices(self):
        raise NotImplementedError

#Regular Square Class using the InterfaceRegularPolygon interface
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

#Regular Trapezoid Class using the InterfaceRegularPolygon interface
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

#Regular Pentagon Class using the InterfaceRegularPolygon interface
class Pentagon(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        raise NotImplementedError

    def Perimeter(self):
        return self.base * 5

    def Get_Vertices(self):
        raise NotImplementedError

#Regular Hexagon Class using the InterfaceRegularPolygon interface
class Hexagon(InterfaceRegularPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return (3 * sqrt(3) * pow(self.base,2) / 2)

    def Perimeter(self):
        return self.base * 6

    def Get_Center(self):
        # center = self.base / (2 * tan(180/6) * (pi/180))

        center = [0,0]
        center[0] = self.base / 2
        center[1] = sqrt(pow(self.base,2) - pow(center[0],2))
        return center

    def Get_Vertices(self):
        center = self.Get_Center()
        vertices = np.array([
        [0,0],
        [self.base,0],
        [center[0]+self.base,center[1]],
        [self.base,center[1]*2],
        [0,center[1]*2],
        [center[0]-self.base,center[1]]
        ],dtype=object)
        return vertices

