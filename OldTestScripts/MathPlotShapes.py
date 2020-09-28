import matplotlib.pyplot as plt
import numpy as np
import IRegularPoly as irp 

def Get_Triangle_Input():
    get_base = int(input("input the Base Length: "))
    new_tri = irp.Triangle(get_base)
    Convert_irp_Triangle(new_tri)

def Convert_irp_Triangle(new_tri):
    vertices = new_tri.Get_Vertices()
    triangle = plt.Polygon(vertices,closed=True,fc='grey',ec='red')
    Build_Graph(triangle, new_tri)

def Get_Rectangle_Input():
    get_base = int(input("input the Base Length: "))
    get_height = int(input("input the Height Length: "))
    new_rect = irp.Rectangle(get_base,get_height)
    Convert_irp_Rectangle(new_rect)

def Convert_irp_Rectangle(new_rect):
    rectangle = plt.Rectangle((0,0),new_rect.base,new_rect.height,fc='grey',ec='red')
    Build_Graph(rectangle, new_rect)

def Get_Hexagon_Input():
    get_base = int(input("input the base length: "))
    new_hex = irp.Hexagon(get_base)
    Convert_irp_Hexagon(new_hex)

def Convert_irp_Hexagon(new_hex):
    vertices = new_hex.Get_Vertices()
    hexagon = plt.Polygon(vertices,closed=True,fc='grey',ec='red')
    Build_Graph(hexagon, new_hex)

def Build_Graph(plot_object,irp_object):
    ax = plt.gca()
    gx = plt.grid(b=True,which='major',axis='both')
    ax.add_patch(plot_object)
    ax.set_title(F'Area = {irp_object.Area()} Perimeter = {irp_object.Perimeter()}')
    plt.axis("scaled")
    plt.show()

def graph():
    ax = plt.gca()
    plt.axis("scaled")
    plt.show()

# graph()
# Get_Hexagon_Input()

# Get_Triangle_Input()
# Get_Rectangle_Input()
# x = None
# y = None
# z = None
# op = None

# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)

