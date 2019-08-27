list1=input("enter list:")
n=input("enter element to be searched:")
flag=0
for i in range(len(list1)):
    if(list1[i]==n):
        print n," is found at ",i+1," th position"
        flag=1

if(flag==0):
        print "not found"
        
