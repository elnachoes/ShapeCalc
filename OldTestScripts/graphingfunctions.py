from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt 
import IGraphingFunctions as igf



class GraphFunction:
    def __init__(self,y, label = None):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.gx = plt.grid(b = True, which = 'major' ,axis = 'both',linewidth = 1, color = "red", linestyle = '--')
        self.y = y
        self.label = label
        # self.ax.spines['left'].set_position('center')
        # self.ax.spines['bottom'].set_position('zero')
        # self.ax.spines['right'].set_color('blue')
        # self.ax.spines['top'].set_color('blue')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

    def Plot(self, x_values = np.linspace(-5,5,100)):
        plt.plot(x_values,self.y, 'b', label = self.label)
        plt.legend(loc='upper left')
        plt.show() 


x = np.linspace(-100,100,100)
y = igf.LinearFunction(x,3,25)
graph = GraphFunction(y.Equation(),y.Label())
graph.Plot()
# print(z.Label())