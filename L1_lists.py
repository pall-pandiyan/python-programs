# lists are defined using round brackets "()"
# lists are ordered, changable, allow duplicates and contail any type of data (even list).

aList = ["apple", "Orange", "banana", "Cherry"]
print(aList)

# we can access the length of the list using len() function
print("Length of this list is",len(aList))

# we can use type() to view type of the variable (it will show its class)
print("Type of the list",type(aList))

# using for loop to print items
print("Print using for..each loop:")
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

