n=raw_input("enter string")
m=raw_input("enter character to be searched:")
flag=0
for i in range(len(n)):
    if(n[i]==m):
        print m," is found at ",i+1," th position"
        flag=1
if(flag==0):
    print "character is not found"
        
        
