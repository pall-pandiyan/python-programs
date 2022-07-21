def check_pangram(string:str) -> bool:
    if len(string)<26:
        return False

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabets:
        if letter not in string:
            return False
    return True

if __name__ == "__main__":
    string = input("Enter your string: ").strip().lower()
    if check_pangram(string):
        print(f"{string} is pangram!")
    else:
        print(f"{string} is not pangram!")


# Sample

# Enter your string: abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz is pangram!

# Enter your string: abcdefghijklmnopqrstuvwxy
# abcdefghijklmnopqrstuvwxy is not pangram!