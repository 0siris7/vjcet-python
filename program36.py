vowel=['A','E','I','O','U','a','e','i','o','u']
n=raw_input("enter string:")
count=0

for i in range(len(n)):
    for j in range(len(vowel)):
        if(n[i]==vowel[j]):
            count=count+1


print "the number of vowels is:",count
            
