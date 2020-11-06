#Python libraries
import numpy as np
import math
import abc

#interface Class for making other Graphing Function Classes
class IGraphingFunctions(abc.ABC):

    #Equation is an abstract method for returning a function of an object
    @abc.abstractmethod
    def Equation():
        return 0
    
    #Label is an abstract method for returning a label for a function of an object
    @abc.abstractmethod
    def Label():
        return 0 

#linear function class using the IGraphingFunctions interface
class LinearFunction(IGraphingFunctions):
    def __init__(self, x_values, slope = 1, coefficient = 0):
        self.x_values = x_values
        self.slope = slope
        self.coefficient = coefficient

    def Equation(self):
        return self.slope * self.x_values + self.coefficient

    def Label(self):
        return f'y = {self.slope}x + {self.coefficient}'

#square function class using the IGraphingFunctions interface
class SquareFunction(IGraphingFunctions):
    def __init__(self, x_values, slope = 1, coefficient = 0):
        self.x_values = x_values
        self.slope = slope
        self.coefficient = coefficient

    def Equation(self):
        return self.slope * pow(self.x_values,2) + self.coefficient

    def Label(self):
        return f'y = {self.slope}x^2 + {self.coefficient}'

#cubic function class using the IGraphingFunctions interface
class CubicFunction(IGraphingFunctions):
    def __init__(self, x_values, slope = 1, coefficient = 0):
        self.x_values = x_values
        self.slope = slope
        self.coefficient = coefficient

    def Equation(self):
        return self.slope * pow(self.x_values,3) + self.coefficient

    def Label(self):
        return f'y = {self.slope}x^2 + {self.coefficient}'