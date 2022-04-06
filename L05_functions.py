# functions are block of code that will run when we can the funtion. we can call the function any number of times. its general practice to group a block of codes that we use repeatly as a function.

# in python a function can be defined using keywor "def" keyword folowed by a unique name and round brackets "()"
def hello():
    print("Hello word!")

# to call the defined function we can use function name and round brackets "()"
hello()

# to pass a value to the function from the function calling side, we have to specify the name and number of values inside the round brackets "()"
def printString(name):
    print(name)

printString("Rahul")

# we can also return a value to the calling point from the function using "return" keyword
def returnStr(name):
    return ("The name is "+name)

print(returnStr("Dhinesh"))

# if we do not know the number of values to be passed into a function we can use "*" before varriable name to store any number of arguments as list.
def my_function(*args):
    print(args)
my_function("one","two","three","Four")

# same as above but to pass unknown number of key/value pairs use "**" before varriable name to store as dictionary.


# to store a default value for an argument in function we can use "=" to store it. if we do not pass a value for that argument the default value will be used.
def myFunction(name="Unavailable"):
    print("The name is",name)
myFunction()        # The name is Unavailable
myFunction("Harry") # The name is Harry


# a recursion is when a function is repeately call itself to perform some tasks.
print("Figuring odd or even using recursion: ",end=" ")
def oddOrEven(number):
    if (number == 0 or number == 1):
        return "Even Number!"
    elif (number == 1):
        return "Odd Number!"
    else:
        return oddOrEven(number-2)

print(oddOrEven(9))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print("Lambda function:",end=" ")
print(x(5))

#Lambda functions can take any number of arguments:
x= lambda a,b : a*b
print("Lambda with 2 args:",end=" ")
print(x(5,10))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print("The doubler:",mydoubler(11))
print("The tripler:",mytripler(11))

'''
the output will be...

Hello word!
Rahul
The name is Dhinesh
('one', 'two', 'three', 'Four')
The name is Unavailable
The name is Harry
Figuring odd or even using recursion:  Even Number!
Lambda function: 15
Lambda with 2 args: 50
The doubler: 22
The tripler: 33
'''