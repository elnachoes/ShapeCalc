#Other scripts in ShapeCalc
import UserInput as User

#Python libraries
import enum

#enumeration that contains the calculation types
class CalculationCase(enum.Enum):
    Shape_Calculator = 1
    Graphing_Calculator = 2

#switch statement that switches the calculations
#creates new graph and plots the new graph
def calculation_switch(user_choice):
    casenum = CalculationCase(user_choice)

    if casenum == CalculationCase.Shape_Calculator:
        User.ShapeCalc()

    if casenum == CalculationCase.Graphing_Calculator:
        User.GraphCalc()

#main function that creates a new graph
#lists the calculation types possible then gets input from user
#passes user_choice and new_graph to the calculation switch 
#plots graph
def main():
    print("\nwelcome to a cmd graphic calculator!")

    for cases in CalculationCase:
        print(F'--{cases.name} {cases.value}--')

    user_choice = int(input("\ninput a selection: "))
    calculation_switch(user_choice)

if __name__ == "__main__":
    main()
