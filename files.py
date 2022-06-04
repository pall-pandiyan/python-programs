import os

fruits = ["apples", "oranges", "grapes", "mangos"]

f = open("test.txt", "w")
for fruit in fruits:
    f.write(fruit+"\n")
f.close()

f = open("test.txt")
print("f.read(10):", f.read(10))
f.close()

f = open("test.txt")
print("f.read():", f.read())
f.close()

f = open("test.txt")
print("f.readline():", f.readline())
f.close()

f = open("test.txt")
print("file reading using for loop:", end=" ")
for fruit in f.read():
    if fruit != "\n":
        print(fruit, end="")
    else:
        print(end=" ")
print()
f.close()

# remove the file if it does not needed anymore
os.remove("test.txt")

# file handler canbe opened using open()
# it takes first parameter as the target file
# the second parameter is the mode to open the target.
# if the second parameter is not given, the default mode "rt" will be used


# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
