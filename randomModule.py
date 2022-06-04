import random

# random module have uniform method which will take two parameters (start and end limit) and returns a random float value, we can further use round or int to refine our results. (rounding 1.5 will return 2, but int method will return 1).

print("random.uniform(1,10):", random.uniform(1,10))
print("int(random.uniform(100, 150)):", int(random.uniform(100, 150)))
print("round(random.uniform(100, 150)):", round(random.uniform(100, 150)))


# the output will be...

# random.uniform(1,10): 5.879905617184167
# int(random.uniform(100, 150)): 116
# round(random.uniform(100, 150)): 140