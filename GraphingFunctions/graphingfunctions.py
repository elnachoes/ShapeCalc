from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt 
import IGraphingFunctions as igf



class Graph:
    def __init__(self,y, label = None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.gx = plt.grid(b = True, which = 'major' ,axis = 'both',linewidth = 1, color = "red", linestyle = '--')
        self.x = np.linspace(-np.pi,np.pi,100)
        self.y = y
        self.label = label
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['right'].set_color('blue')
        self.ax.spines['top'].set_color('blue')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

    def plot(self):

        # y = self.linear_function(3,1)
        plt.plot(self.x,self.y, 'b', label = self.label)
        # plt.plot(5,5, 'p')
        plt.legend(loc='upper left')
        plt.show() 

    def square_function(self,slope = 1, coefficient = 0):
        return slope * (pow(self.x,2)) + coefficient

x = np.linspace(-5,5,100)
z = igf.SquareFunction(x,3,25)
graph = Graph(z.Equation(),z.Label())
graph.plot()
# print(z.Label())