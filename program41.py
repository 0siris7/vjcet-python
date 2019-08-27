list1=input("enter marks of five subjects:")
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]

avg=float(sum/5)

print "the average is:",avg
print "the sum is:",sum
