class Vehicle():

    def __init__(self, m, y):
        self.modelName = m
        self.madeYear = y

    def start(self):
        print("The vehicle started")
        print("Model Name:", self.modelName)
        print("Made Year:", self.madeYear)


if __name__ == "__main__":
    v = Vehicle("Mazda", 2022)
    v.start()


# the output will be...
# The vehicle started
# Model Name: Mazda
# Made Year: 2022
