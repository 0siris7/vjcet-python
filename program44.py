n=input("enter the list:")

for i in range(len(n)):
    for j in range(i,len(n)):
        if(n[i]<n[j]):
            continue
        else:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp

print n



            
