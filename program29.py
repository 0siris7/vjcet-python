def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y

a=input("enter first number")
b=input("enter second number")
print "the numbers are",a," ",b
c,d=swap(a,b)
print "the reverse is:",c,d
