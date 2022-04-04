# text data can be stored in string data type.
# a string can be surrounded by single or double quote (' ' or " ").

# we can print a string literal directly to standared output using print()
print("Hello",end=" ")
print('world')

# also assign to a varriable
greetings = 'Good Morning!'
name = "Ranjith"
print(greetings,name)
print()

# we can also store multiple lines as string using triple single or double quote (''' or """)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)
print()
print(b)
print()
del a,b,name

# string is actually a array, we can access a specific charactor using index (first index starts from 0)
print("Index 1 in greetings",greetings[1])

# we can use colon (":") to specify multiple characters in a string
# Note: when using ":", we have to specify the target index as "start:end". if we do not specify the start index it will point to first charactor. If we do not specify the end index, it will point to last charactor.
# another point is the end index specified will not be in the result, e.x: "[:3]" will results in charactors 0,1,2 but not 3 charactor.
print("First 4 charactors in greetings",greetings[:4])
print("Charactors between 2 to 4 in greetings",greetings[1:4])

# negative indexes are used acces the charactors from the last charactors
# last charactor's index is "-1"
print("Last 4 charactors of greetings",greetings[-4:])

# we can also loop through a string, charactor by charactor
for char in greetings:
    print(char,end=" ")
print()

# a string can be splited using split() function to store into a collection (list, set, tuple). every word seperated by space will a element of the collection
greetingList = list(greetings.split())
print(greetingList)
del greetingList

# we can figure out the length of a string using len() function
print("size of greetings:",len(greetings))

# we can check if a string is within another string using "in" (its exact opposit is "not in")
# note: in python a charactor is also a string with the length of 1
print('Is "Good" in the greetings?:',end=" ")
print("Yes") if 'Good' in greetings else print("No")

# to print() a string with only capital letters we can use upper() function
# it will not modify the varriable, only return the string with capital letter
print(greetings.upper())

# to get a lower case string output, we can use lower()
print(greetings.lower())

"""
Method 	        Description
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle() 	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning

"""

"""
the output will be...
Hello world
Good Morning! Ranjith

Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.

Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.

Index 1 in greetings o
First 4 charactors in greetings Good
Charactors between 2 to 4 in greetings ood
Last 4 charactors of greetings ing!
G o o d   M o r n i n g ! 
['Good', 'Morning!']
size of greetings: 13
Is "Good" in the greetings?: Yes
GOOD MORNING!
good morning!
"""