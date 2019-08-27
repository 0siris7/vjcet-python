a=input("enter list1:")
b=input("enter list2:")

print "max of string 1 is:",max(a)
print "min of string 1 is:",min(a)
print "comparison between string 1 and string 2 is:",cmp(a,b)

n=input("enter object to be appended:")
a.append(n)
print a

m=input("enter object to be counted")
print "the number of times it occurs is:",a.count(m)

list3=input("enter the list to be extended")
a.extend(list3)
print a

o=input("enter object to be inserted at particular index")
p=input("enter index number")
a.insert(p,o)
print a

q=input("enter index of object to be popped:")
print a.pop(q)
print a

r=input("enter object to be removed:")
a.remove(r)
print a

print "list in sorted form is:"
a.sort()
print a

print "reverse of list is:"
a.reverse()
print a
