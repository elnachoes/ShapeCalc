class Square:
    def __init__(self, base=0):
        self.base = base
    
    # def __del__(self):
    #     print("square deleted")

    @property
    def base(self):
        # print("getter")
        return self._base

    @base.setter
    def base(self, value):
        # print("setter")
        self._base = value

    @property
    def area(self):
        # print("getter")
        return self.base ** 2

x = Square(5)
# print(x.base)
print(x.area)

x.base = 6
# print(x.base)
print(x.area)

# print(x.Get_Area())
# print(x.__dict__)