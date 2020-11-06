#Other scripts in ShapeCalc
import IConvexPoly as icp
import IGraphingFunctions as igf
import GraphingScript as gs

#Python libraries
import matplotlib.pyplot as plt
import numpy as np
import enum

#class that contains methods for getting user input 
#for calculating 2d shapes
class ShapeCalcInput:

    #gets base of triangle from user input
    def Get_Triangle_Input(new_graph):
        get_base = float(input("input the Base Length: "))
        new_tri = icp.Triangle(get_base)
        vertices = new_tri.Get_Vertices()
        triangle = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
        new_graph.icp_object = new_tri
        new_graph.patches = triangle

    #gets base and height of rectangle from user input
    def Get_Rectangle_Input(new_graph):
        get_base = float(input("input the Base Length: "))
        get_height = float(input("input the Height Length: "))
        new_rect = icp.Rectangle(get_base,get_height)
        rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
        new_graph.icp_object = new_rect
        new_graph.patches = rectangle

    #gets base from user input for a square from user input
    def Get_Square_Input(new_graph):
        get_base = float(input("input the Base Length: "))
        new_rect = icp.Rectangle(get_base,get_base)
        rectangle = plt.Rectangle((0,0), new_rect.base, new_rect.height, fc = 'grey' , ec = 'red')
        new_graph.icp_object = new_rect
        new_graph.patches = rectangle

    #gets base1, base2, and height for a trapezoid from user input
    def Get_Trapezoid_Input(new_graph):
        get_base1 = float(input("input the Base1 Length: "))
        get_base2 = float(input("input the Base2 Length: "))
        get_height = float(input("input the Height Length: "))
        new_trap = icp.Trapezoid(get_base1,get_base2,get_height)
        vertices = new_trap.Get_Vertices()
        trapezoid = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
        new_graph.icp_object = new_trap
        new_graph.patches = trapezoid

    #gets base of hexagon from user input for a hexagon from user input
    def Get_Hexagon_Input(new_graph):
        get_base = float(input("input the base length: ")) 
        new_hex = icp.Hexagon(get_base)
        vertices = new_hex.Get_Vertices()
        hexagon = plt.Polygon(vertices, closed = True, fc = 'grey', ec = 'red')
        new_graph.icp_object = new_hex
        new_graph.patches = hexagon

#class that contains methods for getting user input 
#for calculating graphing functions 
class GraphCalcInput:

    #gets slope and coefficient for a linear function from user input
    def Get_LinearFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.LinearFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()

    #gets slope and coefficient for a square function from user input
    def Get_SquareFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.SquareFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()
    
    #gets slope and coefficient for a cubic function from user input
    def Get_CubicFunction_Input(new_graph,x_values):
        get_slope = float(input("input the slope of the equation: "))
        get_coefficient =  float(input("input the coefficient of the equation: "))
        y_values = igf.CubicFunction(x_values,get_slope,get_coefficient)
        new_graph.y  = y_values.Equation() 
        new_graph.label = y_values.Label()

#enumeration that contains the calculation types for ShapeCalc
class ShapeCalcInputCalculationCase(enum.Enum):
    triangle = 1
    rectangle = 2
    square = 3
    trapezoid = 4
    hexagon = 5

#enumeration that contains the calculation types for GraphCalc
class GraphCalcInputCalculationCase(enum.Enum):
    LinearFunction = 1
    SquareFunction = 2
    CubicFunction = 3

#switch statement that switches the calculations for ShapeCalc
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

#switch statement that switches the calculations for Graphcalc
def GraphCalc_Calculation_Switch(user_choice,new_graph,x_values):
    casenum = GraphCalcInputCalculationCase(user_choice)
    if casenum == GraphCalcInputCalculationCase.LinearFunction:
        GraphCalcInput.Get_LinearFunction_Input(new_graph,x_values)

    if casenum == GraphCalcInputCalculationCase.SquareFunction:
        GraphCalcInput.Get_SquareFunction_Input(new_graph,x_values)

    if casenum == GraphCalcInputCalculationCase.CubicFunction:
        GraphCalcInput.Get_CubicFunction_Input(new_graph,x_values)

#lists the calculation types possible then gets input from user
#passes user_choice and new_graph to the calculation switch 
#plots graph
def ShapeCalc():
    print("\nwelcome to a shape calculator!")
    new_graph = gs.GraphShape()

    for cases in ShapeCalcInputCalculationCase:
        print(F'--{cases.name} {cases.value}--')

    user_choice = int(input("\ninput a selection: "))
    ShapeCalc_Calculation_Switch(user_choice,new_graph)
    gs.GraphShape().Plot_Graph(new_graph)

#lists the calculation types possible then gets input from user
#x_values is the approximated linespace of a function
#passes user_choice,new_graph, and x_values to the calculation switch 
#plots graph
def GraphCalc():
    print("\nwelcome to a shape calculator!")
    new_graph = gs.GraphFunction()
    x_values = np.linspace(-5,5,100)

    for cases in GraphCalcInputCalculationCase:
        print(F'--{cases.name} {cases.value}--')

    user_choice = int(input("\ninput a selection: "))
    GraphCalc_Calculation_Switch(user_choice,new_graph,x_values)
    gs.GraphFunction.Plot_Graph(new_graph)
