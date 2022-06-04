# this program uses list to store a single dimention integers as array
# and receive a displacement value
# the array will be rotated to the left by given displacement

arr = list(map(int,input("Enter space seperated single dimention arry: ").strip().split()))
n = len(arr)
d = int(input("Enter displacement: ").strip())

def swap(Arr,fi,si,d):
    for i in range(d):
        temp = Arr[fi + i]
        Arr[fi + i] = Arr[si + i]
        Arr[si + i] = temp
        i+=1
    return

def leftRotate(array, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while (i != j):
        if(i < j): # A is shorter 
            swap(array, d - i, d + j - i, i)
            j -= i
        else: # B is shorter 
            swap(array, d - i, d, j)
            i -= j
    swap(array, d - i, d, i)
    return (array)

if __name__ == '__main__':
    print (leftRotate(arr,d,n))
    X = [1,2,3,4,5,6,7]
    print (leftRotate(X,d=2,n=len(X)))

# the output will be...
# Enter space seperated single dimention arry: 1 2 3 4 5 6 7 8 9 10
# Enter displacement: 3
# [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
# [3, 4, 5, 6, 7, 1, 2]