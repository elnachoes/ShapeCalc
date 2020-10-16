import abc
import numpy as np
from math import sqrt
from math import tan
from math import pi

#Interface Class for making other Convex Polygon Classes
#Area is an abstract method for finding Area of an object
#Perimeter is an abstract method for finding the perimeter of an object
#Get_Vertices is an abstract method for finding the vertices given base 
class InterfaceConvexPolygon(abc.ABC):
    @abc.abstractmethod
    def Area(self):
        return 0

    @abc.abstractmethod
    def Perimeter(self):
        return 0

    @abc.abstractmethod
    def Get_Vertices(self):
        return 0

#Regular Triangle Class using the InterfaceConvexPolygon interface
class Triangle(InterfaceConvexPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return (sqrt(3) / 4) * (self.base ** 2)

    def Perimeter(self):
        return self.base * 3
    
    def Height(self):
        height = [0,0]
        height[0] = self.base / 2
        height[1] = sqrt(pow(self.base,2) - pow(height[0],2))
        return height

    #Returns a numpy 2 dimensional array containing the vertices for ploting the object
    #utilizes the pythagorean theorem to find the top vertice
    def Get_Vertices(self):
        Height = self.Height()
        vertices = np.array([
        [0,0],
        [self.base,0],
        [Height[0],Height[1]],
        ],dtype=object)
        return vertices

#Regular Square Class using the InterfaceConvexPolygon interface
class Square(InterfaceConvexPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        return self.base ** 2

    def Perimeter(self):
        return self.base * 4

    def Get_Vertices(self):
        raise NotImplementedError

#Regular Square Class using the InterfaceConvexPolygon interface
class Rectangle(InterfaceConvexPolygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        return self.base * self.height

    def Perimeter(self):
        return (self.base * 2) + (self.height * 2)

    def Get_Vertices(self):
        raise NotImplementedError

#Regular Trapezoid Class using the InterfaceConvexPolygon interface
class Trapezoid(InterfaceConvexPolygon):
    def __init__(self, base, base2, height):
        self.base = base
        self.base2 = base2
        self.height = height

    def Area(self):
        return ((self.base + self.base2) / 2 ) * self.height

    def Perimeter(self):
        return 0

    def Get_Vertices(self):
        return np.array([
            [0, 0], 
            [self.height, 0], 
            [self.height, self.base2], 
            [0, self.base]], 
            dtype=object)

#Regular Pentagon Class using the InterfaceConvexPolygon interface
class Pentagon(InterfaceConvexPolygon):
    def __init__(self, base):
        self.base = base

    def Area(self):
        raise NotImplementedError

    def Perimeter(self):
        return self.base * 5

    def Get_Vertices(self):
        raise NotImplementedError

#Regular Hexagon Class using the InterfaceConvexPolygon interface
class Hexagon(InterfaceConvexPolygon):
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

