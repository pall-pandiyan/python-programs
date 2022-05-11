def isPalindrome(l):
    n = len(l)

    for i in range(len(l)//2):
        if l[i] != l[n-i-1]:
            return False
    return True


if __name__ == "__main__":
    # l = [1,2,3,3,2,1]   # this is polindrome
    # l = [1, 2, 3, "bb", 4, 5]  # this is not

    print("Enter space seperated array elements:", end=" ")
    l = input().strip().split()

    if isPalindrome(l):
        print("This list is Palindrome!")
    else:
        print("This list is not Palindrome")

# the output will be...

# Enter space seperated array elements: 4 5 6 7 8 7 6 5 4
# This list is Palindrome!
