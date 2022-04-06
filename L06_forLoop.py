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
print("range upto 6:")
for x in range(6):
    print(x,end=" ")
print()

