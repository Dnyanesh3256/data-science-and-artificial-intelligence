# Accept a year and check if it a leap year or not

year = int(input("enter year to check : "))

if year % 100 == 0 and year % 400 == 0:
    print("its a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("its a leap year")
else:
    print("its not a leap year")