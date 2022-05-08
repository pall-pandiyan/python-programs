import os
import matplotlib

if (os.path.exists("test.txt")):
    os.remove("test.txt")
else:
    f = open("test.txt", "w")
    f.write(
        "this file created on a whim, you run this program again to remove this file!")
    f.close()

if(os.path.exists("./test/")):
    os.rmdir("./test")
