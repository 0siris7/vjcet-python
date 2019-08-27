s=raw_input("enter string:")
s1=""
i=len(s)-1

while(i>=0):
    s1=s1+s[i]
    i=i-1

print "the reverse is:",s1

if(s1==s):
    print "the string is palindrome"

else:
    print "the string is not palindrome"
    
