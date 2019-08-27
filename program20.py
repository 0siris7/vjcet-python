n=input("enter number")
if(n==1 or n==2):
    print n," is a prime numBer"

else:
    for i in range(2,(n/2)+1):
        if((n%i)==0):
            print n," not prime number"
            break
    else:
        print n," is a prime number"
