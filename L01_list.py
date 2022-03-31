# list items are ordered, changable, allow duplicates and contains any type of data (even other list).
# in this program we will review how to create, modify and manipulate a list

# list is defined using square brackets "[]"
aList = ["apple", "Orange", "banana", "Cherry"]
print(aList)

# we can access the length of the list using len() function
print("Length of this list is",len(aList))

# we can use count() function to count a specified element of a list
print("Counting rhe apples: ",aList.count("apple"))

# we can use index() function to access the first index of a specified value
print("First index of apple is:", aList.index("apple"))

# we can use type() to view type of the variable (it will show its class)
print("Type of the list",type(aList))

# using for loop to print items
print("Print using for loop:")
for item in aList:
    print(item,end=" ")
print()

# using index to print items
print("Print list using index:")
for i in range(len(aList)):
    print(aList[i],end=" ")
print()

# using negative values as index
print("using negative values as index:")
for i in range(1,len(aList)+1):
    print(aList[-i],end=" ")
print()

# using while loop to access the list
print("using while loop:")
i= 0
while (i<len(aList)):
    print(aList[i], end=" ")
    i+=1
print()

# using list comprehension
print("print using list comprehension:")
[print(i, end=" ") for i in aList]
print()

# overwriting value in a list
aList[:2] = ["blueberry", "watermelon"]
print("overwrite values:")
print(aList)

# insert() function allows us to insert a new element into the list with specified index
aList.insert(2,"berry")
print("using insert() function:")
print(aList)

# append() function allows us to add a single element at the end of the list
aList.append("oranges")
print("using append() function:")
print(aList)

# extend() function allows us to extend the list by appending another list (any other collection) at the end
aList.extend(["apple", "grapes"])
print("using extend() function:")
print(aList)

# using sort() function to sort a list
aList.sort()
print("sorting in ascending order:")
print(aList)
print()

aList.sort(reverse=True)
print("sorting in decending order:")
print(aList)
print()

print("sort with case insensitive:")
aList.sort(key=str.lower)
print(aList)
print()

# using reverse() function to reverse the indexes of the a list
aList.reverse()
print("Reversed list:")
print(aList)
print()

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
bList = aList.copy()

#Another way to make a copy is to use the built-in method list().
cList = list(aList)

# using remove() function we can a remove specified value
aList.remove("watermelon")
print("watermelon removed:")
print(aList)
print("second list using copy() function:")
print(bList)
print("third list using list() function:")
print(cList)
print()

# join aList and bList using "+"
abList = aList + bList
print("abList:")
print(abList)
print()

# join aList and cList using extend() function
acList = list()
acList.extend(aList)
acList.extend(cList)
print("acList:")
print(acList)
print()

# join cList and bList using for loop
cbList = cList.copy()
for x in bList:
    cbList.append(x)
print("cbList:")
print(cbList)
print()

# to remove a element using a index, we can use pop() function
# if you did not mention the index, by default it will remove the last element.
aList.pop(1)
print("index 1 popped:")
print(aList)

# we can alse use del keyword to remove a element from a list
# to delete an entire list we only need to specify the list name
del aList[-1]
print("Deleting the last element:")
print(aList)

# clear() function used to clear all the elements in the list
aList.clear()
print("Cleared:")
print(aList)

'''
Method      Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''


'''
the output of this program will be..

['apple', 'Orange', 'banana', 'Cherry']
Length of this list is 4
Counting rhe apples:  1
First index of apple is: 0
Type of the list <class 'list'>
Print using for..each loop:
apple Orange banana Cherry 
Print list using index:
apple Orange banana Cherry 
using negative values as index:
Cherry banana Orange apple 
using while loop:
apple Orange banana Cherry 
print using list comprehension:
apple Orange banana Cherry 
overwrite values:
['blueberry', 'watermelon', 'banana', 'Cherry']
using insert() function:
['blueberry', 'watermelon', 'berry', 'banana', 'Cherry']
using append() function:
['blueberry', 'watermelon', 'berry', 'banana', 'Cherry', 'oranges']
using extend() function:
['blueberry', 'watermelon', 'berry', 'banana', 'Cherry', 'oranges', 'apple', 'grapes']
sorting in ascending order:
['Cherry', 'apple', 'banana', 'berry', 'blueberry', 'grapes', 'oranges', 'watermelon']

sorting in decending order:
['watermelon', 'oranges', 'grapes', 'blueberry', 'berry', 'banana', 'apple', 'Cherry']

sort with case insensitive:
['apple', 'banana', 'berry', 'blueberry', 'Cherry', 'grapes', 'oranges', 'watermelon']

Reversed list:
['watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']

watermelon removed:
['oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']
second list using copy() function:
['watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']
third list using list() function:
['watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']

abList:
['oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple', 'watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']

acList:
['oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple', 'watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']

cbList:
['watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple', 'watermelon', 'oranges', 'grapes', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']

index 1 popped:
['oranges', 'Cherry', 'blueberry', 'berry', 'banana', 'apple']
Deleting the last element:
['oranges', 'Cherry', 'blueberry', 'berry', 'banana']
Cleared:
[]

'''
