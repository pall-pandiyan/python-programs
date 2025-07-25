class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    def __init__(self, value):
        if not hasattr(self, "value"):
            self.value = value


a = A(10)
print("a.value:", a.value)

b = A(10)
print("b.value:", b.value)

print("a is b?:", a is b)


a.value = 20
print("updating a.value to 20")
print("a.value:", a.value)
print("b.value:", b.value)
