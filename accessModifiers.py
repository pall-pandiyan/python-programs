# access modifiers are used to restrict the usage of a variable or method of a class.
# in python by default class members are public.
# protected members are defined by prefixing underscore '_' before their name and only accesable to its class and derived class.
# private members are defined by prefixing two underscores '--' before their name and only accessable throughtout that class.

class Product():

    def __init__(self, n, p, d):
        self.name = n           # default public member
        self._price = p         # protected member
        self.__description = d  # private member

    def getDetails(self):
        print("Name:", self.name)
        print("Price:", self._price)
        print("Description:", self.__description)


if __name__ == "__main__":
    p1 = Product("Shampoo", "$3", "Its very good for removing dandraft!")
    p1.getDetails()


# the output will be...

# Name: Shampoo
# Price: $3
# Description: Its very good for removing dandraft!
