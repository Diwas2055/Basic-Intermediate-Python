# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the 
# data members of the class when an object of the class is created. 
# In Python the __init__() method is called the constructor and 
# is always called when an object is created.

class Student:
    # creating Python constructor
    def __init__(self, name, age):
        # variables
        self.name = name
        self.age = age

    # Python class method

    def Print(self):
        # printing the name and age
        print("Student name is :", self.name)
        print("Student age is : ", self.age)


# creating object of type Student
student = Student('XYZ', 22)
# calling the Print method
student.Print()
