num=input("enter number")
n=num
rev=0
while(num!=0):
    digit=num%10
    rev=(rev*10)+digit
    num=num/10

if(rev==n):
    print "the number is a palindrome number"

else:
    print "number is not a palindrome number" 
    
