# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# to create a class use the keyword "class"
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class myClass:
    name = ""
    age = 0

    # All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # added a function into the class to print its members
    def printValues(self):
        print("Name is",self.name)
        print("Age is",self.age)

# creating object to the class
obj = myClass("Jhon",36)
obj.printValues()

# You can delete properties on objects by using the del keyword:
del obj.name, obj.age

# You can delete objects by using the del keyword:
del obj

"""
the output will be...
Name is Jhon
Age is 36

"""