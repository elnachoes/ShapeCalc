#Other scripts in ShapeCalc
import IConvexPoly as icp
import IGraphingFunctions as igf

#Python libraries
import matplotlib.pyplot as plt
import numpy as np
import abc 

class IMatPlotGraphing(abc.ABC):
    @abc.abstractmethod
    def Graph_Setup():
        return 0

    @abc.abstractmethod
    def Plot_Graph():
        return 0 

class GraphShape(IMatPlotGraphing):
    def __init__(self, patches = None, icp_object = None):
        self.patches = patches
        self.icp_object = icp_object
        self.Graph_Setup()

    def Graph_Setup(self):        
        self.ax = plt.gca()
        self.gx = plt.grid(b = True, which = 'major' , axis = 'both')

    def Plot_Graph(self, value):
        value.ax.add_patch(value.patches)
        value.ax.set_title(f'Area = {value.icp_object.Area()} Perimeter = {value.icp_object.Perimeter()}',fontweight='bold',color='blue')
        plt.axis('scaled')
        plt.show()

class GraphFunction(IMatPlotGraphing):
    def __init__(self,y = None, label = None):
        self.y = y
        self.label = label
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.Graph_Setup()

    def Graph_Setup(self):
        self.gx = plt.grid(b = True, which = 'major' ,axis = 'both',linewidth = 1, linestyle = '--')
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

    def Plot_Graph(self):
        x_values = np.linspace(-5,5,100)
        plt.plot(x_values,self.y, 'b', label = self.label)
        plt.legend(loc = 'upper left')
        plt.axis('square')
        plt.show() 

