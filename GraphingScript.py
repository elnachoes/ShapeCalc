import matplotlib.pyplot as plt
import IConvexPoly as icp

class Graph:
    def __init__(self, patches = None, icp_object = None):
        self.patches = patches
        self.icp_object = icp_object
        self.ax = plt.gca()
        self.gx = plt.grid(b = True, which = 'major' , axis = 'both')

    def Plot_Graph(self, value):
        value.ax.add_patch(value.patches)
        value.ax.set_title(F'Area = {value.icp_object.Area()} Perimeter = {value.icp_object.Perimeter()}')
        plt.axis("scaled")
        plt.show()