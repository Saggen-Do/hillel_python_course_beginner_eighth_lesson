from datetime import datetime

x = datetime.now()
year = lambda year: x.year
month = lambda month: x.month
day = lambda day: x.day


print(year(year))
print(month(month))
print(day(day))
