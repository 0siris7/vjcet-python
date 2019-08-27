def fact(n):
    if(n==0):
        return 1

    else:
        return n*fact(n-1)

a=input("enter number:")
b=fact(a)

print "the factorial of number ",a," is:",b
