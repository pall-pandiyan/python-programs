# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printValues(self):
        print("Name is",self.name)
        print("Age is",self.age)


# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    def __init__(self, name, age, year):
        # we can use super() function or directly the parent class name to initialise its constrator
        super().__init__(name,age)
        self.year = year

    def printValues(self):
        super().printValues()
        print("Year is",self.year)
    
obj = Student("Bill", 23, 2021)
obj.printValues()

"""
the output will be...
Name is Bill
Age is 23
Year is 2021
"""