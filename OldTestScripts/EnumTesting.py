import enum
class Case(enum.Enum):
    case1 = 1
    case2 = 2


user_input = int(input("pick a case, 1-2: "))
casenum = Case(user_input)

def case1():
    print("this is case 1")

def case2():
    print("this is case 2")

if casenum == Case.case1:
    case1()
if casenum == Case.case2:
    case2()

