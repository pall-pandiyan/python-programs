import sys

def main():
    print("Number of arguments: ", sys.argv)
    print()
    print("Python Platform: ", sys.platform)
    print()
    print("Python Version: ", sys.winver)
    print()
    print("PATH environment variable: ", sys.path)

if ( __name__ == "__main__" ):
    main()

# the output will be...

# Number of arguments:  ['D:/.cas/git-repos/python-programs/sysModule.py']

# Python Platform:  win32

# Python Version:  3.8

# PATH environment variable:  ['D:\\.cas\\git-repos\\python-programs', 'C:\\Program Files\\Python38\\python38.zip', 'C:\\Program Files\\Python38\\DLLs', 'C:\\Program Files\\Python38\\lib', 'C:\\Program Files\\Python38', 'C:\\Users\\admin\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Program Files\\Python38\\lib\\site-packages']