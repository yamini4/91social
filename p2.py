# python program to calculate the number of days between two dates

from datetime import date

date1 = date(2020, 7, 2)
date2 = date(2020, 7, 11)

diff = date2 - date1

print("difference between two dates: ", diff.days, "days")
