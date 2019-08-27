year=input("enter year to be checked")

if(year%100==0):
    if(year%400==0):
        print year," is leap year"

if(year%4==0):
    print year," is leap year"

else:
    print year," is not leap year"
