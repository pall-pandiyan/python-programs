def outer_func(x):
    def inner_func(y):
        print("x:", x)
        print("y:", y)
        return x+y
    return inner_func

a = outer_func(10)
b = a(15)
print(b)
