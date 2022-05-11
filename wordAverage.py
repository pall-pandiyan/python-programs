def wordAverage(lst):
    sum = 0
    for item in lst:
        sum = sum + len(item)

    return (sum//len(lst))

if __name__ == "__main__":
    text1 = "India will be 5 trillian economy by 2025"
    text2="India will surpass US economy by 2040"

    lst1 = list(text1.split())
    lst2 = list(text2.split())

    print("Average for text1:", wordAverage(lst1))
    print("Average for text2:", wordAverage(lst2))
