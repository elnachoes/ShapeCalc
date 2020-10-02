import matplotlib.pyplot as plt
import IConvexPoly as icp
from GraphingScript import Graph as Graph
from IConvexPoly import Trapezoid

#Gets base of triangle from user input
#new_graph is what the shape will be graphed onto
def Get_Triangle_Input(new_graph):
    get_base = float(input("input the Base Length: "))
    new_tri = icp.Triangle(get_base)
    Convert_icp_Triangle(new_tri,new_graph)

#converts icp object new_tri into a polygon patch
def Convert_icp_Triangle(new_tri, new_graph):
    vertices = new_tri.Get_Vertices()
    triangle = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
    new_graph.icp_object = new_tri
    new_graph.patches = triangle

#Gets base and height of rectangle from user input
#new_graph is what the shape will be graphed onto
def Get_Rectangle_Input(new_graph):
    get_base = float(input("input the Base Length: "))
    get_height = float(input("input the Height Length: "))
    new_rect = icp.Rectangle(get_base,get_height)
    Convert_icp_Rectangle(new_rect,new_graph)

#Gets base from user input
#new_graph is what the shape will be graphed onto
def Get_Square_Input(new_graph):
    get_base = float(input("input the Base Length: "))
    new_rect = icp.Rectangle(get_base,get_base)
    Convert_icp_Rectangle(new_rect,new_graph)

#converts icp object new_rect into a rect patch
def Convert_icp_Rectangle(new_rect, new_graph):
    rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
    new_graph.icp_object = new_rect
    new_graph.patches = rectangle

def Get_Trapezoid_Input(new_graph):
    get_base1 = float(input("input the Base1 Length: "))
    get_base2 = float(input("input the Base2 Length: "))
    get_height = float(input("input the Height Length: "))
    new_trap = icp.Trapezoid(get_base1,get_base2,get_height)
    Convert_icp_Trapezoid(new_graph, new_trap)

def Convert_icp_Trapezoid(new_graph, new_trap):
    vertices = new_trap.Get_Vertices()
    trapezoid = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
    new_graph.icp_object = new_trap
    new_graph.patches = trapezoid

#Gets base of hexagon from user input
#new_graph is what the shape will be graphed onto
def Get_Hexagon_Input(new_graph):
    get_base = float(input("input the base length: ")) 
    new_hex = icp.Hexagon(get_base)
    Convert_icp_Hexagon(new_hex,new_graph)

#converts icp object new_hex into a polygon patch
def Convert_icp_Hexagon(new_hex, new_graph):
    vertices = new_hex.Get_Vertices()
    hexagon = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
    new_graph.icp_object = new_hex
    new_graph.patches = hexagon
