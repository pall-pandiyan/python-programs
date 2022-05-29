class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is sitting now!")
    
    def roll_over(self):
        print(f"{self.name} is rolling-over!")

def main():
    my_dog = Dog("Wille", 6)
    your_dog = Dog("Lucy", 3)

    print(f"My dog name is {my_dog.name}")
    my_dog.sit()
    print()

    print(f"Your dog name is {your_dog.name}")
    your_dog.roll_over()

if __name__ == "__main__":
    main()

# the output will be...

# My dog name is Wille
# Wille is sitting now!

# Your dog name is Lucy
# Lucy is rolling-over!