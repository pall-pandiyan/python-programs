from datetime import date

print("Enter date in 'dd/mm/yyyy' of 'dd-mm-yyyy' format:", end=" ")
Str = input().strip()
day = int(Str[:2])
month = int(Str[3:5])
year = int(Str[-4:])

a = date(year=year, month=month, day=day)
print("a:", a)
print("type(a):", type(a))