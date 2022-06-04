# if statement is used to control the execution flow of the program

age = int(input("Enter your age: ").strip())

print("Typical if else statement:")
if age<18:
    print("Entry denied!")
else:
    print("Entry granted!")

# in this segment we get the input from user, strip off its excess spaces, convert in into integer and store it into variable named "age"
# the "if" keyword checks a condition (if age is less than 18, but not 18), if it is true it will follow this flow.
# if the condition is not true, the else segment will executed.

# we can do the same thing in one line using one line if else statement
print("one line if else statement:")
print("Entry denied!") if age > 18 else print("Entry granted!")


'''
Comparison operators are used to compare two values:

Operator 	Name 	                    Example
    == 	    Equal 	                    x == y
    != 	    Not equal 	                x != y
    > 	    Greater than 	            x > y
    < 	    Less than 	                x < y
    >= 	    Greater than or equal to 	x >= y
    <= 	    Less than or equal to 	    x <= y
'''

'''
Logical operators are used to combine conditional statements:

Operator 	Description 	                Example
    and  	Returns True if both statements are true 	                            x < 5 and  x < 10
    or 	    Returns True if one of the statements is true 	                           x < 5 or x < 4
    not 	Reverse the result, returns False if the result is true 	        not(x < 5 and x < 10)
'''

'''
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator 	Description 	Example
    is  	Returns True if both variables are the same object 	            x is y
    is not 	Returns True if both variables are not the same object 	        x is not y
'''

'''
Membership operators are used to test if a sequence is presented in an object:

Operator 	Description 	Example
    in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
    not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y 	
'''

"""
the output will be...

Enter your age: 18
Typical if else statement:
Entry granted!
one line if else statement:
Entry granted!
"""