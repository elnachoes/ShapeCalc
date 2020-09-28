import enum
import matplotlib.pyplot as plt
import IRegularPoly as irp
from GraphingScript import Graph as Graph

def Get_Triangle_Input(new_graph):
    get_base = float(input("input the Base Length: "))
    new_tri = irp.Triangle(get_base)
    Convert_irp_Triangle(new_tri,new_graph)

def Convert_irp_Triangle(new_tri,new_graph):
    vertices = new_tri.Get_Vertices()
    triangle = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
    new_graph.irp_object = new_tri
    new_graph.patches = triangle

def Get_Rectangle_Input(new_graph):
    get_base = float(input("input the Base Length: "))
    get_height = float(input("input the Height Length: "))
    new_rect = irp.Rectangle(get_base,get_height)
    Convert_irp_Rectangle(new_rect,new_graph)

def Convert_irp_Rectangle(new_rect,new_graph):
    rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
    new_graph.irp_object = new_rect
    new_graph.patches = rectangle

#Gets base of hexagon from user input
#new_graph is what the shape will be graphed onto
def Get_Hexagon_Input(new_graph):
    get_base = float(input("input the base length: "))
    new_hex = irp.Hexagon(get_base)
    Convert_irp_Hexagon(new_hex,new_graph)

#converts irp object new_hex into a polygon patch
def Convert_irp_Hexagon(new_hex,new_graph):
    vertices = new_hex.Get_Vertices()
    hexagon = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
    new_graph.irp_object = new_hex
    new_graph.patches = hexagon

#enumeration that contains the calculation types
class Case(enum.Enum):
    triangle = 1
    rectangle = 2
    hexagon = 3

#switch statement that switches the calculations
#creates new graph and plots the new graph
def calculation_switch(user_choice):
    new_graph = Graph()
    casenum = Case(user_choice)
    if casenum == Case.triangle:
        Get_Triangle_Input(new_graph)
    if casenum == Case.rectangle:
        Get_Rectangle_Input(new_graph)
    if casenum == Case.hexagon:
        Get_Hexagon_Input(new_graph)
    Graph().Plot_Graph(new_graph)

def main():
    for cases in Case:
        print(F'--{cases.name} {cases.value}--')
    user_choice = int(input("input a selection: "))
    calculation_switch(user_choice)

main()

