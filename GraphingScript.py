import matplotlib.pyplot as plt
import IConvexPoly as icp

class Graph:
    def __init__(self, patches = None, irp_object = None):
        self.patches = patches
        self.irp_object = irp_object
        self.ax = plt.gca()
        self.gx = plt.grid(b = True, which = 'major' , axis = 'both')

    def Plot_Graph(self, value):
        value.ax.add_patch(value.patches)
        value.ax.set_title(F'Area = {value.irp_object.Area()} Perimeter = {value.irp_object.Perimeter()}')
        plt.axis("scaled")
        plt.show()