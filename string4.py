s=input("Enter String:")
a1=s.split(" ")
a2=set(a1)
for val in a2:
    s=a1.count(val)
    print(val,"Count=",s)
