from re import findall as fa

def main():
    line = "Mobile number is +1-3124-555-010 and the zip code is 21544"
    # result = fa(r'\w+ (\d+)', line)
    result = fa(r'(\d+)-(\d+)', line)
    print(result)

if ( __name__ == "__main__" ):
    main()