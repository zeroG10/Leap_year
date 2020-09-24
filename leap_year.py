def a_leap_year():
    year = int(input("Input year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("This year is high!!!")
        return year
    elif year % 400 == 0:
        print("This year is high!!!")
        return year
    else:
        print("This is not a leap year!!!")
        return year


what_year = a_leap_year()
