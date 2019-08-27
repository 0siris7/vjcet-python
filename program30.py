def add(x,y):
    c=x+y
    print "result is ",c
    return
def sub(x,y):
    c=x-y
    print "result is ",c
    return
def mul(x,y):
    c=x*y
    print "the result is ",c
    return
def div(x,y):
    c=x/y
    print "the result is ",c
    return
def exp(x,y):
    c=x**y
    print "the result is ",c
    return

print "CALCULATOR MENU\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponent\n"
a=input("enter first number:")
b=input("enter second number:")
d=input("enter choice:")
if(d==1):
    add(a,b)

elif(d==2):
    sub(a,b)

elif(d==3):
    mul(a,b)

elif(d==4):
    div(a,b)

else:
    exp(a,b)
