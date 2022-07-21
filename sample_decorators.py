import datetime

def exec_time(func):
    def return_func(*args, **kargs):
        now = datetime.datetime.now()
        result = func(*args, **kargs)
        
        then = datetime.datetime.now()
        print(f"execution time for {func.__name__} is {then-now}")
        return result
    
    return return_func

@exec_time
def addition(a, b, c, d):
    return a + b + c + d

@exec_time
def multiplication(a, b, c):
    return a * b * c

@exec_time
def division(a, b):
    return a / b



print("ADDITION ", addition(10, 20, 30, 40))
print("Multiplicationn ", multiplication(10, 20, 40))
print("Division ", division(20, 10))