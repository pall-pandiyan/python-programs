from dataclasses import replace


fruits = ["apples", "oranges", "grapes", "mangos"]
f = open("test.txt", "w")
f.write(replace(fruits))
