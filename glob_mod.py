def f():
    global x
    x = 2
    return x

x = 1
print(f()+x)

