s=input("Enter String:")
a1=list(s)
a2=set(a1)
for ch in a2:
    if a1.count(ch)>1:
        print(ch,"Count=",a1.count(ch))
