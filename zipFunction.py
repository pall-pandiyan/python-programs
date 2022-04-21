"""
i usually use zip funciton to use more than one variable on for loop.
you can pass two or more iterates to zip function and it will return the same type iterate with their values zipped together.
for example: value of index 0's of all iterates will form a different iterate of the same type and so on so forth.
the result will have the length of the shortest input iterate.
"""
aTuple = (1,2,3,4,5,6)
print("aTuple is:", aTuple)
bTuple = (8,6,5,4,2)
print("bTuple is:", bTuple)
print("zip of aTuple and bTuple is:", end=" ")
for x in zip(aTuple, bTuple):
    print(x, end=" ")
print()