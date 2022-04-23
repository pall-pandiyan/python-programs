def fibonacci(n, lst=list()):
    global count
    count += 1

    if len(lst) == 0:
        lst = list('0'*(n+1))
        lst[0:2] = [0,1]

    if (lst[n] == '0'):
        lst[n] = fibonacci(n-1, lst) + fibonacci(n-2, lst)

    return int(lst[n])

count = 0
# n = int(input("Enter n: ").strip())
# the maximum limit to recursion depth is 998
n = 998
print(f"fib({n}) is",fibonacci(n))
print(f"it took {count} loops!")

"""
the output will be...
fib(998) is 16602747662452097049541800472897701834948051198384828062358553091918573717701170201065510185595898605104094736918879278462233015981029522997836311232618760539199036765399799926731433239718860373345088375054249
it took 1995 loops!

[Done] exited with code=0 in 0.098 seconds
"""