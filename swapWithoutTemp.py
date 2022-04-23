"""
lets see how we can swap the values of two variable without using temp variable
"""

a = 10
b = 20
print("Before swap:", end=" ")
print(f"A = {a} B = {b}")

# this method only usable if the value to be swaped are integers
a = (a+b)-(b:=a)
print("(a+b)-(b:=a):", end=" ")
print(f"A = {a} B = {b}")

# this is more direct way to sway values and there is no limited of data type of the variables
a,b = b,a
print("a,b = b,a:", end=" ")
print(f"A = {a} B = {b}")

"""
the output will be...

Before swap: A = 10 B = 20
(a+b)-(b:=a): A = 20 B = 10
a,b = b,a: A = 10 B = 20
"""