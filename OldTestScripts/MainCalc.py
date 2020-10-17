import CalcFunctions

class Program:

    calculation_type_list = [
        "Regular Quadrilaterals",
        "Circle Area",
        "Circle Circumference",
        "Sphere Surface Area",
        "Sphere Volume"
    ]
    calculation = None
    calculation_function = None
    calculation_answer = None
    memory = []

    def get_input_regular_quadrilaterals(self):
        unit_of_measurement = input("\nEnter Unit Of Measurement: ")
        base1 = float(input("Enter The Length in {} Of The First Base: ".format(unit_of_measurement)))
        base2 = float(input("Enter The Length in {} Of The Second Base(For Trapezoids,Same As Base One For Other Regular Quads): ".format(unit_of_measurement)))
        height = float(input("Enter The Height in {} Of The Trapezoid: ".format(unit_of_measurement)))

        self.calculation = CalcFunctions.Regular_Quadrilaterals(unit_of_measurement, base1, base2, height)
        self.calculation_function = CalcFunctions.Regular_Quadrilaterals.calculate_reg_quad_area
        self.execute_calculation()

    def get_input_circle_area(self):
        unit_of_measurement = input("\nEnter Unit Of Measurement: ")
        radius = float(input("Enter The Length in {} Of The Radius: ".format(unit_of_measurement)))

        self.calculation = CalcFunctions.Circle_Area_Circumference(unit_of_measurement, radius)
        self.calculation_function = CalcFunctions.Circle_Area_Circumference.calculate_circle_area
        self.execute_calculation()

    def get_input_circle_circumference(self):
        unit_of_measurement = input("\nEnter Unit Of Measurement: ")
        radius = float(input("Enter The Length in {} Of The Radius: ".format(unit_of_measurement)))

        self.calculation = CalcFunctions.Circle_Area_Circumference(unit_of_measurement, radius)
        self.calculation_function = CalcFunctions.Circle_Area_Circumference.calculate_circumference
        self.execute_calculation()

    def get_input_sphere_surface_area(self):
        pass

    #Function That Lets The User Choose To Start A New Calculation
    def user_continue_choice(self):
        user_choice = input("\nEnter New Calculation? y/n: ")
        if user_choice.lower() == "y":
            print("\nOk")
        elif user_choice.lower() == "n":
            exit()

    def user_calculation_choice(self):
        print("\n----Select A Calculation----")
        print("----Or Type mem For Memory----")
        number_of_calculation_types = 0
        for x in self.calculation_type_list:
            print("--{} {}--".format(x, number_of_calculation_types))
            number_of_calculation_types += 1
        selected_calculation = input("\nInputHere (0-{}): ".format(number_of_calculation_types - 1))

        if selected_calculation == "0":
            self.get_input_regular_quadrilaterals()
        elif selected_calculation == "1":
            self.get_input_circle_area()
        elif selected_calculation == "2":
            self.get_input_circle_circumference()
        elif selected_calculation == "mem".lower():
            self.print_memory()


    def execute_calculation(self):
        self.calculation_answer = self.calculation_function(self.calculation)
        self.memory.append(self.calculation_answer)
        print(self.calculation_answer)

    def print_memory(self):
        print("\n")
        for x in self.memory:
            print("--{}--".format(x))

    def main(self):
        print("\n----Shape Calculator----")
        running = True
        while running:
            self.user_continue_choice()
            self.user_calculation_choice()

Program().main()

