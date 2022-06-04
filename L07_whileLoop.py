# With the while loop we can execute a set of statements as long as a condition is true.
print("Print i as long as i is less than 6:",end=" ")
i = 1
while i < 6:
    print(i,end=" ")
    i += 1
print()

# With the break statement we can stop the loop even if the while condition is true.
print("break when i is 3:",end=" ")
i = 1
while i < 6:
    if i == 3:
        break
    print(i,end=" ")
    i += 1
print()

# With the continue statement we can stop the current iteration, and continue with the next
print("Continue to the next iteration if i is 3:",end=" ")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i,end=" ")
print()

# With the else statement we can run a block of code once when the condition no longer is true.
#Print a message once the condition is false.
print("print 1 to 6:",end=" ")
i = 1
while i < 6:
    print(i,end=" ")
    i += 1
else:
    print()
    print("i is no longer less than 6")

"""
the output will be...

Print i as long as i is less than 6: 1 2 3 4 5 
break when i is 3: 1 2 
Continue to the next iteration if i is 3: 1 2 4 5 6 
print 1 to 6: 1 2 3 4 5 
i is no longer less than 6
"""