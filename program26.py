n=input("enter number")

for i in range(0,n+1):
    m=i*i
    
    if(m==n):
        print n," is a perfect square"
        break
        
    
else:
    print n," is not a perfect square"
        
