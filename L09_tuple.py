# tuple items are ordered, unchangable, allows duplicates and contains any type of data (even other tuple).
# in this program we will review how to create, modify and manipulate a tuple

# tuple is defined using round brackets "()"
aTuple = ("apple", "orange", "grape")
print("aTuple is:",aTuple)

# to find how many elements a tuple have, we can use len() function
print("The length of aTuple is:",len(aTuple))

# we can count a specific item in the tuple using count() function
print("The count of apple is:",aTuple.count("apple"))

# we can figure out the first index of a specified value
print("The first index of orange is:",aTuple.index("orange"))

# as usual we can figure out the type of the varriable by using type() function
print("The type of the aTuple is:",type(aTuple))

# using tuple() function to copy or define a tuple
bTuple = tuple(aTuple)
cTuple = tuple(("banana", "watermelon"))
print("bTuple is:",bTuple)
print("cTuple is:",cTuple)

# printing a tuple using for loop
print("Printing aTuple using for loop:",end=" ")
for x in aTuple:
    print(x,end=" ")
print()

# acessing items in tuple using index value
print("Aceessing values using index:", end=" ")
for x in range(len(aTuple)):
    print(aTuple[x],end=" ")
print()

# acessing item in tuple using negative value
print("Acessing values using negative index:",end=" ")
for x in range(1,len(aTuple)+1):
    print(aTuple[-x],end=" ")
print()

# print using while loop
print("Print aTuple using while loop:",end=" ")
i=0
while(i<len(aTuple)):
    print(aTuple[i],end=" ")
    i+=1
print()

# overwritting a value in tuple
# tuple is unchangable, we cannot overwrite a existing value
# however we can convert in to list, make the neceesary changes and convert it back to tuple
tempList = list(aTuple)
tempList[2] = "mango"
aTuple = tuple(tempList)
print("Changed list:",aTuple)

# tuple is immutable so we cannot add a value like list
# but we can add another tuple using "+" symbol
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
aTuple += ("grape",)
print("Added grape in aTuple:",aTuple)

# we can use "*" symbol to multiply a tuple just like string
xTuple = aTuple*3
print("aTuple * 3 is:", xTuple)
del xTuple

# we cannot remove a value in a tuple directly,
# we can workaround by converting it to a list, make the changes and convert back into a tuple.
# using del keyword we can delete a tuple entirely
del bTuple
del cTuple
# print(bTuple) # will generate an error 'bTuple' is not defined.

# unpacking is assigning items in the tuples to variables,
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
(var1,var2,var3,var4) = aTuple
print("unpacked vars:",var1,var2,var3,var4)
del var1,var2,var3,var4

(a,b,*waste_list) = aTuple
print("The needed a,b:",a,b)
print("The wasted waste_list:",waste_list)
del a,b,waste_list

'''
Method 	    Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

'''
the output of this program will be...

aTuple is: ('apple', 'orange', 'grape')
The length of aTuple is: 3
The count of apple is: 1
The first index of orange is: 1
The type of the aTuple is: <class 'tuple'>
bTuple is: ('apple', 'orange', 'grape')
cTuple is: ('banana', 'watermelon')
Printing aTuple using for loop: apple orange grape 
Aceessing values using index: apple orange grape 
Acessing values using negative index: grape orange apple 
Print aTuple using while loop: apple orange grape 
Changed list: ('apple', 'orange', 'mango')
Added grape in aTuple: ('apple', 'orange', 'mango', 'grape')
aTuple * 3 is: ('apple', 'orange', 'mango', 'grape', 'apple', 'orange', 'mango', 'grape', 'apple', 'orange', 'mango', 'grape')
unpacked vars: apple orange mango grape
The needed a,b: apple orange
The wasted waste_list: ['mango', 'grape']
'''