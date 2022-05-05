import datetime as dt

date = dt.datetime.now()

day = "0"+str(date.day) if date.day<10 else str(date.day)
month = "0"+str(date.month) if date.month<10 else str(date.month)
year = str(date.year)
formattedDate = day + "/" + month + "/" + year

print("date:", date)
print("date.strftime():", date.strftime("%d/%m/%Y"))
print("formattedDate:", formattedDate)


# the output will be...

# date: 2022-05-05 22:26:48.035445
# date.strftime(): 05/05/2022
# formattedDate: 05/05/2022