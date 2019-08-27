f1=0
f2=1

n=input("enter limit")
print f1,"\n",f2

for i in range(3,n+1):
    f3=f1+f2
    print f3," "
    f1=f2
    f2=f3
