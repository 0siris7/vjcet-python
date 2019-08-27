def add(n):
    a=n%10
    if(n==0):
        return 0

    else:
        return a+add(n/10)

b=input("enter number:")
c=add(b)

print "the sum of number ",b," is:",c
