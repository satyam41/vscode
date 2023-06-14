"""Calender Test:

Month Code:
    J   F   M   A   M   J   July   Aug   Sep   Oct   Nov    Dec 
    1   4   4   0   2   5   0       3     6     1     4      6   
if L.Y:
    0   3

Day Code:
    Sun - 1
    Mon - 2
    Tue - 3
    Wed - 4
    Thus - 5
    Fri - 6
    Sat - 0


Cent. Code:
        1600    1700    1800    1900    2000
         6       4        2      0       6
        
formula = (date + month_code + year + l.y + cent._code)/7

"""
import csv

print("Welcome to Caleder Test")

# taking date from user:
print("Format of the entering the date is: dd/mm/yyyy")
user_day = int(input("Enter the day: "))
user_month = int(input("Enter the month: "))
user_year = input("Enter the year: ")
short_year = int(user_year[2:])
print(user_day,'/',user_month,'/',user_year)

centCode = 0
cent_code = 0

# time for assing century code:
if cent_code == 1600 or 2000:
    centCode = 6

elif cent_code == 1700:
    centCode = 4

elif cent_code == 1800:
    centCode = 2

elif cent_code == 1900:
    centCode = 0

# number of leap year in a century:
leap_year_user_year = short_year
leap_year = leap_year_user_year/4
# print(leap_year)

# leap year program:
lp_year = int(user_year)
if (lp_year % 4) == 0:
   if (lp_year % 100) == 0:
       if (lp_year % 400) == 0:
           True
       else:
           False
   else:
       True
else:
   False


# now time for give the month code for non-leap and leap year year calendar:
try:
    if leap_year == True:
        if user_month == 1:
            month_code = 0
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")
        
        elif user_month == 2:
            month_code = 3
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


    elif leap_year == False:

        if user_month == 1 or 10:
            month_code = 1
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 2 or 3 or 11:
            month_code = 4
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 4 or 7:
            month_code = 0
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 5:
            month_code = 2
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 6:
            month_code = 5
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 8:
            month_code = 3
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")


        elif user_month == 9 or 12:
            month_code = 6
            day_name = (user_day + month_code + short_year + leap_year + centCode)%7
            print(day_name)
            if day_name == 1:
                print("Sunday")
            elif day_name == 2:
                print("Monday")
            elif day_name == 3:
                print("Tueday")
            elif day_name == 4:
                print("Wednesday")
            elif day_name == 5:
                print("Thursday")
            elif day_name == 6:
                print("Friday")
            elif day_name == 0:
                print("Saturday")
                
except Exception as e:
    print(e)
# this is all for testing:
# print(user_year[2:])

# using formula to get the day

# day_name = (user_day + month_code + user_year[2:] + leap_year + cent_code)/7
