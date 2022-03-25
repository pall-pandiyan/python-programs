# using python list to create and manuplate a one dimentional array
# 
# pop() in list used to remove a element in a list,
# without any index as argument it will remove the last element (we can also assign it to a variable)
# 
# append(6) in list used to add a element at the end of the list
#
# remove() is used to remove a element by refering its value
# 
# reverse() is used to flip the list element indexes
#
# sort() is used to sort into acending order (unless reverse=true argument is given)

def array_test():
    ar = [3, 2, 4, 5]

    pp = ar.pop()
    print("poped:",pp)

    ar.append(6)

    print(ar)
    print("Index of 4: ", ar.index(4))  # index of given value

    ar.remove(4)  # remove the first occurence of item with given value
    print("Removed 4: ", ar)

    ar.reverse()
    print("reversed: ", ar)
    print("sorted return: ", sorted(ar))

    ar.sort()
    print("sorted in place: ", ar)

def main():
    array_test()


if __name__ == "__main__":
    main()


# the output will be..
#
# poped: 5 
# [3, 2, 4, 6]
# Index of 4:  2
# Removed 4:  [3, 2, 6]
# reversed:  [6, 2, 3]
# sorted return:  [2, 3, 6]
# sorted in place:  [2, 3, 6]
