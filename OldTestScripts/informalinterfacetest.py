class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and callable(subclass.name) and hasattr(subclass, 'age') and callable(subclass.age))


class Person(metaclass = PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        return self.name

    def age(self):
        return self.age

#bradyn = Friend("Bradyn", 18)
#print(issubclass(Friend, Person))
#print(isinstance(Friend, bradyn))
#print(Friend.__mro__)


