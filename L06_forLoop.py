# A "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
print("elements in fruits:",end=" ")
for x in fruits:
    print(x,end=" ")
print()

# Loop through the letters in the word "banana"
print("Charactors in 'banana:",end=" ")
for x in "banana":
    print(x,end=" ")
print()

# With the "break" statement we can stop the loop before it has looped through all the items:
print("Print everything before banana:",end=" ")
for x in fruits:  
    if x == "banana":
        break
    print(x,end=" ")
print()

# With the "continue" statement we can stop the current iteration of the loop, and continue with the next:
print("Skip a iteration if the element is 'banana':",end=" ")
for x in fruits:
    if x == "banana":
        continue
    print(x,end=" ")
print()

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note: the specified last number will not be included.
print("range upto 6:")
for x in range(6):
    print(x,end=" ")
print()

# print the range 
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
print("range between 2 to 30 incremented by 3:")
for x in range(2,30,3):
    print(x,end=" ")
else:
    print()

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
print("Nested loops:")
adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y,end=" ")
    print()

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass

"""
the output will be...

elements in fruits: apple banana cherry 
Charactors in 'banana: b a n a n a 
Print everything before banana: apple 
Skip a iteration if the element is 'banana': apple cherry 
range upto 6:
0 1 2 3 4 5 
range between 2 to 30 incremented by 3:
2 5 8 11 14 17 20 23 26 29 
Nested loops:
red apple red banana red cherry 
big apple big banana big cherry 
tasty apple tasty banana tasty cherry 
"""