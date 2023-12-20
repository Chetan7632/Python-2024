# Variable-length Argument-

def add(*a):
    s=0
    for n in a:
        s=s+n
        print("Addition=",s)
add(11)
add(11,22)
add(11,22,100)
add(11,22,100,11,22)
add(10,20,30,40,50,60,70)

