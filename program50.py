l=[",",".",":",";","(",")","_","-","?"]
s=raw_input("enter string")
t=""
f=open("a.txt","w")
f.write(s)
f.close()


f=open("a.txt","r")
k=f.read()
for i in k:
    if(i not in l):
        t=t+i
print t
f.close()
