import enum
import UserInput as User
from GraphingScript import Graph 

#enumeration that contains the calculation types
class Calculationcase(enum.Enum):
    triangle = 1
    rectangle = 2
    square = 3
    hexagon = 4

#switch statement that switches the calculations
#creates new graph and plots the new graph
def calculation_switch(user_choice,new_graph):
    casenum = Calculationcase(user_choice)
    if casenum == Calculationcase.triangle:
        User.Get_Triangle_Input(new_graph)
    if casenum == Calculationcase.rectangle:
        User.Get_Rectangle_Input(new_graph)
    if casenum == Calculationcase.square:
        User.Get_Square_Input(new_graph)
    if casenum == Calculationcase.hexagon:
        User.Get_Hexagon_Input(new_graph)

#main function that creates a new graph
#lists the calculation types possible then gets input from user
#passes user_choice and new_graph to the calculation switch 
#plots graph
def main():
    new_graph = Graph()
    for cases in Calculationcase:
        print(F'--{cases.name} {cases.value}--')
    user_choice = int(input("input a selection: "))
    calculation_switch(user_choice,new_graph)
    Graph().Plot_Graph(new_graph)

main()

