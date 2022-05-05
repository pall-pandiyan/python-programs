name1 = ["Ale", "Ben", "Carl", "Dean"]
name2 = name1
name3 = name2[:]

name3[0] = "Abby"
name2[1] = "Barney"

sum = 0
for ln in (name1, name2, name3):
  print(ln)
  if(ln[0] == "Abby"):
    sum += 1
  if(ln[1] == "Barney"):
    sum += 10

print(sum)

# the output will be...

# ['Ale', 'Barney', 'Carl', 'Dean']
# ['Ale', 'Barney', 'Carl', 'Dean']
# ['Abby', 'Ben', 'Carl', 'Dean']
# 21