print("Program to print array pattern")
print("------------------------------")
print()
print("Please enter the size of the array: ",end='')
n = int(input())
samp = list()

#for _ in range(n):
#    samp.append(0)
samp.append([0]*n)
# print(samp)

sol = list()
for i,j in zip(range(n), range(n-1,-1,-1)):
    temp = samp[0].copy()
    temp[i] = temp[j] = 1
    sol.append(temp)
    for i in temp:
        print(i," ",end='')
    print()
# print(len(sol))