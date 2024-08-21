"""
Leap year checker:

A year is a leap year if:

Divisible by 400: A year is a leap year if it is divisible by 400.
Divisible by 100 but not 400: A year is not a leap year if it is divisible by 100 but not by 400.
Divisible by 4 but not 100: A year is a leap year if it is divisible by 4 but not by 100.
Not divisible by 4: A year is not a leap year if it is not divisible by 4.

To break it down

the year must be divible by 4
the year must be divisible by 400 but not 100.

"""

year = int(input("enter the year : "))
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("its  a leap year")
else:
    print("its not a leap year")