print("Count Duplicates")
print("----------------")
print()
print("Please enter the number of elements: ",end='')
n = int(input())
print("Please enter the elements: ", end='')
ilist = list(map(int,input().strip().split()))
uset = set(ilist)
print("Number of duplicate elements:",len(ilist) - len(uset))