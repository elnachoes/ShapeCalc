import numpy as np
import enum
import matplotlib.pyplot as plt
import IConvexPoly as icp
import IGraphingFunctions as igf
import GraphingScript as gs
from IConvexPoly import Trapezoid

class ShapeCalcInput():

    #Gets base of triangle from user input
    #new_graph is what the shape will be graphed onto
    def Get_Triangle_Input(new_graph):
        get_base = float(input("input the Base Length: "))
        new_tri = icp.Triangle(get_base)
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
        rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
        new_graph.icp_object = new_rect
        new_graph.patches = rectangle
        # Convert_icp_Rectangle(new_rect,new_graph)

    #Gets base from user input
    #new_graph is what the shape will be graphed onto
    def Get_Square_Input(new_graph):
        get_base = float(input("input the Base Length: "))
        new_rect = icp.Rectangle(get_base,get_base)
        rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
        new_graph.icp_object = new_rect
        new_graph.patches = rectangle

    def Get_Trapezoid_Input(new_graph):
        get_base1 = float(input("input the Base1 Length: "))
        get_base2 = float(input("input the Base2 Length: "))
        get_height = float(input("input the Height Length: "))
        new_trap = icp.Trapezoid(get_base1,get_base2,get_height)
        vertices = new_trap.Get_Vertices()
        trapezoid = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
        new_graph.icp_object = new_trap
        new_graph.patches = trapezoid

    #Gets base of hexagon from user input
    #new_graph is what the shape will be graphed onto
    def Get_Hexagon_Input(new_graph):
        get_base = float(input("input the base length: ")) 
        new_hex = icp.Hexagon(get_base)
        vertices = new_hex.Get_Vertices()
        hexagon = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
        new_graph.icp_object = new_hex
        new_graph.patches = hexagon

#enumeration that contains the calculation types
class ShapeCalcInputCalculationCase(enum.Enum):
    triangle = 1
    rectangle = 2
    square = 3
    trapezoid = 4
    hexagon = 5

#switch statement that switches the calculations
#creates new graph and plots the new graph
def ShapeCalc_Calculation_Switch(user_choice,new_graph):
    casenum = ShapeCalcInputCalculationCase(user_choice)
    if casenum == ShapeCalcInputCalculationCase.triangle:
        ShapeCalcInput.Get_Triangle_Input(new_graph)
    if casenum == ShapeCalcInputCalculationCase.rectangle:
        ShapeCalcInput.Get_Rectangle_Input(new_graph)
    if casenum == ShapeCalcInputCalculationCase.square:
        ShapeCalcInput.Get_Square_Input(new_graph)
    if casenum == ShapeCalcInputCalculationCase.trapezoid:
        ShapeCalcInput.Get_Trapezoid_Input(new_graph)
    if casenum == ShapeCalcInputCalculationCase.hexagon:
        ShapeCalcInput.Get_Hexagon_Input(new_graph)

#lists the calculation types possible then gets input from user
#passes user_choice and new_graph to the calculation switch 
#plots graph
def ShapeCalc():
    new_graph = gs.GraphShape()
    print("\nwelcome to a shape calculator!")
    for cases in ShapeCalcInputCalculationCase:
        print(F'--{cases.name} {cases.value}--')
    user_choice = int(input("\ninput a selection: "))
    ShapeCalc_Calculation_Switch(user_choice,new_graph)
    gs.GraphShape().Plot_Graph(new_graph)


class GraphCalcInput:
    
    def Get_LinearFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.LinearFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()

    def Get_SquareFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.SquareFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()
    
    def Get_CubicFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.CubicFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()

class GraphCalcInputCalculationCase(enum.Enum):
    LinearFunction = 1
    SquareFunction = 2
    CubicFunction = 3

def GraphCalc_Calculation_Switch(user_choice,new_graph,x_values):
    casenum = GraphCalcInputCalculationCase(user_choice)
    if casenum == GraphCalcInputCalculationCase.LinearFunction:
        GraphCalcInput.Get_LinearFunction_Input(new_graph,x_values)
    if casenum == GraphCalcInputCalculationCase.SquareFunction:
        GraphCalcInput.Get_SquareFunction_Input(new_graph,x_values)
    if casenum == GraphCalcInputCalculationCase.CubicFunction:
        GraphCalcInput.Get_CubicFunction_Input(new_graph,x_values)

def GraphCalc():
    new_graph = gs.GraphFunction()
    x_values = np.linspace(-5,5,100)
    print("\nwelcome to a shape calculator!")
    for cases in GraphCalcInputCalculationCase:
        print(F'--{cases.name} {cases.value}--')
    user_choice = int(input("\ninput a selection: "))
    GraphCalc_Calculation_Switch(user_choice,new_graph,x_values)
    gs.GraphFunction.Plot_Graph(new_graph)
