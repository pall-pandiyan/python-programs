# numpy is a python framework speacialised in manupulating array
# at first i import numpy with element named 'np'
# and used function array() to initialize the array value
# zeroes() funciton takes the dimention and initialize create the given dimention of zeros
# Note that zeroes() function one argument, in this case (2,3) is a tuple with dimentions

import numpy as np

n1=np.array([10,20,30,40])
print("n1 array is",n1)

n2=np.array([[1,2,3],[3,4,5],[5,6,7]])
print("n2 array is")
print(n2)

n3=np.zeros((2,3))
print("n3 array is")
print(n3)

# n1 array is [10 20 30 40]
# n2 array is
# [[1 2 3]
#  [3 4 5]
#  [5 6 7]]
# n3 array is
# [[0. 0. 0.]
#  [0. 0. 0.]]