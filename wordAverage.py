def wordAverage(lst):
    sum = 0
    for item in lst:
        sum = sum + len(item)
    return (sum/len(lst))


if __name__ == "__main__":
    text1 = "Python is fun!!!"
    text2 = "Python is easy to learn, use and understand!"

    lst1 = list(text1.split())
    lst2 = list(text2.split())

    print("text1:", text1)
    print("text2:", text2)

    print("Word average for text1:", wordAverage(lst1))
    print("Word average for text2:", wordAverage(lst2))

# the output will be...

# text1: Python is fun!!!
# text2: Python is easy to learn, use and understand!
# Word average for text1: 4.666666666666667
# Word average for text2: 4.625
