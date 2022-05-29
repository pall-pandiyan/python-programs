class Restrarant:
    def __init__(self, name, ctype):
        self.restrarant_name = name
        self.cuisine_type = ctype

    def describe_restrarant(self):
        print(f"Restrarant type: {self.restrarant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restrarant(self):
        print("Restrarant is open.")

def main():
    restrarant = Restrarant("Flowing River", "soup")
    print(f"name of the restrarant is {restrarant.restrarant_name}")
    print(f"cuisine type is {restrarant.cuisine_type}")

    restrarant.describe_restrarant()
    restrarant.open_restrarant()

if __name__ == "__main__":
    main()

# the output will be...

# name of the restrarant is Flowing River
# cuisine type is soup
# Restrarant type: Flowing River
# Cuisine Type: soup
# Restrarant is open.