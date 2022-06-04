import datetime as dt

date = dt.datetime.now()

day = "0"+str(date.day) if date.day<10 else str(date.day)
month = "0"+str(date.month) if date.month<10 else str(date.month)
year = str(date.year)
formattedDate = day + "/" + month + "/" + year

print("date:", date)
print("date.strftime():", date.strftime("%d/%m/%Y"))
print("formattedDate:", formattedDate)


# Directive 	Description 	Example 	Try it
# %a 	Weekday, short version 	Wed 	
# %A 	Weekday, full version 	Wednesday 	
# %w 	Weekday as a number 0-6, 0 is Sunday 	3 	
# %d 	Day of month 01-31 	31 	
# %b 	Month name, short version 	Dec 	
# %B 	Month name, full version 	December 	
# %m 	Month as a number 01-12 	12 	
# %y 	Year, short version, without century 	18 	
# %Y 	Year, full version 	2018 	
# %H 	Hour 00-23 	17 	
# %I 	Hour 00-12 	05 	
# %p 	AM/PM 	PM 	
# %M 	Minute 00-59 	41 	
# %S 	Second 00-59 	08 	
# %f 	Microsecond 000000-999999 	548513 	
# %z 	UTC offset 	+0100 	
# %Z 	Timezone 	CST 	
# %j 	Day number of year 001-366 	365 	
# %U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
# %W 	Week number of year, Monday as the first day of week, 00-53 	52 	
# %c 	Local version of date and time 	Mon Dec 31 17:41:00 2018 	
# %C 	Century 	20 	
# %x 	Local version of date 	12/31/18 	
# %X 	Local version of time 	17:41:00 	
# %% 	A % character 	% 	
# %G 	ISO 8601 year 	2018 	
# %u 	ISO 8601 weekday (1-7) 	1 	
# %V 	ISO 8601 weeknumber (01-53) 	01



# the output will be...

# date: 2022-05-05 22:26:48.035445
# date.strftime(): 05/05/2022
# formattedDate: 05/05/2022