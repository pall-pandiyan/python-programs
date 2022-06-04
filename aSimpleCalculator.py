def calculate(s):
    s = s.replace(" ", "")
    op = ""
    opInd = ""

    for i in range(len(s)):
        try:
            temp = int(s[i])
        except:
            op = s[i]
            opInd = i
            break
    
    no1 = int(s[:opInd])
    try:
        no2 = int(s[opInd+1:])
    except:
        return -2

    if   ( op == "+" ): return ( no1 + no2 )
    elif ( op == "-" ): return ( no1 - no2 )
    elif ( op == "*" ): return ( no1 * no2 )
    elif ( op == "/" ): return ( no1 / no2 )
    else              : return -1


def main():
    inputString = input("Please enter a simple query (with +, -, *, /) : ").strip()
    result = calculate(inputString)
    result = "Error! Please input a simple query!" if ( result == -1 ) else result
    result = "Error! Invalid Operator!" if ( result == -2 ) else result
    print(result)

if __name__ == "__main__":
    main()


# the output will be...

# Please enter a simple query (with +, -, *, /) : 33*235
# 7755