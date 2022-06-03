# Dataclass is a decorator defined in the dataclasses module.
# It was introduced in python 3.7. 
# A dataclass decorator can be used to implement classes that define objects with only data and very minimal functionalities. 

# The syntax of the dataclass is:

# Syntax: @dataclasses.dataclass(*, init=True, repr=True, 
#                                    eq=True, order=False, unsafe_hash=False, 
#                                    frozen=False)

# Parameters:-

#     init: If true  __init__() method will be generated
#     repr: If true  __repr__() method will be generated
#     eq: If true  __eq__() method will be generated
#     order: If true  __lt__(), __le__(), __gt__(), and __ge__() methods will be generated.
#     unsafe_hash: If False __hash__() method is generated according to how eq and frozen are set
#     frozen: If true assigning to fields will generate an exception.


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


# dataclasses.Field()

# The field() objects describe each defined field.  

# -> Syntax: dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True, 
#                               hash=None, init=True, compare=True, metadata=None)

# Parameters:
#   ->  default : This field is used to specify default values for this field.
#   ->  default_factory : This field accepts a function and returns the initial value of the field, it must be a zero-argument.
#   ->  init : If true this field is included as a parameter to the generated __init__() method.
#   ->  repr : If true (the default), this field is included in the string returned by the generated __repr__() method.
#   ->  hash : If true, this field is included in the generated __hash__() method.
#   ->  compare : If true (the default), this field is included in the generated equality and comparison methods (__eq__(), __gt__().
#   ->  metadata : This can be a mapping or None. None is treated as an empty dict.

# Importing the dataclass and field from the dataclasses module.
from dataclasses import dataclass, field
@dataclass()
class Student():
    name: str
    stu_id: int
    # Defining a class attribute with a default value.
    clss: int = field(default=10)


student = Student('HTD', 17)
print(student)

