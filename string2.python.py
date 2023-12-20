s=input("Enter String:")
c1=0
c2=0
a1=['a','e','i','o','u','A','E','I','O','U']
for ch in s:
    if ch in a1:
        c1=c1+1
    else:
        c2=c2+1
    print("Vowels count=",c1)
    print("Consonent count=",c2)
