# A set is a collection which is unordered, unchangeable*, unindexed and does not allow duplicate values
# Note: Set items are unchangeable, but you can remove items and add new items.
# set items can be of any data types!

# a set is defined using curly brackets "{}"
aSet = {"apple", "mango", "watermelon", "apple"}
print("aSet is:",aSet)  # here the duplicate 'apple' will not appear in the set

# we can get the length of the set using len() function
print("Length of the aSet is:",aSet)

# as usual we can see the type of the variable by using type() function
print("Type of the aSet is:",type(aSet))

# we can initialise or convert a list or tuple to set using set() function
# Note: intilising using constructor (in this case set()) will need two round brakets
bSet = set(("Volvo", "BMW", "Audi"))
print("bSet is:",bSet)

# we can delete a set using "del" keyword
del bSet

# print set values using for loop
# set does not have index value so we should use for..each loop
print("Printing set using for loop: ",end=" ")
for item in aSet:
    print(item,end=" ")
print()

# we can use "in" keyword to check if a specified value is present on a set
print("Is apple is in the set?",end=" ")
#print("apple" in aSet)
target = 'apple'
if(target in aSet):
    print('Yes! "',target,'" is in the set',sep="")
else:
    print('No! "', target, '" is not in the set',sep="")

# we cannot change a existing item in the set.
# but we can add items using add() function.
# note the set is not ordered, so the item will appear in order.
aSet.add("blueberry")
print("aSet is now:",aSet)

# to add items of another set into current set we can use update() function
# again! the duplicate values will be ignored
# update() can be used with any collections like list or tuple
aSet.update({"banana", "apple", "orange"})
print('Updated aSet will be:',aSet)

# one of the main advantages of using set is union() function
# just like update(), but union() will return a set consists of elements in both sets (discarding duplicates ofcourse!) and will not alter the both sets in any way.
bSet = set(("BMW", "Audi", "Dodge", "Benz"))
cSet = aSet.union(bSet)
print("united set is:",cSet)

# intersection() function will return a set contains duplicate values between two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("Intersection set is:",z)

# intersection_update() function is just like intersection(), but it simply updates a set and not return any values
x.intersection_update(y)
print("Intersection_update of x is:",x)

# symmetric_difference() function will return a set with element on both set and completely remove the duplicates, both set will not change in any way.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print("symmetric differece:",z)

# symmetric_difference_update() function will combine two sets and removes the duplicate element completely
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("symmetric difference update:",x)

del x,y,z

# to remove a item from the set we can use remove() function
aSet.remove("apple")
print('Removed "apple":',aSet)

# but if we try to remove an item which is not in the set it will raise an error.
# we can use discard() function to remove an item and if the specified item is not exists in the set it simply does nothing!
aSet.discard("berry")
aSet.discard("apple")
aSet.discard("orange")
print("After dicarding:",aSet)

# we can also use pop() function to remove an item from the set
# but pop() will remove the last item in the set and one of features of the set is, it is unordered. so we cannot control which item will be removed.
# but the return value of pop() function will be the removed item
lottery_winner = aSet.pop()
print("And the Grand Winner of the lottery is:", lottery_winner)
print("the unlucky items are:",aSet)

# clear() function clears all the items in the set
# but the set itself is still there (an empty set)
aSet.clear()
print("After clearing:",aSet)

# but deleting with "del" keyword will completly distroys the set
del aSet
# print(aSet)   # will throw an error (aSet is not defined)

'''
Method 	            Description
add()	            Adds an element to the set
clear()	            Removes all the elements from the set
copy()	            Returns a copy of the set
difference()	    Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	        Remove the specified item
intersection()	    Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	    Returns whether two sets have a intersection or not
issubset()	        Returns whether another set contains this set or not
issuperset()	    Returns whether this set contains another set or not
pop()	            Removes an element from the set
remove()	        Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	        Update the set with the union of this set and others

'''


'''
the output of this program will be...

aSet is: {'mango', 'watermelon', 'apple'}
Length of the aSet is: {'mango', 'watermelon', 'apple'}
Type of the aSet is: <class 'set'>
bSet is: {'Volvo', 'BMW', 'Audi'}
Printing set using for loop:  mango watermelon apple 
Is apple is in the set? Yes! "apple" is in the set
aSet is now: {'blueberry', 'mango', 'watermelon', 'apple'}
Updated aSet will be: {'mango', 'orange', 'blueberry', 'banana', 'watermelon', 'apple'}
united set is: {'mango', 'orange', 'BMW', 'Benz', 'banana', 'Dodge', 'apple', 'Audi', 'blueberry', 'watermelon'}
Intersection set is: {'apple'}
Intersection_update of x is: {'apple'}
symmetric differece: {'microsoft', 'google', 'banana', 'cherry'}
symmetric difference update: {'microsoft', 'google', 'banana', 'cherry'}
Removed "apple": {'mango', 'orange', 'blueberry', 'banana', 'watermelon'}
After dicarding: {'mango', 'blueberry', 'banana', 'watermelon'}
And the Grand Winner of the lottery is: mango
the unlucky items are: {'blueberry', 'banana', 'watermelon'}
After clearing: set()

'''