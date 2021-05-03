from datetime import date

today = date.today()
print("Today is:", today)

current_day = today.day
current_month = today.month
current_year = today.year
print("{}-{}-{}".format(current_day,current_month,current_year))

dd = int(input("Day: "))
mm = int(input("Month: "))
yy = int(input("Year: "))
print("DoB is: {}-{}-{}".format(dd,mm,yy))

if dd > 31 or mm > 12 or yy > current_year:
    print("Error in date of birth")
    exit()

if dd <= current_day:
    r_day = current_day - dd
if mm <= current_month:
    r_mon = current_month - mm
if yy <= current_year and mm >= current_month:
    r_yr = current_year - yy - 1
else:
    r_yr = current_year - yy
if dd > current_day:
    current_month -= 1
    current_day += 30
    r_day = current_day - dd
    if mm > current_month:
        current_year -= 1
        current_month += 12
        r_mon = current_month - mm

print("Your age till date is: {} years {} months {} days".format(r_yr,r_mon,r_day))