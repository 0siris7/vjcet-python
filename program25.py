a=input("enter upper limit")
b=input("enter lower limit")

for i in range(a,b+1):
    if i>1:
        for j in range(2,(i/2)+1):
            if(i%j==0):
                break
        else:
            print i
