n=input("enter number")
sum=0
temp=n
while(temp>0):
    m=temp%10
    sum+=m**3
    temp//=10

if(n==sum):
    print n," is armstrong"
else:
    print n," is not armstrong"
