# dictionary is one of the collection in python
# dictionary values are changable, ordered, and allow duplicates and can contain any types of date.
# dictionary items should contain key and value pair seperated by a colon ":"
# dictionary values can be assed using key as index.

# "{}" curly brackets are used to define a dictionary
aDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print the whole dictionary
print("aDict is:",aDict)

# print specific value
print('aDict["brand"] is:',aDict["brand"])
print('aDict.get("year") is:', aDict.get("year"))

# print using for loop
print("Print using for loop:", end=" ")
for x in aDict.keys():
    print(x,"=",aDict.get(x),end=";  ")
print()

print("for loop with zip()", end=" ")
for x in zip(aDict.keys(),aDict.values()):
    print(x,end=" ")
print()

print("for loop with items()",end=" ")
for x,y in aDict.items():
    print(x,"=",y,end=";  ")
print()

# External functions
# type() function used to identify the class of the give variable
print("Type of aDict is:",type(aDict))

# len() function used to find size of the dictionary
print("Length of the aDict is:",len(aDict))

# copy() function can used to copy a dictionary
bDict = aDict.copy()
print("copying bDict:",bDict)

# dict() function can used to copy a dictionary or define a dictionary
bDict = dict(aDict)
print("copy using dict():",bDict)

# change specific values
aDict["year"] = 2010
print("After updated using index:",aDict)

# use update() function to update a dictionary
aDict.update({"year": 2011})
print("After updated using update():",aDict)

# use update() function to add new value in dictionary
aDict.update({"color":"red"})
print("After insert values using update():",aDict)

# checking for a key
if "year" in aDict:
    print("\"year\" is in aDict's keys")

# using pop() function to remove a key/value pair
aDict.pop("model")
print("After poping model:",aDict)

# using popitem() function to remove the last key/value pair
aDict.popitem()
print("After poping last value:",aDict)

# using del keyword to remove a value
del aDict["year"]
print("After deleting \"year\":",aDict)

# clear() function to clear all the values in dictionary
# but the dictionary itself is not deleted
aDict.clear()
print("Afer clear() function:",aDict)

del aDict
#print("This will throw an error: ",aDict)

"""
Method 	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

"""
the output will be...
aDict is: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
aDict["brand"] is: Ford
aDict.get("year") is: 1964
Print using for loop: brand = Ford;  model = Mustang;  year = 1964;  
for loop with zip() ('brand', 'Ford') ('model', 'Mustang') ('year', 1964) 
for loop with items() brand = Ford;  model = Mustang;  year = 1964;  
Type of aDict is: <class 'dict'>
Length of the aDict is: 3
copying bDict: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
copy using dict(): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
After updated using index: {'brand': 'Ford', 'model': 'Mustang', 'year': 2010}
After updated using update(): {'brand': 'Ford', 'model': 'Mustang', 'year': 2011}
After insert values using update(): {'brand': 'Ford', 'model': 'Mustang', 'year': 2011, 'color': 'red'}
"year" is in aDict's keys
After poping model: {'brand': 'Ford', 'year': 2011, 'color': 'red'}
After poping last value: {'brand': 'Ford', 'year': 2011}
After deleting "year": {'brand': 'Ford'}
Afer clear() function: {}
"""