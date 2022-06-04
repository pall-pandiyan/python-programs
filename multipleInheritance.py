class A():
    name = "A"
    value = 10
    def call(self):
        print("This is Class A:")

class B():
    name = "B"
    value = 20
    def call(self):
        print("This is Class B:")

class C(A, B):
    name = "C"
    value = 30

obj = C()
obj.call()