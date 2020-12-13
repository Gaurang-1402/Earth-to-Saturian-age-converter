def earth_to_saturnian_age_converter():

    birthday_date_int= int(input("When was the Earthling you are talking to born on Earth? "))

    birthday_date_years = birthday_date_int // 10000
    birthday_date_months_with_days= birthday_date_int % 10000
    birthday_date_month= birthday_date_months_with_days // 100
    birthday_date_days= birthday_date_months_with_days % 100

    year_today= 2020
    month_today= 9
    day_today= 25

    if birthday_date_month>month_today:
        lived_years= year_today- birthday_date_years-1
    else:
        lived_years= year_today- birthday_date_years

    if birthday_date_month>month_today:
        lived_months= (month_today - birthday_date_month) + 12
    else:
        lived_months= month_today-birthday_date_month

    if birthday_date_days>day_today:
        lived_days= (day_today-birthday_date_days) + 30
    else:
        lived_days= day_today-birthday_date_days


    total_days_lived= lived_years * 365 + lived_months * 30 + lived_days

    # print("Years=", lived_years)
    # print("Months=",lived_months)
    # print("Days=", lived_days)
    # print("Total days lived:", total_days_lived)

    earth_to_saturnian_age_converter= float(total_days_lived/10759)
    print("This Earthling is", earth_to_saturnian_age_converter,"Saturn-years old. How cute.")
    # print("Days= ", n)

    #added= l+m+n
    #print(added)
    #print(float(added/10759))

# Using the same assumptions about Earth units as in problem 4,
# can you write a program to determine your Saturnian age? In this problem, you only need
# to determine Saturn-years. Here's the catch: Instead of entering the Earthling's age, you enter
# their birthdate (the format is [year][month][day]):
#
# When was the Earthling you are talking to born on Earth? 19930315
# This Earthling is 0.9204387024816433 Saturn-years old. How cute.
# Do this in the function earth_to_saturnian_age_converter, inside the file EarthToSaturnianAgeConverter.py.
#
# HINT: You may not use any string methods in this problem, but modulo (%) and
# integer division (//) may come in handy if you consider the birthdate (i.e. 19930315) as an integer.

### DO NOT WRITE CODE BEYOND THIS LINE ###


if __name__ == '__main__':
    earth_to_saturnian_age_converter()
