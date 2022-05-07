x = 10
x = 'a'
try:
    print(x)
except NameError:
    print("variable does not exists! try checking variable name!")
except:
    print("Something went wrong!")
else:
    print("Things went well!")
finally:
    print("try-except block finished!")


# we can also manually throw an exception
if (type(x) is not int):
    raise Exception("x should be a integer number!")
if (x < 0):
    raise Exception("x cannot be negative!")
