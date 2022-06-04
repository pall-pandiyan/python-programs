# comments are lines that we announce the compiler to skip executing
# in python to make a line comment we need to use hashtag "#"
# to make a multiple line comment we need to enclose them using three single or double quotes (''' or """)

# this is a single line comment

''' this
is
multi line
comments '''

""" this
is also
multi line
comments """


# in python we dont need to specify the datatype of the variale, python will assume the type dynamically. we can  variable name, "=" and ofcourse the value to be assigned.

# variabel naming rules:
# variable name should only contain alphabet, number and underscore ("_")
# variable name should start with a alphabet or underscore but not numbers.
# python variables are case sensitive.
# number values can be full numbers or integers (int) or floating point values (float)
# string data should enclosed with either sigle or double quote (' ' or " ")
marks = 83.7
greetings = 'hello everyone!'
complexNo = 5+0j

# we can get the value from user using "input()", we can insert a string as query inside the brackets.
# "strip()" function to strip off left and right excess spaces.
# the user input usually of type string, so "int()" function is to convert it to integer.
name = input("Enter your name:").strip()
age = int(input("Enter your age:").strip())

# we can assign multiple variables with multiple values in single line using comma (,)
no1, no2, no3 = 1, 2, 3

# we can assign a single value to multiple variables using equal "=" sign
no4 = no5 = no6 = 10


# use print() function to print someting out in the standard output
# we can directly enter string data enclosed with single or double quote to print out string data
# or specify variable name to print its value
# we can print multiple values seperated by comma (,) Note: using comma (,) will include a space in the output. we can modify it using sep keyword. using sep="-" will include a hypen.
# every print() function will insert a newline charactor at the end of the line, we can modify it using "end" keyword. end=" " will include a space at the end of the line
print("Age:",age)   # Age: 20
print("Marks",marks,sep=": ")    # Marks:83.7
print(greetings,"I am",name)
print("complex number:",complexNo)

# to figure out the type of a variable we can use type() function
print("Type of name",type(name))
print("Type of age",type(age))
print("Type of marks",type(marks))
print("Type of complexNo",type(complexNo))

# to completely detete a variable we can use a "del" keyword
del name, age, marks, greetings, complexNo
del no1, no2, no3, no4, no5, no6

# we can't refer the variable anymore
# if we do it will throw an error, the varriable is not defined
#print(name)

"""
the output will be...

Enter your name:Rajesh
Enter your age:24
Age: 24
Marks: 83.7
hello everyone! I am Rajesh
complex number: (5+0j)
Type of name <class 'str'>
Type of age <class 'int'>
Type of marks <class 'float'>
Type of complexNo <class 'complex'>

"""