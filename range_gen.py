def custom_range(start:int, stop:int, step:int=1):
    while True:
        if step > 0 and (start >= stop):
            break

        if step < 0 and (start <= stop):
            break

        yield start

        start = start + step

print(list(custom_range(1,5)))
print(list(custom_range(1,1)))
print(list(custom_range(10,0,-1)))

