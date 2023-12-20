def count_upper_lower(s):
    c1=0
    c2=0
    for ch in s:
        if ch.isupper():
            c1=c1+1
        if ch.islower():
            c2=c2+1
            print("UpperCase=",c1)
            print("LowerCase=",c2)
s=input("Enter String:")
count_upper_lower(s)
