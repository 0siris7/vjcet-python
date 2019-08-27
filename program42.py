list1=input("enter list:")
minimum=list1[0]

for i in range(1,len(list1)):
    if(list1[i]<minimum):
        minimum=list1[i]

print "the minimum is:",minimum

