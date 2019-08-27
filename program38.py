s1=raw_input("enter first string:")
s2=raw_input("eter second string:")
s3=""

for i in range(len(s1)):
    if s1[i] not in s3:
        s3=s3+s1[i]
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                print s1[i]
                break
