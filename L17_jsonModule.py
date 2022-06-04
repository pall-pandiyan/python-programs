import json

# loads() in json module will helps us to load a json string into a dictionary
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print("y:", y)
print("type(y):", type(y))
print()

# dumps() in json module will converts a dictionary (or anything actually.. string, int, boolean, list, tuple, etc,.) to json (javascript) equivalent.
a = {"name": "John", "age": 30, "city": "New York"}
b = json.dumps(a)
print("b:", b)
print("type(b):", type(b))
print()

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# dumps() also accepts parameters like indent to make it readable, separators to modify the default comma(,) that separates the members and colon(:) that separates the key, value pair, sort_keys parameter that accepts a boolean value to sort the display of member list.
print(json.dumps(x, indent=2, separators=(";", "="), sort_keys=True))
print()

print('json.dumps({"name": "John", "age": 30})',
      json.dumps({"name": "John", "age": 30}))
print('json.dumps(["apple", "bananas"])', json.dumps(["apple", "bananas"]))
print('json.dumps(("apple", "bananas"))', json.dumps(("apple", "bananas")))
print('json.dumps("hello")', json.dumps("hello"))
print("json.dumps(42)", json.dumps(42))
print("json.dumps(31.76)", json.dumps(31.76))
print("json.dumps(True)", json.dumps(True))
print("json.dumps(False)", json.dumps(False))
print("json.dumps(None)", json.dumps(None))

# Python 	JSON
# dict 	Object
# list 	Array
# tuple 	Array
# str 	String
# int 	Number
# float 	Number
# True 	true
# False 	false
# None 	null


# the output will be...

# y: {'name': 'John', 'age': 30, 'city': 'New York'}
# type(y): <class 'dict'>

# b: {"name": "John", "age": 30, "city": "New York"}
# type(b): <class 'str'>

# json.dumps({"name": "John", "age": 30}) {"name": "John", "age": 30}
# json.dumps(["apple", "bananas"]) ["apple", "bananas"]
# json.dumps(("apple", "bananas")) ["apple", "bananas"]
# json.dumps("hello") "hello"
# json.dumps(42) 42
# json.dumps(31.76) 31.76
# json.dumps(True) true
# json.dumps(False) false
# json.dumps(None) null
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
