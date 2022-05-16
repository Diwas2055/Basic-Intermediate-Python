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
