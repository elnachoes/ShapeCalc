from math import pi

dimension_of_measurement = None

class Regular_Quadrilaterals:
    def __init__(self, unit_of_measurement, base1, base2, height):    
        self.unit_of_measurement = unit_of_measurement
        self.base1 = base1
        self.base2 = base2
        self.height = height 

    def calculate_reg_quad_area(self):
        area = ((self.base1 + self.base2) / 2) * self.height
        dimension_of_measurement = "Squared"
        return "The Area Of The Regular Quadrilateral Is {} {} {}".format(area,self.unit_of_measurement,dimension_of_measurement)

class Circle_Area_Circumference():
    def __init__(self, unit_of_measurement, radius):
        self.unit_of_measurement = unit_of_measurement
        self.radius = radius

        #Function That Calculates Circumference 
    def calculate_circumference(self):
        area = (self.radius ** 2) * pi
        dimension_of_measurement = "Long"
        return "The Circumference Of The Area Is {} {} {}".format(area,self.unit_of_measurement,dimension_of_measurement)

    #Function That Calculates Circle Area
    def calculate_circle_area(self):
        circumference = self.radius * (2 * pi)
        dimension_of_measurement = "Squared"
        return "The Circumference Of The Circle Is {} {} {}".format(circumference,self.unit_of_measurement,dimension_of_measurement)

class Sphere_Volume_Surface_Area():
    def __init__(self):
        self.unit_of_measurement = unit_of_measurement
        self.radius = radius

    def calculate_sphere_volume(self):
        sphere_volume = (self.radius ** 3) * ((4/3) * pi)
        dimension_of_measurement = "Cubed"
        return "The Volume of the Sphere Is {} {} {}".format(sphere_volume,self.unit_of_measurement, dimension_of_measurement)
    
    #Function That Calculates Sphere Surface Area
    def calculate_sphere_surface_area(self):
        sphere_surface_area = (self.radius ** 2) * (4 * pi)
        dimension_of_measurement = "Squared"
        return "The Surface Area Of The Sphere Is {} {} {}".format(sphere_surface_area, self.unit_of_measurement, dimension_of_measurement)