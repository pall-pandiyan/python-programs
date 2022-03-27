# this programs get single dimention elements from input
# and rotate the array clock-wise once

arr = list(map(int,input("Enter arry elements: ").strip().split()))
n = len(arr)


def cyclicRotation(arr,n):
    lastElement = arr[n-1]
    remaining_elements = arr[:n-1]
    new_array = [lastElement] + remaining_elements
    return (new_array)


if __name__ == '__main__':
    print (cyclicRotation(arr,n))

# the output will be...
# Enter arry elements: 10 20 30 40 50
# [50, 10, 20, 30, 40]