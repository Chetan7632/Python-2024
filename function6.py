def show(s1,s2):
    a1=set(s1)
    a2=set(s2)
    print("Union=",a1.union(a2))
    print("Intersection=",a1.intersection(a2))
s1=input("Enter String1:")
s2=input("Enter String2:")
show(s1,s2)
