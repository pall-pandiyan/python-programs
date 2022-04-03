"""
# using this method i can run upto 1995
# using 1996 will throw an error
def oddOrEven(number):
    if(number<2):
        return not (number%2)
    else:
        return oddOrEven(number-2)

target = int(input("Enter the Number to check: ").strip())
if(oddOrEven(target)):
    print("The Number is Even!")
else:
    print("The Number is Odd!")
"""

#"""
# using this method i can use any number without problem
# the limitation seems to be in the if clause
def oddOrEven(number):
    if (number == 0 or number == 1):
        return "Even Number!"
    elif (number == 1):
        return "Odd Number!"
    else:
        return oddOrEven(number-2)

target = int(input("Enter the Number to check: ").strip())
print(oddOrEven(9))
#"""