import abc
import numpy as np
import math

class IGraphingFunctions(abc.ABC):
    @abc.abstractmethod
    def Equation():
        return 0
    
    @abc.abstractmethod
    def Label():
        return 0 

class LinearFunction(IGraphingFunctions):
    def __init__(self, x_values, slope = 1, coefficient = 0):
        self.x_values = x_values
        self.slope = slope
        self.coefficient = coefficient

    def Equation(self):
        return self.slope * self.x_values + self.coefficient

    def Label(self):
        return f'y = {self.slope}x + {self.coefficient}'

class SquareFunction:
    def __init__(self, x_values, slope = 1, coefficient = 0):
        self.x_values = x_values
        self.slope = slope
        self.coefficient = coefficient

    def Equation(self):
        return self.slope * pow(self.x_values,2) + self.coefficient

    def Label(self):
        return f'y = {self.slope}x^2 + {self.coefficient}'

class CubicFunction:
    pass