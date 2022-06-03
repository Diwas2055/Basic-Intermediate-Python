# Dataclass is a decorator defined in the dataclasses module.
# It was introduced in python 3.7. 
# A dataclass decorator can be used to implement classes that define objects with only data and very minimal functionalities. 


#! Without dataclasses we should write the following code: Using repr() Method
class Person:
    def __init__(self, name, country, age):
        self.Name = name
        self.Country = country
        self.Age = age

    # repr() Function returns a printable representation of the object passed to it.
    # repr() function calls __repr__() of the given object
    # You can easily implement/override __repr__() so that repr() works differently.
    # defining __repr__() method to control what
    # to return for objects of Person
    
    def __repr__(self):
        return "Name: {}, Country: {}, Age: {}".format(self.Name, self.Country, self.Age)


candidate = Person("Joe Biden", "USA", 78)
print("Without dataclasses:-")
print("The candidate is:", candidate)



#! With dataclasses we can write the following code:
from dataclasses import dataclass

@dataclass
class Person:
    Name: str
    Country: str
    Age: int


candidate = Person("Joe Biden", "USA", 78)
print("With dataclasses:-")
print("The candidate is:",candidate)


#!  Optimizing Data Classes
from dataclasses import dataclass

# A memory profiler for Python.
from pympler import asizeof

# Slots can be used to make classes faster and use less memory. 
# Data classes have no explicit syntax for working with slots,
# but the normal way of creating slots works for data classes as well.

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    # A way to tell Python not to use a dict, and only allocate space for a fixed set of attributes.
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
print("Simple Position:",simple)
print("Slot Position:",slot)
print("Size of Simple Position:",asizeof.asizeof(simple))
print("Size of Slot Position:",asizeof.asizeof(slot))
