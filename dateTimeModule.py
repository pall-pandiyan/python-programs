import datetime as dt

date = dt.datetime.now()
day = "0"+str(date.day) if date.day<10 else str(date.day)
month = "0"+str(date.month) if date.month<10 else str(date.month)
year = str(date.year)
formattedDate = day + "/" + month + "/" + year
print(date)
print(formattedDate)

# the output will be...

# 2022-05-05 22:14:30.253327
# 05/05/2022