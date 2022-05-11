def isPalindrome(l):
    n = len(l)

    for i in range(len(l)//2):
        if l[i] != l[n-i-1]:
            return False
    return True

if __name__ == "__main__":
    #l = [1,2,3,3,2,1]   # this is polindrome
    l = [1,2,3,"bb",4,5]  # this is not

    if isPalindrome(l):
        print("This list is palindrome!")
    else:
        print("This is not polindrome")
